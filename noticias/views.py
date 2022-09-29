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
    noticias_1 = dados['articles'][1]
    noticias_2 = dados['articles'][2]
    noticias_3 = dados['articles'][3]
    noticias_4 = dados['articles'][4]
    noticias_5 = dados['articles'][5]

    return render(request, 'noticias/index.html', {'noticias': noticias, 'noticias_1': noticias_1,
                                                   'noticias_2': noticias_2, 'noticias_3': noticias_3,
                                                   'noticias_4': noticias_4, 'noticias_5': noticias_5})
