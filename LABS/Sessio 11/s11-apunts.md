# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Sessió 11 | DL 27 MAIG 2024 |

# Sessió 11. Base de dades no relacional: MongoDB. Replicació a MongoDB.

## 1. Exemple d'ús de mongoDB

### 1. Instal·la't mongoDB. Tens dues opcions:

#### 1.a) Instal·lació com a servidor en el teu sistema operatiu. Pots seguir les indicacions de https://docs.mongodb.com/manual/administration/install-on-linux/

#### 1.b) Instal·lant Docker, un gestor de contenidors de Linux, i baixant el contenidor per a MongoDB que conté la darrera versió del servidor (mongod) i del client CLI (mongosh):

```
sudo apt-get install docker.io
docker -v
sudo su
docker info
docker pull mongo
docker images
```

Arrancarem una instància del servidor mongod:

```
docker run -d -p 27017:27017 --name mongodabd mongo mongod
```

Podem veure quines contenidors de Docker estan executant-se i els recursos que consumeixen amb:

```
docker stats
```

I executar el client CLI mongosh sobre la instància mongodabd de forma interactiva (-it), per tal de crear bases de dades, col·leccions i documents:

```
docker exec -it mongodabd mongosh
```

### 2. Connecta't amb el client de línies de comanda (mongo). Crea una base de dades (dabd) amb dues col·leccions (alumne i professor) on inserirem diferents documents. També practiquem les cerques, actualitzacions i eliminacions de documents.

```
use dabd
show dbs
db.createCollection('alumne')
show dbs
show collections
```

T'has fixat que realment no s'ha creat la base de dades dabd fins que no hem creat la col·lecció alumne? mongoDB és un gandul, no fa la feina fins que realment és necessari.

```
db.alumne.insert({'nom': 'Oriol', 'c1': 7, 'observacions': 'Treballa'})
db.alumne.insert({'nom': 'Pau', 'c1': 4})
db.alumne.insert({'nom': 'Paula', 'c1': 6})
db.alumne.insert({'nom': 'Pol', 'c1': 6})
db.alumne.insert({'nom': 'Pau', 'c1': 6})
db.alumne.find()
db.alumne.find({'nom': 'Pau'})
db.alumne.find({'nom': /Pa/})
db.alumne.find({'nom': /pa/})
db.alumne.find({'nom': /pa/i})
db.alumne.find({'c1': {$gt: 5}})
db.alumne.find({'c1': {$gt: 5}}, {'nom': 1})
```

Als nous documents afegeix automàticament el camp \_id amb un identificador únic que els identifica, ja que no li hem indicat cap.

Creem un índex de tipus text amb el que podem fer cerques molt més eficients (per defecte les col·leccions només tenen un índex format amb el camp \_id):

```
db.alumne.createIndex({nom: "text"})
db.alumne.find({$text: {$search: "Pol"}})
```

Mira't com són els [índexs a mongoDB](https://www.mongodb.com/docs/manual/indexes/), els tipus d'índex que proporciona i les propietats que poden tenir.

Creem i treballem sobre la segona col·lecció professor, fent insercions, actualitzacions i eliminacions:

```
db.professor.insert({'nom': 'Balqui', 'afició': 'Música'})
show collections
db.professor.insert({'nom': 'Jordi', 'afició': 'DIY', 'assignatures': ['DABD', 'PMUD', 'INFO']})
db.professor.update({'nom': {$eq: 'Balqui'}}, {$set: {'assignatures': ['DABD']}})
db.professor.find({'nom': {$eq: 'Balqui'}})
db.professor.remove({'nom': {$eq: 'Jordi'}})
```

