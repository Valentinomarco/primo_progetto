from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("<h1>Ciao a tutti! Benvenuti nella homepage!</h1>")
# Create your views here.

#L2
def menu(request):
    return HttpResponse("<ol><li>Prima opzione</li><li>Seconda opzione</li><li>Terza opzione</li></ol>")
    #L3
def chisiamo(request):
    return render(request, "chi_siamo.html")
    #L4
def variabili(request):
    context= { 'var1': '10','var2': 'ciao', 'var3' : '123 hello world'}
    return render(request, "variabili.html",context)
    #L5
def index(request):
    return render(request, "index.html")
