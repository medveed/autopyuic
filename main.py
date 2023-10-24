import datetime
import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse as arg

pyuic5_command = 'pyuic5 {ui} -o {py}'

os.system('title AutoPyUIC')
gettime = lambda: f'[{datetime.datetime.now().strftime("%H:%M:%S")}]'
on_off = lambda x: 'on' if x else 'off'


class UIFileHandler(FileSystemEventHandler):
    def on_moved(self, event):
        if event.dest_path.endswith('.ui'):
            source_file = event.dest_path
            output_file = source_file.replace('.ui', '.py')
            cmd = pyuic5_command.format(ui=source_file, py=output_file)
            subprocess.call(cmd, shell=True)
            print(f'{gettime()} Updated: {source_file} -> {output_file}')


if __name__ == '__main__':
    parser = arg.ArgumentParser(description=
                                'Monitors directory for changes to .ui files and converts them to .py using pyuic5.')
    parser.add_argument('directory',
                        type=str,
                        help='Directory to monitor. Set to "/" to monitor the current directory.')
    parser.add_argument('-r', '--recursive',
                        action='store_true',
                        dest='recursive',
                        default=False,
                        help='Enable monitoring of subdirectories.')
    args = parser.parse_args()
    directory = args.directory
    event_handler = UIFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=args.recursive)
    observer.start()
    if args.recursive:
        print('INFO: Recursive mode turned on.')
    print(f'{gettime()} Started monitoring directory {directory} for changes to .ui files...\n')
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
