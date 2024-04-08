# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Activitat 1 Apunts aprovats.db | ABRIL 2024 |

|      |                                                                                                                            aprovats.db                                                                                                                            |                                                                                                                            registre_parelles.db                                                                                                                            |                                                                                                                            linies_factura.db                                                                                                                            |
| ---- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Link | [<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/Exemples%20Activitat%201/Activitat1-apunts-aprovats.md) | [<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/Exemples%20Activitat%201/Activitat1-apunts-registre_parelles.md) | [<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/Exemples%20Activitat%201/Activitat1-apunts-linies_factura.md) |

#

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

## Taula Aprovats Inicial:

```
code   name                                 city                district      grade  pdate       subject  semester
-----  -----------------------------------  ------------------  ------------  -----  ----------  -------  --------
C1813  Gabriel Pla Madrigal                 Sant Pere de Ribes  Garraf        4.3    2018-01-07  ARCO     Q4      
C4864  Alicia Losada Sánchez                Sant Pere de Ribes  Garraf        6.4    2018-06-21  PRO1     Q2      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  8.3    2016-11-01  INTE     Q5      
C4922  Gema Bustos Uriarte                  Canyelles           Garraf        5.7    2019-01-11  ESIN     Q3      
C9137  Cristina Berrocal Ferrández          Sant Sadurní        Alt Penedès   4.5    2018-05-06  XACO     Q4      
C8106  Carla Real-Rivera                    La Granada          Alt Penedès   9.3    2019-02-25  PACO     Q5      
C3556  Guillermo Tomé Escudero              La Granada          Alt Penedès   9.3    2017-09-30  ESC2     Q3      
C7096  Mario Alemán Tomé                    Cunit               Baix Penedès  7.6    2016-04-05  INDI     Q4      
C3066  Sergio del Zamorano                  Sant Pere de Ribes  Garraf        8.9    2018-11-05  ESTA     Q3      
C8990  Vicenta Teruel Mendoza               Els Monjos          Alt Penedès   9.5    2016-07-09  INEP     Q3      
C3556  Guillermo Tomé Escudero              La Granada          Alt Penedès   6.2    2019-05-18  FISI     Q1      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   5.3    2019-10-29  INTE     Q5      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        7.3    2018-06-28  INTE     Q5      
C6627  Lorena Barba Casado                  Vilafranca          Alt Penedès   8.3    2016-09-18  PRO1     Q2      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  4      2016-10-01  FOPR     Q1      
C7997  Nicolás Viñas Armas                  El Vendrell         Baix Penedès  6.7    2017-08-03  FOPR     Q1      
C2256  Guillermo Sala Pizarro               Calafell            Baix Penedès  6.1    2017-08-18  LOAL     Q2      
C3556  Guillermo Tomé Escudero              La Granada          Alt Penedès   4.9    2017-04-24  SIOP     Q3      
C7017  Eugenia del Gil                      Canyelles           Garraf        9      2017-04-11  ESC1     Q2      
C2553  Nuria Costa Antón                    Vilafranca          Alt Penedès   6.4    2019-08-05  ADSO     Q5      
C9872  Soledad Gil Tello                    Sitges              Garraf        7.8    2019-06-18  INCO     Q1      
C5741  Begoña Suárez                        Vilafranca          Alt Penedès   8.2    2018-03-23  ESTA     Q3      
C0643  Martin Casanova-Palomares            Cunit               Baix Penedès  4.4    2017-03-31  EMPR     Q4      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  4.1    2016-06-10  PTIN     Q6      
C3556  Guillermo Tomé Escudero              La Granada          Alt Penedès   6.1    2019-04-05  PTIN     Q6      
C8918  Montserrat Galan Olmedo              Sitges              Garraf        6.7    2019-11-17  ARCO     Q4      
C7096  Mario Alemán Tomé                    Cunit               Baix Penedès  5.6    2019-06-29  ESIN     Q3      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        8.8    2019-03-28  MATD     Q2      
C9872  Soledad Gil Tello                    Sitges              Garraf        7.5    2016-04-01  ADSO     Q5      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   6.1    2017-05-08  FISI     Q1      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  8.9    2019-01-10  SEAX     Q6      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        5.5    2017-02-04  PACO     Q5      
C8990  Vicenta Teruel Mendoza               Els Monjos          Alt Penedès   8.5    2019-07-07  ESIN     Q3      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   6      2018-10-30  INEP     Q3      
C8106  Carla Real-Rivera                    La Granada          Alt Penedès   6.7    2018-03-24  ARCO     Q4      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  5.3    2020-02-28  FUIN     Q6      
C7997  Nicolás Viñas Armas                  El Vendrell         Baix Penedès  7.8    2018-07-29  SODX     Q5      
C8918  Montserrat Galan Olmedo              Sitges              Garraf        4.4    2020-02-16  INEP     Q3      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  9.4    2017-10-17  PROP     Q5      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  7.2    2016-09-04  EMPR     Q4      
C9872  Soledad Gil Tello                    Sitges              Garraf        6.1    2019-08-21  INTE     Q5      
C5867  Joan Cuenca Cánovas                  Els Monjos          Alt Penedès   6.9    2018-03-27  PROP     Q5      
C5069  Silvia Lourdes Llorens Rozas         Cubelles            Garraf        5.1    2018-12-29  SODX     Q5      
C5069  Silvia Lourdes Llorens Rozas         Cubelles            Garraf        7.6    2016-04-03  FISI     Q1      
C5867  Joan Cuenca Cánovas                  Els Monjos          Alt Penedès   7.4    2017-07-05  AMEP     Q4      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  8      2017-03-25  DABD     Q6      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  6.8    2018-04-07  XAMU     Q6      
C7017  Eugenia del Gil                      Canyelles           Garraf        7.8    2016-04-19  SODX     Q5      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  9      2017-02-21  FUIN     Q6      
C0602  Elisa Mármol Sanjuan                 Calafell            Baix Penedès  4.3    2019-05-08  SODX     Q5      
C7997  Nicolás Viñas Armas                  El Vendrell         Baix Penedès  7.1    2016-07-23  EMPR     Q4      
C3066  Sergio del Zamorano                  Sant Pere de Ribes  Garraf        6      2016-06-13  DABD     Q6      
C5741  Begoña Suárez                        Vilafranca          Alt Penedès   4.5    2017-06-15  FUIN     Q6      
C8208  Carlos Barranco                      Sitges              Garraf        7.6    2019-06-30  PTIN     Q6      
C4864  Alicia Losada Sánchez                Sant Pere de Ribes  Garraf        6.4    2018-01-11  EMPR     Q4      
C4922  Gema Bustos Uriarte                  Canyelles           Garraf        4.9    2019-11-08  PRO1     Q2      
C6894  Catalina Casas Jerez                 Sant Pere de Ribes  Garraf        5.1    2016-08-18  SEAX     Q6      
C5069  Silvia Lourdes Llorens Rozas         Cubelles            Garraf        7.3    2020-02-20  PRO1     Q2      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        5.7    2018-09-13  LOAL     Q2      
C7017  Eugenia del Gil                      Canyelles           Garraf        6.2    2018-10-04  SIOP     Q3      
C3556  Guillermo Tomé Escudero              La Granada          Alt Penedès   7.4    2018-12-29  LOAL     Q2      
C3066  Sergio del Zamorano                  Sant Pere de Ribes  Garraf        6.8    2018-09-21  AMEP     Q4      
C9872  Soledad Gil Tello                    Sitges              Garraf        7.5    2019-10-12  MATD     Q2      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   4      2020-01-31  FOMA     Q1      
C0643  Martin Casanova-Palomares            Cunit               Baix Penedès  8.8    2017-04-18  FOMA     Q1      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        9.8    2019-02-19  ESIN     Q3      
C6894  Catalina Casas Jerez                 Sant Pere de Ribes  Garraf        6.6    2018-06-10  SODX     Q5      
C8990  Vicenta Teruel Mendoza               Els Monjos          Alt Penedès   8.4    2016-03-19  INCO     Q1      
C8179  Belen Jover Puerta                   Sitges              Garraf        5.3    2019-06-24  XAMU     Q6      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  5.3    2018-10-02  ESTA     Q3      
C2413  Juana del Álvaro                     Cubelles            Garraf        9.1    2019-06-03  ESTA     Q3      
C4864  Alicia Losada Sánchez                Sant Pere de Ribes  Garraf        4.4    2018-04-09  ARCO     Q4      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        5.5    2018-07-22  ESTA     Q3      
C8990  Vicenta Teruel Mendoza               Els Monjos          Alt Penedès   7.5    2018-08-20  SODX     Q5      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   7.1    2019-08-12  FUIN     Q6      
C7997  Nicolás Viñas Armas                  El Vendrell         Baix Penedès  4.8    2019-09-14  SEAX     Q6      
C8179  Belen Jover Puerta                   Sitges              Garraf        7.6    2016-11-18  PACO     Q5      
C8918  Montserrat Galan Olmedo              Sitges              Garraf        6.9    2017-05-19  ESIN     Q3      
C9872  Soledad Gil Tello                    Sitges              Garraf        9.1    2019-03-02  INDI     Q4      
C8918  Montserrat Galan Olmedo              Sitges              Garraf        8.9    2016-10-24  FOPR     Q1      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        8.6    2017-11-21  INEP     Q3      
C2413  Juana del Álvaro                     Cubelles            Garraf        9.1    2019-01-03  INTE     Q5      
C0643  Martin Casanova-Palomares            Cunit               Baix Penedès  6.3    2020-01-15  PROP     Q5      
C2413  Juana del Álvaro                     Cubelles            Garraf        4.5    2019-03-23  FOPR     Q1      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   7.3    2019-09-15  ARCO     Q4      
C8106  Carla Real-Rivera                    La Granada          Alt Penedès   4.6    2018-08-16  PROP     Q5      
C5867  Joan Cuenca Cánovas                  Els Monjos          Alt Penedès   10     2019-09-12  MATD     Q2      
C2256  Guillermo Sala Pizarro               Calafell            Baix Penedès  9.6    2019-09-17  FOMA     Q1      
C1813  Gabriel Pla Madrigal                 Sant Pere de Ribes  Garraf        6      2019-05-12  SIOP     Q3      
C0602  Elisa Mármol Sanjuan                 Calafell            Baix Penedès  6.6    2019-07-20  SIOP     Q3      
C2413  Juana del Álvaro                     Cubelles            Garraf        4.4    2016-08-17  AMEP     Q4      
C0643  Martin Casanova-Palomares            Cunit               Baix Penedès  9.8    2016-10-06  SODX     Q5      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  10     2019-01-20  ADSO     Q5      
C5741  Begoña Suárez                        Vilafranca          Alt Penedès   6      2018-04-23  PTIN     Q6      
C0602  Elisa Mármol Sanjuan                 Calafell            Baix Penedès  5.4    2019-03-12  LOAL     Q2      
C9872  Soledad Gil Tello                    Sitges              Garraf        6      2016-10-09  LOAL     Q2      
C5741  Begoña Suárez                        Vilafranca          Alt Penedès   5.4    2016-06-20  EMPR     Q4      
C3556  Guillermo Tomé Escudero              La Granada          Alt Penedès   5.8    2018-06-07  DABD     Q6      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   4.7    2017-07-19  ESC2     Q3      
C1813  Gabriel Pla Madrigal                 Sant Pere de Ribes  Garraf        7      2017-06-02  PRO1     Q2      
C8990  Vicenta Teruel Mendoza               Els Monjos          Alt Penedès   6.6    2020-03-01  DABD     Q6      
C5867  Joan Cuenca Cánovas                  Els Monjos          Alt Penedès   5.9    2016-07-07  ESC1     Q2      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  4.1    2017-05-04  XACO     Q4      
C4922  Gema Bustos Uriarte                  Canyelles           Garraf        8.1    2016-10-03  ARCO     Q4      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        6.5    2019-08-02  FUIN     Q6      
C8179  Belen Jover Puerta                   Sitges              Garraf        6.3    2017-04-28  SODX     Q5      
C0643  Martin Casanova-Palomares            Cunit               Baix Penedès  7.6    2019-08-04  DABD     Q6      
C2553  Nuria Costa Antón                    Vilafranca          Alt Penedès   4.3    2018-12-02  XACO     Q4      
C3543  Alfonso del Ayala                    Vilafranca          Alt Penedès   5.5    2016-06-17  ESC1     Q2      
C5069  Silvia Lourdes Llorens Rozas         Cubelles            Garraf        4.3    2017-09-09  SEAX     Q6      
C0602  Elisa Mármol Sanjuan                 Calafell            Baix Penedès  7.7    2017-10-14  FISI     Q1      
C5867  Joan Cuenca Cánovas                  Els Monjos          Alt Penedès   9.8    2019-04-23  SODX     Q5      
C9872  Soledad Gil Tello                    Sitges              Garraf        4.1    2017-06-23  XACO     Q4      
C4922  Gema Bustos Uriarte                  Canyelles           Garraf        4.1    2016-08-29  ESTA     Q3      
C5741  Begoña Suárez                        Vilafranca          Alt Penedès   5.9    2019-01-06  LOAL     Q2      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  5.6    2019-01-13  PACO     Q5      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        7.2    2019-07-19  FOPR     Q1      
C8918  Montserrat Galan Olmedo              Sitges              Garraf        8.5    2017-07-04  FISI     Q1      
C0643  Martin Casanova-Palomares            Cunit               Baix Penedès  7.3    2018-12-25  PRO1     Q2      
C2553  Nuria Costa Antón                    Vilafranca          Alt Penedès   6.8    2018-10-13  INTE     Q5      
C2553  Nuria Costa Antón                    Vilafranca          Alt Penedès   6.3    2019-02-16  ESC1     Q2      
C4221  Esperanza Valentín                   Cunit               Baix Penedès  8.2    2016-06-06  ARCO     Q4      
C8918  Montserrat Galan Olmedo              Sitges              Garraf        6.9    2019-09-17  XACO     Q4      
C9137  Cristina Berrocal Ferrández          Sant Sadurní        Alt Penedès   6.7    2017-12-19  INDI     Q4      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  9.8    2019-06-25  FOMA     Q1      
C5069  Silvia Lourdes Llorens Rozas         Cubelles            Garraf        8.1    2019-08-01  FOMA     Q1      
C5741  Begoña Suárez                        Vilafranca          Alt Penedès   5.9    2017-12-06  XAMU     Q6      
C7997  Nicolás Viñas Armas                  El Vendrell         Baix Penedès  9.8    2020-02-18  XAMU     Q6      
C2553  Nuria Costa Antón                    Vilafranca          Alt Penedès   7.9    2018-02-23  INDI     Q4      
C4864  Alicia Losada Sánchez                Sant Pere de Ribes  Garraf        9.9    2018-05-30  ESC2     Q3      
C9872  Soledad Gil Tello                    Sitges              Garraf        9.2    2019-03-11  ESC1     Q2      
C2413  Juana del Álvaro                     Cubelles            Garraf        4.5    2017-05-10  PROP     Q5      
C9137  Cristina Berrocal Ferrández          Sant Sadurní        Alt Penedès   8.2    2017-12-03  MATD     Q2      
C3904  Jose Miguel Mariano Mercader Arnaiz  Vilanova            Garraf        9.5    2018-11-24  PTIN     Q6      
C2147  Lucía Villa Coello                   Cunit               Baix Penedès  8.8    2020-01-08  AMEP     Q4      
C7997  Nicolás Viñas Armas                  El Vendrell         Baix Penedès  8.9    2017-05-17  XACO     Q4      
C3066  Sergio del Zamorano                  Sant Pere de Ribes  Garraf        9.2    2018-03-27  ARCO     Q4      
C1813  Gabriel Pla Madrigal                 Sant Pere de Ribes  Garraf        4.2    2019-03-01  SODX     Q5      
C5741  Begoña Suárez                        Vilafranca          Alt Penedès   7.9    2019-01-31  PRO1     Q2      
C5069  Silvia Lourdes Llorens Rozas         Cubelles            Garraf        5.4    2018-12-02  INCO     Q1      
C3066  Sergio del Zamorano                  Sant Pere de Ribes  Garraf        5      2018-06-02  PRO1     Q2      
C1503  Pilar Bustamante Criado              Sitges              Garraf        8.5    2019-04-20  INEP     Q3      
C6894  Catalina Casas Jerez                 Sant Pere de Ribes  Garraf        6.1    2017-05-21  ADSO     Q5      
C9872  Soledad Gil Tello                    Sitges              Garraf        5      2019-04-23  AMEP     Q4      
C7017  Eugenia del Gil                      Canyelles           Garraf        4.9    2016-03-20  DABD     Q6      
C8179  Belen Jover Puerta                   Sitges              Garraf        9.3    2016-08-06  PTIN     Q6      
C8179  Belen Jover Puerta                   Sitges              Garraf        4.3    2017-03-31  ADSO     Q5      
C8208  Carlos Barranco                      Sitges              Garraf        7.7    2017-10-06  ESTA     Q3      
C7997  Nicolás Viñas Armas                  El Vendrell         Baix Penedès  9.6    2019-03-11  PRO1     Q2      
C7096  Mario Alemán Tomé                    Cunit               Baix Penedès  7      2018-09-03  INTE     Q5
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

    ```
    WITH RankedStudents AS (
    SELECT
        code,
        name,
        city,
        district,
        grade,
        pdate,
        subject,
        semester,
        ROW_NUMBER() OVER (PARTITION BY subject, semester ORDER BY grade DESC) AS rank
    FROM
        aprovat
    )
    SELECT
    code,
    name,
    grade,
    subject, 
    semester
    FROM
    RankedStudents
    WHERE           
    rank = 1      
    ORDER BY
    semester, subject;
    ```
    ```
    code   name                                 grade  subject  semester
    -----  -----------------------------------  -----  -------  --------
    C8918  Montserrat Galan Olmedo              8.5    FISI     Q1      
    C2147  Lucía Villa Coello                   9.8    FOMA     Q1      
    C8918  Montserrat Galan Olmedo              8.9    FOPR     Q1      
    C8990  Vicenta Teruel Mendoza               8.4    INCO     Q1      
    C9872  Soledad Gil Tello                    9.2    ESC1     Q2      
    C3556  Guillermo Tomé Escudero              7.4    LOAL     Q2      
    C5867  Joan Cuenca Cánovas                  10     MATD     Q2      
    C7997  Nicolás Viñas Armas                  9.6    PRO1     Q2      
    C4864  Alicia Losada Sánchez                9.9    ESC2     Q3      
    C3904  Jose Miguel Mariano Mercader Arnaiz  9.8    ESIN     Q3      
    C2413  Juana del Álvaro                     9.1    ESTA     Q3      
    C8990  Vicenta Teruel Mendoza               9.5    INEP     Q3      
    C0602  Elisa Mármol Sanjuan                 6.6    SIOP     Q3      
    C2147  Lucía Villa Coello                   8.8    AMEP     Q4      
    C3066  Sergio del Zamorano                  9.2    ARCO     Q4      
    C2147  Lucía Villa Coello                   7.2    EMPR     Q4      
    C9872  Soledad Gil Tello                    9.1    INDI     Q4      
    C7997  Nicolás Viñas Armas                  8.9    XACO     Q4      
    C2147  Lucía Villa Coello                   10     ADSO     Q5      
    C2413  Juana del Álvaro                     9.1    INTE     Q5      
    C8106  Carla Real-Rivera                    9.3    PACO     Q5      
    C4221  Esperanza Valentín                   9.4    PROP     Q5      
    C0643  Martin Casanova-Palomares            9.8    SODX     Q5      
    C2147  Lucía Villa Coello                   8      DABD     Q6      
    C2147  Lucía Villa Coello                   9      FUIN     Q6      
    C3904  Jose Miguel Mariano Mercader Arnaiz  9.5    PTIN     Q6      
    C4221  Esperanza Valentín                   8.9    SEAX     Q6      
    C7997  Nicolás Viñas Armas                  9.8    XAMU     Q6
    ```

   6. Parelles d'estudiants diferents que tenen la mateixa nota en la mateixa assignatura

    ```
    SELECT DISTINCT a1.name AS student1, a2.name AS student2, a1.grade, a1.subject
    FROM aprovat a1
    JOIN aprovat a2 ON a1.grade = a2.grade AND a1.subject = a2.subject AND a1.code <> a2.code
    ORDER BY a1.grade, a1.subject, a1.name, a2.name;
    ```
    ```
    student1                      student2                      grade  subject
    ----------------------------  ----------------------------  -----  -------
    Esperanza Valentín            Soledad Gil Tello             4.1    XACO   
    Soledad Gil Tello             Esperanza Valentín            4.1    XACO   
    Carla Real-Rivera             Montserrat Galan Olmedo       6.7    ARCO   
    Montserrat Galan Olmedo       Carla Real-Rivera             6.7    ARCO   
    Martin Casanova-Palomares     Silvia Lourdes Llorens Rozas  7.3    PRO1   
    Silvia Lourdes Llorens Rozas  Martin Casanova-Palomares     7.3    PRO1   
    Eugenia del Gil               Nicolás Viñas Armas           7.8    SODX   
    Nicolás Viñas Armas           Eugenia del Gil               7.8    SODX   
    Joan Cuenca Cánovas           Martin Casanova-Palomares     9.8    SODX   
    Martin Casanova-Palomares     Joan Cuenca Cánovas           9.8    SODX
    ```

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

    1. Número d'estudiants de cada ciutat

    ```
    SELECT city, COUNT(*) AS num_estudiants FROM aprovat GROUP BY city;
    ```
    ```
    city                num_estudiants
    ------------------  --------------
    Calafell            6             
    Canyelles           8             
    Cubelles            11            
    Cunit               26            
    El Vendrell         7             
    Els Monjos          10            
    La Granada          9             
    Sant Pere de Ribes  16            
    Sant Sadurní        3             
    Sitges              23            
    Vilafranca          21            
    Vilanova            10
    ```
    2. L'estudiant amb nota mitja més alta
   
    ```
    SELECT code, name, AVG(grade) AS avg_grade FROM aprovat
    GROUP BY code, name
    ORDER BY avg_grade DESC
    LIMIT 1;
    ```
    ```
    code   name                     avg_grade
    -----  -----------------------  ---------
    C1503  Pilar Bustamante Criado  8.5
    ```
    3. Nombre d'aprovats (inclou els compensables) per cada any
   
    ```
    SELECT strftime('%Y', pdate) AS year, COUNT(*) AS num_approved
    FROM aprovat
    WHERE grade >= 5
    GROUP BY strftime('%Y', pdate);
    ```
    ```
    year  num_approved
    ----  ------------
    2016  22          
    2017  23          
    2018  30          
    2019  43          
    2020  6
    ```
    4. L'assignatura amb més aprovats (inclous els compensables)
   
    ```
    SELECT subject, COUNT(*) AS num_approved
    FROM aprovat
    WHERE grade >= 5         
    GROUP BY subject
    ORDER BY num_approved DESC
    LIMIT 1;
    ```
    ```
    subject  num_approved
    -------  ------------
    SODX     8
    ```
    5. Quins estudiants tenen dos o més compensables (nota igual o superior a 4 i inferior a 5) en la fase final (de Q3 a Q6)
   
    ```
    SELECT code, name
    FROM (
        SELECT code, name, COUNT(*) AS num_compensables
        FROM aprovat
        WHERE grade >= 4 AND grade < 5 AND semester IN ('Q3', 'Q4', 'Q5', 'Q6') 
        GROUP BY code, name
    ) AS student_compensables
    WHERE num_compensables >= 2;
    ```
    ```
    code   name                
    -----  --------------------
    C1813  Gabriel Pla Madrigal
    C2413  Juana del Álvaro
    ```
    6. Parelles d'estudiants diferents que viuen a la mateixa ciutat

    ```
    SELECT DISTINCT a.code AS student1_code, a.name AS student1_name, b.code AS student2_code, b.name AS student2_name, a.city
    FROM aprovat a
    JOIN aprovat b ON a.city = b.city AND a.code < b.code;
    ```
    ```
    student1_code  student1_name              student2_code  student2_name                 city              
    -------------  -------------------------  -------------  ----------------------------  ------------------
    C1813          Gabriel Pla Madrigal       C3066          Sergio del Zamorano           Sant Pere de Ribes
    C1813          Gabriel Pla Madrigal       C4864          Alicia Losada Sánchez         Sant Pere de Ribes
    C1813          Gabriel Pla Madrigal       C6894          Catalina Casas Jerez          Sant Pere de Ribes
    C4864          Alicia Losada Sánchez      C6894          Catalina Casas Jerez          Sant Pere de Ribes
    C4221          Esperanza Valentín         C7096          Mario Alemán Tomé             Cunit             
    C4922          Gema Bustos Uriarte        C7017          Eugenia del Gil               Canyelles         
    C3556          Guillermo Tomé Escudero    C8106          Carla Real-Rivera             La Granada        
    C3066          Sergio del Zamorano        C4864          Alicia Losada Sánchez         Sant Pere de Ribes
    C3066          Sergio del Zamorano        C6894          Catalina Casas Jerez          Sant Pere de Ribes
    C3543          Alfonso del Ayala          C5741          Begoña Suárez                 Vilafranca        
    C3543          Alfonso del Ayala          C6627          Lorena Barba Casado           Vilafranca        
    C2147          Lucía Villa Coello         C4221          Esperanza Valentín            Cunit             
    C2147          Lucía Villa Coello         C7096          Mario Alemán Tomé             Cunit             
    C2553          Nuria Costa Antón          C3543          Alfonso del Ayala             Vilafranca        
    C2553          Nuria Costa Antón          C5741          Begoña Suárez                 Vilafranca        
    C2553          Nuria Costa Antón          C6627          Lorena Barba Casado           Vilafranca        
    C5741          Begoña Suárez              C6627          Lorena Barba Casado           Vilafranca        
    C0643          Martin Casanova-Palomares  C2147          Lucía Villa Coello            Cunit             
    C0643          Martin Casanova-Palomares  C4221          Esperanza Valentín            Cunit             
    C0643          Martin Casanova-Palomares  C7096          Mario Alemán Tomé             Cunit             
    C8918          Montserrat Galan Olmedo    C9872          Soledad Gil Tello             Sitges            
    C5867          Joan Cuenca Cánovas        C8990          Vicenta Teruel Mendoza        Els Monjos        
    C0602          Elisa Mármol Sanjuan       C2256          Guillermo Sala Pizarro        Calafell          
    C8208          Carlos Barranco            C8918          Montserrat Galan Olmedo       Sitges            
    C8208          Carlos Barranco            C9872          Soledad Gil Tello             Sitges            
    C8179          Belen Jover Puerta         C8208          Carlos Barranco               Sitges            
    C8179          Belen Jover Puerta         C8918          Montserrat Galan Olmedo       Sitges            
    C8179          Belen Jover Puerta         C9872          Soledad Gil Tello             Sitges            
    C2413          Juana del Álvaro           C5069          Silvia Lourdes Llorens Rozas  Cubelles          
    C1503          Pilar Bustamante Criado    C8179          Belen Jover Puerta            Sitges            
    C1503          Pilar Bustamante Criado    C8208          Carlos Barranco               Sitges            
    C1503          Pilar Bustamante Criado    C8918          Montserrat Galan Olmedo       Sitges            
    C1503          Pilar Bustamante Criado    C9872          Soledad Gil Tello             Sitges
    ```
    7. La comarca amb més número d'estudiants
   
    ```
    SELECT district, COUNT(*) AS num_students
    FROM aprovat
    GROUP BY district
    ORDER BY num_students DESC
    LIMIT 1;
    ```
    ```
    district  num_students
    --------  ------------
    Garraf    68
    ```
    8. Els dos estudiants amb nota mitja més alta
   
    ```
    SELECT code, name, AVG(grade) AS avg_grade FROM aprovat
    GROUP BY code, name
    ORDER BY avg_grade DESC
    LIMIT 2;
    ```
    ```
    code   name                     avg_grade
    -----  -----------------------  ---------
    C1503  Pilar Bustamante Criado  8.5      
    C6627  Lorena Barba Casado      8.3
    ```
    9.  Any en que hi han més aprovats (inclou els compensables)
   
    ```
    SELECT strftime('%Y', pdate) AS year,
        COUNT(*) AS total_approved
    FROM aprovat
    WHERE grade >= 4
    GROUP BY strftime('%Y', pdate)
    ORDER BY total_approved DESC
    LIMIT 1;
    ```
    ```
    year  total_approved
    ----  --------------
    2019  48
    ```
    10. Les dues assignatures amb més aprovats (inclou els compensables)
   
    ```
    SELECT subject, COUNT(*) AS num_passes
    FROM aprovat
    WHERE grade >= 4 -- Considering grades equal to or above 4 as passes
    GROUP BY subject
    ORDER BY num_passes DESC
    LIMIT 2;
    ```
    ```
    subject  num_passes
    -------  ----------
    SODX     10        
    PRO1     9
    ```
    11. Quins estudiants tenen almenys 3 assignatures aprovades en un mateix quadrimestre
   
    ```
    SELECT code, name
    FROM (
        SELECT code, name, semester, COUNT(DISTINCT subject) AS approved_subjects
        FROM aprovat
        WHERE grade >= 5
        GROUP BY code, name, semester
    ) AS subquery
    WHERE approved_subjects >= 3;
    ```
    ```
    code   name                               
    -----  -----------------------------------
    C3904  Jose Miguel Mariano Mercader Arnaiz
    C4221  Esperanza Valentín                 
    C5069  Silvia Lourdes Llorens Rozas       
    C9872  Soledad Gil Tello
    ```
    12. Parelles d'assignatures diferents del quadrimestre Q4 aprovades pel mateix estudiant
   
    ```
    SELECT DISTINCT a1.code,
                    a1.name,
                    a1.subject AS subject1,
                    a2.subject AS subject2,
                    a1.semester
    FROM aprovat a1
    JOIN aprovat a2 ON a1.code = a2.code
    WHERE a1.semester = 'Q4'
    AND a2.semester = 'Q4'
    AND a1.subject < a2.subject;
    ```
    ```
    code   name                         subject1  subject2  semester
    -----  ---------------------------  --------  --------  --------
    C8918  Montserrat Galan Olmedo      ARCO      XACO      Q4      
    C7997  Nicolás Viñas Armas          EMPR      XACO      Q4      
    C3066  Sergio del Zamorano          AMEP      ARCO      Q4      
    C4864  Alicia Losada Sánchez        ARCO      EMPR      Q4      
    C9872  Soledad Gil Tello            INDI      XACO      Q4      
    C4221  Esperanza Valentín           ARCO      XACO      Q4      
    C9137  Cristina Berrocal Ferrández  INDI      XACO      Q4      
    C2553  Nuria Costa Antón            INDI      XACO      Q4      
    C2147  Lucía Villa Coello           AMEP      EMPR      Q4      
    C9872  Soledad Gil Tello            AMEP      INDI      Q4      
    C9872  Soledad Gil Tello            AMEP      XACO      Q4
    ```
# 

1. Quines dependències funcionals (D.F.) té el problema? Usa els mateixos noms
d'atributs que els que apareixen a la taula.

```
                code → name, city, district, grade, pdate, subject, semester
