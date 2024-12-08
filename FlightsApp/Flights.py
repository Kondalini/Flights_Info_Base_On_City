import requests

API_KEY ="fdbe84ce39bc2cf61895e80bf3c6f9f3"
BASE_URL = "https://api.aviationstack.com/v1/flights"

def get_flights_by_country(arrival_country, departure_country):
    try:
        url = f"{BASE_URL}?access_key={API_KEY}&arr_country={arrival_country}&dep_country={departure_country}"
      

        response = requests.get(url)
        #Check status cod eof response
        if response.status_code == 200:
            print("Request was successful")
        elif response.status_code == 401:
            print("Unauthorized! Check your API key.")
        elif response.status_code == 404:
            print("Not found! Check the URL or endpoint.")
        elif response.status_code == 429:
            print("Rate limit exceeded! Try again later.")
        else:
            print(f"Request failed with status code {response.status_code}.")


        if response.status_code == 200:
           data= response.json()
           print("API response data:",data)
        else:
            print("No data to display due to failed request.")
    except Exception as e:
           print(f"An error occurred {e}")

    departure_country = input("Enter the departure country:")
    arrival_country = input("Enter arrival country")



    get_flights_by_country(arrival_country,departure_country)

      


