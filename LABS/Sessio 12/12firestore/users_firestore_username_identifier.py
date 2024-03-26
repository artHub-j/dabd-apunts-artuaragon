#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from optparse import OptionParser

import firebase_admin
#from firebase_admin import credentials
from firebase_admin import firestore


optp = OptionParser()
# optp.add_option("-i", "--init", dest="init", action="store_true", default=False,
# help="create the database and collection")
optp.add_option("-a", "--add", dest="add", action="store_true", default=False,
        help = "add new pairs to collection")
optp.add_option("-d", "--delete", dest="delete", action="store_true", default=False,
        help = "delete an user")
optp.add_option("-l", "--list", dest="list", action="store_true", default=False,
        help = "list all users")

(opt, args) = optp.parse_args()


#No cal cridar a credentials.Certificate si es configura la següent variable de Linux amb la ruta al fitxer amb les credencials
#export GOOGLE_APPLICATION_CREDENTIALS="/path/credentials_file.json"
#cred = credentials.Certificate('credentials_file.json')

firebase_admin.initialize_app()
db = firestore.client()


# No cal fer la inicialització ja que a l'afegir documents en una col·lecció inexistent ja es crea automàticament
# if opt.init:
#   print("Creating users collection")
#   db.collection('users')

if opt.add:
  print("Adding further users, leave empty username to finish")
  while True:
    u = input("username: ")
    if not u:
      break
    p = input("passwd: ")
    # db.collection('users').add({'username': u, 'passwd': p})
    #Millor que l'usuari sigui l'identificador del document, així ens assegurem que sigui únic
    db.collection('users').document(u).set({'passwd': p})

elif opt.delete:
  print("Deleting an user")
  u = input("username: ")
  doc = db.collection('users').document(u).get()
  if doc.exists:
    db.collection('users').document(u).delete()
    print("User %s deleted." % u)
  else:
    print("User %s not found." % u)

elif opt.list:
  print("Listing full users collection:")
  for doc in db.collection('users').stream():
    print(doc.id, doc.to_dict())

else:
  print("Checking some user")
  u = input("username:")
  p = input("passwd:")
  doc = db.collection('users').document(u).get()
  if doc.exists and doc.to_dict()['passwd'] == p:
    print("Access granted to user: %s via passwd: %s" % (u, p))
  else:
    print("Access denied")

