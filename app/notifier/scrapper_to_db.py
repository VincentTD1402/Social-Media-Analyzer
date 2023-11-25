from scrapper.scrapper import *

from enum import Enum


class Platform(str, Enum):
    playstore = 'Playstore'
    youtube = 'Youtube'
    appstore = 'Appstore'
    website = 'Website'
    reddit = 'Reddit'
    ggnews = 'News'


class StoreDB:
    def __init__(self):
        pass
    
    @staticmethod
    def get_data(name, url, max_count):
        
        if name == Platform.playstore.value:
            df = get_playstore_comment(url=url, 
                                       max_count=max_count)
        elif name == Platform.youtube.value:
            df = get_youtube_comment(url=url, 
                                     max_count=max_count)
        elif name == Platform.appstore.value:
            df = get_appstore_comment(url=url, 
                                      max_count=max_count)
        elif name == Platform.website.value:
            df = get_website_comment(urls=[url])

        elif name == Platform.reddit.value:
            df = get_reddit_comment(url=url)

        elif name == Platform.ggnews.value:
            df = get_google_news(query=url, 
                                 max_results=max_count)
            
        else:
            raise ValueError("This platform is not supported! Type one in Playstore, Youtube, Appstore, Website, Reddit, News")
        
        return df

