from django.shortcuts import render
from django.http import HttpResponse




def inicio( request):
  return render(request,'index.html')

def Nosotros(request):
    return HttpResponse ('vista profesores')
def contacto (request):
    return HttpResponse('vista estudiantes')





