from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    assert False   # uncomment to dump local variables into debugger
    return render(request, 'hours_ahead.html', {'hour_offset': offset,
                                                'next_time': dt})

