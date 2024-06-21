# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon
Apunts de l'assignatura DABD a la UPC. LAB + TEO.

## Xuleta Comandes MySQL/PostgreSQL

|                            |       SQLite3       |                                                                           MySQL                                                                           |                                                                         PostgreSQL                                                                        |
|:--------------------------:|:-------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Iniciar sessió:            | sqlite3 filename.db | mysql -u est_username -p                                                                                                                                  | psql -h ubiwan.epsevg.upc.edu -U est_username -W                                                                                                          |
| Ajuda:                     | .help               | \h                                                                                                                                                        | \h (Sintaxis SQL) i \? (Comandes CLI)                                                                                                                     |
| Sortir:                    | .quit / .exit       | \q                                                                                                                                                        | \q                                                                                                                                                        |
| Llistar db:                | -                   | show databases;                                                                                                                                           | \l                                                                                                                                                        |
| Canviar de bd:             | -                   | \u                                                                                                                                                        | \c                                                                                                                                                        |
| Llistar taules/vistes:     | .tables             | show tables;                                                                                                                                              | \d                                                                                                                                                        |
| Veure esquema taula/vista: | .schema tablename   | desc table/view;                                                                                                                                          | \d table/view                                                                                                                                             |
| Importar SQL:              | -                   | mysql -u username -p databasename < data.sql                                                                                                              | psql -U username databasename < data.sql                                                                                                                  |
| Exportar SQL:              | -                   | mysqldump -u username -p databasename [tablename] > data.sql (Si vols poder importar-la en altres SGBD pot ser convenient usar l’opcio --compatible=ansi) | pg dump -U username databasename [-t tablename] > data.sql (Format mes compatible afegint opcions: --no-tablespaces --no-owner --no-acl --column-inserts) |

## Solucions LABS

| Sessió |S1|S2|S3|S4|S5|S6|S7|S8|S9|S10|S11|S12|
|----|--|--|--|--|--|--|--|--|--|--|--|--|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%201/s1-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%202/s2-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%203/s3-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%204/s4-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%205/s5-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%206/s6-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%207/s7-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%208/s8-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%209/s9-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%2010/s10-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%2011/s11-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%2012/s12-apunts.md)|

### Notes LABS 1ª Part (Sessió 1 - 6) [10%]

| Sessions           |S1| S2                               | S3 | S4 | S5 | S6 |
|--------------------|--|----------------------------------|----|----|----|----|
| Nota  |5/5 |3/5                                | 5/5  | 4.5/5  | 4/5  | 5/5  |
| Errors             |Bé|MySQL taula movies no existeix.  | Bé | Host havia de ser ubiwan.epsevg.upc.edu. | No es poden editar/eliminar usuaris que tenen caràcter ".   | Bé |

|Nota Total LABS 1ª Part|
|:---:|
|<b>8.6</b>|

### Notes LABS 2ª Part (Sessió 7 - 12) [10%]

| Sessions           |S7 (1p) |S8 (1p) |S9 (1p) |S10 (1p) |S11 (3p) |S12 (3p) |
|--------------------|--|--|--|---|---|---|
| Nota  | 4/5 | 3/5 | 3.5/5 | 0/5 | 5/5 | 4.5/5 |
| Errors             | No ben raonat postgres. |  Interessos mal calculats. |Valors de work_mem,  maintenance_work_mem i effective_cache_size no adients. |  MySQL No ben raonat, No logs Postgres, PostgreSQL Millora no adequada, No ben raonat | Bé | Contractes no són un map<int, text> |

|Nota Total LABS 2ª Part|
|:---:|
|<b> 7.8 </b>|

## Exemples d'Examen LAB (Activitat 1) [10%]

| Examen LAB |aprovats.db (2022-2023) |registre_parelles.db (2023-2024 A)|linies_factura.db (2023-2024 B)|
|:--:|:---------:|:------------------:|:---------------:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/Exemples%20Activitat%201/Activitat1-apunts-aprovats.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/Exemples%20Activitat%201/Activitat1-apunts-registre_parelles.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/Exemples%20Activitat%201/Activitat1-apunts-linies_factura.md)|

<!--
## Directory Tree

