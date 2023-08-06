from pathlib import Path
from typing import List
import argparse
import os
import subprocess
import sys
import tempfile
import time

import colorama

from bmgen.info import VERSION

class bmgen():
    SEP_STR = '============================================================'
    ESCAPE_MAP = str.maketrans({
        '\'': '\\\'',
        '\0': '\\0',
        '\a': '\\a',
        '\b': '\\b',
        '\f': '\\f',
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t',
        '\v': '\\v',
    })
    
    @staticmethod
    def get_printable_command(args: List[str], prefix: str | None=None) -> str:
        printable_args = []
        for arg in args:
            quote = '\'' if ' ' in arg else ''
            printable_args.append(quote + arg.translate(bmgen.ESCAPE_MAP) + quote)
        return (f'{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}[{prefix}]{colorama.Style.NORMAL} ' if prefix else '') + colorama.Fore.BLUE + ' '.join(printable_args) + colorama.Fore.RESET
    
    def __init__(self, rebuild: bool):
        self.command_id = 0
        self.failed_command_num = 0
        self.output_dir = ''
        self.rebuild = rebuild
    
    def print_error(self, msg: str, prefix: str='ERROR') -> None:
        print(f'{colorama.Fore.RED}{colorama.Style.BRIGHT}[{prefix}]{colorama.Style.NORMAL} {msg}{colorama.Fore.RESET}', file=sys.stderr)
    
    def abort(self, msg: str) -> None:
        self.print_error(msg, prefix='BUILD FAILED')
        self.print_error(f'{self.failed_command_num} command{"" if self.failed_command_num == 1 else "s"} failed')
        sys.exit(1)
    
    def set_output_dir(self, new: str) -> None:
        self.output_dir = new
        
        if os.path.islink(new):
            if not os.path.exists(new):
                os.makedirs(Path(new).resolve())
        else:
            os.symlink(tempfile.mkdtemp(prefix='bmgen-'), new)
    
    def skip_file(self, source_path: str, output_path: str) -> bool:
        return os.path.exists(output_path) and os.path.getmtime(source_path) < os.path.getmtime(output_path)
    
    def start_command(self, title: str) -> None:
        print(f'{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}[{self.command_id}]{colorama.Style.NORMAL} {title}{colorama.Fore.RESET}')
    
    def command_error(self, msg: str, mandatory: bool) -> None:
        self.failed_command_num += 1
        self.print_error(msg)
        if mandatory:
            self.abort(f'Mandatory command #{self.command_id} wasn\'t successfully executed!')
        else:
            self.print_error(f'Command #{self.command_id} failed!', prefix='FAIL')
    
    def exec_command(self, args: List[str], mandatory: bool, print_command: bool=True, output_file: str | None=None, skip: bool=False) -> None:
        if skip:
            if print_command:
                print(bmgen.get_printable_command(args, prefix='SKIP; ' + output_file))
            return
        
        printable_command = bmgen.get_printable_command(args, prefix=output_file)
        if print_command:
            print(printable_command + '\n' + bmgen.SEP_STR)
        
        proc = subprocess.run(args, text=True)
        
        print(bmgen.SEP_STR)
        if proc.returncode != 0:
            self.command_error(f'Command exited with a non-zero exit code ({proc.returncode}): {printable_command}', mandatory)
    
    def end_command(self):
        self.command_id += 1

def main() -> None:
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument('--version', action='store_true', help='print version and exit')
    ap.add_argument('-d', '--directory', default='.', help='specify the working directory')
    ap.add_argument('-s', '--script', default='bmgen.py', help="path of the build script to execute")
    ap.add_argument('-r', '--rebuild', action='store_true', help="force the execution of all commands")
    args = ap.parse_args()
    
    if args.version:
        print('bmgen v' + VERSION)
        return
    
    os.chdir(args.directory)
    
    if not os.path.exists(args.script):
        print(f'Script "{args.script}" does not exist!', file=sys.stderr)
        sys.exit(1)
    
    with open(args.script, 'r') as f:
        script_code = f.read()
    
    # TODO debug and release builds
    # TODO separate the code for modifying builtins
    start_time = time.time()
    inst = bmgen(args.rebuild)
    exec('import builtins\nbuiltins.bmgen = _bmgen\nbuiltins.inst = _inst\ndel _bmgen\ndel _inst\n' + script_code, {}, {'_bmgen': bmgen, '_inst': inst})
    
    if inst.command_id > 0:
        print()
    
    print(f'{colorama.Fore.GREEN}{colorama.Style.BRIGHT}Build finished after {"%.3f"%(time.time() - start_time)} seconds')
    if inst.failed_command_num > 0:
        print(colorama.Fore.YELLOW, end='')
    print(f'{inst.failed_command_num} command{"" if inst.failed_command_num == 1 else "s"} failed{colorama.Style.RESET_ALL}')

if __name__ == '__main__':
  main()
