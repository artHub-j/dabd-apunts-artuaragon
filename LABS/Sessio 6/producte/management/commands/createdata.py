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