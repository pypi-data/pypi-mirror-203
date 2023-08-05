# Ref: Adapted from Register class in https://github.com/bad-address/iasm

from collections import namedtuple, OrderedDict
from unicorn import arm_const
from functools import partial
from bitstring import Bits
from fnmatch import fnmatch

_supported_regs = {
    'arm': (
        arm_const, 'UC_ARM_REG_', set(), 'r15', {
            'r9': 'sb',
            'r11': 'fp',
            'r12': 'ip',
            'r13': 'sp',
            'r14': 'lr',
            'r15': 'pc'
        }, ["r[0-9]", "r1*", "cpsr"], {
            'cpsr': (
                32,
                OrderedDict(
                    [
                        ('N', 31),
                        ('Z', 30),
                        ('C', 29),
                        ('V', 28),
                        ('Q', 27),
                        ('J', 24),
                        (1, None),
                        ('GE', slice(16, 20)),
                        (2, None),
                        ('E', 9),
                        ('A', 8),
                        ('I', 7),
                        ('F', 6),
                        ('T', 5),
                        (3, None),
                        ('M', slice(0, 5)),
                        (4, None),
                        ('IT', (slice(25, 27), slice(10, 16))),
                        (5, None),
                        ('...........', slice(20, 24)),
                    ]
                )
            )
        }
    )
    }

class Register(
    namedtuple('R', ('mu', 'name', 'const', 'alias', 'f_dscrs', 'sz'))
):
    ''' A representation of a CPU register.'''

    @property
    def val(self):
        try:
            return self.mu.reg_read(self.const)
        except Exception as err:
            raise Exception(
                f"Register {self.name} ({self.alias}) could not be read under symbolic constant {self.const}."
            ) from err

    @val.setter
    def val(self, v):
        self.mu.reg_write(self.const, v)

    def is_available(self):
        ''' Return if the register can be readed without an error. '''
        try:
            _ = self.val
            return True
        except:
            return False

    def repr_val(self):
        v = self.val
        if isinstance(v, int):
            return v
        elif isinstance(v, tuple):
            return '(' + ', '.join(i for i in v) + ')'
        else:
            raise Exception(
                "Unknown register type'%s' for '%s'" % (type(v), self.name)
            )
    
    def display_name(self):
        return ("%s/%s" % (self.name, self.alias)) if self.alias else self.name

    def __repr__(self):
        return "%s = %s" % (self.display_name(), self.repr_val())

    def __eq__(self, other):
        if not isinstance(other, Register):
            return False
        return self.name == other.name and self.val == other.val


def _get_flag(reg, flag_descr, reg_sz):
    ''' Return a Bits representation of a subset of the register <reg>.

        The subset is defined by the flag descriptor assuming a register
        of <reg_sz> size.

        >>> reg = _make_registers_dummy(['cpsr'], [0b1000000000001100])[0]

        An integer means a single bit:

        >>> _get_flag(reg, 0, 16).bin    # LSB
        '0'
        >>> _get_flag(reg, 15, 16).bin    # MSB
        '1'

        A slice object means a range of bits:

        >>> _get_flag(reg, slice(0, 4), 16).bin
        '1100'

        A tuple of integers and slices means a range of bits that
        cannot be represented by a single slice because they are
        non-contiguous.

        >>> _get_flag(reg, (15, 14, slice(0, 4)), 16).bin
        '101100'
        '''
    # Note: we reverse the bits at the begin and then at the end.
    # This allows the indexing notation to put the low numbers (0)
    # on the right to select LSB and the high number (N-1) on the left
    # to select the MSB
    bs = Bits(uint=reg.val, length=reg_sz)[::-1]
    if isinstance(flag_descr, int):
        seq = [bs[flag_descr:flag_descr + 1]]
    elif isinstance(flag_descr, slice):
        seq = [bs[flag_descr]]
    else:
        assert isinstance(flag_descr, tuple)
        seq = [
            (bs[d:d + 1] if isinstance(d, int) else bs[d]) for d in flag_descr
        ]

    assert isinstance(seq, list) and all(isinstance(b, Bits) for b in seq)
    return sum(b[::-1] for b in seq)

