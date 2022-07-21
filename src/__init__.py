import json


# Return True if id existe in waiters.json
def connexion(id):
    with open('src/waiters.json') as f:
        data = json.load(f)
    for x in data:
        if id == x["id"]:
            return True
    return False


print('Entrer votre ID :')
x = int(input())
if connexion(x):
    print('Bienvenue !')
else:
    print('ID inconnu.')