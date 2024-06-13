#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
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

# Connexió a Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Crear el keyspace i les taules
def create_keyspace_and_tables():
    session.execute("DROP KEYSPACE IF EXISTS bank")
    session.execute("""
        CREATE KEYSPACE bank WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1}
    """)
    session.execute("USE bank")
    
    session.execute("""
        CREATE TABLE comptes (
            acc_id bigint PRIMARY KEY,
            type text,
            balance float,
            contractes list<frozen<map<text, text>>>
        )
    """)
    session.execute("""
        CREATE TABLE adreces (
            address text PRIMARY KEY,
            phone text,
            titulars set<bigint>
        )
    """)

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
    print(f"{num_comptes} comptes will be inserted.")
    for i in range(num_comptes):
        print(i+1, end='\r')
        acc_id = randint(100000000000, 999999999999)
        balance = randint(100, 99999) / 100
        typ = atypes[r(3)]
        session.execute(
            """
            INSERT INTO comptes (acc_id, type, balance, contractes)
            VALUES (%s, %s, %s, [])
            """,
            (acc_id, typ, balance)
        )

def create_adreces():
    print(f"{num_adreces} adreces will be inserted.")
    for i in range(num_adreces):
        print(i+1, end='\r')
        address = fake.address().replace('\n', ' ')
        phone = fake.phone_number()
        session.execute(
            """
            INSERT INTO adreces (address, phone, titulars)
            VALUES (%s, %s, {})
            """,
            (address, phone)
        )

def create_titulars():
    print(f"{num_titulars} titulars will be inserted.")
    adreces = list(session.execute("SELECT address FROM adreces"))
    
    for address_val in adreces:
        owner_id = randint(10000000, 99999999)
        session.execute(
            """
            UPDATE adreces
            SET titulars = titulars + {%s}
            WHERE address = %s
            """,
            (owner_id, address_val.address)
        )
    
    remaining_titulars = num_titulars - num_adreces
    for i in range(remaining_titulars):
        print(i+1, end='\r')
        owner_id = randint(10000000, 99999999)
        address_val = choice(adreces)
        session.execute(
            """
            UPDATE adreces
            SET titulars = titulars + {%s}
            WHERE address = %s
            """,
            (owner_id, address_val.address)
        )

def create_contractes():
    print(f"{num_contractes} contractes will be inserted.")
    comptes = list(session.execute("SELECT acc_id FROM comptes"))
    adreces = list(session.execute("SELECT address, titulars FROM adreces"))
    
    for compte_val in comptes:
        address_val = choice(adreces)
        if not address_val.titulars:
            continue
        owner_id = choice(list(address_val.titulars))
        owner = randname(2) + ' ' + randname(4)
        contracte = {"owner_id": str(owner_id), "owner": owner}
        session.execute(
            """
            UPDATE comptes
            SET contractes = contractes + [%s]
            WHERE acc_id = %s
            """,
            (contracte, compte_val.acc_id)
        )
    
    remaining_contractes = num_contractes - num_comptes
    for i in range(remaining_contractes):
        print(i+1, end='\r')
        compte_val = choice(comptes)
        address_val = choice(adreces)
        if not address_val.titulars:
            continue
        owner_id = choice(list(address_val.titulars))
        owner = randname(2) + ' ' + randname(4)
        contracte = {"owner_id": str(owner_id), "owner": owner}
        session.execute(
            """
            UPDATE comptes
            SET contractes = contractes + [%s]
            WHERE acc_id = %s
            """,
            (contracte, compte_val.acc_id)
        )

def main():
    create_keyspace_and_tables()
    create_comptes()
    create_adreces()
    create_titulars()
    create_contractes()
    
    print("S'han inserit les dades correctament.")

    # Comprovacions
    print("COMPTES: ", session.execute("SELECT COUNT(*) FROM comptes").one().count)
    print("ADRECES: ", session.execute("SELECT COUNT(*) FROM adreces").one().count)
    print("TITULARS: ", sum(len(row.titulars) for row in session.execute("SELECT titulars FROM adreces")))
    print("CONTRACTES: ", sum(len(row.contractes) for row in session.execute("SELECT contractes FROM comptes")))
    
if __name__ == "__main__":
    main()
