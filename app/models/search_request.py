# -*- coding: utf8 -*-
"""
Class definition to process any address request of type string and find an address, location and a wiki page nearby if possible.
To use the entire module : first Create an instance of Request("request to be processed") then Request.process()
"""
import json
import os
import re
import requests
import googlemaps
import random

from app.config import Config


class Request:
    """
    Takes a question to be processed in the form of a string, returns a dict in the form of 
            {
                "status": "",
                "adresses_answer": ""
                "wiki_answer": ""
                "coordinates": {}
            } 
    """

    def __init__(self, text):
        self.__status = "NOT_PROCESSED"
        self.text_to_process = text

    def process(self):
        """
        process self.text_to_process through parser, Gmap_address, Wiki_search, return a dict() object in the form of : 
        {
            "status": "",
            "adresses_answer": ""
            "wiki_answer": ""
            "coordinates": {}
        } 
        values of which are depending on the returns of the different Classes methods.
        "status" value is to ne used to know what is the state of the processed request :
        - "NOT_PROCESSED" => either Request.process() has not be used or the parser has failed
        - "NO_RESULTS" => failure to find an address
        - "OK" => address and wiki are found, 
        - "OK_WIKI_FAILED" => address found, no wiki found, a standard answer is still returned in "wiki_answer"
        - "SEVERAL_ADRESS" => several candidates were found for the address.
        """
        parser = Parser(
            self.text_to_process, Config.filter, "stopwords.json", "stopwords.json"
        )
        if parser.filter() == 0 and parser.prioritize() == 0:
            self.__status = "PARSER_OK"
            address = Gmap_address(parser.prioritized_result, Config.google_api)
            address_return = address.find_address()

            if address_return == 0:
                self.__status = "ADDRESS_OK"
                wiki = Wiki_search(address.location, "500", "stopwords.json")

                if wiki.find_wiki_content() == 0:
                    self.__status = "OK"
                    return self.return_format(
                        "stopwords.json",
                        "result_ok",
                        wiki.wiki_text,
                        address.location,
                        address.formatted_address,
                    )
                else:
                    self.__status = "OK_WIKI_FAILED"
                    return self.return_format(
                        "stopwords.json",
                        "result_ok",
                        wiki.wiki_text,
                        address.location,
                        address.formatted_address,
                    )

            elif address_return == 1:
                self.__status = "NO_RESULTS"
                return self.return_format("stopwords.json", "no_results", "", {})

            else:
                self.__status = "SEVERAL_ADRESS"
                return self.return_format(
                    "stopwords.json",
                    "Several_results",
                    "",
                    {},
                    (" ou: ".join(address_return) + " ?"),
                )
        else:
            self.__status = "NOT_PROCESSED"
            return self.return_format("stopwords.json", "no_results", "", {})

    def return_format(self, json_file, json_key, wiki, location, *args):
        """
        takes a JSON file as string, a key as string, a location as a dict and *args
        return a dict() in the form of
        {
            "status": self.__status,
            "adresses_answer": "a random choice between json-key of json_file" + " concatenation of *args in the form of a string if any *args
            "wiki_answer": wiki
            "coordinates": location
        }  
        """
        with open(
            os.path.dirname(os.path.abspath(__file__)) + "/"+ json_file,
            encoding="utf8",
        ) as f:
            data = json.load(f)

        if len(args) == 0:
            return {
                "status": self.__status,
                "adresses_answer": random.choice(data[str(json_key)]),
                "wiki_answer": wiki,
                "coordinates": location,
            }
        else:
            return {
                "status": self.__status,
                "adresses_answer": random.choice(data[str(json_key)])
                + " "
                + ", ".join([str(arg) for arg in args]),
                "wiki_answer": wiki,
                "coordinates": location,
            }


class Parser:
    """
    Used to parse and prioritize any string (self.text_to_parse) given a regex (self.regex), 
    stopwords (stopwords_file_Json) and an optional priority words file (priority_words_file_Json used by self.prioritize) both of the JSON format
    """

    def __init__(
        self, text_to_parse, regex, stopwords_file_Json, priority_words_file_Json=None
    ):
        self.text_to_parse = text_to_parse
        self.filtered_result = []
        self.prioritized_result = []
        self.stopwords = stopwords_file_Json
        self.priortywords = priority_words_file_Json
        self.regex = regex

    def filter(self):
        """
        applies a regex (self.regex) to a to a string (self.text_to_parse) then removes from the resulting list any words that matches the words["stop_words"]
        contained in self.stopwords JSON file (case independent).
        returns 0 and affect the result in the form af a list in self.filtered_result in case of success.
        returns 1 in case of any failure
        """

        try:
            result = re.findall(self.regex, self.text_to_parse)
            stopwords = set()
            with open(
                os.path.dirname(os.path.abspath(__file__)) + "/" + self.stopwords,
                encoding="utf8",
            ) as f:
                data = json.load(f)
            [stopwords.add(item) for item in data["stop_words"]]
            words_to_remove = []
            [
                words_to_remove.append(word)
                for word in result
                if word in stopwords or word.lower() in stopwords
            ]
            [result.remove(word) for word in words_to_remove]

        except:
            return 1
        else:
            self.filtered_result = result
            return 0

    def prioritize(self):
        """
        ordonates words from a list (self.filtered_result) given words["priority_words"] from a json file (self.priortywords)
        returns a re-ordered list with any words of self.filtered_result that are placed one index before words
        that matches prirority words if any,
        then words that begins with a capital letter if any then the remainder of words.
        """
        words = []
        results = []
        try:
            with open(
                os.path.dirname(os.path.abspath(__file__)) + "/" + self.priortywords,
                encoding="utf8",
            ) as f:
                data = json.load(f)
                [words.append(item) for item in data["priority_words"]]
            [
                results.append(
                    self.filtered_result[self.filtered_result.index(word) + 1]
                )
                for word in words
                if word in self.filtered_result
            ]
            for item in self.filtered_result:
                x = "".join(re.findall("(^[A-Z][a-zA-Z]+)", item))
                if x not in results and x != "":
                    results.append(x)
            [
                results.append(item)
                for item in self.filtered_result
                if not item in results and not item in words
            ]
        except:
            return 1
        else:
            self.prioritized_result = results
            return 0


