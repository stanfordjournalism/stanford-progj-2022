import csv
import json
import os
import time

import requests


def geocode(url, addresses, results=[], batch_size=1000, throttle=1):
    payload = {
        'f': 'json',
        'addresses': json.dumps({'records': addresses[0:batch_size] })
    }
    response = requests.post(url, data=payload)
    data = response.json()
    results.extend(data['locations'])
    # If records remain to process, perform a recursive call
    remaining_addresses = addresses[batch_size:]
    if remaining_addresses:
        time.sleep(throttle)
        geocode(
            url, remaining_addresses,
            results=results,
            batch_size=batch_size,
            throttle=throttle
        )
    return results

if __name__ == '__main__':
    addresses = [
        {
            'attributes': {
                'OBJECTID': 1,
                'Address': '450 Jane Stanford Way',
                'City': 'Stanford',
                'Region': 'CA',
                #'Postal': '94305'
            }
        },
        {
            'attributes': {
                'OBJECTID': 2,
                'Address': '1600 Amphitheatre Pkwy',
                'City': 'Mountain View',
                'Region': 'CA',
                #'Postal': '94043'
            }
        }
    ]
    url = "https://locator.stanford.edu/arcgis/rest/services/Geocode/NorthAmerica_Composite/GeocodeServer/geocodeAddresses"
    results = geocode(url, addresses, batch_size=1)
    from pprint import pprint
    pprint(results)
