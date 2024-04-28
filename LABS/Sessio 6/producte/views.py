from django.shortcuts import render

# Create your views here.

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