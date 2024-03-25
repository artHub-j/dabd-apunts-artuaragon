# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Sessió 1 | DL 19 FEBRER 2024 |
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

# Solució:

### DNI de tots els titulars, sense repeticions.
    SELECT DISTINCT(owner_id) FROM accounts;
### DNI de Gaspar Gregorio.
    SELECT owner_id FROM accounts WHERE owner="Gaspar Gregorio";
### Comptes amb saldo superior a 1000.
    SELECT DISTINCT(acc_id),balance FROM accounts WHERE balance>1000;
### Comptes que no són de tipus 'L'.
    SELECT DISTINCT(acc_id),type FROM accounts WHERE type <> 'L';
### Saldo disponible complert per cadascun dels titulars (sumant tots els seus comptes), sense repeticions.
    SELECT owner_id, SUM(balance) FROM accounts GROUP BY owner_id;
### Nom i telèfon sense repeticions a on el DNI sigui el d'Alonso Quijano (complicadeta, caldrà fer alguna subquery. 2 tuples). (Podries fer-la amb una única query? Necessita queries anidades)
    SELECT DISTINCT owner, phone, owner_id FROM accounts WHERE owner_id = (SELECT DISTINCT owner_id FROM accounts WHERE owner = "Alonso Quijano");
### Parells de noms de la mateixa persona, identificada per DNI, sense repeticions (complicadeta, caldrà fer joins. 5 tuples). % Necessita join
    SELECT DISTINCT(a1.owner),a2.owner FROM accounts a1 JOIN accounts a2 ON a1.owner_id=a2.owner_id WHERE a1.owner<>a2.owner;

    SELECT DISTINCT(a1.owner),a2.owner FROM accounts a1 JOIN accounts a2 ON a1.owner_id=a2.owner_id WHERE a1.owner<a2.owner UNION SELECT DISTINCT(a2.owner),a1.owner FROM accounts a1 JOIN accounts a2 ON a1.owner_id=a2.owner_id WHERE a1.owner>a2.owner;
### Compte amb el saldo major (és el 119774916201 amb 9818.59 eur).
    SELECT acc_id, max(balance) FROM accounts;
### Compte amb el saldo menor (és el 171174310952 amb 28.89 eur).
    SELECT acc_id, min(balance) FROM accounts;
### Noms de titulars sense repeticions que comencen amb "Caballero de" (4 tuples).
    SELECT DISTINCT(owner) FROM accounts WHERE owner LIKE "Caballero de%";
 ### Titular que té el major saldo sumant tots els seus comptes (és el 6435323 amb 17351.02 eur).
    SELECT owner_id, max(total) FROM (SELECT owner_id, SUM(balance) AS total FROM accounts GROUP BY owner_id);
### Titular que té el menor saldo sumant tots els seus comptes (és el 6152436 amb 687.78 eur).
    SELECT owner_id, min(total) FROM (SELECT owner_id, SUM(balance) AS total FROM accounts GROUP BY owner_id);
### Saldo total i saldo mig de tots els comptes del banc arrodonit a 2 decimals (106118.38 eur i 2210.80 eur respectivament).
    SELECT sum(balance), round(avg(balance),2) FROM (SELECT DISTINCT(acc_id),balance FROM accounts);
### DNI de tots els titulars, sense repeticions, amb el número de comptes que té cada titular.
    SELECT owner_id, count(*) FROM accounts GROUP BY owner_id;
### Llistat amb el número de titulars amb un compte, número de titulars amb dos comptes, ... (Ha de donar 1|8, 2|4, 3|10, 4|1, 6|1, 7|1)
    SELECT nc, count(*) FROM (SELECT count(*) AS nc FROM accounts GROUP BY owner_id) GROUP BY nc;
### Comptes, sense repeticions, amb el número de titulars que té cada compte.
    SELECT acc_id, count(*) FROM accounts GROUP BY acc_id;
### Llistat amb el número de comptes amb un titular, número de comptes amb dos titulars, ... (Ha de donar 1|33, 2|15)
    SELECT nt, count(*) FROM (SELECT count(*) AS nt FROM accounts GROUP BY acc_id) GROUP BY nt;
### Incementa amb 100 eur d'interessos el saldo dels comptes de tipus "L".
    UPDATE accounts SET balance = balance + 100 WHERE type = 'L';
### Intercanvia els tipus "L" i "C" de tots els comptes.
    UPDATE accounts SET type = CASE
    WHEN type='L' THEN 'C'
    WHEN type='C' THEN 'L'
    ELSE type
    END;
### Al titular que tingui el major saldo sumant tots els seus comptes del banc li regalem un nou compte de tipus 'C' amb un saldo de 300 eur. El número del compte nou el calcularem incrementant el número del compte més gran de tot el banc.
    INSERT INTO accounts SELECT (SELECT MAX(acc_id) FROM accounts)+1, 'C', 300, owner, owner_id, phone, address FROM (SELECT *, MAX(b) FROM (SELECT *, SUM(balance) as b FROM accounts GROUP BY owner_id));
