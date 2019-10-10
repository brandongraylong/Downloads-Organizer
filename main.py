#!/usr/bin/python3

import sys
import os
import shutil
import time

from tkinter import filedialog
from tkinter import Tk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent


class AnyEventHandler(FileSystemEventHandler):
    def __init__(self, abs_path):
        self._abs_path = abs_path
        organize_current_files_and_folders(self._abs_path)
        super().__init__()

    def on_any_event(self, event):
        if type(event) is FileCreatedEvent:
            organize_current_files_and_folders(self._abs_path)


def get_extension_name(name: str) -> str:
    ext = os.path.splitext(name)[1][1:].lower()
    if not ext:
        raise Exception
    return ext

def get_args():
    return sys.argv[1:]

def get_abs_path() -> str:
    args = get_args()
    if args[0] == '-p' or args[0] == '--path' and len(args) == 2:
        return args[1]

    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        raise Exception
    return folder_selected

def get_files_and_dirs(abs_path: str) -> tuple:
    directories = []
    files = []

    for item in os.listdir(abs_path):
        item_abs_path = os.path.join(os.path.join(abs_path, item))
        if os.path.isfile(item_abs_path):
            ext = ''
            try:
                ext = get_extension_name(item)
            except Exception:
                ext = 'NO EXTENSION'
            files += [(item, ext, item_abs_path)]
        elif os.path.isdir(item_abs_path):
            directories += [(item, item_abs_path)]

    return directories, files

def organize_current_files_and_folders(abs_path: str) -> None:
    directories, files = get_files_and_dirs(abs_path)

    for f in files:
        new_dir_loc = os.path.join(abs_path, f[1])
        dir_in_cwd = False
        for dir_name, dir_abs_path in directories:
            if f[1] == dir_name:
                dir_in_cwd = True
                break

        if not dir_in_cwd:
            os.mkdir(new_dir_loc)

        new_file_loc = os.path.join(new_dir_loc, f[0])
        shutil.move(f[2], new_file_loc)

        directories, files = get_files_and_dirs(abs_path)

def main() -> None:
    abs_path = ''
    try:
        abs_path = get_abs_path()
        observer = Observer()
        observer.schedule(AnyEventHandler(abs_path), abs_path, recursive=False)
        observer.start()
    except Exception:
        exit(1)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    exit(0)

if __name__ == "__main__":
    main()
