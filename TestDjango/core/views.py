
from django.shortcuts import render, HttpResponse
from django.template import Template, context
from django.template import loader

# Create your views here.
#def home (request):
#     return render(request, 'core/home.html')

def compra(request):
     return render(request, "core/compra.html")

def inicio (request):
     return render(request, 'core/inicio.html')

def bandanas (request):
     return render(request, 'core/bandanas.html')

def identificadores (request):
     return render(request, 'core/identificadores.html')     

def accesorios (request):
     return render(request, 'core/accesorios.html')

def correas (request):
     return render(request, 'core/correas.html')

def registro (request):
     return render(request, 'core/registro.html')
     
def conocenosMejor (request):
     return render(request, 'core/conocenosMejor.html')

#def cabesera(request):
    #doc_externo=open("C:/Users/jack/Desktop/mal/TestDjango/core/templates/core/home.html")     
    #cabeseraa=template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template('home.html')
    #ctx=context()
    #Documento=doc_externo.render('')
    #return HTTPResponse(Documento)