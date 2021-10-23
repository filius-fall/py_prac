# import urllib.request
# import json

# def get_all_video_in_channel(channel_id):
#     api_key = "AIzaSyCXm6-jqAFUlE5ysRZau3_LJ38Q-x5-gs8"

#     base_video_url = 'https://www.youtube.com/watch?v='
#     base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

#     first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
#     print("first")

#     video_links = []
#     url = first_url
#     ss = 0
#     while ss<=3:
#         print("while")
#         inp = urllib.request.urlopen(url)
#         resp = json.load(inp)

#         for i in resp['items']:
#             if i['id']['kind'] == "youtube#video":
#                 video_links.append(base_video_url + i['id']['videoId'])

#         try:
#             next_page_token = resp['nextPageToken']
#             url = first_url + '&pageToken={}'.format(next_page_token)
#         except:
#             break
#         ss += 1
#     print("return")
#     return video_links

# k = get_all_video_in_channel("UCmSy2p4qeO3cr_BPCF4oSeQ")
# # print(k)
# print(type(k))




# import required packages
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# provide the url of the channel whose data you want to fetch
urls = [
	'https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ'
]


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for url in urls:
        driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a', id='video-title')
        views = soup.findAll(
            'span', class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a', id='video-title')
        print('Channel: {}'.format(url))
        i = 0 # views and time
        j = 0 # urls
        for title in titles[:10]:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text,
                                                                views[i].text, views[i+1].text, video_urls[j].get('href')))
            i += 2
            j += 1


main()
