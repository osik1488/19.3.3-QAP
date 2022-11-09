import json
import requests
status ='avalable'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(res.content)

data = {
  "id": 101,
  "category": {
    "id": 101,
    "name": "doggistyle"
  },
  "name": "goddog",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "sof"
    }
  ],
  "status": "available"
}

res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(data, ensure_ascii=False))
print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


res = requests.delete(f"https://petstore.swagger.io/v2/pet/101")
print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


res = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(data, ensure_ascii=False))
print(res.status_code)
print(res.text)
print(res.json())
print(res.content)




image = '1.jpeg'
files = {'file': (image, open(image, 'rb'), 'image/jpeg')}

res = requests.post(f'https://petstore.swagger.io/v2/pet/101/uploadImage', headers={'accept': 'application/json'}, files=files)

print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


data = {
    "id": 111,
    "username": "user_name",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}


res = requests.post(f"https://petstore.swagger.io/v2/user/", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(data, ensure_ascii=False))
print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


username = "user_name"
password = "123"

res = requests.get(f'https://petstore.swagger.io/v2/user/login?login={username}&password={password}',
                   headers={'accept': 'application/json'})

print('GET /user/login  Logs user into the system')
print(res.status_code)
print( res.json())
print(res.headers)



res = requests.get(f"https://petstore.swagger.io/v2/user/logout", headers={'accept': 'application/json'})
print('GET /user/logout  Logs user out the system')
print(res.status_code)
print(res.text)



data = {
    "id": 117,
    "username": "OS",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 2
}

res = requests.put(f'https://petstore.swagger.io/v2/user/user_name',headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(data, ensure_ascii=False))

print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


res = requests.delete(f'https://petstore.swagger.io/v2/user/OS', headers={'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


data= {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
res = requests.post(f'https://petstore.swagger.io/v2/user/createWithList', headers={'accept': 'application/json','Content-Type': 'application/json'}, data=json.dumps(data, ensure_ascii=False))
print(res.status_code)
print(res.text)
print(res.json())
print(res.content)



data = {
   "id": 1,
  "petId": 1,
  "quantity": 1,
  "shipDate": "2022-11-08T17:38:17.208Z",
  "status": "placed",
  "complete": True
}
#

res = requests.post(f'https://petstore.swagger.io/v2/store/order', headers={'accept': 'application/json','Content-Type': 'application/json'}, data=json.dumps(data, ensure_ascii=False))
print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


orderId = 1

res = requests.get(f'https://petstore.swagger.io/v2/store/order/1', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(res.content)


res = requests.delete(f'https://petstore.swagger.io/v2/store/order/1', headers={'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(res.content)
