# [ Sessió 3 | DL 04 MARÇ 2024 | Arturo Aragón ]

## Construıu a MySQL i a PostgreSQL queries que obtingin:

### Les taules que tenen m ́es de 50 registres (a PostgreSQL no  ́es possible)

    SELECT * FROM information_schema.tables WHERE table_rows  > 50;

### quantes taules visibles s’anomenen ’accounts’

    SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'accounts';

### quantes columnes s ́on de qualsevol varietat de tipus ’int’

    SELECT COUNT(*) FROM information_schema.columns WHERE column_type = 'int';

### quantes columnes s ́on de qualsevol varietat de tipus ’char’

    SELECT COUNT(*) FROM information_schema.columns WHERE column_type = 'char';

### quantes vistes hi ha

    SELECT COUNT(*) FROM information_schema.views;

## Permisos GRANT i REVOKE

### Podem donar permisos amb la comanda GRANT:
    
    GRANT perm ́ıs ON database.tablename TO username;

### Podem treure permisos amb la comanda REVOKE:

    REVOKE permis ON database.tablename FROM username;

### On el permis pot ser, entre d’altres, SELECT, INSERT, UPDATE, DELETE, ALL. . . Podem indicar que el permıs nom ́es afecti a algunes columnes, per exemple GRANT perm ́ıs(columnes) ON . . . Canvia permisos de la taula de pel·l ́ıcules a PostgreSQL (no teniu permissos per gestionar els permissos al MySQL d’ubiwan).

### Treu el permıs d’eliminar i prova de fer un DELETE.

    REVOKE DELETE ON movies FROM est_d9971765;

### Treu el permıs d’actualitzar i prova de fer un UPDATE.
    REVOKE UPDATE ON movies FROM est_d9971765;

### Treu el permıs d’inserir i prova de fer un INSERT.
    REVOKE INSERT ON movies FROM est_d9971765;

### Treu el permıs de consultar i prova de fer un SELECT.
    REVOKE SELECT ON movies FROM est_d9971765;

### Torna a donar tots els permisos a la taula i prova si ja pots fer SELECT, INSERT, UPDATE i DELETE.
    GRANT ALL ON movies TO est_d9971765

### Treu el permıs de consultar el camp nom de les pel·l ́ıcules. Cal fer un REVOKE SELECT i un GRANT SELECT (columnes).
    -

## Normalitzacio


### Treballarem el problema 3 dels comptes bancaris (sense variants).

    Postgres: A vegades cal posar " dobles cometes " al nom de variables, per evitar errors de caracters.

    UPDATE ON CASCADE: (A taula adreces p.e.) Totes les adreces foreign key s'actualitzen
    DELETE ON CASCATE: P.e. factures e items de factures. (Volem borrar un titular si s'esborra una adreca de correu electronic.)

    Exemple importacio de dades a altres taules normalitzades (accounts to adreces):
        insert adreces select distinct(adress), phone FROM accounts;

### Llista les dependencies funcionals i normalitza a 3FN.

    Normalitzat a 3FN:
        owner_id -> address
        phone -> address
        address -> phone
        acc_id -> balance, type
        acc_id, owner_id -> owner

#

    create table titulars(
        owner_id int PRIMARY KEY not null,
        address varchar(100) references adreces(address)
    );

    create table adreces(
        address varchar(100) PRIMARY KEY not null,
        phone int not null unique
    );

    create table comptes(
        acc_id bigint PRIMARY KEY not null,
        balance real not null,
        type char(1) not null
    );

    create table contractes(
        acc_id bigint not null references comptes,
        owner_id int references titulars,
        owner varchar(40) not null,
        PRIMARY KEY(acc_id, owner_id)
    );

#
    CORRECCIO JORDI:

    DROP TABLE adreces;
    DROP TABLE titulars;
    DROP TABLE comptes;
    DROP TABLE contractes;

    create table adreces(
        address varchar(100) not null PRIMARY KEY,
        phone int unique
    );

    create table titulars(
        owner_id int not null PRIMARY KEY,
        address varchar(100) references adreces(address) ON UPDATE CASCADE
    );

    create table comptes(
        acc_id bigint not null PRIMARY KEY,
        balance real not null,
        type char(1) not null
    );

    create table contractes(
        acc_id bigint not null references comptes ON UPDATE CASCADE,
        owner_id int not null references titulars ON UPDATE CASCADE,
        owner varchar(40) not null,
        PRIMARY KEY(acc_id, owner_id)
    );

#

    -- Insert data into "adreces" table
    INSERT INTO adreces (address, phone)
    SELECT DISTINCT address, phone FROM accounts;

    -- Insert data into "titulars" table
    INSERT INTO titulars (owner_id, address)
    SELECT DISTINCT owner_id, address FROM accounts;

     -- Insert data into "comptes" table
    INSERT INTO comptes (acc_id, balance, type)
    SELECT DISTINCT acc_id, balance, type FROM accounts;

    -- Insert data into "contractes" table
    INSERT INTO contractes (acc_id, owner_id, owner)
    SELECT DISTINCT acc_id, owner_id, owner FROM accounts;


### Defineix els esquemes relacionals amb les claus prim`aries, alternatives i foranes.
    -

### Crea les taules corresponents a MySQL/PostgreSQL.
    -

### Traspassa tota la informacio de la taula accounts sense normalitzar a aquestes noves taules normalitzades.
    -

### Torna a fer les consultes SQL de la 1a sessio sobre aquestes noves taules.
    -