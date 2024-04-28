# <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/bd0f85c2-26ab-488e-98e3-cce94a095788" alt="Logo_UPC svg" width="40" height="40"> dabd-apunts-artuaragon | Sessió 6 | DL 22 ABRIL 2024 | 

# Sessió 6. Exemple d'ORM: Django + BD relacional

Crearem un servidor web amb una eina ORM (Object Relational Mapping). Ens ajudarem del framework Django, un framework escrit en Python que permet desenvolupar servidors web amb rapidesa i seguretat.

## PART 1. Posar en funcionament un servidor web Django

1) Instal·leu-vos el framework Django. Usarem la versió 3.1 que ja només treballa sobre Python v3. Podeu seguir els passos de Installing an official release with pip, que bàsicament consisteix crear un entorn virtual amb Python 3 i instal·lar Django a dins seu amb la comanda pip:

    ```
    $ virtualenv --python=python3 django
    $ cd django
    $ source bin/activate
    $ pip install Django
    ```
2) Podem comprovar si Django està instal·lat i la seva versió amb la comanda:

    ```
    $ python -m django --version
    ```
3) Creem un projecte Django anomenat, per exemple, dabd:

    ```
    $ django-admin startproject dabd
    ```
4) Entreu dins de la carpeta dabd. Podem arrancar un servidor web que escolti en el port 8080 (és un servidor de desenvolupament, no l'useu mai en servidors en producció):

    ```
    $ python manage.py runserver 8080
    ```
    Ara amb el navegador podreu accedir a la URL http://127.0.0.1:8080/ i rebrem un missatge de benvinguda.

5) Creem una aplicació dins del projecte de dabd per gestionar productes, l'anomenarem producte:

    ```
    $ python manage.py startapp producte
    ```
6) Creem una base de dades amb les taules inicials perquè Django pugui treballar, com les que guardaran els usuaris i grups d'usuaris. Per defecte crearà una base de dades sqlite3 anomenada db.sqlite3, a no ser que modifiquem la configuració del nostre projecte dins del fitxer dabd/settings.py per usar altres SGBD com MySQL, PostgreSQL o Oracle. Desprès creem un usuari administrador. Finalment tornem a arrancar el servidor:

    ```
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver 8080
    ```
    Podem provar d'accedir a la part administrativa del servidor web disponible a la URL http://127.0.0.1:8080/admin. De moment només podem gestionar usuaris i grups. La part administrativa també se l'anomena backoffice o backend.

## PART 2. Crear nous models

7) Creem dos models per guardar plantilles de productes i variants de producte dins del fitxer producte/models.py. Les plantilles de productes (ProductTemplate) permeten guardar els productes genèrics, per exemple "Bicicleta BMX" i les variants (ProductVariant) són les variants del producte genèric o plantilla, per exemple "Vermella", "Blava", "Platejada". Fixa't que cada model es defineix com una classe de Python i es convertirà en una taula de la base de dades. Els atributs de cada classe de Python es convertiran en els camps de de la taula. Django ofereix diferents tipus de camps (CharField, IntegerField, DecimalField, DateField, ForeignKey, ...). El mètode de la classe anomenat __str__ s'utilitza per definir com es mostren els registres d'una taula, per exemple els tres productes anteriors es veurien llistats com [VERME] Bicicleta BMX, [BLAVA] Bicicleta BMX, [PLATA] Bicicleta BMX.

    ```python
    from django.db import models


    class ProductTemplate(models.Model):
        name = models.CharField(max_length=200)
        list_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
        cost_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
        salable = models.BooleanField()
        ...

        def __str__(self):
            return self.name


    class ProductVariant(models.Model):
        template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
        code = models.CharField(max_length=200)
        ...

        def __str__(self):
            return '[' + self.code + '] ' + self.template.name
    ```
8) Hem d'incloure l'aplicació producte dins del projecte dabd. Afegirem la línia amb l'aplicació de productes dins del fitxer de configuració dabd/settings.py:
    ```python
    INSTALLED_APPS = [
        'producte.apps.ProducteConfig',
        ...
    ```
9) Indiquem que hem fet canvis al nostre model per tal que es calculin els canvis a fer a la base de dades mitjançant una migració (crea un fitxer amb les instruccions SQL dels canvis). Desprès podem veure les sentències SQL que s'executarien i, si ens convencen, apliquem la migració (executa les instruccions SQL anteriors a la base de dades):
    ```shell
    $ python manage.py makemigrations producte
    $ python manage.py sqlmigrate producte 0001
    $ python manage.py migrate
    ```
10)   Indiquem que els models creats són gestionables des de la part administrativa. Editem el fitxer producte/admin.py perquè contingui:
```python
from django.contrib import admin
from .models import ProductTemplate, ProductVariant
admin.site.register(ProductTemplate)
admin.site.register(ProductVariant)
```

