# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Sessió 9 | DL 13 MAIG 2024 | 

## A. Instal·lació de PostgreSQL

Instal·la el servidor i client de PostgreSQL:
```
$ sudo apt-get install postgresql postgresql-client
```
## B. Configuració
Quan s'instal.la PostgreSQL es crea un usuari postgres (usuari tant del sistema GNU/Linux com de la base de dades que tenen el mateix nom postgres). Aquest usuari ens permetrà administrar/configurar PostgreSQL. Amb ell podrem accedir al client de PostgreSQL (psql) sense que ens demani cap contrasenya:
```
$ sudo su postgres
$ psql
\l
\q
```
Amb aquestes comandes de Unix podem crear usuaris addicionals amb la seva clau d'accés (password) i bases de dades que pertanyin a un usuari en concret:
```
$ createuser --pwprompt --createdb --no-createrole --no-superuser nom_usuari
$ createdb nom_base_de_dades -O nom_usuari
```
Crea un usuari anomenat userdabd i una base de dades anomenada dabd que pertanyi a l'usuari userdabd.

Configurar l'accés a PostgreSQL (hba - Host Basic Access)
Si volem accedir amb l'usuari anterior amb la contrasenya que li hem donat (encriptada amb md5) enlloc d'usar un usuari del sistema operatiu Linux que es digui igual, cal modificar el fitxer /etc/postgresql/12/main/pg_hba.conf (cal canviar el número 12 segons la versió de PostgreSQL que tenim) canviant aquesta línia:
```
# "local" is for Unix domain socket connections only
local   all             all                                     peer
per

# "local" is for Unix domain socket connections only
local   all             all                                     md5
Si també volem accedir des d'algunes màquines de l'exterior faríem (aquest exemple permet accedir a la mateixa màquina, a les màquines de la xarxa local 192.168.0.x i màquines de 62.57.200.x):

# IPv4 local connections:
host    all         all         127.0.0.1/32          md5
host    all         all         192.168.0.0 255.255.255.0 md5
host    all         all         62.57.200.0 255.255.248.0 md5
Desprès caldrà rearrancar el servidor PostgreSQL:

$ sudo service postgresql restart
```

que equival a fer: 
```
$ sudo /etc/init.d/postgresql restart
```
## C. Treballar amb el client psql
Podem accedir amb el client psql a una base de dades i usuari en concret (psql nom_base_de_dades nom_usuari). En el nostre cas:
```
$ psql dabd userdabd
\l
\d
\q
```
Amb \l veurem el llistat de totes les bases de dades disponibles (només tenim les plantilles template0 i template1 i la base de dades interna del propi SGBD anomenada postgres). Amb \d veurem les taules de la base de dades actual (no en hi ha cap).

Crearem varies taules i afegirem vàries files des del fitxer de comandes SQL bigger.sql que trobareu a ubiwan. El fitxer bigger.sql inicia una transacció on crea i omple 3 taules (accounts, owners i names) i és una variació de l'exemple de comptes bancaris sense adreces. Si hi ha algun problema (per exemple ja existia una taula anomenada accounts) es fa un ROLLBACK. Desprès consultarem de nou les taules i índexs creats, i el detall de cada taula:
```
$ psql dabd userdabd < bigger.sql
$ psql dabd userdabd
\d
\d names
\d owners
\d accounts
\di
```
Provem a fer un SELECT amb dos JOIN:
```
SELECT * from names n, owners o, accounts a WHERE n.nif=o.own_id AND n.name=o.own_name AND o.acc_id=a.acc_id;
Nota: És el mateix que fer aquest SELECT on posem de forma explícita les paraules JOIN:

SELECT * from names n JOIN owners o ON n.nif=o.own_id AND n.name=o.own_name JOIN accounts a ON o.acc_id=a.acc_id;
```
## D. Optimitzar postgreSQL
La configuració per defecte de postgreSQL és molt conservadora. Podem augmentar notablement el seu rendiment si li assignem més memòria RAM per fer molts dels seus processos.

Optimització general

Cal editar els següents paràmetres del fitxer /etc/postgresql/12/main/postgresql.conf (cal canviar el número 12 segons la versió de PostgreSQL que tenim) i posteriorment reiniciar el servidor PostgreSQL. Aquesta proposta s'ha extret de diferents tutorials com per exemple Tuning_Your_PostgreSQL_Server. També podem usar la calculadora Pg Tune.

Per saber que significa cada paràmetre mira la documentació de postgreSQL.

| Paràmetre            | Valor per defecte | Recomanat                            | Notes                                                              |
|----------------------|-------------------|--------------------------------------|--------------------------------------------------------------------|
| shared_buffers       |                   | 0.25 * Available Memory              | Veure Nota (a)                                                     |
| work_mem             | 4MB               | Available Memory / (max_connections) | Si no arriba a 16MB, caldria comprar més memòria                   |
| maintenance_work_mem | 64MB              | Available Memory / 8                 |                                                                    |
| wal_buffers          | 64kB              | -1 (agafarà 8MB o 16MB)              | Noves versions postgres agafarà automàticament 8MB o 16MB si és -1 |
| effective_cache_size | 4GB               | Available Memory * 0.75              |                                                                    |
| cpu_tuple_cost       | 0.0100            | 0.0030                               |                                                                    |
| cpu_index_tuple_cost | 0.0050            | 0.0010                               |                                                                    |
| cpu_operator_cost    | 0.0025            | 0.0005                               |                                                                    |

