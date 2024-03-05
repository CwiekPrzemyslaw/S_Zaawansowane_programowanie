import requests


class Brewery:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.brewery_type = data.get('brewery_type')
        self.street = data.get('street')
        self.city = data.get('city')
        self.state = data.get('state')
        self.postal_code = data.get('postal_code')
        self.country = data.get('country')
        self.phone = data.get('phone')
        self.website_url = data.get('website_url')

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nType:
            {self.brewery_type}\nAddress: {self.street},
            {self.city}, {self.state},
            {self.postal_code}\nCountry: {self.country}\nPhone:
                {self.phone}\nWebsite: {self.website_url}\n"


def get_breweries():
    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(url)
    data = response.json()
    return [Brewery(brewery_data) for brewery_data in data[:20]]


def main():
    breweries = get_breweries()
    print(breweries)

    if breweries:
        for idx, brewery in enumerate(breweries, 1):
            print(f"--- Brewery {idx} ---")
            print(brewery)


main()
