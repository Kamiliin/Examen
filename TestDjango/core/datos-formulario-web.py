import urllib.request

datos = b'Receta Python No. 9-7: Enviar Datos a una Pagina Web'

solicitud = urllib.request.Request('https://form.blogspot.com/form_contacto', data=datos, method='POST')

# Inicio solicitud:
formulario = urllib.request.urlopen(solicitud)

print(formulario.status)
print(formulario.reason)