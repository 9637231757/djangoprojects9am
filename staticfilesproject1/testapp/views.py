from django.shortcuts import render
import datetime

# Create your views here.
def date_time_view(request):

    date = datetime.datetime.now()
    h = int(date.strftime('%H'))

    if h<12:
        msg='Hello Guests !! Good Morning'
    elif h<16:
        msg='Hello Guests !! Good Afternoon'
    elif h<21:
        msg='Hello Guests !! Good Evening'
    else:
        msg='Hello Guests !! Good Night'

    my_dict = {'msg':msg,'date':date}

    return render(request,"testapp/results.html",my_dict)
