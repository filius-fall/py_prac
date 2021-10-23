# import requests
# from bs4 import BeautifulSoup

# from googleapiclient.discovery import build


# link = "https://www.youtube.com/c/BOLDcast/videos"


# page = requests.get(link)
# soup = BeautifulSoup(page.content,'html.parser')

# k = soup.find_all('div')
# print(k[0])



# Import Module
from googleapiclient.discovery import build
 
# Create YouTube Object
youtube = build('youtube', 'v3',
                developerKey='AIzaSyCXm6-jqAFUlE5ysRZau3_LJ38Q-x5-gs8')
 
ch_request = youtube.channels().list(
    part='statistics',
    id='UCVXA3FX3fCv-YEuBlxpeFVg')
 
# Channel Information
ch_response = ch_request.execute()
 
sub = ch_response['items']
# vid = ch_response['items'][0]['statistics']['videoCount']
# views = ch_response['items'][0]['statistics']['viewCount']
 
print("Total Subscriber:- ", sub)
# print("Total Number of Videos:- ", vid)
# print("Total Views:- ", views)