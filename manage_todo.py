from email import header
import requests
import json

URL = "http://127.0.0.1:8000/todoapi"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

def post_data():
    data = {
        'id':'13',
        'title':'is',
        'description':'completely study whole syallabus of ADBMS',
        'date':'2022-06-21T10:07:07Z',
        'completed':'True'
    }
    headers = {'content-Type':'applicaion/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers, data=json_data)
    data = r.json()
    print(data)


def update_data():
    data = {
        'id':'3',
        'title':'stuy syallabus',
        'description':'completely study whole syallabus of ADBMS',
        'date':'2022-06-21T10:07:07Z',
        'completed':'False'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data=json_data)
    data = r.json()
    print(data)

def delete_data(id):
    data = {
        'id':id
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data=json_data)
    data = r.json()
    print(data)

get_data()