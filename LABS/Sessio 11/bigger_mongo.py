#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient, ASCENDING
from random import randint, choice
from faker import Faker

fake = Faker('es_ES')

# Nombre d'elements a crear
num_comptes = 900
num_adreces = 500
num_titulars = 1000
num_contractes = 4000
atypes = ('C', 'L', 'S')
vowels = ('a', 'e', 'i', 'o', 'u')
somecons = ('b', 'd', 'f', 'k', 'l', 'm', 'p', 'r', 's')

# Connexió a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.bank

def r(lim):
    "0 <= random int < lim"
    return randint(0, lim-1)

def randname(syll):
    "random name with syll 2-letter syllables"
    v = len(vowels)
    c = len(somecons)
    res = str()
    for i in range(syll):
        res += somecons[r(c)] + vowels[r(v)]
    return res.capitalize()

def create_comptes():
    print("%d comptes will be inserted." % num_comptes)
    comptes = db.comptes
    comptes.delete_many({})
    
    for i in range(num_comptes):
        print(i+1, end='\r')
        acc_id = randint(100000000000, 999999999999)
        balance = randint(100, 99999) / 100
        typ = atypes[r(3)]
        comptes.insert_one({"acc_id": acc_id, "type": typ, "balance": balance, "contractes": []})

    comptes.create_index([("acc_id", ASCENDING)], unique=True)

def create_adreces():
    print("%d adreces will be inserted." % num_adreces)
    adreces = db.adreces
    adreces.delete_many({})
    
    for i in range(num_adreces):
        print(i+1, end='\r')
        address = fake.address()
        phone = fake.phone_number()
        adreces.insert_one({"address": address, "phone": phone, "titulars": []})
    
    adreces.create_index([("address", ASCENDING)], unique=True)
    adreces.create_index([("phone", ASCENDING)], unique=True)

def create_titulars():
    print("%d titulars will be inserted." % num_titulars)
    adreces = db.adreces
    
    # Afegim com a minim un titular a cada adreca
    for address_val in adreces.find():
        owner_id = randint(10000000, 99999999)
        adreces.update_one(
            {"address": address_val["address"]},
            {"$push": {"titulars": {"owner_id": owner_id}}}
        )
    
    # Afegim la resta dels titulars que queden a cada adreca
    remaining_titulars = num_titulars - num_adreces
    for i in range(remaining_titulars):
        print(i+1, end='\r')
        owner_id = randint(10000000, 99999999)
        address_val = list(adreces.aggregate([{'$sample': {'size': 1}}]))[0]
        adreces.update_one(
            {"address": address_val["address"]},
            {"$push": {"titulars": {"owner_id": owner_id}}}
        )

def create_contractes():
    print("%d contractes will be inserted." % num_contractes)
    comptes = db.comptes
    adreces = db.adreces
    
    # Afegim com a minim un contracte a cada compte
    for compte_val in comptes.find():
        address_val = list(adreces.aggregate([{'$sample': {'size': 1}}]))[0]
        owner_id = choice(address_val['titulars'])['owner_id']
        owner = randname(2) + ' ' + randname(4)
        comptes.update_one(
            {"acc_id": compte_val["acc_id"]},
            {"$push": {"contractes": {"owner_id": owner_id, "owner": owner}}}
        )
    
    # Afegim la resta dels contractes que queden a cada compte
    remaining_contractes = num_contractes - num_comptes
    for i in range(remaining_contractes):
        print(i+1, end='\r')
        compte_val = list(comptes.aggregate([{'$sample': {'size': 1}}]))[0]
        address_val = list(adreces.aggregate([{'$sample': {'size': 1}}]))[0]
        if not address_val['titulars']:
            continue  # Ens assegurem que hi ha titulars a l'adreça
        owner_id = choice(address_val['titulars'])['owner_id']
        owner = randname(2) + ' ' + randname(4)
        comptes.update_one(
            {"acc_id": compte_val["acc_id"]},
            {"$push": {"contractes": {"owner_id": owner_id, "owner": owner}}}
        )

def main():
    db.drop_collection("comptes")
    db.drop_collection("adreces")
    create_comptes()
    create_adreces()
    create_titulars()
    create_contractes()
    
    print("S'han inserit les dades correctament.")

    # Comprovacions
    print("COMPTES: ", db.comptes.count_documents({}))
    print("ADRECES: ", db.adreces.count_documents({}))
    print("TITULARS: ", sum([len(doc["titulars"]) for doc in db.adreces.find()]))
    print("CONTRACTES: ", sum([len(doc["contractes"]) for doc in db.comptes.find()]))
    
if __name__ == "__main__":
    main()

# Possibles Errors:
# A) Script no funciona *
# a) No 900 comptes *
# b) No 500 adreces *
# c) No 1000 titulars *
# d) No 4000 contractes *
# e) No índex únic account_id *
# f) No index únic address *
# g) No index únic phone *
# h) Titulars no dins adreces *
# i) Contractes no dins comptes *
# j) Contractes no són objectes *
# k) Un contracte té molts titulars *
# L) No b.d. bank *
# m) Núm. contr./tit. no triats aleatòriame *
# n) Afegeixes col·lecció titulars *
# o) Afegeixes col·lecció contractes * 
# p) Comptes sense cap contracte *
# q) Adreces sense cap titular *
# r) Nom owner dins adreces *
