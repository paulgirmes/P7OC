# -*- coding: utf8 -*-

import json
import os
import re
import googlemaps
import warnings

if __name__ == "__main__":
    import sys
    dossier = os.path.dirname(os.path.abspath(__file__))
    while not dossier.endswith('app'):
        dossier = os.path.dirname(dossier)
    dossier = os.path.dirname(dossier)
    if dossier not in sys.path:
        sys.path.append(dossier)
from app.config import Config

class Parser():

    def filter(self, sentence):
        result = re.findall(Config.filter, sentence)        
        stopwords = []
        with open(os.path.dirname(os.path.abspath(__file__))+"\\stopwords.json", encoding='utf8') as f:
            data = json.load(f)
        [stopwords.append(item) for item in data["stop_words"]]
        lower_result = re.findall(Config.filter, sentence.lower())
        for word in stopwords:
            try :
                result.pop(lower_result.index(word))
                lower_result.pop(lower_result.index(word))
            except:
                pass
        return result

    def prioritize(self, w_to_test):
        words = []
        results = []
        with open(os.path.dirname(os.path.abspath(__file__))+"\\stopwords.json", encoding='utf8') as f:
            data = json.load(f)
            [words.append(item) for item in data["priority_words"]]
        
        [results.append(w_to_test[w_to_test.index(word)+1]) for word in words if word in w_to_test]
        for item in w_to_test:
            x = "".join(re.findall("(^[A-Z][a-zA-Z]+)", item))
            if x not in results and x != '':
                results.append(x)
        [results.append(item) for item in w_to_test if not item in results and not item in words]

        return results


class Place():
    
    
    def __init__(self, prioritized_results):
        self.prioritized_results = prioritized_results
        self.formatted_address = ""
        self.place_id = ""
        self.location = ""
        self.name  = ""
        self.candidates = []

    def find_address(self):
        try:
            gmaps = googlemaps.Client(key=Config.google_api)
            result = gmaps.find_place(input=(" ".join(self.prioritized_results)), input_type="textquery", 
            language="french", fields=["name", "formatted_address", "place_id"])
            x = len(result.get("candidates"))
            if x == 1:
                self.formatted_address=(result.get("candidates")[0]).get("formatted_address")
                self.name = (result.get("candidates")[0]).get("name")
                self.place_id = (result.get("candidates")[0]).get("place_id")
                return 0
            elif x > 1:
                self.candidates = result.get("candidates")
                return self.candidates
            elif x==0:
                return 1
        except:
            raise
    
    def find_coordinates(self):
        try:
            gmaps = googlemaps.Client(key=Config.google_api)
            result = gmaps.geocode(self.formatted_address)
            location = (result[0]).get("geometry").get("location")
            self.location = "latitude "+str(location["lat"])+", longitude "+str(location["lng"])
        except:
            raise
        else:
            self.location = "latitude "+str(location["lat"])+", longitude "+str(location["lng"])
            return 0

prioritized_results = ["Ministère", "culture"]
sult = Place(prioritized_results)
print(sult.find_address())
print(sult.formatted_address)