from __future__ import print_function
from sys import implementation

from ipykernel.kernelbase import Kernel
import logging

from arm_kernel.emulator import Emulator
from arm_kernel.preprocessor import Preprocessor, BlockType
from arm_kernel.view import View

class ArmKernel(Kernel):
    implementation = 'ARM Assembly'
    implementation_version = '1.0'
    language = 'ARM Assembly'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/html',
        'file_extension': '.txt',
    }
    banner = "ARM Assembly - code an ARM CPU"
    
    view = View()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.emulator = Emulator()

    def _execute_code(self, content: dict):
        
        try:
            state = self.emulator.execute_code(content["code"])
            if len(content["views"]) > 0:
                stream_content = {
                    'metadata': {},
                    'data': {'text/html': self.view.get_view(content["views"][0], state)}
                }
                self.send_response(self.iopub_socket, 'display_data', stream_content)
        except Exception as error:
            raise Exception(f"Error executing code: {str(error)}")
        


    def _handle_config(self, config: dict):
        # For now only handle memory:
        if config.get("memory") is not None:
            mem_config = config["memory"]
            for item in mem_config.get("items"):
                self.emulator.add_memory_item(item)

        stream_content = {
            'metadata': {},
            'data': {'text/html': f"<p>-- kernel configured successfully --</p>"}
            }
        self.send_response(self.iopub_socket, 'display_data', stream_content)
    
    def _handle_subroutine(self, subroutine: dict):
        label = subroutine["label"]
        self.emulator.add_subroutine(label, subroutine["code"])
        stream_content = {
            'metadata': {},
            'data': {'text/html': f"<p>-- subroutine {label} registered successfully --</p>"}
            }
        self.send_response(self.iopub_socket, 'display_data', stream_content)


    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        if silent:
            return

        try:
            # Preprocess
            parsed_block = Preprocessor.parse(code)
            
            match parsed_block[0]:
                case BlockType.TEXT:
                    self._execute_code(parsed_block[1])
                case BlockType.CONFIG:
                    self._handle_config(parsed_block[1])
                case BlockType.SUBROUTINE:
                    self._handle_subroutine(parsed_block[1])

        except Exception as e:
                self.report_error(e)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
        }
    
    def report_error(self, err: Exception):
        stream_content = {
            'metadata': {},
            'data': {'text/html': f"<p>Error: {str(err)}</p>"}
        }
        self.send_response(self.iopub_socket, 'display_data', stream_content)