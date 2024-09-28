#!/bin/bash

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null
then
    echo "GitHub CLI (gh) could not be found. Please install it from https://cli.github.com/"
    exit 1
fi

# Authenticate with GitHub
gh auth login

# Get the latest tag
LATEST_TAG=$(git describe --tags `git rev-list --tags --max-count=1`)

# Check if the latest tag was found
if [ -z "$LATEST_TAG" ]; then
    echo "No tags found in the repository."
    exit 1
fi

# Create a release for the latest tag
gh release create $LATEST_TAG

# Check if the release was created successfully
if [ $? -ne 0 ]; then
    echo "Failed to create a release for tag $LATEST_TAG."
    exit 1
fi

# Upload the release asset
# Replace 'path/to/your/file' with the actual file path you want to upload
gh release upload $LATEST_TAG path/to/your/file

# Check if the file was uploaded successfully
if [ $? -ne 0 ]; then
    echo "Failed to upload the file to the release."
    exit 1
fi

echo "Release created and file uploaded successfully."