name, city, district → code, grade, pdate, subject, semester
   subject, semester → code, name, city, district, grade, pdate
```
O
```
Student code determines student name, city, and county:
{ code } -> { name, city, district }

Subject code determines subject semester:
{ subject } -> { semester }

Student code and subject code determine grade, passing date, and semester:
{ code, subject } -> { grade, pdate, semester }

Passing date and subject code determine grade:
{ pdate, subject } -> { grade }

Passing date and student code determine grade:
{ pdate, code } -> { grade }

Passing date and subject code determine semester:
{ pdate, subject } -> { semester }
```

3. A partir de les D.F. anteriors, crea les taules adequades per tal que
estiguin normalitzades en 3FN. Recorda de definir les claus primàries,
alternatives i foranes, les polítiques ON DELETE i ON UPDATE de les claus
foranes i si els atributs són NOT NULL.

```
CREATE TABLE Student (
  code CHAR(4) PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  city VARCHAR(50) NOT NULL,
  district VARCHAR(50) NOT NULL
);
```
```
CREATE TABLE Subject (
  subject CHAR(4) PRIMARY KEY,
  semester CHAR(2) NOT NULL
);
```
```
CREATE TABLE Grade (
  code CHAR(4) NOT NULL,
  subject CHAR(4) NOT NULL,
  grade DECIMAL(3, 1) NOT NULL,
  pdate DATE NOT NULL,
  PRIMARY KEY (code, subject),
  FOREIGN KEY (code) REFERENCES Student(code) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (subject) REFERENCES Subject(subject) ON DELETE CASCADE ON UPDATE CASCADE
);
```

4. Trasllada les dades de la taula original a les taules normalitzades.

```
INSERT INTO Student (code, name, city, district)
SELECT DISTINCT code, name, city, district
FROM aprovat;
```
```
INSERT INTO Subject (subject, semester)
SELECT DISTINCT subject, semester
FROM aprovat;
```
```
INSERT INTO Grade (code, subject, grade, pdate)
SELECT code, subject, grade, pdate
FROM aprovat;
```

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