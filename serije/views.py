from django.shortcuts import render, get_object_or_404
from .models import Serije, Epizoda


# Create your views here.
def serije(request):


    queryset = Serije.objects.all().order_by('-date')

    context = {
        'queryset': queryset,
    }

    return render(request, 'serije.html', context)




def serije_detaljno(request, slug):

    obj = get_object_or_404(Serije, slug=slug)

    epiz = Epizoda.objects.filter(epizode=obj).order_by('-epizode_date')

    context = {
        'object': obj,
        'epiz': epiz
    }
    return render(request, 'serije-detaljno.html', context)
