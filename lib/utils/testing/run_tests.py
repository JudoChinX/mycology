from test_readme import check_files_in_readme
from test_image_metadata import check_image_metadata

# This script checks that all recipe and resource files are listed in the root README.md file.
check_files_in_readme()

# This script checks the metadata of all image files in the documents/images directory.
check_image_metadata()