- <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> dabd-apunts-artuaragon/
  - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Exemples Activitat 1/
    - ├── Activitat1-apunts-aprovats.md
    - ├── Activitat1-apunts-linies_factura.md
    - ├── Activitat1-apunts-registre_parelles.md
    - ├── aprovats1.txt
    - ├── aprovats2.txt
    - ├── aprovats3.txt
    - ├── aprovats.db
    - ├── linies_factura.db
    - ├── linies_factura_v1.txt
    - ├── linies_factura_v2.txt
    - ├── registre_parelles.db
    - ├── registre_parelles_v1.txt
    - └── registre_parelles_v2.txt
  - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> LABS/
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 1/
      - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 01set_theory/
        - ├── set_theory.db
        - ├── set_theory.sql
        - └── set_theory.txt
      - └── s1-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 10/
      - └── s10-apunts.md
      - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 11/
        - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 11mongodb/
        - └── users_mongodb.py
      - └── s11-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 12/
        - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 12firestore/
        - ├── users_firestore.py
        - └── users_firestore_username_identifier.py
      - └── s12-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 2/
        - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 02accounts/
          - ├── accounts1.db
          - ├── accounts2.db
          - ├── accounts2.txt
          - ├── accounts.sql
          - └── accounts.txt
        - └── s2-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 3/
        - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 03claus_foranees/
          - └── maqfact_foreign_keys.sql
        - └── s3-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 4/
        - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 04python_sqlinjection/
          - ├── users_sqlite_inj.py
          - └── users_sqlite_no_inj.py
          - ├── prova.db
      - ├── s4-apunts.md
      - ├── sqlite3
      - ├── users.db
      - ├── users_mysql.py
      - └── users_postgres.py
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 5/
        - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 05mysql_php/
        - ├── add_users.html
        - ├── add_users.php
      - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> crud-php-mysql-artuaragon/
        - ├── add_edit.php
        - ├── b_drop.png
        - ├── b_edit.png
        - ├── config.php
        - ├── delete.php
        - └── index.php
      - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> crud-php-mysql-simple-inicial/
        - ├── add_edit.php
        - ├── b_drop.png
        - ├── b_edit.png
        - ├── config.php
        - └── index.php
        - ├── list_users.html
        - ├── list_users.php
        - ├── users.html
        - └── users.php
      - └── s5-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 6/
      - └── s6-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 7/
      - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 07indexs/
        - ├── bigger.py
        - └── consulta_bigger.py
      - └── s7-apunts.md
    - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 8/
      - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 08transactions_triggers/
        - └── transaccions.py
      - └── s8-apunts.md
    - └── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> Sessio 9/
        - ├── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> 09postgresql/
        - └── bigger.sql
      - └── s9-apunts.md
  - ├── Practiques (Sessions 1, 2, 3 i 4).pdf
  - ├── README.md
  - └── <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/1dc870d5-fb16-43e4-97e9-9b5873051af9" width="15" alt="folder"> TEO/
-->

## Annex: Tasques habituals que sol fer un administrador de PostgreSQL

### Crear usuari
```
sudo su postgres
createuser --pwprompt --createdb nom_usuari
```
### Eliminar usuari
```
sudo su postgres
dropuser nom_usuari
```
### Veure usuaris donats d'alta
```
$ sudo su postgres
$ psql
# select * from pg_shadow;
```
### Crear base de dades
```
sudo su postgres
createdb nom_base_de_dades -O nom_usuari
```
o bé:
```
$ psql
postgres=# CREATE DATABASE nom_base_de_dades OWNER nom_usuari;
```
### Eliminar base de dades
```
sudo su postgres
dropdb nom_base_de_dades
```
### Usuaris usant la base de dades i matar queries
Per saber quins usuaris estan usant les diferents b.d. o quines queries s'estan executant:
```
SELECT * FROM pg_stat_activity;
```
Per matar una query en concret, hem d'agafar el número de la columna procpid del llistat anterior i fer:
```
SELECT pg_cancel_backend(procpid);
```
### Còpies de Seguretat
```
pg_dump nom_base_de_dades > filename
```
Es recupera amb:
```
psql nom_base_de_dades < filename
```
