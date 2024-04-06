# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Sessió 5 | DL 18 MARÇ 2024 | 

## Enunciat:

### Sessió 5. MySQL & PHP:

<p style="text-align: justify;">
En aquesta sessió aprendrem com connectar una petita aplicació web escrita amb el llenguatge PHP amb MySQL (podríem fer-la connectant a PostgreSQL enlloc de MySQL).

Els fitxers inicials els trobaràs a la carpeta /home/public/dabd/05mysql_php d'ubiwan. El servidor ubiwan, a més de tenir instal·lats els SGBD MySQL i PostgreSQL, té un servidor web apache amb un intèrpret de PHP. Pots deixar els teus fitxers html i php a la carpeta public_html del teu home i seran accessibles públicament amb la URL http://ubiwan.epsevg.upc.edu/~nom_usuari (si encara no tens la carpeta public_html l'hauràs de crear i donar-li permisos d'accés a tothom, segueix les instruccions de la pàgina http://ubiwan.epsevg.upc.edu/)

</p>

1. Mira els fitxers users.html i users.php. Copia'ls a la teva carpeta public_html i introdueix les teves dades (usuari, contrasenya i base de dades) a users.php. Prova'l accedint a http://ubiwan.epsevg.upc.es/~nom_usuari/users.html.
2. Fes el mateix amb els fitxers list_users.html i list_users.php.
3. Fes el mateix amb els fitxers add_users.html i add_users.php.
4. Copia el contingut de la carpeta /home/public/dabd/05mysql_php/crud-php-mysql-simple-inicial al teu public_html. Conté una petita aplicació web que fa les operacions CRUD (Create, Read, Updade i Delete) a la taula d'usuaris. Posa les teves dades de connexió a config.php i prova'l accedint a http://ubiwan.epsevg.upc.es/~nom_usuari/index.php. Mira el codi d'aquesta aplicació web, en especial el fitxer add_edit.php, i si no l'entens pregunta. Fixa't que les dades que s'envien per la URL s'envien pel mètode GET i estan accessibles en el diccionari $_GET i les dades d'un formulari HTML s'envien pel mètode POST i estan accessibles en el diccionari $_POST.
5. Prova les operacions d'afegir i actualitzar usuaris. Comprova si es pot fer SQL injection i en cas de que així sigui arregla-ho per prevenir-ho. Per exemple pots provar d'afegir els següents usuaris amb una contrasenya qualsevol:

    - Versió MySQL', (SELECT @@version));-- x
    - Usuari', (SELECT user()));-- x
    - Taules', (SELECT group_concat(table_name) FROM information_schema.- - tables WHERE table_schema=database()));-- x

6. L'operació d'eliminar usuaris no està implementada. Crea un fitxer delete.php que la implementi.

## Criteris de correcció:

- No fet.
- No funciona afegir usuaris i no puc provar res.
- No es poden editar usuaris.
- No es poden eliminar usuaris.
- No es poden editar usuaris que tenen caràcter ' o ".
- No es poden eliminar usuaris que tenen caràcter ' o ".
- Permet SQL injection.
- L'eliminació d'usuaris no et porta a la pàgina inicial.
- Per eliminar usuaris no fa falta mostrar el formulari de crear/editar usuaris.

## Solució

| | Carpeta |
|:-:|:-------:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/tree/main/LABS/Sessio%205/05mysql_php/crud-php-mysql-artuaragon)|

| |delete.php|add_users.php |
|:-:|:-:|:-:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%205/05mysql_php/crud-php-mysql-artuaragon/delete.php)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%205/05mysql_php/crud-php-mysql-artuaragon/add_edit.php)|