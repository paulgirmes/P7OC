# -*- coding: utf8 -*-

import json
import os
import re
import requests
import googlemaps
import random

if __name__ == "__main__":

    import sys
    dossier = os.path.dirname(os.path.abspath(__file__))
    while not dossier.endswith('app'):
        dossier = os.path.dirname(dossier)
    dossier = os.path.dirname(dossier)
    if dossier not in sys.path:
        sys.path.append(dossier)
from app.config import Config


class Request():
    
    def __init__(self, text):
        self.text_to_process = text
        self.filtered_result = []
        self.prioritized_result = []
        self.formatted_address = ""
        self.location = {}
        self.name  = ""
        self.candidates = []
    
    
    def filter(self):
        try:
            result = re.findall(Config.filter, self.text_to_process)        
            stopwords = []
            with open(os.path.dirname(os.path.abspath(__file__))+"\\stopwords.json", encoding='utf8') as f:
                data = json.load(f)
            [stopwords.append(item) for item in data["stop_words"]]
            lower_result = re.findall(Config.filter, self.text_to_process.lower())
            for word in stopwords:
                try :
                    result.pop(lower_result.index(word))
                    lower_result.pop(lower_result.index(word))
                except:
                    pass
        except:
            raise
        else:    
            self.filtered_result = result
            return 0

    def prioritize(self):
        words = []
        results = []
        try:
            with open(os.path.dirname(os.path.abspath(__file__))+"\\stopwords.json", encoding='utf8') as f:
                data = json.load(f)
                [words.append(item) for item in data["priority_words"]]
            [results.append(self.filtered_result[self.filtered_result.index(word)+1]) for word in words if word in self.filtered_result]
            for item in self.filtered_result:
                x = "".join(re.findall("(^[A-Z][a-zA-Z]+)", item))
                if x not in results and x != '':
                    results.append(x)        
            [results.append(item) for item in self.filtered_result if not item in results and not item in words]
        except:
            raise
        else:
            self.prioritized_result = results
            return 0

    def find_address(self):
        try:
            gmaps = googlemaps.Client(key=Config.google_api)
            i = len(self.prioritized_result)
            while i > 0:
                result = gmaps.find_place(input=(" ".join(self.prioritized_result[0:(i-1)])), input_type="textquery",language="french",
                fields=["name", "formatted_address", "geometry/location"])
                if result["status"] == "OK":
                    x = len(result.get("candidates"))
                    if x == 1:
                        self.formatted_address=(result.get("candidates")[0]).get("formatted_address")
                        self.name = (result.get("candidates")[0]).get("name")
                        self.location = (result.get("candidates")[0]).get("location")
                        return 0
                    elif x > 1:
                        self.candidates = result.get("candidates")
                        return self.candidates
                else:
                    i-=1
            return 1
        except:
            raise

    def find_wiki_content(self):
        try:
            S = requests.Session()

            URL = "https://fr.wikipedia.org/w/api.php"

            params = {
                "format": "json",
                "list": "geosearch",
                "gscoord": (str(self.location["lat"])+"|"+str(self.location["lng"])),
                "gslimit": "3",
                "gsradius": "500",
                "action": "query"
            }

            R = S.get(url=URL, params=params)
            data = R.json()
            places = data['query']['geosearch']
            
            if len(places)>0:
                for place in places:
                    print(place['title'])
                i = random.randint(0, (len(places)-1))
                page = places[i]['title']
                U = S.get(url=URL, params={"action":"query","format":"json","prop":"extracts","titles":page,"formatversion":"2","exsentences":"2","exlimit":"1","explaintext":"1", "exsectionformat":"plain"})
                return(U.json()["query"]["pages"][0]["extract"])
            else:
                with open(os.path.dirname(os.path.abspath(__file__))+"\\stopwords.json", encoding='utf8') as f:
                    mots=json.load(f)
                print(mots["no_wiki"][random.randint(0, (len(mots["no_wiki"])-1))])
        except:
            raise

    def process(self):
        return None 

if __name__ == "__main__":
    pass