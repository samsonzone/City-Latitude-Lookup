import requests
import pandas as pd
import zipfile
import os
import sys

# Constants
CITIES_DATA_URL = "https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.74.zip"

def get_latitude(city, state):
    """Fetch latitude of a city using Nominatim (OpenStreetMap)."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'city': city,
        'state': state,
        'format': 'json'
    }
    headers = {
        'User-Agent': 'latitude-finder-script'  # Required by Nominatim
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if response.status_code == 200 and data:
        return float(data[0]['lat'])
    else:
        print("Error fetching location data. Check your input.")
        exit(1)

def load_cities():
    """Load and filter city data (population > 500,000)."""
    # Download and unzip dataset
    response = requests.get(CITIES_DATA_URL)
    if response.status_code != 200:
        print("Error fetching city dataset.")
        exit(1)
    
    # Save and extract data
    with open('cities.zip', 'wb') as file:
        file.write(response.content)

    with zipfile.ZipFile('cities.zip', 'r') as zip_ref:
        zip_ref.extractall('cities_data')

    # Load the extracted CSV
    cities_df = pd.read_csv('cities_data/worldcities.csv')
    
    # Filter for major cities (population > 500,000)
    major_cities = cities_df[cities_df['population'] > 500000]
    
    # Cleanup files
    os.remove('cities.zip')
    os.system('rm -rf cities_data')
    
    return major_cities

def find_cities_at_latitude(latitude, cities):
    """Find cities at the given latitude (±0.5 degrees) and group by country."""
    matching_cities = cities[abs(cities['lat'] - latitude) <= 0.5]
    grouped = matching_cities.groupby('country').apply(lambda x: list(x['city'])).to_dict()
    return grouped

def main():
    # Check if arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python3 citylookup.py <city> <state>")
        exit(1)

    # Read city and state from command-line arguments
    city = sys.argv[1]
    state = sys.argv[2]

    # Get latitude
    latitude = get_latitude(city, state)
    print(f"Latitude of {city.title()}, {state.upper()}: {latitude}")

    # Load city data
    cities = load_cities()

    # Find matching cities grouped by country
    grouped_cities = find_cities_at_latitude(latitude, cities)

    # Display results
    if grouped_cities:
        print("\nMajor cities at the same latitude (grouped by country):")
        for country, city_list in grouped_cities.items():
            print(f"{country}: {', '.join(city_list)}")
    else:
        print("No matching cities found at this latitude.")

if __name__ == "__main__":
    main()
