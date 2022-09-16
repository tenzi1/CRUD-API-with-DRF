#This module acts as third party app for class based view CRUD API using Django REST framework
import requests
import json

URL = "http://127.0.0.1:8000/api_class/"

#[GET] Operation
def get_data(id=None):
    data = {
        'id':id
    }
    json_data = json.dumps(data)
    res = requests.get(url=URL, data = json_data)
    data = res.json()
    print(data)

# get_data()
# ________________________________________________________________
#[POST] Operation
def post_data():
    data = {
        'name':'John',
        'roll':103,
        'city':'NY'
    }
    json_data = json.dumps(data)
    res = requests.post(url=URL, data = json_data)
    data = res.json()
    print(data)
# post_data()


# ________________________________________________________________
#[PUT] Operation
def put_data(id):
    data = {
        'id':id,
        'name':'John Mayer',
        # 'roll':103,
        'city':'NY'
    }
    json_data = json.dumps(data)
    res = requests.put(url=URL, data = json_data)
    data = res.json()
    print(data)
# put_data(3)

# ________________________________________________________________
#[DELETE] Operation

def delete_data():
    data = {
        'id': 2
    }
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data=json_data)
    data = res.json()
    print(data)

delete_data()

