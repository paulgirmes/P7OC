
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
                "name" : "Museum of Contemporary Art Australia","opening_hours" : {"open_now" : False,"weekday_text" : []},
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
                    "extract": "A pet door or pet flap (also referred to in more specific terms, such as cat flap, cat door, dog door, or doggy door) is a small opening to allow pets to enter and exit a building on their own without needing a person to open the door.  Originally simple holes, the modern form is a hinged and often spring-loaded panel or flexible flap, and some are electronically controlled.  They offer a degree of protection against wind, rain, and larger-bodied intruders entering the dwelling. Similar hatches can let dogs through fences at stiles. A related concept is the pet gate, which is easy for humans to open but acts as a secure pet barrier, as well as the automated left- or right-handed pet doors.\n\n\n== Purpose ==\nA pet door is found to be convenient by many owners of companion animals, especially dogs and cats, because it lets the pets come and go as they please, reducing the need for pet-owners to let or take the pet outside manually, and curtailing unwanted behaviour such as loud vocalisation to be let outside, scratching on doors or walls, and (especially in the case of dogs) excreting in the house. They also help to ensure that a pet left outdoors can safely get back into the house in the case of inclement weather.\n\n\n== Features ==\n\nThe simplest type are bottom-weighted flaps hung from the top of the opening, which swing shut on their own, but may be spring-aided to increase wind resistance. These flaps often feature magnets around the edges to help keep the door closed against weather and wind. Some pet doors have side-mounted hinges and swing open like saloon doors."}]}}


class Test_parser():
    

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

        def mock_get(*args,**kargs):
            return Maps_MockResponse()
        def mock_get2(*args,**kargs):
            return Maps_MockResponse2()
        def mock_get3(*args,**kargs):
            return Maps_MockResponse3()

        monkeypatch.setattr(googlemaps, "Client", mock_get)
        x = utils.Request("")
        x.prioritized_result=["OpenClassrooms", "Salut", "GrandPy", "connais"]
        x.find_address()
        print(x.formatted_address)
        assert x.find_address() == 0
        assert x.formatted_address ==  expected

        monkeypatch.setattr(googlemaps, "Client", mock_get2)
        x = utils.Request("")
        x.prioritized_result=["OpenClassrooms", "Salut", "GrandPy", "connais"]
        x.find_address()
        print(x.formatted_address)
        assert x.find_address() == 1
        assert x.formatted_address ==  ""

        monkeypatch.setattr(googlemaps, "Client", mock_get3)
        x = utils.Request("")
        x.prioritized_result=["OpenClassrooms", "Salut", "GrandPy", "connais"]
        x.find_address()
        print(x.formatted_address)
        assert x.find_address() == [{"formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                "geometry" : {"location" : {"lat" : -33.8599358,"lng" : 151.2090295},
                "viewport" : {"northeast" : {"lat" : -33.85824767010727,"lng" : 151.2102470798928},
                "southwest" : {"lat" : -33.86094732989272,"lng" : 151.2075474201073}}},
                "name" : "Museum of Contemporary Art Australia","opening_hours" : {"open_now" : False,"weekday_text" : []},
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

def test_wiki(monkeypatch):

    def wikimock_get(*args,**kargs):   
        return Wiki_MockResponse()
    monkeypatch.setattr(requests, "Session", wikimock_get)
    r = utils.Request("bla")
    r.location = {"lat" : -33.8599358,"lng" : 151.2090295}
    assert r.find_wiki_content() == "A pet door or pet flap (also referred to in more specific terms, such as cat flap, cat door, dog door, or doggy door) is a small opening to allow pets to enter and exit a building on their own without needing a person to open the door.  Originally simple holes, the modern form is a hinged and often spring-loaded panel or flexible flap, and some are electronically controlled.  They offer a degree of protection against wind, rain, and larger-bodied intruders entering the dwelling. Similar hatches can let dogs through fences at stiles. A related concept is the pet gate, which is easy for humans to open but acts as a secure pet barrier, as well as the automated left- or right-handed pet doors.\n\n\n== Purpose ==\nA pet door is found to be convenient by many owners of companion animals, especially dogs and cats, because it lets the pets come and go as they please, reducing the need for pet-owners to let or take the pet outside manually, and curtailing unwanted behaviour such as loud vocalisation to be let outside, scratching on doors or walls, and (especially in the case of dogs) excreting in the house. They also help to ensure that a pet left outdoors can safely get back into the house in the case of inclement weather.\n\n\n== Features ==\n\nThe simplest type are bottom-weighted flaps hung from the top of the opening, which swing shut on their own, but may be spring-aided to increase wind resistance. These flaps often feature magnets around the edges to help keep the door closed against weather and wind. Some pet doors have side-mounted hinges and swing open like saloon doors."
        
        
    
def test_process():
        r = utils.Request("bla")
        assert r.process() == None


    