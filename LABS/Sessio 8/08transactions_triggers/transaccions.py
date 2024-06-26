#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Prèviament cal fer:
sqlite3 comptes.db 
CREATE TABLE IF NOT EXISTS comptes (titular text, saldo decimal);
INSERT INTO comptes VALUES ('a',1000), ('b',1000);

Programa que permet mostrar com:
1) Sense el commit no hi ha durabilitat en la transacció.
2) commit() desprès de cada execute(): la transacció està mal programada i es pot perdre
   la coherència si el client perd o avorta la connexió durant el5 segons d'espera.
"""

import sqlite3
from time import sleep

def query(c, q, p):
    c.execute(q, p)

c = sqlite3.connect("comptes.db")

qpag = "UPDATE comptes SET saldo = saldo - ? WHERE titular = ?"
qreb = "UPDATE comptes SET saldo = saldo + ? WHERE titular = ?"

query(c, qpag, (50, 'a'))
print("50 eur pagats per a")
sleep(5)
query(c, qreb, (50 ,'b'))
print("50 eur rebuts per b")

fer = input("Vols fer la transferencia? (SI/NO): ")

if fer.upper() == "SI":
    c.commit()
    print("Transferència realitzada amb èxit.")
else:
    c.rollback()
    print("Transferència cancel·lada.")

c.close() 
