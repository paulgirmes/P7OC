import os, sys
import googlemaps
import pytest
import requests

import sys

from app.models import search_request
from app.config import Config


word_list = ["OpenClassrooms", "Salut", "GrandPy", "connais"]
formatted_address = [
    {
        "formatted_address": "7 Cité Paradis, 75010 Paris, France",
        "geometry": {
            "location": {"lat": -33.8599358, "lng": 151.2090295},
            "viewport": {
                "northeast": {"lat": -33.85824767010727, "lng": 151.2102470798928},
                "southwest": {"lat": -33.86094732989272, "lng": 151.2075474201073},
            },
        },
        "name": "OpenClassrooms",
        "opening_hours": {"open_now": False, "weekday_text": []},
        "photos": [
            {
                "height": 2268,
                "html_attributions": [
                    '\u003ca href="https://maps.google.com/maps/contrib/113202928073475129698/photos"\u003eEmily Zimny\u003c/a\u003e'
                ],
                "photo_reference": "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                "width": 4032,
            }
        ],
        "rating": 4.3,
    },
    {
        "formatted_address": "7 Cité Paradis, 75010 Paris, France",
        "geometry": {
            "location": {"lat": -33.8599358, "lng": 151.2090295},
            "viewport": {
                "northeast": {"lat": -33.85824767010727, "lng": 151.2102470798928},
                "southwest": {"lat": -33.86094732989272, "lng": 151.2075474201073},
            },
        },
        "name": "Museum of Contemporary Art Australia",
        "opening_hours": {"open_now": False, "weekday_text": []},
        "photos": [
            {
                "height": 2268,
                "html_attributions": [
                    '\u003ca href="https://maps.google.com/maps/contrib/113202928073475129698/photos"\u003eEmily Zimny\u003c/a\u003e'
                ],
                "photo_reference": "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                "width": 4032,
            }
        ],
        "rating": 4.3,
    },
]

candidates = list(
    [x["name"] + " situé " + x["formatted_address"] for x in formatted_address]
)


class Test_parser:

    test_entries = [
        "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
        "24444 fes68 zzsrnt4 rs54eqv654 sftrts     *ù(^$^:)à'ç(k",
    ]
    filter_expected_results = [
        ["Salut", "GrandPy", "connais", "adresse", "OpenClassrooms"],
        ["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"],
    ]
    prioritize_expected_results = [
        ["OpenClassrooms", "Salut", "GrandPy", "connais"],
        ["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"],
    ]

    def test_filter(self):
        for index, value in enumerate(Test_parser.test_entries):
            parser = search_request.Parser(
                value, Config.filter, "stopwords.json", "stopwords.json"
            )
            assert parser.filter() == 0
            assert parser.filtered_result == Test_parser.filter_expected_results[index]

    def test_prioritize(self):
        for index, value in enumerate(Test_parser.filter_expected_results):
            parser = search_request.Parser(
                value, Config.filter, "stopwords.json", "stopwords.json"
            )
            parser.filtered_result = value
            assert parser.prioritize() == 0
            assert (
                parser.prioritized_result
                == Test_parser.prioritize_expected_results[index]
            )


class Maps_MockResponse:
    response = ""

    def __init__(self, key=""):
        pass

    @staticmethod
    def Client(*arg, **kargs):
        pass

    @staticmethod
    def find_place(*arg, **kargs):
        if Maps_MockResponse.response == "ok_1_candidate":
            return {
                "candidates": [
                    {
                        "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                        "geometry": {
                            "location": {"lat": -33.8599358, "lng": 151.2090295},
                            "viewport": {
                                "northeast": {
                                    "lat": -33.85824767010727,
                                    "lng": 151.2102470798928,
                                },
                                "southwest": {
                                    "lat": -33.86094732989272,
                                    "lng": 151.2075474201073,
                                },
                            },
                        },
                        "name": "Museum of Contemporary Art Australia",
                        "opening_hours": {"open_now": False, "weekday_text": []},
                        "photos": [
                            {
                                "height": 2268,
                                "html_attributions": [
                                    '\u003ca href="https://maps.google.com/maps/contrib/113202928073475129698/photos"\u003eEmily Zimny\u003c/a\u003e'
                                ],
                                "photo_reference": "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                                "width": 4032,
                            }
                        ],
                        "rating": 4.3,
                    }
                ],
                "debug_log": {"line": []},
                "status": "OK",
            }

        elif Maps_MockResponse.response == "ok_several_candidates":
            return {
                "candidates": [
                    {
                        "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                        "geometry": {
                            "location": {"lat": -33.8599358, "lng": 151.2090295},
                            "viewport": {
                                "northeast": {
                                    "lat": -33.85824767010727,
                                    "lng": 151.2102470798928,
                                },
                                "southwest": {
                                    "lat": -33.86094732989272,
                                    "lng": 151.2075474201073,
                                },
                            },
                        },
                        "name": "OpenClassrooms",
                        "opening_hours": {"open_now": False, "weekday_text": []},
                        "photos": [
                            {
                                "height": 2268,
                                "html_attributions": [
                                    '\u003ca href="https://maps.google.com/maps/contrib/113202928073475129698/photos"\u003eEmily Zimny\u003c/a\u003e'
                                ],
                                "photo_reference": "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                                "width": 4032,
                            }
                        ],
                        "rating": 4.3,
                    },
                    {
                        "formatted_address": "7 Cité Paradis, 75010 Paris, France",
                        "geometry": {
                            "location": {"lat": -33.8599358, "lng": 151.2090295},
                            "viewport": {
                                "northeast": {
                                    "lat": -33.85824767010727,
                                    "lng": 151.2102470798928,
                                },
                                "southwest": {
                                    "lat": -33.86094732989272,
                                    "lng": 151.2075474201073,
                                },
                            },
                        },
                        "name": "Museum of Contemporary Art Australia",
                        "opening_hours": {"open_now": False, "weekday_text": []},
                        "photos": [
                            {
                                "height": 2268,
                                "html_attributions": [
                                    '\u003ca href="https://maps.google.com/maps/contrib/113202928073475129698/photos"\u003eEmily Zimny\u003c/a\u003e'
                                ],
                                "photo_reference": "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                                "width": 4032,
                            }
                        ],
                        "rating": 4.3,
                    },
                ],
                "debug_log": {"line": []},
                "status": "OK",
            }

        elif Maps_MockResponse.response == "no_results":
            return {"candidates": [], "status": "NO_RESULTS"}


