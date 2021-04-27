#! /usr/bin/python3

import requests
import pandas as pd
from bs4 import BeautifulSoup

def getURLData(api, number, countryCode):

    # OBJECTIVE: Get HTML data from url

    # Fill in phone number and country to url
    url = "http://apilayer.net/api/validate?access_key={}&number={}&country_code={}&format=1".format(api, number, countryCode)
    req = requests.get(url)

    # Parse HTML data
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

# Write API key from Numverify
API = ""

# Ask for phone number and country
number = input("Enter phone number: ")
countryCode = input("Specify country code (E.g. US): ")

# Get webpage's information
htmlData = getURLData(API, number, countryCode)
print(htmlData)