from django.shortcuts import render
import requests
from django.http import JsonResponse


# Create your views here.
def index(request):
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=fd9ba178c352444dba4bcbda028f4352')

    response = requests.get(url)
    dados = response.json()
    noticias = dados['articles'][0]

    return render(request, 'noticias/index.html', {'noticias': noticias})
