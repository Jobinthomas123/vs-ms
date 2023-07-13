import json
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

filename = 'NTC Songbook Songs 2022'
folder_id = '1TGIH190m1t7dXA4hLrf3GqN0R2B4TT8T'
page_token = None

songs = []

while True:
    query = "parents='" + folder_id + "' and trashed=false"
    response = service.files().list(q=query, spaces='drive', fields='nextPageToken, files(id, name, webViewLink)', pageToken=page_token).execute()
    items = response.get('files', [])

    for item in items:
        file_id = item['id']
        file_name = item['name']
        song_number, song_title = file_name.split('-', 1)
        share_link = f'https://drive.google.com/file/d/{file_id}/view?usp=sharing'
        song = {'song_number': int(song_number), 'title': song_title.strip(), 'key': 0, 'link': share_link}
        songs.append(song)

    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break

# Sort songs by song number
songs.sort(key=lambda x: x['song_number'])

# Write songs to JSON file
with open('music.json', 'w') as f:
    json.dump(songs, f, indent=4)


