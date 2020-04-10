import os
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from flask import url_for


def test_app(client):
    assert client.get(url_for('index')).status_code == 200


def test_liveserver(client):
    with webdriver.Firefox() as driver:
        driver.get("http://127.0.0.1:5000/index")
        assert driver.find_element_by_css_selector("body").text == "hello world"
  
