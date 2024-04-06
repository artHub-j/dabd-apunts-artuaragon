# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Activitat 1 Apunts | ABRIL 2024 |

## Instruccions

- Per obrir arxiu:
```
sqlite3 nom.db
```
- Activar format taules:
```
.header on
.mode column
```
- Veure totes les taules 
```
.tables
```
- I la seva estructura:
```
.schema nom_taula
```

## Solució

1. Crea les queries que responguin les següents preguntes (una sola query per cada pregunta). Has de distingir el fet que un alumne aprova una assignatura (apareix en la relació) del fet que un alumne REALMENT aprova l'assignatura (apareix en la relació amb una puntuació igual o major a 5).

   1. Número d'estudiants de cada comarca

    ```
    SELECT district, COUNT(*) AS num_students
    FROM aprovat
    GROUP BY district;  
    ```

    ```
    district      num_students
    ------------  ------------
    Alt Penedès   43          
    Baix Penedès  39          
    Garraf        68
    ```

    ```
    SELECT district -> Seleccionem la taula de les comarques amb SELECT.
    COUNT(*) AS num_students -> Comptem el nombre total de files de la columna num_students amb COUNT. * indica que els comptem tots.
    FROM aprovat -> Indiquem la taula sobre la que volem extreure la info.
    GROUP BY district -> Agrupem els resultats per la columna district, de manera que la funció COUNT(*) calcula el nombre d'estudiants per a cada districte per separat.
    ```
    
   2. Els estudiants que tenen la nota més alta

    ```
    SELECT *
    FROM aprovat
    WHERE grade = (SELECT MAX(grade) FROM aprovat);
    ```

    ```
    code   name                 city        district      grade  pdate       subject  semester
    -----  -------------------  ----------  ------------  -----  ----------  -------  --------
    C5867  Joan Cuenca Cánovas  Els Monjos  Alt Penedès   10     2019-09-12  MATD     Q2      
    C2147  Lucía Villa Coello   Cunit       Baix Penedès  10     2019-01-20  ADSO     Q5
    ```

   3. Quants estudiants no tenen cap assignatura suspesa (nota inferior a 5)

    ```
    SELECT COUNT(DISTINCT code) AS estudiants_sense_suspeses
    FROM aprovat
    WHERE code NOT IN (
        SELECT DISTINCT code
        FROM aprovat
        WHERE grade < 5
    );
    ```

    ```
    estudiants_sense_suspeses
    -------------------------
    10
    ```

   4. Any en que hi ha més compensables (nota igual o superior a 4 i inferior a 5)

    ```
    SELECT strftime('%Y', pdate) AS year, COUNT(*) AS compensables
    FROM aprovat
    WHERE grade >= 4 AND grade < 5
    GROUP BY strftime('%Y', pdate)
    ORDER BY compensables DESC
    LIMIT 1;
    ```

    ```
    year  compensables
    ----  ------------
    2017  9
    ```

   5. L'estudiant amb més nota de cada assignatura ordenades per quadrimestre i assignatura
   6. Parelles d'estudiants diferents que tenen la mateixa nota en la mateixa assignatura

- Algunes consultes extra:

    1. Nombre d'assignatures aprovades (nota superior a 5.0) per alumne. Mostra unicament el nom i el numero d'asssignatures aprovades.

    ```
    SELECT name, COUNT(*) AS assignatures_aprovades FROM aprovat WHERE grade>=5.0 GROUP BY name;
    ```

    ```
    name                                 assignatures_aprovades
    -----------------------------------  ----------------------
    Alfonso del Ayala                    6                     
    Alicia Losada Sánchez                3                     
    Begoña Suárez                        6                     
    Belen Jover Puerta                   4                     
    Carla Real-Rivera                    2                     
    Carlos Barranco                      2                     
    Catalina Casas Jerez                 3                     
    Cristina Berrocal Ferrández          2                     
    Elisa Mármol Sanjuan                 3                     
    Esperanza Valentín                   7                     
    Eugenia del Gil                      3                     
    Gabriel Pla Madrigal                 2                     
    Gema Bustos Uriarte                  2                     
    Guillermo Sala Pizarro               2                     
    Guillermo Tomé Escudero              5                     
    Joan Cuenca Cánovas                  5                     
    Jose Miguel Mariano Mercader Arnaiz  10                    
    Juana del Álvaro                     2                     
    Lorena Barba Casado                  1                     
    Lucía Villa Coello                   7                     
    Mario Alemán Tomé                    3                     
    Martin Casanova-Palomares            5                     
    Montserrat Galan Olmedo              5                     
    Nicolás Viñas Armas                  6                     
    Nuria Costa Antón                    4                     
    Pilar Bustamante Criado              1                     
    Sergio del Zamorano                  5                     
    Silvia Lourdes Llorens Rozas         5                     
    Soledad Gil Tello                    8                     
    Vicenta Teruel Mendoza               5
    ```
1. Quines dependències funcionals (D.F.) té el problema? Usa els mateixos noms
d'atributs que els que apareixen a la taula.


3. A partir de les D.F. anteriors, crea les taules adequades per tal que
estiguin normalitzades en 3FN. Recorda de definir les claus primàries,
alternatives i foranes, les polítiques ON DELETE i ON UPDATE de les claus
foranes i si els atributs són NOT NULL.


4. Trasllada les dades de la taula original a les taules normalitzades.


5. Resol les mateixes queries de l'apartat 1) sobre les taules normalitzades.
    1. a)
    2. b)
    3. c)
    4. d)
    6. e)
    7. f)


6. La data en que s'han aprovat (inclou els compensables) les assignatures durant el 2019 es retarda 7 dies

    1. Quina seria la query per resoldre aquest problema sobre la taula no normalitzada?

    2. I en les taules normalitzades?
#