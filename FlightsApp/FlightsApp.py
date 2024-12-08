
import requests
import json

API_KEY = "fdbe84ce39bc2cf61895e80bf3c6f9f3"
BASE_URL = "https://api.aviationstack.com/v1/flights"

# A simple mapping of cities to IATA codes
CITY_TO_IATA = {
    'Sofia': 'SOF',  # Sofia, Bulgaria
    'New York': 'JFK',  # John F. Kennedy, USA
    'London': 'LHR',  # London Heathrow, UK
    'Berlin': 'TXL',  # Berlin, Germany
    'Paris': 'CDG',  # Charles de Gaulle, France
    'Tokyo': 'HND',  # Haneda, Japan
    'Dubai': 'DXB',  # Dubai, UAE
    'Moscow': 'SVO',  # Sheremetyevo, Russia
    # Add more cities and IATA codes as needed
}

def get_flights_by_city(arrival_city, departure_city):
    try:
        # Map city names to IATA codes
        arrival_iata = CITY_TO_IATA.get(arrival_city)
        departure_iata = CITY_TO_IATA.get(departure_city)

        if not arrival_iata or not departure_iata:
            print("Invalid city name. Please enter valid city names.")
            return
        
        # Construct the URL for the API call using IATA codes
        url = f"{BASE_URL}?access_key={API_KEY}&arr_iata={arrival_iata}&dep_iata={departure_iata}"
      
        response = requests.get(url)

        if response.status_code == 200:
            print("Request was successful")
            data = response.json()  # Parse the JSON response directly
        elif response.status_code == 401:
            print("Unauthorized! Check your API key.")
            return
        elif response.status_code == 404:
            print("Not found! Check the URL or endpoint.")
            return
        elif response.status_code == 429:
            print("Rate limit exceeded! Try again later.")
            return
        else:
            print(f"Request failed with status code {response.status_code}.")
            return

        # Check if 'data' exists in response and process it
        if "data" not in data or not data["data"]:
            print("No flight data available for the specified airports.")
            return

        print(f"Flights between {departure_city} and {arrival_city}:")
        for flight in data['data'][:10]:  # Limit to the first 10 results
            airline = flight['airline']['name']
            arrival_airport = flight["arrival"]["airport"]
            arrival_code = flight["arrival"]["iata"]
            arrival_terminal = flight["arrival"]["terminal"]
            arrival_gate = flight["arrival"]["gate"]
            arrival_estimatedTime = flight["arrival"]["estimated"]
            arrival_scheduledTime = flight["arrival"]["scheduled"]



            departure_airport = flight['departure']["airport"]
            departure_code = flight['departure']["iata"]
            departure_delay = flight['departure']["delay"]
            departure_estimatedTime = flight['departure']["estimated"]
            departure_scheduledTime = flight['departure']["scheduled"]
            departure_terminal = flight['departure']["terminal"]


            flight_num  =flight['flight']['number']
            flight_date = flight['flight_date']
            flight_status = flight['flight_status']



            #airline = flight.get('airline', {}).get('name', 'Unknown airline')
            #arrival_airport = flight.get("arrival", {}).get("airport", "Unknown airport")
           # departure_airport = flight.get("departure", {}).get("airport", "Unknown airport")
            print(f"Airline: {airline} -> Departure Airport: {departure_airport} ({departure_code}) "
            f"Delay: {departure_delay}, Departure Scheduled Time: {departure_scheduledTime} "
            f"Departure Estimated Time: {departure_estimatedTime}, Terminal: {departure_terminal} "
            f"-> Arrival Airport: {arrival_airport} ({arrival_code})")

            print(f"Flight number: {flight_num} -> Flight date: {flight_date} -> Flight status: {flight_status} ")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for input and call the function
departure_city = input("Enter the departure city: ")  # e.g., "Sofia"
arrival_city = input("Enter the arrival city: ")  # e.g., "London"

get_flights_by_city(arrival_city, departure_city)
