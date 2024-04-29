#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from random import randint
from faker import Faker
fake = Faker('es_ES')

num_comptes = 900
num_adreces = 500
num_titulars = 1000
num_contractes = 4000
atypes = ('C', 'L', 'S')
vowels = ('a', 'e', 'i', 'o', 'u')
somecons = ('b', 'd', 'f', 'k', 'l', 'm', 'p', 'r', 's')

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


def create_comptes(cur):
  print("%d comptes will be inserted." % num_comptes)
  cur.execute("DROP TABLE IF EXISTS comptes")
  cur.execute("""CREATE TABLE comptes(
    acc_id bigint NOT NULL PRIMARY KEY,
    type char(1) NOT NULL,
    balance float NOT NULL
  )""")

  for i in range(num_comptes):
    print(i+1, end = '\r')
    acc_id  = randint(100000000000, 999999999999)
    balance = randint(100, 99999)/100
    typ = atypes[r(3)]
    try:
      # print("INSERT INTO comptes VALUES ('%s', '%s', '%s')" % (acc_id, typ, balance))
      cur.execute("INSERT INTO comptes VALUES ('%s', '%s', '%s')" % (acc_id, typ, balance))
    except mysql.connector.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s). Error information: %s" % (acc_id, typ, balance, e))
    conn.commit()


def create_adreces(cur):
  print("%d adreces will be inserted." % num_adreces)
  cur.execute("DROP TABLE IF EXISTS adreces")
  cur.execute("""CREATE TABLE adreces(
    address varchar(100) NOT NULL PRIMARY KEY,
    phone varchar(20) DEFAULT NULL UNIQUE
  )""")

  for i in range(num_adreces):
    print(i+1, end = '\r')
    address = fake.address()
    phone   = fake.phone_number()
    try:
      # print("INSERT INTO adreces VALUES ('%s', '%s')" % (address, phone))
      cur.execute("INSERT INTO adreces VALUES ('%s', '%s')" % (address, phone))
    except mysql.connector.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s). Error information: %s" % (address, phone, e))
    conn.commit()


def create_titulars(cur):
  print("%d titulars will be inserted." % num_titulars)
  cur.execute("DROP TABLE IF EXISTS titulars")
  cur.execute("""CREATE TABLE titulars(
    owner_id int NOT NULL PRIMARY KEY,
    address varchar(100) NOT NULL REFERENCES adreces ON UPDATE CASCADE
  )""")

  for i in range(num_titulars):
    print(i+1, end = '\r')
    owner_id = randint(10000000, 99999999)
    cur.execute("SELECT address FROM adreces ORDER BY RAND() LIMIT 1;")
    address = cur.fetchone()[0]
    try:
      # print("INSERT INTO titulars VALUES ('%s', '%s')" % (owner_id, address))
      cur.execute("INSERT INTO titulars VALUES ('%s', '%s')" % (owner_id, address))
    except mysql.connector.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s). Error information: %s" % (owner_id, address, e))
    conn.commit()


def create_contractes(cur):
  print("%d contractes will be inserted." % num_contractes)
  cur.execute("DROP TABLE IF EXISTS contractes")
  cur.execute("""CREATE TABLE contractes(
    acc_id bigint NOT NULL REFERENCES comptes ON UPDATE CASCADE,
    owner_id int NOT NULL REFERENCES titulars ON UPDATE CASCADE,
    owner varchar(40) NOT NULL,
    PRIMARY KEY(acc_id, owner_id)
  )""")

  for i in range(num_contractes):
    print(i+1, end = '\r')
    cur.execute("SELECT acc_id   FROM comptes  ORDER BY RAND() LIMIT 1")
    acc_id   = cur.fetchone()[0]
    cur.execute("SELECT owner_id FROM titulars ORDER BY RAND() LIMIT 1")
    owner_id = cur.fetchone()[0]
    owner    = randname(2) + ' ' + randname(4)
    cur.execute("SELECT * FROM contractes WHERE acc_id='%s' AND owner_id='%s'" % (acc_id, owner_id))
    while bool(cur.fetchone()):
      cur.execute("SELECT owner_id FROM titulars ORDER BY RAND() LIMIT 1")
      owner_id = cur.fetchone()[0]
      cur.execute("SELECT * FROM contractes WHERE acc_id='%s' AND owner_id='%s'" % (acc_id, owner_id))

    try:
      # print("INSERT INTO contractes VALUES ('%s', '%s', '%s')" % (acc_id, owner_id, owner)))
      cur.execute("INSERT INTO contractes VALUES ('%s', '%s', '%s')" % (acc_id, owner_id, owner))
    except mysql.connector.IntegrityError as e:
      conn.rollback()
      print("Error inserting (%s, %s, %s). Error information: %s" % (acc_id, owner_id, owner, e))
    conn.commit()


# Programa principal
conn = mysql.connector.connect(
  host="ubiwan.epsevg.upc.edu",
  user="est_d9971765",
  password="dB.d9971765",
  database="est_d9971765"
)

cur = conn.cursor()

create_comptes(cur)
create_adreces(cur)
create_titulars(cur)
create_contractes(cur)

cur.close()