class Test_Gmap_address:
    def gmaps_mock_get(self, response_type):
        Maps_MockResponse.response = response_type
        return Maps_MockResponse

    def test_find_address(self, monkeypatch):
        expected = "7 Cité Paradis, 75010 Paris, France"

        monkeypatch.setattr(
            "app.models.search_request.googlemaps.Client", self.gmaps_mock_get("ok_1_candidate")
        )
        address = search_request.Gmap_address(word_list, "xxx")
        assert address.find_address() == 0
        assert address.formatted_address == expected
        assert address.location == {"lat": -33.8599358, "lng": 151.2090295}

        monkeypatch.setattr(
            "app.models.search_request.googlemaps.Client", self.gmaps_mock_get("no_results")
        )
        address = search_request.Gmap_address(word_list, "xxx")
        assert address.find_address() == 1
        assert address.formatted_address == ""

        monkeypatch.setattr(
            "app.models.search_request.googlemaps.Client",
            self.gmaps_mock_get("ok_several_candidates"),
        )
        address = search_request.Gmap_address(word_list, "xxx")
        assert address.find_address() == candidates


class Wiki_MockResponse:

    R = 0

    @staticmethod
    def Session(*arg, **kargs):
        pass

    @staticmethod
    def get(url="", params={}):
        try:
            params["list"] == "geosearch"
            Wiki_MockResponse.R = 1
        except:
            Wiki_MockResponse.R = 0
        return Wiki_MockResponse

    @staticmethod
    def json(*arg, **kargs):
        if Wiki_MockResponse.R == 1:
            return {
                "batchcomplete": "",
                "query": {
                    "geosearch": [
                        {
                            "pageid": 18618509,
                            "ns": 0,
                            "title": "Wikimedia Foundation",
                            "lat": 37.7891838,
                            "lon": -122.4033522,
                            "dist": 0,
                            "primary": "",
                        },
                        {
                            "pageid": 42936625,
                            "ns": 0,
                            "title": "Foxcroft Building",
                            "lat": 37.789166666667,
                            "lon": -122.40333333333,
                            "dist": 2.5,
                            "primary": "",
                        },
                    ]
                },
            }
        else:
            return {
                "batchcomplete": "true",
                "query": {
                    "normalized": [
                        {"fromencoded": "false", "from": "Pet_door", "to": "Pet door"}
                    ],
                    "pages": [
                        {
                            "pageid": 3276454,
                            "ns": 0,
                            "title": "Pet door",
                            "extract": "A pet door or pet flap (also referred to in more specific terms, such as cat flap, cat door, dog door, or doggy door) is a small opening to allow pets to enter and exit a building on their own without needing a person to open the door.",
                        }
                    ],
                },
            }


class Test_wiki:
    def wikimock_get(self):
        return Wiki_MockResponse()

    def test_wikiself(self, monkeypatch):
        monkeypatch.setattr(requests, "Session", self.wikimock_get)
        wiki = search_request.Wiki_search({"lat": -33.8599358, "lng": 151.2090295}, 500, "stopwords.json")
        assert wiki.find_wiki_content() == 0
        assert (
            "A pet door or pet flap (also referred to in more specific terms, such as cat flap, cat door, dog door, or doggy door) is a small opening to allow pets to enter and exit a building on their own without needing a person to open the door. Plus d'informations ici <a href='https://fr.wikipedia.org/wiki/Pet_door'>https://fr.wikipedia.org/wiki/Pet_door</a>"
            in wiki.wiki_text
        )


