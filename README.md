# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon
Apunts de l'assignatura DABD a la UPC. LAB + TEO

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

|    |S1|S2|S3|S4|S5|
|----|--|--|--|--|--|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/a67f4be1f5b7fcbb9a8d204dfa7c11a67b3da0bd/LABS/Sessio%201/s1-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/a67f4be1f5b7fcbb9a8d204dfa7c11a67b3da0bd/LABS/Sessio%202/s2-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/a67f4be1f5b7fcbb9a8d204dfa7c11a67b3da0bd/LABS/Sessio%203/s3-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/a67f4be1f5b7fcbb9a8d204dfa7c11a67b3da0bd/LABS/Sessio%204/s4-apunts.md)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">]([https://example.com](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/a67f4be1f5b7fcbb9a8d204dfa7c11a67b3da0bd/LABS/Sessio%205/s5-apunts.md))|


## Notes LABS (Sessió 2 - 6) [10%]

| Sessions           | S2                               | S3 | S4 | S5 | S6 |
|--------------------|----------------------------------|----|----|----|----|
| Nota (entre 0 i 5) | 3                                | 5  | -  | -  | -  |
| Errors             | MySQL taula movies no existeix.  | -  | -  | -  | -  |

