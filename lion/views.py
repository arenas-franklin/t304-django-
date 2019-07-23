from django.shortcuts import render

# Create your views here.
def pagina_inicial(request):
    context ={"nome": "franklin","cachorros": ["mel", "tobias", "madona", "radija"]}
    return render(request, 'index.html',context)
