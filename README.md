# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon
Apunts de l'assignatura DABD a la UPC. LAB + TEO.

## Xuleta Comandes MySQL/PostgreSQL

|   |MySQL|PostrgreSQL|
|---|-----|---------|
|Iniciar sessió: |mysql -u est_username -p | psql -h ubiwan.epsevg.upc.edu -U est_username -W|
|Ajuda: |\h| \h (Sintaxis SQL) i \\? (Comandes CLI)|
|Sortir: |\q|\q|
|Llistar db: |show databases;| \l|
|Canviar de bd: |\u| \c|
|Llistar taules/vistes: |show tables;|\d|
|Veure esquema taula/vista: |desc table/view;|\d table/view|
|Importar SQL: |mysql -u username -p databasename < data.sql| psql -U username databasename < data.sql|
|Exportar SQL: |mysqldump -u username -p databasename [tablename] > data.sql (Si vols poder importar-la en altres SGBD pot ser convenient usar l’opcio --compatible=ansi)| pg dump -U username databasename [-t tablename] > data.sql (Format mes compatible afegint opcions: --no-tablespaces --no-owner --no-acl --column-inserts)|

## Solucions LABS

|    |S1|S2|S3|S4|S5|S6|S7|S8|S9|S10|S11|S12|
|----|--|--|--|--|--|--|--|--|--|--|--|--|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%201/s1-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%202/s2-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%203/s3-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%204/s4-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%205/s5-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%206/s6-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%207/s7-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%208/s8-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%209/s9-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%2010/s10-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%2011/s11-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%2012/s12-apunts.md)|

## Notes LABS 1ª Part (Sessió 1 - 6) [10%]

| Sessions           |S1| S2                               | S3 | S4 | S5 | S6 |
|--------------------|--|----------------------------------|----|----|----|----|
| Nota (entre 0 i 5) |5 |3                                | 5  | 4.5  | 4  | -  |
| Errors             |Bé|MySQL taula movies no existeix.  | Bé | Host havia de ser ubiwan.epsevg.upc.edu. | No es poden editar/eliminar usuaris que tenen caràcter ".   | -  |

|Total Provisional|
|:---:|
|6.6|

## Notes LABS 2ª Part (Sessió 7 - 12) [10%]

| Sessions           |S7|S8|S9|S10|S11|S12|
|--------------------|--|--|--|---|---|---|
| Nota (entre 0 i 5) |- |- |- | - | - | - |
| Errors             |- |- |- | - | - | - |

## Exemples d'Activitat 1

|    |aprovats.db|
|----|:--:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/Exemples%20Activitat%201/Activitat1-apunts.md)|

#
