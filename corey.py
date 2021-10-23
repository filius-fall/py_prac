from googleapiclient.discovery import build

api_key = "AIzaSyB1iK3ryrKRkXBBJ7FmkKvpQCRXNFF1nN0"

youtube = build('youtube','v3',developerKey=api_key)


request = youtube.channels().list(
    part = 'statistics',
    forUsername = '3kliksphilip'

)

response = request.execute()

print(response)