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
    
    for i in range(num_titulars):
        print(i+1, end='\r')
        owner_id = randint(10000000, 99999999)
        address_doc = list(adreces.aggregate([{'$sample': {'size': 1}}]))[0]
        adreces.update_one(
            {"address": address_doc["address"]},
            {"$push": {"titulars": {"owner_id": owner_id}}}
        )

def create_contractes():
    print("%d contractes will be inserted." % num_contractes)
    comptes = db.comptes
    adreces = db.adreces
    
    contractes_creats = 0

    # Primer, assegurem que cada compte tingui almenys un contracte
    for compte_doc in comptes.find():
        address_doc = list(adreces.aggregate([{'$sample': {'size': 1}}]))[0]
        if not address_doc['titulars']:
            continue  # Ens assegurem que hi ha titulars a l'adreça
        owner_id = choice(address_doc['titulars'])['owner_id']
        owner = randname(2) + ' ' + randname(4)
        
        comptes.update_one(
            {"acc_id": compte_doc["acc_id"]},
            {"$push": {"contractes": {"owner_id": owner_id, "owner": owner}}}
        )
        contractes_creats += 1
    
    # Ara, creem la resta dels contractes fins arribar a num_contractes
    while contractes_creats < num_contractes:
        compte_doc = list(comptes.aggregate([{'$sample': {'size': 1}}]))[0]
        address_doc = list(adreces.aggregate([{'$sample': {'size': 1}}]))[0]
        if not address_doc['titulars']:
            continue  # Ens assegurem que hi ha titulars a l'adreça
        owner_id = choice(address_doc['titulars'])['owner_id']
        owner = randname(2) + ' ' + randname(4)
        
        comptes.update_one(
            {"acc_id": compte_doc["acc_id"]},
            {"$push": {"contractes": {"owner_id": owner_id, "owner": owner}}}
        )
        contractes_creats += 1

def main():
    db.drop_collection("comptes")
    db.drop_collection("adreces")
    create_comptes()
    create_adreces()
    create_titulars()
    create_contractes()
    
    print("Dades introduides correctament.")

    # Comprovacions
    # assert db.comptes.count_documents({}) == num_comptes, "Error: No hi ha 900 comptes"
    # assert db.adreces.count_documents({}) == num_adreces, "Error: No hi ha 500 adreces"
    # assert sum([len(doc["titulars"]) for doc in db.adreces.find()]) == num_titulars, "Error: No hi ha 1000 titulars"
    # assert sum([len(doc["contractes"]) for doc in db.comptes.find()]) == num_contractes, "Error: No hi ha 4000 contractes"
    # assert all(len(doc["contractes"]) > 0 for doc in db.comptes.find()), "Error: Hi ha comptes sense cap contracte"

if __name__ == "__main__":
    main()
