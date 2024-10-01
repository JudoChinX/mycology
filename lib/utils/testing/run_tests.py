from test_image_metadata import check_image_metadata
from test_readme_documents import check_readme_documents
from test_readme_images import check_readme_images

# This script checks the metadata of all image files in the documents/images directory.
check_image_metadata()

# This script checks that all recipe and resource files are listed in the root README.md file.
check_readme_documents()

# This script checks that all image files in the documents/images directory are linked in the markdown files.
check_readme_images()