class Gmap_address:
    """
    used to find an address and a location from a give word list,
    a google-maps valid API key must also be given.
    """

    def __init__(self, word_list, api_key):
        self.word_list = word_list
        self.formatted_address = ""
        self.location = {}
        self.name = ""
        self.candidates = []
        self.api_key = api_key

    def find_address(self):
        """
        makes several queries to google maps API with self.wordlist as text query beginning with all words from the list in a single query
        and continuing with a next query with the last word from self.wordlist removed until no word left.
        returns 0 and affects the result to self.formatted-address (string) and self.location(dict) whenever a single address is returned by gmaps API
        returns a list of candidates if more than one address.
        returns 1 if any failure occurs.
        """
        gmaps = googlemaps.Client(key=self.api_key)
        to_analyse = list(self.word_list)
        i = 0
        while i < len(self.word_list):
            try:
                result = gmaps.find_place(
                    input=(" ".join(to_analyse)),
                    input_type="textquery",
                    language="french",
                    fields=["name", "formatted_address", "geometry/location"],
                    location_bias="ipbias"
                )
                if result["status"] == "OK":
                    x = len(result["candidates"])
                    if x == 1:
                        self.formatted_address = str(
                            result["candidates"][0]["formatted_address"]
                        )
                        self.name = result["candidates"][0]["name"]
                        self.location = result["candidates"][0]["geometry"]["location"]
                        return 0
                    elif x > 1:
                        self.candidates = result["candidates"]
                        return list(
                            [
                                candidate["name"]
                                + " situé "
                                + candidate["formatted_address"]
                                for candidate in result["candidates"]
                            ]
                        )
                else:
                    to_analyse.pop(-1)
            except:
                return 1
            i += 1
        return 1


class Wiki_search:
    """
    used to find an information about a location (self.location), a search radius must be given at init of instance
    """

    def __init__(self, coordinates, search_radius_m, json_file):
        self.location = coordinates
        self.wiki_text = ""
        self.radius = search_radius_m
        self.default_text_file = json_file

    def find_wiki_content(self):
        """
        makes a "geosearch" request to Wikipedia API given coordinates as a dict (self.coordinates)
        and a search radius constraint as a string.
        if any result makes an "extract" request to Wikipedia API with one random result of the previous query.
        returns 0 and affects the text from the extract formatted with an hyperlink to self.wikitext(string)
        and a random text from self.default_text_file["Wiki"],
        returns 1 and affects a random text from self.default_text_file["no_wiki"] in case of no results or any failure occurs.
        """

        try:
            S = requests.Session()

            URL = "https://fr.wikipedia.org/w/api.php"

            params = {
                "format": "json",
                "list": "geosearch",
                "gscoord": (
                    str(self.location["lat"]) + "|" + str(self.location["lng"])
                ),
                "gslimit": "3",
                "gsradius": self.radius,
                "action": "query",
            }

            R = S.get(url=URL, params=params)
            data = R.json()
            places = data["query"]["geosearch"]

            i = random.randint(0, (len(places) - 1))
            page = places[i]["title"]
            U = S.get(
                url=URL,
                params={
                    "action": "query",
                    "format": "json",
                    "prop": "extracts",
                    "titles": page,
                    "formatversion": "2",
                    "exsentences": "2",
                    "exlimit": "1",
                    "explaintext": "1",
                    "exsectionformat": "plain",
                },
            )
            with open(
                os.path.dirname(os.path.abspath(__file__))
                + "/"
                + self.default_text_file,
                encoding="utf8",
            ) as f:
                mots = json.load(f)

            self.wiki_text = (
                mots["Wiki"][random.randint(0, (len(mots["Wiki"]) - 1))]
                + (U.json()["query"]["pages"][0]["extract"])
                + " Plus d'informations ici <a href='https://fr.wikipedia.org/wiki/"
                + (U.json()["query"]["pages"][0]["title"]).replace(" ", "_")
                + "'>"
                + "https://fr.wikipedia.org/wiki/"
                + (U.json()["query"]["pages"][0]["title"]).replace(" ", "_")
                + "</a>"
            )
            return 0
        except:
            with open(
                os.path.dirname(os.path.abspath(__file__))
                + "/"
                + self.default_text_file,
                encoding="utf8",
            ) as f:
                mots = json.load(f)
            self.wiki_text = mots["no_wiki"][random.randint(0, (len(mots["no_wiki"]) - 1))]
            return 1


if __name__ == "__main__":
    pass