Pots trobar més detalls de totes les operacions CRUD de mongoDB a [Mongo CRUD Operations](https://www.mongodb.com/docs/manual/crud/#crud).

Per eliminar la base de dades faríem això, però no ho facis de moment:

```
db.dropDatabase()
```

Disposem d'eines potents per processar grans quantitats de dades i obtenir dades agregades. Per exemple [Map-Reduce](https://www.mongodb.com/docs/manual/core/map-reduce/) on indiquem dues funcions escrites amb JavaScript, la primera per fer el mapping del tots els registres per obtenir una parella clau-valor i la segona per fer el reduce de les parelles claus-valors per obtenir el resultat de l'agregació dins d'una nova col·lecció. En aquest exemple volem obtenir la nota mitja del control 1 dels alumnes que el seu nom comenci per "Pa" agrupats segons el seu nom. Per veure el resultat real de la nova col·lecció "nota_mitja" cal que afegiu un .find() al final que com saps obté tots els elements d'una col·lecció:

```js
db.alumne.mapReduce(
  function () {
    emit(this.nom, this.c1);
  }, //map function
  function (key, values) {
    return Array.avg(values);
  },
  {
    //reduce function
    out: "nota_mitja",
    query: { nom: /pa/i },
  }
);
```

Una altra tècnica d'agregació de dades que tenen les noves versions de mongoDB és l'[Aggregation Pipelines](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/). Aquest exemple obté el mateix resultat que l'exemple anterior:

```js
db.alumne.aggregate([
  { $match: { nom: /pa/i } },
  { $group: { _id: "$nom", nota_mitja: { $avg: "$c1" } } },
]);
```

### 3. Instal·la't un client amb GUI de mongoDB, per exemple [MongoDB Compass](https://www.mongodb.com/products/tools/compass) (Community Edition). Connecta't al servidor i mira't i gestiona els continguts de la base de dades dabd. Ves a una de les col·leccions de la base de dades dabd i mira't les diferents pestanyes que ofereix:

- Documents: Consulta dels documents en vista llista o taula
- Aggregations: On podem crear i gestionar Aggregation Pipelines. Crea un com el que hem definit abans amb la comanda aggregate().
- Explain Plan: Per avaluar el rendiment de les consultes (prova diferents filtres, a veure quin pot aprofitar algun índex)
- Indexes: Gestió dels índexs de la col·leció, observa que per defecte sempre en tenen un basat en el camp \_id

### 4) Instal·lat la llibreria Python de mongoDB:

```
pip3 install pymongo
```

Mira el codi del programa Python users_mongodb.py i executa'l varies vegades per:

- Opció -i: Crea una base de dades i una col·lecció
- Opció -a: Afegeix nous usuaris i contrasenyes
- Opció -l: Llista tots els usuaris i contrasenyes
- Opció -d: Elimina un usuari
- Sense cap opció: Mira si existeix un usuari i contrasenya en concret

El codi permet fer SQL injection o alguna cosa similar? En cas afirmatiu, què caldria fer per evitar-ho?

### 5. Feina a fer

Cal adaptar l'script bigger.py de la Sessió 7. Índexs que crea 900 comptes, 500 adreces, 1000 titulars i 4000 contractes per fer-ho en una base de dades mongoDB anomenada bank. L'has de pujar a la tasca d'aquesta sessió. Consells:

- Aprèn a usar la llibreria pymongo en poc temps a partir d'exemples. Mira't el codi de l'script users_mongodb.py i exemples de codi en recursos a la web:

1. [Tutorial de pymongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)
2. [Exemples de tasques específiques de pymongo](https://pymongo.readthedocs.io/en/stable/examples/index.html)

- No has de crear una col·lecció de mongoDB per cada taula de l'esquema relacional. Recordar que a mongoDB, com a la majoria de les BD no relacionals, pots guardar valors no atòmics en els camps, com els subdocuments i els arrays que permeten guardar un document o llistes de dades dins d'un camp respectivament. Per exemple, com que la taula titular només guarda el owner_id del titular i la seva adreça, els podem guardar directament dins la col·lecció adreces: cada adreça tindrà un array amb els titulars que viuen en aquella adreça. O dins la col·lecció comptes podem guardar els titulars de cada compte, o sigui els contractes (own_id i owner). A una adreça hi viuen pocs titulars i un compte té pocs titulars, per tant seran arrays molt petits. A més és molt habitual les operacions de consulta de les dades d'un compte i les dades d'una adreça. Així, amb una única operació de lectura i sense haver de fer joins perquè no en tenim, podem obtenir totes les dades d'un compte (tipus, saldo i titulars del compte). Idem amb la lectura d'una adreça i les persones que hi viuen.
- El nombre de contractes d'un compte i el nombre de titulars d'una adreça han de ser aleatoris però com a mínim n'hi ha d'haver un (per exemple no té sentit un compte sense cap contracte, el compte ha de pertànyer com a mínim a una persona).
- Cada vegada que s'executi l'script cal que elimini els documents de totes les col·leccions, de forma que desprès d'executar-lo han d'haver-hi sempre 900 comptes, 500 adreces, 1000 titulars i 4000 contractes.
- El mateix script ha de crear els índexs que siguin necessaris per accelerar els accessos a les col·leccions o per evitar dades repetides (índexs únics). Mira la documentació de [com crear índexs des de pymong](https://pymongo.readthedocs.io/en/stable/tutorial.html#indexing). Algunes comprovacions per evitar repeticions les hauràs de fer a nivell de codi, per exemple per comprovar no afegir dos titulars amb el mateix owner_id en adreces diferents o en el mateix compte bancari.
- Com hem dit, els titulars els guardem com arrays dins de la col·lecció adreces, suposem que aquest camp es diu 'titulars'. Per comprovar si un titular està dins d'un adreça, hem de cercar que algun element de l'array 'titulars' de la col·lecció adreces coincideixi amb el titular. Ho podem fer usant l'operador $elemMatch:

```
res = db.adreces.find_one({'titulars': {'$elemMatch': {'$eq': owner_id}}})
```

Per obtenir un document aleatori pots usar l'operador $sample de les agregacions de mongoDB. Per exemple per obtenir una adreça aleatòria de la col·lecció de 500 adreces:

```
adreces = list(db.adreces.aggregate([{'$sample': {'size': 1}}]))
```

## 2. Replicació en MongoDB

### 1) mongoDB, igual que la majoria de bases de dades no SQL i també algunes SQL, permet replicació per tal de tenir redundància i alta disponibilitat.

Podem definir un conjunt de rèplica que és un conjunt de processos de servidor mongod gestionant el mateix conjunt de dades. De tots aquests conjunt de processos o nodes, només un d'ells és considerat el node primari i la resta els nodes secundaris. Les operacions d'escriptura només les rep el node primari, les de lectura per defecte també encara que també poden ser servides pels nodes secundaris, permetent millorar el rendiment de les operacions de lectura doncs millorem la disponibilitat i que les dades puguin ser servides per nodes locals (més propers als clients que les demanen).

El node primari guarda els canvis de les operacions d'escriptura en les seves bases de dades i ho registra en el log (oplog) i de forma asíncrona replica aquests canvis en els nodes secundaris (tant en les seves bases de dades com en els seus propis logs).

Si el node primari deixa d'estar disponible, es fa una votació entre els nodes restants per escollir quin és el nou node primari. Entre tots els nodes es van enviant missatges per saber quins dels restants estan disponibles (heartbeat).

En un conjunt de rèplica, a més de node primari i nodes secundaris, també podem tenir nodes àrbitre. Aquests no guarden cap tipus de dada, només serveixen per fer la votació i desempatar, per exemple quan el nombre de nodes és parell.

Es recomana que el conjunt de rèplica com a mínim tingui 3 nodes (un primari i dos secundaris; o un primari, un secundari i un àrbitre). Com a màxim mongoDB permet conjunts de rèplica amb 50 nodes dels quals com a màxim 7 poden votar.

Consulta el manual per conèixer més detalls de la [replicació a mongoDB](https://www.mongodb.com/docs/manual/replication/) (hi ha varis diagrames que il·lustren l'explicació anterior). Trobaràs més detalls sobre els diferents tipus de nodes, com es sincronitzen les dades i els logs, diferents arquitectures de conjunts de rèplica per tal de tenir més o menys toleràncies a errors dels seus membres, distribució de càrrega, distribució geogràfica dels membres, ...

### 2. Instal·la Docker, un gestor de contenidors de Linux, i baixa el contenidor per a MongoDB que conté la darrera versió del servidor (mongod) i del client CLI (mongosh):

```
sudo apt-get install docker.io
docker -v
sudo su
docker info
docker pull mongo
docker images
```

La darrera comanda ens mostra les imatges de contenidors que tenim disponibles per poder ser arrancats en qualsevol moment, actualment només mongo. Podríem baixar-nos contenidors per servidors PostgreSQL, MySQL, etc.

Anem a crear un conjunt de rèplica de MongoDB (Replica Set) amb 3 nodes, aquests nodes o instàncies seran tres contenidors de noms mongo1, mongo2 i mongo3 que arrenquin mongod escoltant en diferents ports. Aquest exercici està basat en l'article [Creating a MongoDB replica set using Docker](https://www.sohamkamani.com/docker/mongo-replica-set/). En un cas real aquests nodes estarien situats en diferents servidors i segurament en diferents data centers separats físicament per evitar que alguna incidència física o catàstrofe natural pugui afectar tots els nodes simultàniament.

Primer crearem una xarxa fictícia amb Docker anomenada my-mongo-cluster:

```
docker network ls
docker network create my-mongo-cluster
docker network ls
```

Ara arrancarem les 3 instàncies del servidor mongod:

```
docker run -d -p 30001:27017 --name mongo1 --net my-mongo-cluster mongo mongod --replSet my-mongo-set

docker run -d -p 30002:27017 --name mongo2 --net my-mongo-cluster mongo mongod --replSet my-mongo-set

docker run -d -p 30003:27017 --name mongo3 --net my-mongo-cluster mongo mongod --replSet my-mongo-set
```

Els paràmetres indicats per arrancar cada instància serveixen per:

- docker run : Start a container from an image
- -d: Detached. Start the container in background, detached from the terminal
- -p 30001:27017 : Expose port 27017 in our container, as port 30001 on the localhost
- --name mongo1 : name this container “mongo1”
- --net my-mongo-cluster : Add this container to the “my-mongo-cluster” network.
- mongo : the name of the image we are using to spawn this container
- mongod --replSet my-mongo-set : Run mongod while adding this mongod instance to the replica set named “my-mongo-set”

Podem veure quines contenidors de Docker estan executant-se i els recursos que consumeixen amb:

```
docker stats
```

Anem a executar el client CLI mongosh sobre la instància mongo1 de forma interactiva (-it), per tal de configurar el conjunt rèplica:

```js
docker exec -it mongo1 mongosh
config = {
"\_id" : "my-mongo-set",
"members" : [
{
"_id" : 0,
"host" : "mongo1:27017"
},
{
"_id" : 1,
"host" : "mongo2:27017"
},
{
"_id" : 2,
"host" : "mongo3:27017"
}
]
}
rs.initiate(config)
rs.status()
```

Podem comprovar que el conjunt rèplica té 3 membres, un PRIMARY i dos SECONDARY. El prompt ha canviat per my-mongo-set:PRIMARY>, indicant-nos que estem connectats al PRIMARY. Les comandes que afecten al Replica Set comencen amb rs. Mira't la documentació de MongoDB sobre [els mètodes disponibles per la replicació](https://www.mongodb.com/docs/manual/reference/method/js-replication/) per veure les possibilitats que ofereix, com per exemple afegir un membre (add), afegir un membre que només és àrbitre (addArb), eliminar un membre (remove), forçar que un node primari esdevingui secundari provocant una votació (stepDown), ...

Anem a crear una base de dades dabd que contindrà la col·lecció alumne amb un document amb l'alumne Pau:

```
db = (new Mongo('localhost:27017')).getDB('dabd')
db.alumne.insert({nom : 'Pau'})
db.alumne.find()
```

Obre una 2a terminal per tal d'executar el client mongo sobre la instància mongo2 de forma interactiva i comprovar que realment té la mateixa informació:

```
docker exec -it mongo2 mongosh
db = (new Mongo('mongo2:27017')).getDB('dabd')
rs.secondaryOk()
db.alumne.find()
```

Ha calgut fer rs.secondaryOk() per indicar que els nodes secundaris poden respondre a lectures (per defecte només fan la sincronització de les dades però no són actius a peticions externes).

Fes el mateix amb una 3a terminal: Executa el client mongo sobre la instància mongo3 de forma interactiva i comprova que realment té la mateixa informació

Insereix un nou document des del clients connectats a mongo2 i a mongo3. Què passa? Per què no es pot?

```
db.alumne.insert({nom : 'Marta'})
```

Executa les següents comandes a mongo1. rs.stepDown() converteix el node PRIMARY en un SECONDARY i per tant força l'elecció d'un nou PRIMARY. Ara quin node és el PRIMARY?

```
rs.stepDown()
rs.status()
```

Obre una nova terminal i atura temporalment el node mongo2. Mira de nou l'estat dels nodes amb rs.status() per veure l'estat del node mongo2 i si hi hagut canvi de node PRIMARY:

```
docker stop mongo2
```

Tona a arrancar mongo2 i torna a mirar l'estat de tots els nodes:

```
docker start mongo2
```

Si tens mongosh instal·lat en el teu PC, pots connectar-te directament a un dels nodes del replicat set mitjançant els port 30001, 30002 o 30003. Per exemple:

```js
mongosh localhost:30001

my-mongo-set:PRIMARY> use dabd
switched to db dabd
my-mongo-set:PRIMARY> db.alumne.find()
{ "\_id" : ObjectId("60a35a3c4570c50f5affb14d"), "nom" : "Pau" }
```
