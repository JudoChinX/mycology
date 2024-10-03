import os

def find_files_with_extensions(file_dirs: list, file_extensions: list) -> list:
    file_dirs_objects = []
    for directory in file_dirs:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(tuple(file_extensions)):
                    file_dirs_objects.append(f'{root}/{file}')
    return file_dirs_objects
