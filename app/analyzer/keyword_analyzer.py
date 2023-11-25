import yake
import re 
from typing import Optional

class KeywordExtraction:
    def __init__(self):
        pass
    #text preprocessing
    @staticmethod
    def pre_filter(text):
        prog = re.compile("^(\\s*([A-Z]))")
        parts = text.split('\n')
        buffer = ''
        for part in parts:
            sep = ' '
            if prog.match(part):
                sep = '\n\n'
            buffer += sep + part.replace('\t',' ').replace('"','')
        return buffer

    @staticmethod
    def keywordpredict(text: Optional[str] = None , lan: Optional[str] = None, max_ngram: Optional[int] = None, numberofkeywords: Optional[int] = None):
        text = KeywordExtraction.pre_filter(text)
        keyword_json = {
            "text":text,
            "keyword":[]
        }
        with open('app/analyzer/vietnames-stopwords.txt', encoding="utf8") as stop_fil:
            stopwords = set(stop_fil.read().lower().split("\n"))
        if lan == "vi" and 10> max_ngram > 0:
            kw_extractor = yake.KeywordExtractor(lan=lan, n=max_ngram, dedupLim=0.9, dedupFunc='seqm', windowsSize=1, top=numberofkeywords, stopwords=stopwords)
            keywords = kw_extractor.extract_keywords(text)
            for kw in keywords:
                keyword_json['keyword'].append(kw)
        elif lan == "en" and 10> max_ngram > 0:
            kw_extractor = yake.KeywordExtractor(lan=lan, n=max_ngram, dedupLim=0.9, dedupFunc='seqm', windowsSize=1, top=numberofkeywords)
            keywords = kw_extractor.extract_keywords(text)
            for kw in keywords:
                keyword_json['keyword'].append(kw)
        else:
            raise ValueError('Your configuration is not valid. lan parameter should be vi or en and max_ngram should be larger than 0 and smaller than 10')
        return keyword_json