class FlagRegister(Register):
    def _define_flags_description(self):
        for name, descr in self.f_dscrs.items():
            if descr is None:
                continue

            fget = partial(_get_flag, reg=self, flag_descr=descr, reg_sz=self.sz)
            prop = property(fget, doc='Flag %s' % name)
            setattr(self, name, prop)

    def repr_val(self):
        bs = []
        names = []
        for name, descr in self.f_dscrs.items():
            if descr is None:
                bs.append(' ')
                names.append(' ')
                continue

            b = _get_flag(self, flag_descr=descr, reg_sz=self.sz)
            bs.append(b)

            name = name[:len(b.bin)]
            if len(name) < len(b):
                name += " " * (len(b) - len(name))
            names.append(name)

        up = ''.join(b if b == ' ' else b.bin for b in bs)
        down = ''.join(names)

        return up + '\n' + down

    def __repr__(self):
        ''' Representation of flags

            >>> f_dscrs = OrderedDict([('N', 31), ('Z', 30), (1, None), ('M', slice(0, 5, None))])
            >>> FlagRegister(mu, 'eax', unicorn.x86_const.UC_X86_REG_EAX, None, f_dscrs, 32)
            eax =
            00 00000
            NZ M
            '''
        return "%s =\n%s" % (self.display_name(), self.repr_val())

# Took away PC var, might have to add it later if more archs are supported.
def get_registers(mu, arch_name:str = "arm", mode_name: str = "") -> list[Register]:
    mod, regprefix, ignore, pc_name, aliasses, _, f_regs = _supported_regs[
        arch_name]
    if isinstance(pc_name, dict):
        pc_name = pc_name[mode_name]

    const_names = [n for n in dir(mod) if n.startswith(regprefix)]
    const_names.sort()

    regnames = [n.replace(regprefix, '') for n in const_names]
    consts = [getattr(mod, n) for n in const_names]

    regs = []
    for name, const in zip(regnames, consts):
        name = name.lower()
        if name in ignore:
            continue

        alias = aliasses.get(name, None)
        if name in f_regs:
            reg_sz, f_dscrs = f_regs[name]
            reg = FlagRegister(mu, name, const, alias, f_dscrs, reg_sz)
            reg._define_flags_description()
        else:
            reg = Register(mu, name, const, alias, None, None)

        if not reg.is_available():
            continue

        regs.append(reg)

    return regs

def select_registers(regs, globs) -> list[Register]:
    ''' Filter the registers by name following the globs expressions
        (fnmatch).

        Use '?' as a wildcard for a single character and '*' for zero or
        more characters:

        >>> list(select_registers(regs, ['e?x']))
        [eax = 0, ebx = 0]

        >>> list(select_registers(regs, ['e*']))
        [eax = 0, ebx = 0, eip = 0, esi = 0]

        >>> list(select_registers(regs, ['*i*']))
        [eip = 0, esi = 0]

        Charsets can be used with "[seq]" and "[!seq]".

        >>> list(select_registers(regs, ['e[acde]x']))
        [eax = 0]

        >>> list(select_registers(regs, ['e[!acde]x']))
        [ebx = 0]

        Exact names can be used as well:

        >>> list(select_registers(regs, ['eip']))
        [eip = 0]

        Several globs can be applied at the same time: any
        register matching at least one of the globs will be returned

        >>> list(select_registers(regs, ["eax", "ebx"]))
        [eax = 0, ebx = 0]

        A glob prefixed with "!" will negate the match. This is a way
        to block registers matched by a previous glob:

        >>> list(select_registers(regs, ["e*", "!eip"]))
        [eax = 0, ebx = 0, esi = 0]

        The registers allowed by globs determine also the order: registers
        allowed first appear before.

        >>> list(select_registers(regs, ["e*", "!e?x", "eax"]))
        [eip = 0, esi = 0, eax = 0]

        If not glob is given no register is selected:

        >>> list(select_registers(regs, []))
        []
    '''

    if not globs:
        return iter(list())

    selected = []
    for g in globs:
        if g and g[0] == "!":
            selected = [r for r in selected if not fnmatch(r.name, g[1:])]
        else:
            more = [
                r for r in regs if r not in selected and fnmatch(r.name, g)
            ]
            selected += more

    return selected