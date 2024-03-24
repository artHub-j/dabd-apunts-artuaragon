# [ Sessió 1 | DL 19 FEBRER 2024 | Arturo Aragón ]
## Sobre la taula de comptes (accounts1.db)

### Crea una nova base de dades:
    sqlite3 accounts1.db
### Crea una taula accounts amb aquests camps: (acc id int, type char(1), balance real, owner text, owner id int, phone int, address text)
    CREATE TABLE t1(acc_id int, type char(1), balance real, owner text, 
                    owner_id int, phone int, address text);
### Mira el contingut del fitxer accounts.txt que cont e les dades a inserir i esbrina com usar-lo per afegir les dades a la taula anterior.
    .import accounts.txt t1
### Per comprovar que s'han afegit:
    SELECT * FROM t1;
### Crea una nova base de dades:
    sqlite3 accounts2.db
### Mira el contingut del fitxer accounts.sql que conte instruccions SQL amb la taula a crear i les dades a inserir i esbrina com usar-lo. Comprova que el resultat ́es el mateix que important el fitxer .txt.
    .read accounts.sql

#

### to export info into new .txt file:
    .export accounts2.txt
### DNI de tots els titulars, sense repeticions.
    SELECT DISCTINCT owner_id FROM accounts;
### DNI de Gaspar Gregorio.
    SELECT DISTINCT owner_id FROM accounts WHERE owner='Gaspar Gregorio';
### Comptes amb saldo superior a 1000.
    SELECT * FROM accounts WHERE balance>1000;
### Comptes que no s ́on de tipus ’L’.
    SELECT * FROM accounts WHERE type!='L';
### Saldo disponible complert per cadascun dels titulars (sumant tots els seus comptes), sense repeticions.
    SELECT owner, SUM(balance) AS total_balance
    FROM accounts GROUP BY owner;
### Nom i telefon sense repeticions a on el DNI sigui el d’Alonso Quijano (complicadeta, caldra fer alguna subquery. 2 tuples).
    SELECT owner, phone
    FROM accounts
    WHERE owner_id IN (SELECT owner_id FROM accounts WHERE owner = 'Alonso Quijano')
    GROUP BY owner, phone;
### Otra forma:
    SELECT DISTINCT a.owner, a.phone
    FROM accounts AS a
    JOIN accounts AS b ON a.owner_id = b.owner_id
    WHERE b.owner = 'Alonso Quijano';
### Parells de noms de la mateixa persona, identificada per DNI, sense repeticions (complicadeta, caldr`a fer joins. 5 tuples).
    SELECT DISTINCT a.owner AS owner1, b.owner AS owner2
    FROM accounts AS a
    JOIN accounts AS b ON a.owner_id = b.owner_id
    WHERE a.owner <> b.owner;
### Compte amb el saldo major ( ́es el 119774916201 amb 9818.59 eur).
    -
### Compte amb el saldo menor ( ́es el 171174310952 amb 28.89 eur).
    -
### Noms de titulars sense repeticions que comencen amb ”Caballero de” (4 tuples).
    -
#

### Construeix consultes que corresponen a:
    -
### Titular que t ́e el major saldo sumant tots els seus comptes ( ́es el 6435323 amb 17351.02 eur).
    -
### Titular que t ́e el menor saldo sumant tots els seus comptes ( ́es el 6152436 amb 687.78 eur).
    -
### Saldo total i saldo mig de tots els comptes del banc arrodonit a 2 decimals (106118.38 eur i 2210.80 eur respectivament).
    -
### DNI de tots els titulars, sense repeticions, amb el n ́umero de comptes que t ́e cada titular.
    -
### Llistat amb el n ́umero de titulars amb un compte, n ́umero de titulars amb dos comptes, ... (Ha de donar 1—8, 2—4, 3—10, 4—1, 6—1, 7—1)
    -
### Comptes, sense repeticions, amb el n ́umero de titulars que t ́e cada compte.
    -
### Llistat amb el n ́umero de comptes amb un titular, n ́umero de comptes amb dos titulars, ... (Ha de donar 1—33, 2—15)
    -
#

### Construeix instruccions SQL que corresponen a:
    -
### Incementa amb 100 eur d’interessos el saldo dels comptes de tipus ”L”.
    -
### Intercanvia els tipus ”L” i ”C” de tots els comptes.
    -
### Al titular que tingui el major saldo sumant tots els seus comptes del banc li regalem un nou compte de tipus ’C’ amb un saldo de 300 eur. El n ́umero del compte nou el calcularem incrementant el n ́umero del compte m ́es gran de tot el banc.
    -
### Crea una vista que mostri els comptes amb el seu saldo sense duplicitats.
    -
### Altres que tu mateix t’inventis!
    -