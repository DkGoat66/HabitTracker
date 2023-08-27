import requests
from datetime import datetime

USERNAME = "finda"
TOKEN = "asdfsdfsdfasdfasf12fsdfasd"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


GRAPH_ID = "dkadd11"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "hr",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2023,month=2,day=12)
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "2",
}




# response = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
# print(response.text)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_data = {
    "quantity": "4"
}

UPDATE = requests.put(url=update_endpoint,json=update_data, headers=headers)
print(UPDATE.text)