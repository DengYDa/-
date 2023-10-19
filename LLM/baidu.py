import requests
import json


def Access_token(client_id,client_secret):
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json().get("access_token")


if __name__ == '__main__':
    client_id = 'lmciVBEhNTQSkBAnS9wuFVMq'
    client_secret = 'mpiROc11hPxwR89QXLsnp63iVgc1xufX'
    Access_token(client_id,client_secret)
    access_token = "24.b8880010649bd971394b0503c903a0e1.2592000.1700202875.282335-41294219"
