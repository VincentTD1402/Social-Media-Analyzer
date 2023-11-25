from scrapper.scrapper import get_website_comment
import pandas as pd

web_list = ["https://en.wikipedia.org/wiki/Aur%C3%A9lien_Wiik", "https://en.wikipedia.org/wiki/Wiik"]

data = []

for web in web_list:
    result = get_website_comment([web])
    data.append(result)
    print(data)

frame = pd.DataFrame(data)

frame.to_csv('data.csv')
