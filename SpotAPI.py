import requests
import base64

token_url = "https://accounts.spotify.com/api/token"

client_id = "40c191875d7943ec88521e934d1d111d"
client_secret = "020938a704b34ed49bacf15f3a6b1396"

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

headers = {
    "Authorization": f"Basic {client_creds_b64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials"
}

def getToken():
    response = requests.post(token_url, headers=headers, data=data)

    if response.status_code == 200:
    # Extract the access token from the response
        access_token = response.json()["access_token"]
        return access_token
    else:
        print("Failed to get access token:", response.status_code, response.text)

def clientCreds():
    print("client_id: " + client_id)
    print("client_secret: " + client_secret)