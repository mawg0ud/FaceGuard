import os
import requests
from zipfile import ZipFile
import hashlib

# Configuration
DATASET_URL = "https://data-url-for-faceforensics/dataset.zip"
DATASET_DIR = "../datasets/FaceForensics++"
CHECKSUM = "5d41402abc4b2a76b9719d911017c592"  # Example checksum for verification

def download_file(url: str, dest_path: str) -> None:
    """Download a file from a URL to a local path."""
    response = requests.get(url, stream=True)
    with open(dest_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Downloaded dataset to {dest_path}")

def verify_checksum(file_path: str, checksum: str) -> bool:
    """Verify file integrity by comparing MD5 checksum."""
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
    file_checksum = md5_hash.hexdigest()
    return file_checksum == checksum

def extract_zip(file_path: str, dest_dir: str) -> None:
    """Extract a ZIP file to the specified directory."""
    with ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(dest_dir)
    print(f"Extracted files to {dest_dir}")

def main():
    os.makedirs(DATASET_DIR, exist_ok=True)
    dataset_zip_path = os.path.join(DATASET_DIR, "dataset.zip")

    # Download the dataset
    download_file(DATASET_URL, dataset_zip_path)

    # Verify checksum
    if verify_checksum(dataset_zip_path, CHECKSUM):
        print("Checksum verified.")
    else:
        raise ValueError("Checksum verification failed. The file may be corrupted.")

    # Extract the dataset
    extract_zip(dataset_zip_path, DATASET_DIR)

    # Clean up
    os.remove(dataset_zip_path)
    print("Dataset downloaded, verified, and extracted successfully.")

if __name__ == "__main__":
    main()
