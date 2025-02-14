from django.shortcuts import render
import datetime

# Create your views here.

def template_view(request):

    dt = datetime.datetime.now()

    name = 'Rohan'
    id = 107
    address = 'Nashik'
    street = 'altamount'

    my_dict = {'date':dt,'name':name,'id':id,'address':address,'street':street}

    return render(request,'testapp/results.html',my_dict)
