from datetime import datetime
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
    Response = "<H1>Momento actual: {0} </H1>".format(datetime.now().strftime("%A %d/%m%Y %H:%M:%S"))
    return HttpResponse("<H1>El servidor responde que: %s </H1>" % Response)
