
# Google Drive File Sharing Modifier

## Description
This Python script is designed to modify the sharing settings of all files within a specified Google Drive folder. Specifically, it turns off link sharing for each file, effectively setting each file's access to 'restricted'. This ensures that files are no longer accessible via shared links and can only be accessed by users who have been explicitly granted permission.

## Setup and Installation
To use this script, you will need:
- Python installed on your system.
- Google Client Library for Python installed in your Python environment.
- OAuth 2.0 credentials set up in your Google Cloud project for the Google Drive API.
- `credentials.json` file downloaded from your Google Cloud project and placed in the same directory as the script.

## Usage
1. Open the script in a Python editor or IDE.
2. Replace `'your_folder_id_here'` in the `folder_id` variable with the actual ID of the Google Drive folder you wish to modify.
3. Run the script. It will authenticate via OAuth 2.0 and proceed to modify the sharing settings of all files within the specified folder.

## Functionality
- The script uses the Google Drive API to access and modify file permissions.
- It processes files in batches of 100 due to API pagination and continues until all files in the folder have been processed.
- Link sharing permissions are removed from each file, and access is set to restricted.
- The script provides console output for each file it processes, indicating the completion of the operation or any errors encountered.

## Note
- Ensure that you have the necessary permissions to modify the files in the specified folder.
- The script requires internet access to interact with the Google Drive API.
- Handle the OAuth 2.0 credentials and `credentials.json` file securely.

## Author
StreamBit
https://github.com/StreamBit
