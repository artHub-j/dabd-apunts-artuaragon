# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Sessió 4 | DL 11 MARÇ 2024 | 

### Crea les taules tec, maq, evsup i supervisio (pots usar els CREATE TABLE del fitxer maqfact foreign keys.sql).
    -

### Fixat que hi ha claus foranes, i que les clausules de propagacio de modificacions son CASCADE pels UPDATEs i NO ACTION pels DELETEs.
    -

### Comprova si es poden afegir dades a supervisio sense haver afegit res a tec, maq o evsup.
    -

### Recorda que la comprovaci ́o de claus foranes est`a desactivada a SQLite fins que no facis PRAGMA foreign keys = ON;
    -

### Fes pas a pas les queries del fitxer maqfact foreign keys.sql, pensant quin resultat obtindras abans d’executar cada query.

    PRAGMA foreign_keys = OFF;
    "Va be per fer backups de bd. Triga menys ja que no ha de comprovar les restriccions per cada linia."

 