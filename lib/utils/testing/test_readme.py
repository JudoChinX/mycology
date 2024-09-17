# This script checks that all recipe and resource files are listed in the root README.md file.
import os

def check_files_in_readme():
    recipe_dir = 'mycology/recipes'
    recipe_objects = os.listdir(recipe_dir)
    recipe_files = [file for file in recipe_objects if os.path.isfile(os.path.join(recipe_dir, file))]

    resource_dir = 'mycology/resources'
    resource_objects = os.listdir(resource_dir)
    resource_files = [file for file in resource_objects if os.path.isfile(os.path.join(resource_dir, file))]

    files_to_check = recipe_files + resource_files

    readme_file = 'mycology/README.md'
    with open(readme_file, 'r') as file:
        file_contents = file.read()

    print('Checking README.md for all recipe and resource files.')

    for file in files_to_check:
        if ' ' in file:
            # Replace spaces in filename with %20.
            file = file.replace(' ', '%20')
        assert file in file_contents, f'{file} not found in README.md'
