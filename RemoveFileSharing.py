import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)

def change_sharing_settings(service, folder_id):
    query = f"'{folder_id}' in parents"
    page_token = None
    while True:
        response = service.files().list(q=query,
                                        spaces='drive',
                                        fields='nextPageToken, files(id, owners, permissions)',
                                        pageToken=page_token,
                                        pageSize=100).execute()
        for item in response.get('files', []):
            file_id = item['id']
            owner_ids = {owner['permissionId'] for owner in item.get('owners', [])}
            try:
                permissions = item.get('permissions', [])
                for permission in permissions:
                    if permission['id'] not in owner_ids and permission['type'] in ['anyone', 'domain']:
                        service.permissions().delete(fileId=file_id, permissionId=permission['id']).execute()
                
                print(f'Link sharing turned off for file: {file_id}')
            except Exception as e:
                print(f'Error updating file {file_id}: {e}')
        
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

service = get_service()
folder_id = 'your_folder_id_here'  # Replace with your folder ID
change_sharing_settings(service, folder_id)
