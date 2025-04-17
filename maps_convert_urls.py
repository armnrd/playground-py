import os.path
import json
import requests
import pandas as pd
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Replace with your Google Maps API key
with open("secrets.json", "r") as file:
    secrets = json.load(file)
    API_KEY = secrets["google-maps-key"]

# List of CSV files with Google Maps URL's
google_maps_lists = [
    # r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin.csv",
    # r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Banks.csv",
    r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Bookstores.csv",
    r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Libraries.csv",
    r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Coworking.csv",
    r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Cafés.csv",
    r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Clubs Bars Pubs.csv",
    r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Restaurants.csv",
    r"C:\Users\Arindam\Downloads\SavedPlaces\Berlin_ Schl Malls Fit Str_.csv"
]

def latlng_from_url(url):
    match = re.search(r"@([0-9.]+,[0-9.]+)", url)
    return match.group(1) if match else None

def location_address(latlng):
    response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latlng}&key={API_KEY}")
    response_json = response.json()
    if response_json["status"] == "OK":
        result = response_json["results"][0]
        return result["geometry"]["location"], result["formatted_address"]
    else:
        raise Exception("Could not find address")

service = Service(r"C:\Packages\Firefox\geckodriver.exe")
options = Options()
options.binary_location = r"C:\Packages\Firefox\firefox.exe"
driver = webdriver.Firefox(options, service=service)
driver.get("https://www.google.com/maps/place/Academy+of+Arts/data=!4m2!3m1!1s0x47a851e80666919f:0x1db8a72bdb48aa0")
time.sleep(5)

for file in google_maps_lists:
    # Process URLs
    csv_urls = pd.read_csv(file)
    results = []
    for name, url in zip(csv_urls["Title"], csv_urls["URL"]):
        driver.get(url)
        latlng = None
        while not latlng:
            time.sleep(0.25)
            latlng = latlng_from_url(driver.current_url)

        location, address = location_address(latlng)
        results.append({"Name": name, "Address": address, "Location": f"{location["lat"]},{location["lng"]}"})

    # Write processed data to file
    pd.DataFrame(results).to_csv(f"{os.path.dirname(file)}\\proc\\{os.path.basename(file)}", index=False)

driver.quit()