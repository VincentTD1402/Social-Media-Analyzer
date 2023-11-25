from scrapper.core.playstore_scrapper import PlayStoreScrapperConfig, PlayStoreScrapperSource
from scrapper.core.youtube_scrapper import YoutubeScrapperSource, YoutubeScrapperConfig
from scrapper.core.appstore_scrapper import AppStoreScrapperConfig, AppStoreScrapperSource
from scrapper.core.website_crawler_source import TrafilaturaCrawlerConfig, TrafilaturaCrawlerSource
from scrapper.core.reddit_scrapper import RedditScrapperConfig, RedditScrapperSource
from scrapper.core.google_news_source import GoogleNewsConfig, GoogleNewsSource

from config import settings


LOOKUP_PERIOD = settings.PERIOD
COUNTRY = settings.COUNTRY
LANGUAGE = settings.LANGUAGE


# Playstore Scrapper
def get_playstore_comment(url, max_count):
    data = []

    try:
        config = PlayStoreScrapperConfig(  
           app_url = url,
           max_count = max_count, 
           lookup_period = LOOKUP_PERIOD
        )
        response = PlayStoreScrapperSource()
        response_list = response.lookup(config)

        for item in range(len(response_list)):
            response_list[item] = dict(response_list[item])
            id = response_list[item]["meta"]["reviewId"]
            author = response_list[item]["meta"]["userName"]
            content = response_list[item]["meta"]["content"]
            rating = response_list[item]["meta"]["score"]

            json_data = {
                "id": id,
                "author": author,
                "title": None,
                "content": content,
                "rating": rating,
                "source": url
            }
            data.append(json_data)

        result = data

    except:
        raise ValueError("Your configuration is not valid!")
    
    return result


# Youtube Scrapper
def get_youtube_comment(url, max_count):
    data = []

    try:
        config = YoutubeScrapperConfig(
           video_url = url,
           max_comments = max_count,
           lookup_period = LOOKUP_PERIOD
        )
        response = YoutubeScrapperSource()
        response_list = response.lookup(config)

        for item in range(len(response_list)):
            response_list[item] = dict(response_list[item])
            id = response_list[item]["meta"]["comment_id"]
            author = response_list[item]["meta"]["author"]
            content = response_list[item]["meta"]["text"]            

            json_data = {
                "id": id,
                "author": author,
                "title" :None,
                "content": content,
                "rating": None,
                "source": url
            }
            data.append(json_data)
        
        result = data

    except:
        raise ValueError("Your configuration is not valid!")
    
    return result


# Appstore Scrapper
def get_appstore_comment(url, max_count):
    data = []
    try:
        config = AppStoreScrapperConfig(
            app_url = url,
            lookup_period = LOOKUP_PERIOD,
            max_count = max_count
        )
        response = AppStoreScrapperSource()
        response_list = response.lookup(config)

        for item in range(len(response_list)):
            response_list[item] = dict(response_list[item])
            id = response_list[item]["meta"]["id"]
            author = response_list[item]["meta"]["author_name"]
            title = response_list[item]["meta"]["title"]
            content = response_list[item]["meta"]["content"] 
            rating =  response_list[item]["meta"]["rating"]          

            json_data = {
                "id": id,
                "author": author,
                "title": title,
                "content": content,
                "rating": rating,
                "source": url
            }
            data.append(json_data)

        result = data

    except:
        raise ValueError("Your configuration is not valid!")
    
    return result


# Website Scrapper
def get_website_comment(urls):
    data = []

    try:
        config = TrafilaturaCrawlerConfig(urls=urls)
        response = TrafilaturaCrawlerSource()
        response_list = response.lookup(config)

        for item in range(len(response_list)):
            response_list[item] = dict(response_list[item])
            id = response_list[item]["meta"]["id"]
            author = response_list[item]["meta"]["author"]
            title = response_list[item]["meta"]["title"]
            content = response_list[item]["meta"]["raw_text"]

            json_data = {
                "id": id,
                "author": author,
                "title": title,
                "content": content,
                "rating": None,
                "source": urls[0]
            }
            data.append(json_data)

        result = data

    except:
        raise ValueError("Your configuration is not valid!")
        
    return result


# Reddit Scrapper
def get_reddit_comment(url):
    data = []
    try:
        config = RedditScrapperConfig(
            url=url,
            lookup_period = LOOKUP_PERIOD
        )
        response = RedditScrapperSource()
        response_list = response.lookup(config)

        for item in range(len(response_list)):
            response_list[item] = dict(response_list[item])
            id = response_list[item]["meta"]["id"]
            author = response_list[item]["meta"]["author_name"]
            content = response_list[item]["meta"]["extracted_text"]

            json_data = {
                "id": id,
                "author": author,
                "title": None,
                "content": content,
                "rating": None,
                "source": url
            }
            data.append(json_data)

        result = data

    except:
        raise ValueError("Your configuration is not valid!")
        
    return result


# Google News Scrapper
def get_google_news(query, max_results):
    data = []
    try:
        config = GoogleNewsConfig(
            query = query,
            max_results = max_results, 
            lookup_period = LOOKUP_PERIOD,
            language = LANGUAGE,
            country = COUNTRY
        )  
        response = GoogleNewsSource()
        response_list = response.lookup(config)

        for item in range(len(response_list)):
            response_list[item] = dict(response_list[item])
            id = response_list[item]["meta"]["extracted_data"]["id"]
            author = response_list[item]["meta"]["publisher"]["title"]
            title = response_list[item]["meta"]["title"]
            content = response_list[item]["meta"]["extracted_data"]["raw_text"]
            source = response_list[item]["meta"]["url"]

            json_data = {
                "id": id,
                "author": author,
                "title": title,
                "content": content,
                "rating": None,
                "source": source
            }
            data.append(json_data)

        result = data

    except:
        raise ValueError("Your configuration is not valid!")

    return result