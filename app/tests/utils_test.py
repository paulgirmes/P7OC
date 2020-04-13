
import os, sys
import googlemaps
import pytest
import requests
if __name__ == "__main__":

    import sys
    dossier = os.path.dirname(os.path.abspath(__file__))
    while not dossier.endswith('app'):
        dossier = os.path.dirname(dossier)
    dossier = os.path.dirname(dossier)
    if dossier not in sys.path:
        sys.path.append(dossier)
import app.utils.utils as utils


class Maps_MockResponse:
  
    @staticmethod
    def Client(*arg, **kargs):
        pass
    @staticmethod
    def find_place(*arg, **kargs):
        return {"candidates" : [{"formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                "geometry" : {"location" : {"lat" : -33.8599358,"lng" : 151.2090295},
                "viewport" : {"northeast" : {"lat" : -33.85824767010727,"lng" : 151.2102470798928},
                "southwest" : {"lat" : -33.86094732989272,"lng" : 151.2075474201073}}},
                "name" : "Museum of Contemporary Art Australia","opening_hours" : {"open_now" : False,"weekday_text" : []},
                "photos" : [{"height" : 2268,"html_attributions" : ["\u003ca href=\"https://maps.google.com/maps/contrib/113202928073475129698/photos\"\u003eEmily Zimny\u003c/a\u003e"],
                "photo_reference" : "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                "width" : 4032}],"rating" : 4.3}],"debug_log" : {"line" : []},"status" : "OK"}

class Maps_MockResponse2:

    @staticmethod
    def Client(*arg, **kargs):
        pass
    @staticmethod
    def find_place(*arg, **kargs):
        return {"candidates" : [],"status" : "NO_RESULTS"}

class Maps_MockResponse3:
   
    @staticmethod
    def Client(*arg, **kargs):
        pass
    @staticmethod
    def find_place(*arg, **kargs):
        return {"candidates" : [{"formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                "geometry" : {"location" : {"lat" : -33.8599358,"lng" : 151.2090295},
                "viewport" : {"northeast" : {"lat" : -33.85824767010727,"lng" : 151.2102470798928},
                "southwest" : {"lat" : -33.86094732989272,"lng" : 151.2075474201073}}},
                "name" : "OpenClassrooms","opening_hours" : {"open_now" : False,"weekday_text" : []},
                "photos" : [{"height" : 2268,"html_attributions" : ["\u003ca href=\"https://maps.google.com/maps/contrib/113202928073475129698/photos\"\u003eEmily Zimny\u003c/a\u003e"],
                "photo_reference" : "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                "width" : 4032}],"rating" : 4.3},{"formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                "geometry" : {"location" : {"lat" : -33.8599358,"lng" : 151.2090295},
                "viewport" : {"northeast" : {"lat" : -33.85824767010727,"lng" : 151.2102470798928},
                "southwest" : {"lat" : -33.86094732989272,"lng" : 151.2075474201073}}},
                "name" : "Museum of Contemporary Art Australia","opening_hours" : {"open_now" : False,"weekday_text" : []},
                "photos" : [{"height" : 2268,"html_attributions" : ["\u003ca href=\"https://maps.google.com/maps/contrib/113202928073475129698/photos\"\u003eEmily Zimny\u003c/a\u003e"],
                "photo_reference" : "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                "width" : 4032}],"rating" : 4.3}],"debug_log" : {"line" : []},"status" : "OK"}

class Maps_MockResponse4:
   
    @staticmethod
    def Client(*arg, **kargs):
        pass
    @staticmethod
    def find_place(*arg, **kargs):
        return {"candidates" : [],"debug_log" : {"line" : []},"status" : "NO_RESULTS"}


class Wiki_MockResponse():
    
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
            return {"batchcomplete": "","query": {"geosearch": [{"pageid": 18618509,
                "ns": 0,
                "title": "Wikimedia Foundation",
                "lat": 37.7891838,
                "lon": -122.4033522,
                "dist": 0,
                "primary": ""},
                {"pageid": 42936625,
                "ns": 0,
                "title": "Foxcroft Building",
                "lat": 37.789166666667,
                "lon": -122.40333333333,
                "dist": 2.5,
                "primary": ""}]}}
        else:
            return {"batchcomplete": "true","query": {"normalized": [{"fromencoded": "false","from": "Pet_door","to": "Pet door"}],
                    "pages": [{"pageid": 3276454,"ns": 0,"title": "Pet door",
                    "extract": "A pet door or pet flap (also referred to in more specific terms, such as cat flap, cat door, dog door, or doggy door) is a small opening to allow pets to enter and exit a building on their own without needing a person to open the door."}]}}


class Test_request():

    formatted_address = [{"formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                "geometry" : {"location" : {"lat" : -33.8599358,"lng" : 151.2090295},
                "viewport" : {"northeast" : {"lat" : -33.85824767010727,"lng" : 151.2102470798928},
                "southwest" : {"lat" : -33.86094732989272,"lng" : 151.2075474201073}}},
                "name" : "OpenClassrooms","opening_hours" : {"open_now" : False,"weekday_text" : []},
                "photos" : [{"height" : 2268,"html_attributions" : ["\u003ca href=\"https://maps.google.com/maps/contrib/113202928073475129698/photos\"\u003eEmily Zimny\u003c/a\u003e"],
                "photo_reference" : "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                "width" : 4032}],"rating" : 4.3},{"formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                "geometry" : {"location" : {"lat" : -33.8599358,"lng" : 151.2090295},
                "viewport" : {"northeast" : {"lat" : -33.85824767010727,"lng" : 151.2102470798928},
                "southwest" : {"lat" : -33.86094732989272,"lng" : 151.2075474201073}}},
                "name" : "Museum of Contemporary Art Australia","opening_hours" : {"open_now" : False,"weekday_text" : []},
                "photos" : [{"height" : 2268,"html_attributions" : ["\u003ca href=\"https://maps.google.com/maps/contrib/113202928073475129698/photos\"\u003eEmily Zimny\u003c/a\u003e"],
                "photo_reference" : "CmRaAAAAfxSORBfVmhZcERd-9eC5X1x1pKQgbmunjoYdGp4dYADIqC0AXVBCyeDNTHSL6NaG7-UiaqZ8b3BI4qZkFQKpNWTMdxIoRbpHzy-W_fntVxalx1MFNd3xO27KF3pkjYvCEhCd--QtZ-S087Sw5Ja_2O3MGhTr2mPMgeY8M3aP1z4gKPjmyfxolg",
                "width" : 4032}],"rating" : 4.3}]
    candidates = list([x["name"]+" au "+ x["formatted_address"] for x in formatted_address])

    @pytest.fixture(scope="class")
    def setup_function(self, request):
        r = utils.Request("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
        return r

    def mock_get(self, *args,**kargs):
            return Maps_MockResponse()
    def mock_get2(self, *args,**kargs):
        return Maps_MockResponse2()
    def mock_get3(self, *args,**kargs):
            return Maps_MockResponse3()
    def wikimock_get(self, *args,**kargs):   
            return Wiki_MockResponse()
    def mock_get4(self, *args,**kargs):
            return Maps_MockResponse4()

    def test_filter(self):
        test_phrases = ["Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
        "24444 fes68 zzsrnt4 rs54eqv654 sftrts     *ù(^$^:)à'ç(k"]
        expected =[["Salut", "GrandPy", "connais", "adresse", "OpenClassrooms"],["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"]]
        for index, value in enumerate(test_phrases):
            x = utils.Request(value)
            assert x.filter() == 0
            assert x.filtered_result == expected[index]
    
    def test_prioritize(self):
        filter_results = [["Salut", "GrandPy", "connais", "adresse", "OpenClassrooms"],
        ["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"]]
        expected = [["OpenClassrooms", "Salut", "GrandPy", "connais"],["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"]]
        for index, value in enumerate(filter_results):
            x = utils.Request("")
            x.filtered_result = value
            assert x.prioritize() == 0 
            assert x.prioritized_result ==  expected[index]
    
    def test_find_address(self, monkeypatch):
        expected = "7 Cité Paradis, 75010 Paris, France"

        monkeypatch.setattr(googlemaps, "Client", self.mock_get)
        x = utils.Request("")
        x.prioritized_result=["OpenClassrooms", "Salut", "GrandPy", "connais"]
        x.find_address()
        print(x.formatted_address)
        assert x.find_address() == 0
        assert x.formatted_address ==  expected
        assert x.location == {"lat" : -33.8599358,"lng" : 151.2090295}

        monkeypatch.setattr(googlemaps, "Client", self.mock_get2)
        x = utils.Request("")
        x.prioritized_result=["OpenClassrooms", "Salut", "GrandPy", "connais"]
        x.find_address()
        assert x.find_address() == 1
        assert x.formatted_address ==  ""

        monkeypatch.setattr(googlemaps, "Client", self.mock_get3)
        x = utils.Request("")
        x.prioritized_result=["OpenClassrooms", "Salut", "GrandPy", "connais"]
        x.find_address()
        assert x.find_address() == self.candidates

    def test_wikiself(self, monkeypatch, setup_function):
            
        monkeypatch.setattr(requests, "Session", self.wikimock_get)
        setup_function.location = {"lat" : -33.8599358,"lng" : 151.2090295}
        assert setup_function.find_wiki_content() == 0
        assert setup_function.wiki == "A pet door or pet flap (also referred to in more specific terms, such as cat flap, cat door, dog door, or doggy door) is a small opening to allow pets to enter and exit a building on their own without needing a person to open the door. Plus d'informations ici https://en.wikipedia.org/wiki/Pet_door"
        setup_function.location = {}
        setup_function.wiki = ""

    def test_process(self, monkeypatch, setup_function):
        monkeypatch.setattr(googlemaps, "Client", self.mock_get3)
        assert setup_function.process() == {"status" : "SEVERAL_ADRESS",
                                        "adresses_answer" : "j'ai plusieurs idées, peux-tu me préciser le nom et l'adresse que tu veux trouver ?" +" "+", ".join(self.candidates),
                                        "wiki_answer" : "", 
                                        "coordinates" : {}}

        monkeypatch.setattr(googlemaps, "Client", self.mock_get4)
        assert setup_function.process() == {"status" : "NO_RESULTS", 
                                        "adresses_answer" : "je n'arrive pas à te comprendre PARLES PLUS FORT !!!",
                                        "wiki_answer" : "", 
                                        "coordinates" : {}}
                                        
        monkeypatch.setattr(googlemaps, "Client", self.mock_get)
        monkeypatch.setattr(requests, "Session", self.wikimock_get)
        assert setup_function.process() == {"status" : "OK",
                                        "adresses_answer" : "l'adresse est la suivante : 7 Cité Paradis, 75010 Paris, France",
                                        "wiki_answer" : "A pet door or pet flap (also referred to in more specific terms, such as cat flap, cat door, dog door, or doggy door) is a small opening to allow pets to enter and exit a building on their own without needing a person to open the door. Plus d'informations ici https://en.wikipedia.org/wiki/Pet_door",
                                        "coordinates" : {"lat" : -33.8599358,"lng" : 151.2090295}}





    