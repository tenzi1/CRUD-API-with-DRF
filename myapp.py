# this module acts as other applications
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# Retrieving data (GET)
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data=json_data)
    data = res.json()
    print(data)

# get_data(1)
#_____________________________________________________
# Creating Data (POST)
def post_data():
    data = {
        'name':'Mikey',
        'roll':104,
        'city':'Tokyo'
    }
    json_data = json.dumps(data)
    res = requests.post(url=URL, data=json_data)
    data = res.json()
    print(data)
# post_data()

def update_data():
    data = {
        'id':4,
        'name':'Eren Jeager',
        
        'city': 'Berlin'
    }
    json_data = json.dumps(data)
    res = requests.put(url=URL, data = json_data)
    data = res.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id': 2
    }
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data=json_data)
    data = res.json()
    print(data)

delete_data()