class Mock_parser:

    return_type = ""

    def __init__(self, *args, **kwargs):
        self.prioritized_result = ["XXX", "YYY", "ZZZ"]

    def filter(self, *args, **kwargs):
        if Mock_parser.return_type == "pass":
            return 0
        else:
            return 1

    def prioritize(self, *args, **kwargs):
        if Mock_parser.return_type == "pass":
            return 0
        else:
            return 1


class Mock_Gmap_address:

    return_type = ""

    def __init__(self, *args, **kwargs):
        self.prioritized_result = ["XXX", "YYY", "ZZZ"]
        self.location = {"lat": -33.8599358, "lng": 151.2090295}
        self.formatted_address = "7 Cité Paradis, 75010 Paris, France"

    def find_address(self, *args, **kwargs):
        if Mock_Gmap_address.return_type == "pass":
            return 0
        elif Mock_Gmap_address.return_type == "several_results":
            return candidates
        else:
            return 1


class Mock_wiki:

    return_type = ""

    def __init__(self, *args, **kwargs):
        self.wiki_text = "an interesting thing about location with a random intro and a link to the wiki page!"

    def find_wiki_content(self):
        if Mock_wiki.return_type == "pass":
            return 0
        else:
            self.wiki_text = "Nooooooooothing found about this place, or failed"
            return 1


class Test_request:
    def get_parser_mock(self, return_type):
        Mock_parser.return_type = return_type
        return Mock_parser

    def get_gmap_adress_mock(self, return_type):
        Mock_Gmap_address.return_type = return_type
        return Mock_Gmap_address

    def get_wiki_mock(self, return_type):
        Mock_wiki.return_type = return_type
        return Mock_wiki

    def test_process_pass(self, monkeypatch):
        monkeypatch.setattr("app.models.search_request.Parser", self.get_parser_mock("pass"))
        monkeypatch.setattr(
            "app.models.search_request.Gmap_address", self.get_gmap_adress_mock("pass")
        )
        monkeypatch.setattr("app.models.search_request.Wiki_search", self.get_wiki_mock("pass"))
        request = search_request.Request("bla bla")

        assert request.process() == {
            "status": "OK",
            "adresses_answer": "A mon avis l'adresse est la suivante : 7 Cité Paradis, 75010 Paris, France",
            "wiki_answer": "an interesting thing about location with a random intro and a link to the wiki page!",
            "coordinates": {"lat": -33.8599358, "lng": 151.2090295},
        }

    def process_several_results(self, monkeypatch):
        monkeypatch.setattr("app.models.search_request.Parser", self.get_parser_mock("pass"))
        monkeypatch.setattr(
            "app.models.search_request.Gmap_address", self.get_gmap_adress_mock("several_results")
        )
        monkeypatch.setattr("app.models.search_request.Wiki_search", self.get_wiki_mock("pass"))

        request = search_request.Request("bla bla")
        result = request.process()
        assert result["status"] == "Several_results"
        assert result()["wiki_answer"] == ""
        assert request.process()["coordinates"] == {}
        assert type(
            result["adresses_answer"]
        ) == "j'ai plusieurs idées, peux-tu me préciser le nom et l'adresse que tu veux trouver ?" + " " + ", ".join(
            candidates
        )

    def process_fail(self, monkeypatch):
        request = search_request.Request("bla bla")
        monkeypatch.setattr("app.models.search_request.Parser", self.get_parser_mock("fail"))
        result = request.process()
        assert result["status"] == "NOT_PROCESSED"
        assert result["wiki_answer"] == ""
        assert result["coordinates"] == {}
        assert type(result["adresses_answer"]) == type(str(""))

        monkeypatch.setattr("app.models.search_request.Parser", self.get_parser_mock("pass"))
        monkeypatch.setattr(
            "app.models.search_request.Gmap_address", self.get_gmap_adress_mock("fail")
        )
        result = request.process()
        assert result["status"] == "NO_RESULTS"
        assert result["wiki_answer"] == ""
        assert result["coordinates"] == {}
        assert type(result["adresses_answer"]) == type(str(""))

        monkeypatch.setattr("app.models.search_request.Parser", self.get_parser_mock("pass"))
        monkeypatch.setattr(
            "app.models.search_request.Gmap_address", self.get_gmap_adress_mock("several_results")
        )
        monkeypatch.setattr("app.models.search_request.Wiki_search", self.get_wiki_mock("fail"))

        result = request.process()
        assert result["status"] == "OK_WIKI_FAILED"
        assert (
            result["wiki_answer"] == "Nooooooooothing found about this place, or failed"
        )
        assert result["coordinates"] == {"lat": -33.8599358, "lng": 151.2090295}
        assert (
            result["adresses_answer"]
            == "A mon avis l'adresse est la suivante : 7 Cité Paradis, 75010 Paris, France"
        )
