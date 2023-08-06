from brainframe_apps.logger_factory import log

from typing import Tuple
import string

import uuid
import hashlib
import secrets
import base64

import requests
from requests_oauthlib import OAuth2Session
from urllib.parse import urlparse, parse_qs, urlencode

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
# import socketserver
# import ssl
import webbrowser

def make_pkce_code() -> Tuple[str, str]:
    """Generates a PKCE code and returns a code challenge and code verifier. The
    code challenge is provided to Cognito when the flow starts, and the code
    verifier is provided when requesting the access and refresh tokens. These values
    are used by Cognito to ensure that it's talking to the same client throughout
    the entire flow.
    """
    alphanumeric = string.ascii_letters + string.digits
    code_verifier = "".join(secrets.choice(alphanumeric) for _ in range(128))

    code_challenge = hashlib.sha256(code_verifier.encode()).digest()
    code_challenge = (base64.urlsafe_b64encode(code_challenge)
                      .decode()
                      .replace("=", ""))

    return code_challenge, code_verifier


# Define the AWS Cognito credentials
client_id = "5ud60vi8nr5lg0rdsv9j95mrro"
client_secret = ""
user_pool_id = "auth-aotuai-prod"
# cognito domain: https://auth-aotuai-prod.auth.us-east-1.amazoncognito.com
access_token_url = f"https://{user_pool_id}.auth.us-east-1.amazoncognito.com/oauth2/token"
authorize_url = f"https://{user_pool_id}.auth.us-east-1.amazoncognito.com/oauth2/authorize"
redirect_uri = "http://localhost"
ports = [21849, 32047, 31415]


def get_authorization_redirect_url(code_challenge, port):
    OAUTH_SCOPES = [
        "https://api.aotu.ai/admin.brainframe-licenses",
        "https://api.aotu.ai/admin.brainframe-analytics",
    ]
    
    SCOPES = ["email", "aws.cognito.signin.user.admin", "profile", "openid", *OAUTH_SCOPES]
    scopes = " ".join(SCOPES)
    
    params = {
        "response_type": "code",
        "client_id": client_id,
        "scope": scopes,
        "redirect_uri": f'{redirect_uri}:{port}/',
        "state": str(uuid.uuid4()),
        "identity_provider": "COGNITO",
        "code_challenge_method": "S256",
        "code_challenge": code_challenge,
        "access_type": "offline"
    }
    authorization_redirect_url = authorize_url + "?" + urlencode(params)
    return authorization_redirect_url


authorization_code = None
class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract the authorization code from the redirect URL
        redirect_response = self.path

        parsed_url = urlparse(redirect_response)
        query = parse_qs(parsed_url.query)
        code = query['code'][0]
        global authorization_code
        authorization_code = code

        # Display the access token
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(f'<html><body><h1>Authorized by {authorize_url}: {code}</h1></body></html>', 'utf-8'))


def start_server(server_address, callback_handler):

    httpd = HTTPServer(server_address, callback_handler)

    # Create an SSL context to use for the server
    # ssl_context = ssl.SSLContext()
    # ssl_context.verify_mode = ssl.CERT_NONE

    # httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

    server_thread = threading.Thread(target=httpd.handle_request)
    server_thread.start()

    return httpd, server_thread


def get_authorization_code(authorization_redirect_url, port):
    oauth = OAuth2Session(client_id, redirect_uri=authorization_redirect_url)

    server_address = ('', port)

    httpd, httpd_thread = start_server(server_address, CallbackHandler)

    webbrowser.open(authorization_redirect_url)

    httpd_thread.join()

    httpd.server_close()

    global authorization_code
    return authorization_code


def get_access_token(authorization_code, code_verifier, port):
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "code_verifier": code_verifier,
        "code": authorization_code,
        "redirect_uri": f'{redirect_uri}:{port}/',
    }

    access_token_response = requests.post(access_token_url, data=data)

    access_token = access_token_response.json()["access_token"]
    refresh_token = access_token_response.json()["refresh_token"]
    id_token = access_token_response.json()["id_token"]
    expires_in = access_token_response.json()["expires_in"]
    token_type = access_token_response.json()["token_type"]

    return access_token, refresh_token


def make_a_request(access_token):
    headers = {"Authorization": "Bearer " + access_token}
    response = requests.get("https://yourapi.com/", headers=headers)
    log.debug(response.json())


if __name__ == "__main__":

    code_challenge, code_verifier = make_pkce_code()

    # Step 1: Get the authorization code
    port = ports[0]
    authorization_redirect_url = get_authorization_redirect_url(code_challenge, port)
    authorization_code = get_authorization_code(authorization_redirect_url, port)

    # Step 2: Get the access token
    access_token, refresh_token = get_access_token(authorization_code, code_verifier, port)
    log.info(f'--access-token {access_token}')
    log.info(f'--refresh-token {refresh_token}')

    # Step 3: Make a request using the access token
    # make_a_request(access_token)

