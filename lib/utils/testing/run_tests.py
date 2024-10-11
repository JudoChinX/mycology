from test_image_metadata import check_image_metadata
from test_readme_documents import check_readme_documents
from test_readme_images import check_readme_images

DOCUMENT_DIRECTORIES=['documents']
DOCUMENT_FILE_TYPES=['.md']
IMAGE_DIRECTORIES=['documents/images']
IMAGE_FILE_TYPES=['.heic', '.jpg', '.jpeg', '.png', '.heic']

# Check the metadata of all image files in the specified directory.
check_image_metadata(
    image_file_types=IMAGE_FILE_TYPES,
    image_dirs=IMAGE_DIRECTORIES
)

# Check that all recipe and resource files are listed in the root README.md file.
check_readme_documents(
    readme_file='README.md',
    document_file_types=DOCUMENT_FILE_TYPES,
    document_directories=DOCUMENT_DIRECTORIES
)

# Check that all image files in the image_dir are linked in the markdown files in documents_dir.
check_readme_images(
    image_file_types=IMAGE_FILE_TYPES,
    image_dirs=IMAGE_DIRECTORIES,
    document_file_types=DOCUMENT_FILE_TYPES,
    documents_dirs=DOCUMENT_DIRECTORIES
)
