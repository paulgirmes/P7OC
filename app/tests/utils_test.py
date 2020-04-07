
import os, sys

import pytest
from app.utils.utils import Parser, Place

class Test_parser():
    
    
    def test_removestopwords(self):
        test_phrases = ["Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
        "24444 fes68 zzsrnt4 rs54eqv654 sftrts     *ù(^$^:)à'ç(k"]
        result = Parser()
        assert result.filter(test_phrases[0]) == ["Salut", "GrandPy", "connais", "adresse", "OpenClassrooms"]
        assert result.filter(test_phrases[1]) == ["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"]
    
    def test_prioritise(self):
        filter_results = [["Salut", "GrandPy", "connais", "adresse", "OpenClassrooms"],
        ["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"]]
        result = Parser()
        assert result.prioritize(filter_results[0]) == ["OpenClassrooms", "Salut", "GrandPy", "connais"]
        assert result.prioritize(filter_results[1]) == ["24444", "fes", "68", "zzsrnt", "4", "rs", "54", "eqv", "654", "sftrts"]

class Test_place():
    

    def test_find_address(self):
        prioritized_results = [["OpenClassrooms","Salut", "GrandPy", "connais"],["sftrts"], ["Ministère","culture"]]
        result = Place(prioritized_results[0][0])
        assert result.find_address() == 0
        assert result.formatted_address == "7 Cité Paradis, 75010 Paris, France"
        result = Place(prioritized_results[1])
        assert result.find_address() == 1
        result = Place(prioritized_results[2])
        assert len(result.find_address()) > 1


    def test_find_coordinates(self):
        prioritized_results = ["OpenClassrooms","Salut", "GrandPy", "connais"]
        formatted_address = "7 Cité Paradis, 75010 Paris, France"
        result = Place(prioritized_results)
        result.formatted_address = formatted_address
        assert result.find_coordinates() == 0
        assert result.location == "latitude 48.8747265, longitude 2.3505517"

    