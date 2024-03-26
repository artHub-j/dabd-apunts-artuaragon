#! /usr/bin/python3

from optparse import OptionParser
import mysql.connector

def do_query(cursor, query, values=''):
    if opt.show:
        print("Query is: " + query + " with values " + str(values))
    cursor.execute(query, values)

optp = OptionParser()
optp.add_option("-i", "--init", dest="init", action="store_true", default=False,
                help="create the table")
optp.add_option("-a", "--add", dest="add", action="store_true", default=False,
                help = "add new pairs to table")
optp.add_option("-d", "--delete", dest="delete", action="store_true", default=False,
                help = "delete an user")
optp.add_option("-l", "--list", dest="list", action="store_true", default=False,
                help = "list all users")
optp.add_option("-s", "--show", dest="show", action="store_true", default=False,
                help = "show queries")

(opt, args) = optp.parse_args()

conn = mysql.connector.connect(
    host="localhost",
    user="est_d9971765",
    password="dB.d9971765",
    database="est_d9971765"
)
cursor = conn.cursor()

tabname = "users"

if opt.init:
    print("Creating table "+tabname)
    try:
        do_query(cursor, "CREATE TABLE IF NOT EXISTS %s (username VARCHAR(255), passwd VARCHAR(255));" % tabname)
    except mysql.connector.Error as err:
        print("Table not created:", err)
        y = input("Try drop table first? [y]:")
        if y == 'y':
            do_query(cursor, "DROP TABLE IF EXISTS %s;" % tabname)
            do_query(cursor, "CREATE TABLE IF NOT EXISTS %s (username VARCHAR(255), passwd VARCHAR(255));" % tabname)
    conn.commit()
elif opt.add:
    print("Adding further users, leave empty username to finish")
    while True:
        u = input("username: ")
        if not u:
            break
        p = input("passwd: ")
        q = "INSERT INTO %s VALUES (%s, %s);" % (tabname, '%s', '%s')
        do_query(cursor, q, (u, p))
    conn.commit()
elif opt.delete:
    print("Deleting an user")
    u = input("username: ")
    q = "DELETE FROM %s WHERE username=%s;" % (tabname, '%s')
    do_query(cursor, q, (u,))
    conn.commit()
    if cursor.rowcount:
        print("User %s deleted." % u)
    else:
        print("User %s not found." % u)
elif opt.list:
    print("Listing full table "+tabname+":")
    do_query(cursor, "SELECT * FROM %s;" % tabname)
    for row in cursor:
        print("User: %s, passwd: %s" % (row[0], row[1]))
else:
    print("Checking some user")
    u = input("username:")
    p = input("passwd:")
    q = "SELECT * FROM %s WHERE username = %s AND passwd = %s;"  % (tabname, '%s', '%s')
    do_query(cursor, q, (u,p))
    row = cursor.fetchone()
    if row:
        print("Access granted to user: %s via passwd: %s" % (row[0], row[1]))
    else:
        print("Access denied")

cursor.close()
conn.close()
