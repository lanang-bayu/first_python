users = {
    "id" : 1,
    "name" : "Ayesha Ranting",
    "username" : "Ranting",
    "email" : "ayesharanting@gmail.com",
    "address" : {
        "street" : "Puri Surya Jaya, Cluster Vancouver Extension, No J13-53",
        "district" : "Gedangan",
        "city" : "Sidoarjo",
        "zipcode" : "65124",
        "geo" : {
            "lat" : "-37.3158",
            "lng" : "81.6357"
        }
    }
}

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])

print('\nbeda dict dengan json :')
print(users)
print(type(users))
print('\nUbah dict ke json')
import json
result = json.dumps(users)
print(result)
print(type(result))

with open('result.json', 'w') as file:
    json.dump(users, file)
