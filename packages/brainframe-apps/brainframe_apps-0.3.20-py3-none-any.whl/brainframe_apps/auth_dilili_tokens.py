from brainframe_apps.logger_factory import log

import requests
import json

# Set the Keycloak server URL and realm name
AUTH_DILILI_URL = 'http://localhost:8080'
REALM_NAME = 'auth-dilili-prod'
CLIENT_ID = '5ud60vi8nr5lg0rdsv9j95mrro'
CLIENT_SECRET = 'Tu7Tv3nT4teC4esYzs5BMtY1kWHkiLEL'

# Set the user credentials
USERNAME = "dilili-customer"
PASSWORD = "dilili"

def get_access_token():
    token_endpoint = f"{AUTH_DILILI_URL}/realms/{REALM_NAME}/protocol/openid-connect/token"

    # Request an access token using the Keycloak token endpoint
    token_data = {
        "grant_type": "password",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": USERNAME,
        "password": PASSWORD
    }

    # log.debug(f'{token_endpoint}, {token_data}')
    response = requests.post(token_endpoint, data=token_data)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        log.debug(f"Authorized by {token_endpoint}: {response_json}")
        return response_json['access_token'], response_json['refresh_token']
    else:
        log.debug(f"Authorization error {response.status_code} by {token_endpoint}: {response.text}")
        return None, None

if __name__ == "__main__":

    # Extract the access token from the response
    access_token, refresh_token = get_access_token()
    if access_token:
        log.info(f"Access token: {access_token}\nRefresh token: {refresh_token}")
