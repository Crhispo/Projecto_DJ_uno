from datetime import datetime
from django.template import Template, Context
from django.http import HttpResponse


# Request: Sirve para realizar peticiones
# HttpResponse: Sirve para dar respuestas en el protocolo HTTP

# Vista de bienvenida


def welcome(request):  # Argumento de tipo "Request"
    return HttpResponse("Welcome to this Django course")

# Vista de bienvenida en roj0


def welcomeRed(request):  # Argumento de tipo "Request"
    return HttpResponse("<p style='color: red'>Welcome to this Django course</p>")

# Vista de caterias por edad


def ageCategory(request, age):  # Argumento de tipo "Request", parametro edad
    if age >= 18:
        if age >= 60:
            category = "Tercera edad"
        else:
            category = "Adultez"
    else:
        if age < 10:
            category = "Infancia"
        else:
            category = "Adolecencia"
    resultado = category
    return HttpResponse("<H1>Categoria de la edad: %s </H1>" % resultado)

# Vista de caterias por edad


def getCurrentdate(request):  # Argumento de tipo "Request"
    Response = "<H1>Momento actual: {0} </H1>".format(
        datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse("<H1>El servidor responde que: %s </H1>" % Response)


def contentHTML(request, name, age):  # Argumento de tipo "Request"
    content = """
    <html>
    <head>
    <title>
    Contenido HTML
    </title>
    </head>
    <body>
    <p>Nombre: %s / Edad: %s </p>
    </body>
    </html>
    """ % (name, age)
    return HttpResponse(content)


def firtstemplate(request):  # Argumento de tipo "Request"
    # Abrimos el documento que contiene la plantilla
    temexterna = open(
        '../Projecto_DJ_uno/Projecto_DJ_uno/plantillas/firtsTem.html')
    # Se carga el documento en una variable tipo "template":
    template = Template(temexterna.read())
    # Cerrar el documento externo que hemos abierto
    temexterna.close()
    # Crear el contexto:
    context = Context()
    # Renderizar el documento
    document = template.render(context)
    return HttpResponse(document)


def templateParameters(request):  # Argumento de tipo "Request"
    nombre = "Crhistian"
    fechaActual = datetime.now().strftime("%A %d/%m/%Y %H:%M:%S")
    lenguajes = ["python", "Golang", "JavaScript", "C+", "Ruby"]
    # Abrimos el documento que contiene la plantilla
    temexterna = open(
        '../Projecto_DJ_uno/Projecto_DJ_uno/plantillas/temParameters.html')
    # Se carga el documento en una variable tipo "template":
    template = Template(temexterna.read())
    # Cerrar el documento externo que hemos abierto
    temexterna.close()
    # Crear el contexto:
    context = Context(
        {"nombre": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
    # Renderizar el documento
    document = template.render(context)
    return HttpResponse(document)
