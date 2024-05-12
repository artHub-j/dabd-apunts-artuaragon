# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Sessió 8 | DL 06 MAIG 2024 | 

En aquesta sessió practicarem transaccions, disparadors i optimització consultes SQL fent exercicis similars als vistos a teoria sobre SQLite.

## Transaccions

Crea la base de dades comptes a SQLite on hi crearem una taula de comptes i inserirem dos registres per simular que la persona 'a' i la persona 'b' tenen 1000 eur cadascun:
```
sqlite3 comptes.db
CREATE TABLE IF NOT EXISTS comptes (titular text, saldo decimal);
INSERT INTO comptes VALUES ('a',1000), ('b',1000);
```
Obre dos terminals. En una observa els valors de la taula comptes (SELECT * FROM comptes;) i en l'altre executa l'script transaction.py, observant els errors i arreglant-ho:

1) Sense el commit() no hi ha durabilitat en la transacció.
2) commit() desprès de cada execute(): la transacció està mal programada i es pot perdre la coherència si el client perd o avorta la connexió durant els 5 segons d'espera.

Per no perdre la coherència, quantes transaccions hem de tenir? Per tant, a on hem de posar el commit()?

### Exercici i tasca:

Retoca l'script anterior que permeti fer de forma coherent una transacció que liquidi els interessos anuals dels comptes de tipus 'C' de la b.d. bigger.db creada la setmana passada.

| | bigger.db amb |
|:-:|:-------:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">]()|

Suposem que el tipus d'interès és del 1% del saldo actual i només s'aplica als comptes de tipus 'C'. Per tant ingressarem 1 eur per cada 100 eur de saldo que tingui el compte de tipus 'C', arrodonit a 2 decimals (els saldos són en euros i els euros només tenen 2 cèntims).  Aquest diners es transferiran del compte propi del banc que és el compte de tipus 'S' que té el número acc_id menor. Per tant, per liquidar els interessos, el banc transferirà els diners dels interessos des del compte propi del banc (de tipus 'S' que té el número acc_id menor) a cada compte de tipus 'C'. El banc no poc fabricar diners, per tant si sumem el saldo de tots els comptes abans i desprès de fer la liquidació d'interessos han de ser exactament iguals. I tots els comptes han de tenir els saldos només amb dos decimals.

Utilitzeu la b.d. Sqlite3 bigger.db que vam crear la setmana passada amb l'script bigger.py. Només caldrà modificar la taula comptes, taula que guarda la informació dels comptes amb els atributs acc_id, type i balance. És important mantenir la coherència de la base de dades:

- La suma del saldo de tots els comptes abans i desprès de fer la liquidació d'interessos han de ser iguals.
- Tots els saldos han de tenir 2 decimals.
- S'ha de fer la liquidació dels interessos de tots els comptes (o de cap), no ens podem quedar a mitges pq sinó no sabrem a quins compte hem liquidat interessos i a quins no, i a un banc no li fa cap gràcia liquidar els mateixos interessos per duplicat.
  
Puja l'script a la tasca d'Atenea de la sessió 8.

## Solució

| | script-s8 |
|:-:|:-------:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">]()|