Si reengeguem de nou el servidor i entrem a la part administrativa, a més dels usuaris i grups podrem administrar plantilles de productes i productes.

## Exercicis:
- Canvia la configuració del fitxer dabd/settings.py per usar un altre SGBD com per exemple el PostgreSQL del servidor ubiwan.epsevg.upc.edu que escolta pel port 5432 (https://docs.djangoproject.com/en/3.1/ref/settings/#databases), genera les taules a la nova base de dades (python manage.py migrate) i torna a crear un usuari administrador (python manage.py createsuperuser). Per exemple, per PostgreSQL et caldrà instal·lar prèviament la llibreria de Python que permet connectar-se a una base de dades PostgreSQL (pip install psycopg2 o pip install psycopg2-binary).

- Afegeix una nova entitat ProductCategory que siguin les categories (o famílies) de productes que permeti guardar el nom de la categoria, la categoria pare (per tal d'implementar una relació jeràrquica, una categoria pot contenir vàries subcategories i així successivament). I entre les plantilles de productes i categories hi ha una relació de molts a molts (many2many), doncs una plantilla de productes pot pertànyer a vàries categories i viceversa (afegiu aquesta relació només en un lloc, per exemple un camp ManyToManyField a ProductCategory que apunti a ProductTemplate; Django ja crea automàticament la taula intermèdia que implementa la relació de molts a molts). Els camps categoria pare i plantilles de producte haurien de poder ser buits o nulls; mireu a la documentació de Django com podeu usar les opcions blank i null, doncs per defecte els camps no poden ser buits.

<p align="center">
  <img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/ae6b9ec5-65c8-4be5-9588-87b9bd8adcdb">
</p>


## PART 3. Llegir/crear/modificar/eliminar registres des de codi Python

Arranca la shell de python amb accés a Django i executa una a una aquestes instruccions per veure que passa. Comprovaràs que pots fer SQL queries amb simples instruccions Python. Prèviament has d'haver afegit un parell de plantilles de producte des de la part d'administració de Django, afegeix per exemple "Bicicleta BMX" i "Bicicleta MTB".

```shell 
python manage.py shell
```

```shell
>>> from producte.models import ProductTemplate, ProductVariant, ProductCategory

>>> # Obtenim tots els registres/objectes
>>> ProductTemplate.objects.all()
>>> templates = ProductTemplate.objects.all()
>>> for t in templates:
>>>   print(t.name, t.list_price, t.cost_price)

>>> # Obtenim uns quants registres/objectes
>>> templates = ProductTemplate.objects.filter(name='Bicicleta BMX')
>>> templates[0]
>>> templates[0].list_price

>>> # Obtenim un únic registre/objecte i el modifiquem (també es pot usar update())
>>> t = ProductTemplate.objects.get(name='Bicicleta BMX')
>>> t
>>> t.list_price
>>> t.list_price = 1350
>>> t.save()
>>> t.list_price

>>> # Creem un registre/objecte nou (també es pot usar create() i desprès l'eliminem
>>> t = ProductTemplate(name='Monopatí', list_price=200, cost_price=120, salable=True)
>>> ProductTemplate.objects.all()
>>> t.save()
>>> ProductTemplate.objects.all()
>>> t = ProductTemplate.objects.get(name='Monopatí')
>>> t.delete()
>>> ProductTemplate.objects.all()
```

## PART 4. Creació d'un frontend: Vistes i URLs
Ara crearem una simple pàgina web en la part pública del nostre web, el que s'anomena frontoffice o frontend.
Dins del fitxer producte/views.py. es defineixen les vistes que volem oferir. Per exemple copia el següent codi que ofereix dues vistes molt simples, una amb el llistat de productes que podem oferir (només aquells que siguin vendibles) i l'altra amb els detalls d'un producte:

```python
from django.http import HttpResponse
from .models import ProductTemplate, ProductVariant

def index(request):
    product_list = ProductVariant.objects.all()
    output = '<br>'.join([
    	'<a href="/producte/%s">[%s] %s</a>' % (p.id, p.code, p.template.name)
    	for p in product_list if p.template.salable])
    return HttpResponse(output)


def producte(request, producte_id):
    p = ProductVariant.objects.get(id=producte_id)
    output = 'Codi: %s<br>Nom: %s<br>Preu venda: %s' % (p.code, p.template.name, p.template.list_price)
    return HttpResponse(output)
```

Desprès defineix dins del fitxer producte/urls.py les rutes URL que enllaçaran amb les dues vistes que acabem de definir. Segurament el fitxer no existeixi i l'hagis de crear.

```python
from django.urls import path
from . import views

urlpatterns = [
    # ex: /producte/
    path('', views.index, name='index'),
    # ex: /producte/5/
    path('<int:producte_id>/', views.producte, name='producte'),
]
```

I finalment defineix en el fitxer dabd/urls.py la ruta que apunta a la nostra subaplicació de productes, afegint-la a la que ja hi ha que permet fer l'administració des del backend:

```python
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('producte/', include('producte.urls')),
    path('admin/', admin.site.urls),
]
```
Reengega el servidor i prova d'accedir a http://127.0.0.1:8080/producte/ i a clicar en alguns dels links que apareixen, sempre que abans hagis afegit variants de producte que siguin vendibles, doncs només es mostren els vendibles.


## PART 5. Creació de dades fictícies amb les llibreries Faker i Random
Podem usar la llibreria random per generar números aleatoris i la llibreria faker per crear dades inventades similars a les de la realitat (noms, adreces, ciutats, telèfons, emails, etc.). Haurem d'instal·lar la llibreria faker en el nostre entorn virtual de Python (pip install faker).

Podem crear els nostres propis scripts dins del nostre projecte Django per executar-los amb python manage.py. Per exempler aquest script ens permetria crear plantilles, productes i categories fictícies per als nostres models. Aquest script deixarem en una carpeta anomenada commands dins de la carpeta management dins de la nostra app producte. O sigui estarà situat en aquesta ruta <b> django/dabd/producte/management/commands/createdata.py </b>

```python
import random
import faker.providers
from faker import Faker

from django.core.management.base import BaseCommand
from producte.models import ProductTemplate, ProductVariant, ProductCategory

CATEGORIES = [
  'patinet',
  'bici',
  'moto',
  'cotxe',
  'camio',
  'autocar',
  'excavadora',
  'tractor',
  'caravana',
  'autocaravana'
  ]

NUM_PRODUCT_TEMPLATES = 100
NUM_PRODUCT_PRODUCTS = 200
NUM_PRODUCT_CATEGORIES = len(CATEGORIES)

class Provider(faker.providers.BaseProvider):
  def producte_categoria(self):
    return self.random_element(CATEGORIES)

class Command(BaseCommand):
  help = "Create example data"

  def handle(self, *args, **kwargs):
    fake = Faker()
    fake.add_provider(Provider)

    # Product templates creation
    for i in range(NUM_PRODUCT_TEMPLATES):
      name = ' '.join(fake.words(nb=2, part_of_speech='noun'))
      cost_price = random.randint(0, 99999)/100
      # list_price = [cost_price, cost_price*2]
      list_price = round(cost_price * (1+random.random()),2)
      salable = random.choice([False, True])
      print(name, cost_price, list_price, salable)
      ProductTemplate.objects.create(
        name=name,
        list_price=list_price,
        cost_price=cost_price,
        salable=salable)
    templates = ProductTemplate.objects.all()
    print(templates.count(), "product templates added.")

    # Product variantss creation
    for i in range(NUM_PRODUCT_PRODUCTS):
      code = fake.unique.bothify('PROD-??-###', letters='ABCDE')
      if i<NUM_PRODUCT_TEMPLATES:
        # Així ens assegurem que cada plantilla tingui almenys un producte
        template = templates[i]
      else:
        template = random.choice(templates)
      print(code, template)
      ProductVariant.objects.create(
        code = code,
        template = template
      )
    products = ProductVariant.objects.all()
    print(products.count(), "products added.")

    # Product categories creation
    for i in range(NUM_PRODUCT_CATEGORIES):
      name = fake.unique.producte_categoria()
      pare = None
      # Només la 2a meitat de categories tindran categoria pare
      if (i>NUM_PRODUCT_CATEGORIES/2):
        pare = random.choice(ProductCategory.objects.all())
      # Escollim entre 1 i 5 templates que tindrà cada categoria
      ptemplates = random.choices(templates, k=random.randint(1,5))
      print(name, pare, ptemplates)
      c = ProductCategory.objects.create(
        name = name,
        pare = pare,
      )
      # Afegim les plantilles associades a cada categoria (camp rel és una camp ManyToManyField)
      for t in ptemplates:
        c.rel.add(t)
      c.save()
    categories = ProductCategory.objects.all()
    print(categories.count(), "categories added.")
```

I executant-lo ens crearà les dades fictícies per als nostres models:

```shell
python manage.py createdata 
```

## Solució:

|Carpeta|productes/|
|:-:|:-:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/tree/main/LABS/Sessio%206/producte)|

|Arxius|settings.py|models.py|
|:-:|:-:|:-:|
|Link|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%206/settings.py)|[<img src="https://github.com/artHub-j/dabd-apunts-artuaragon/assets/92806890/771e2532-56fb-4ee6-ae5c-5795eb752acd" width="40" height="40">](https://github.com/artHub-j/dabd-apunts-artuaragon/blob/main/LABS/Sessio%206/producte/models.py)|
