import requests

pixela_endpoint = "https://pixe.la/v1/users"

def create_user() -> None:
    user_params = {
        "token" : "asdcvb654BVC123",
        'username': 'nadavbeithalevi',
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes',
    }
    response = requests.request("POST", url=pixela_endpoint, json=user_params)
    print(response.text)

def create_graph() -> None:

    graph_endpoint = f"{pixela_endpoint}/nadavbeithalevi/graphs"
    graph_params = {
        "id": "graph1",
        "name": "Reading Graph",
        "unit": "Pages",
        "type": "int",
        "color": "shibafu",
    }
    headers = {
        "X-USER-TOKEN": "asdcvb654BVC123"
    }
    response = requests.request("POST", url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)