Nota 1: Available Memory = Memòria física de la màquina menys la memòria usada per altres serveis (sistema operatiu, apache, mysql, ...).

### Configuració del WAL (Write Ahead Log)

checkpoint_timeout: Permet definir el temps màxim que es realitza cada checkpoint que implica escriure a disc les pàgines amb dades modificades i totes les operacions del WAL. Per defecte 5 minuts

max_wal_size: Permet definir la grandària màxima que pot ocupar el WAL. Per defecte 1GB.

Quan s'arribi al temps de checkpoint_timeout o quan el WAL ocupi max_wal_size, el que passi primer, s'escriuen a disc les pàgines amb dades modificades i totes les operacions del WAL. Això implica que el SGBD ha de dedicar molts recursos de I/O a disc cada cert temps. Si incrementem els valors de checkpoint_timeout i/o max_wal_size, el SGBD no tindrà tantes interrupcions però tindrem l'inconvenient que en cas d'una caiguda del sistema, el temps de recuperació serà més gran.

Per a més detalls llegir la documentació: WAL configuration

### Optimització de queries individuals

Per optimitzar queries individuals, podem activar el log de queries lentes, per exemple les que durin més de 50 mseg. Les guardarà a /var/log/postgresql/postgresql-12-main.log:

  log_min_duration_statement = 50

Optimització temporal per fer una importació de moltes dades

Per fer un import d'una b.d. molt voluminosa es pot optimitzar canviant aquests paràmetres (cal tornar a deixar els paràmetres anteriors un cop l'import estigui fet i executar un VACUUM ANALYZE sobre la b.d. per actualitzar les estadístiques internes):

  fsync = off
  shared_buffers = [1/3 of available memory]
  wal_buffers = 1MB
  checkpoint_timeout = 1h
  checkpoint_segments = 300  # Have a *lot* of spare disk space for this
  maintenance_work_mem = [1/3 of available memory]


Aquests són altres paràmetres importants del fitxer de configuració /etc/postgresql/12/main/postgresql.conf, que no cal que modifiqueu.

Port a on escolta el servidor PostgreSQL:

port = 5432
Si només acceptem connexions des del localhost:

listen_addresses = 'localhost'
Però si acceptem connexions de tot arreu:

listen_addresses = '*'
O d'alguna IP en concret (podem posar una llista de IPs separades per comes):

listen_addresses = 'localhost,80.35.151.105'            # what IP address(es) to listen on;

## E. Tasques a fer

a) Instal·la el client i el servidor PostgreSQL en el teu PC o portàtil seguint les instruccions de l'apartat A.

b) Configura el servidor i crea un usuari i una base de dades seguint les instruccions de l'apartat B.

c) Prova el client connectant-lo al servidor seguint les instruccions de l'apartat C.

d) Optimitza el servidor segons la memòria disponible que disposi el teu computador i el màxim de connexions simultànies que necessitis seguint les instruccions de l'apartat D.

e) Estudia si el SGBD PostgreSQL del servidor ubiwan està ben configurat. Tingues en compte que a ubiwan s'executa un servidor de fitxers per a tots els usuaris linux de docència, un servidor web Apache, un SGBD MySQL i un SGBD PostgreSQL.

1. Esbrina la quantitat de RAM disposa el servidor ubiwan.
2. Esbrina la quantitat de CPUs disposa el servidor ubiwan.
3. Esbrina si el disc del servidor ubiwan és un HDD o un SSD
4. Esbrina quina versió de PostgreSQL hi ha instal·lada al servidor ubiwan
5. Esbrina quantes connexions màximes permeses ha configurat l'administrador de sistemes de l'EPSEVG a PostgreSQL
6. Calcula quins paràmetres de configuració de PostgreSQL serien els ideals i compara'ls amb els que hi ha definits.
7. Respon el qüestionari d'Atenea.

Et pot ser d'utilitat mirar el contingut d'aquests fitxers:

- /proc/meminfo
- /proc/cpuinfo
- /sys/block/sda/queue/rotational

## Annex: Tasques habituals que sol fer un administrador de PostgreSQL

## Crear usuari
```
sudo su postgres
createuser --pwprompt --createdb nom_usuari
```
## Eliminar usuari
```
sudo su postgres
dropuser nom_usuari
```
## Veure usuaris donats d'alta
```
$ sudo su postgres
$ psql
# select * from pg_shadow;
```
## Crear base de dades
```
sudo su postgres
createdb nom_base_de_dades -O nom_usuari
```
o bé:
```
$ psql
postgres=# CREATE DATABASE nom_base_de_dades OWNER nom_usuari;
```
## Eliminar base de dades
```
sudo su postgres
dro-pdb nom_base_de_dades
```
## Usuaris usant la base de dades i matar queries
Per saber quins usuaris estan usant les diferents b.d. o quines queries s'estan executant:
```
SELECT * FROM pg_stat_activity;
```
Per matar una query en concret, hem d'agafar el número de la columna procpid del llistat anterior i fer:
```
SELECT pg_cancel_backend(procpid);
```
## Còpies de Seguretat
```
pg_dump nom_base_de_dades > filename
```
Es recupera amb:
```
psql nom_base_de_dades < filename
```