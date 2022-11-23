from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from CyclingStats_app.forms import Eventforms
from CyclingStats_app.forms import Cyclistforms
from CyclingStats_app.models import Event, Cyclist


def index(request):
    template = loader.get_template('inx.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def InsertEvent(request):
    if request.method == "POST":
        if request.POST.get('event_id') and request.POST.get('event_name') and request.POST.get(
                'event_location') and request.POST.get('no_of_audience') and request.POST.get(
                'participation') and request.POST.get('winner_name'):
            saverecord = Event()
            saverecord.event_id = request.POST.get('event_id')
            saverecord.event_name = request.POST.get('event_name')
            saverecord.event_location = request.POST.get('event_location')
            saverecord.no_of_audience = request.POST.get('no_of_audience')
            saverecord.participation = request.POST.get('participation')
            saverecord.winner_name = request.POST.get('winner_name')
            saverecord.save()
            messages.success(request, 'Event ' + saverecord.event_name + ' is saved successfully..!')
            return render(request, 'InsertEvent.html')
    else:
        return render(request, 'InsertEvent.html')


def ShowEvent(request):
    showall = Event.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'ShowEvent.html', context)


def EditEvent(request, id):
    editEventObj = Event.objects.get(event_id=id)
    return render(request, 'EditEvent.html', {"Event": editEventObj})


# def updateEvent(request, id, form=None):
#     UpdateEvent=Event.objects.get(id=id)
#     form-Eventforms(request.POST, instance=UpdateEvent)
#     if form.is_valid():
#         form.save()
#         messages.success(request,"Record update successfully..!")
#         return render(request,'EditEvent.html',{"Event":UpdateEvent})

def updateEvent(request, id):
    UpdateEvent = Event.objects.get(event_id=id)
    form = Eventforms(request.POST, instance=UpdateEvent)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updates succesfully!!')
        return render(request, 'EditEvent.html', {"Event": UpdateEvent})


def DelEvent(request, id):
    delEvent = Event.objects.get(event_id=id)
    delEvent.delete()
    showdata = Event.objects.all()
    return render(request, "inx.html", {"Event": showdata})


def ShowCyclist(request):
    showall = Cyclist.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'ShowCyclist.html', context)


def InsertCyclist(request):
    if request.method == "POST":
        if request.POST.get('cyclist_id') and request.POST.get('name') and request.POST.get(
                'contest') and request.POST.get('rank') and request.POST.get('email') and request.POST.get(
                'event_id') and request.POST.get('country') and request.POST.get('age'):
            saverecord = Cyclist()
            saverecord.cyclist_id = request.POST.get('cyclist_id')
            saverecord.name = request.POST.get('name')
            saverecord.contest = request.POST.get('contest')
            saverecord.rank = request.POST.get('rank')
            saverecord.email = request.POST.get('email')
            saverecord.event_id = request.POST.get('event_id')
            saverecord.country = request.POST.get('country')
            saverecord.age = request.POST.get('age')
            saverecord.save()
            messages.success(request, 'Cyclist ' + saverecord.name + ' is saved successfully..!')
            return render(request, 'InsertCyclist.html')
    else:
        return render(request, 'InsertCyclist.html')


def EditCyclist(request, id):
    editCyclistObj = Cyclist.objects.get(cyclist_id=id)
    return render(request, 'EditCyclist.html', {"Cyclist": editCyclistObj})


def updateCyclist(request, id):
    UpdateCyclist = Cyclist.objects.get(cyclist_id=id)
    form = Cyclistforms(request.POST, instance=UpdateCyclist)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated successfully..!')
        return render(request, 'EditCyclist.html', {"Cyclist": UpdateCyclist})


def DelCyclist(request, id):
    delEvent = Cyclist.objects.get(cyclist_id=id)
    delEvent.delete()
    showdata = Cyclist.objects.all()
    return render(request, "inx.html", {"Cyclist": showdata})


def SortEvent(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = Event.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'SortEvent.html', context)
    else:
        return render(request, 'SortEvent.html')


def SortCyclist(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = Cyclist.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'SortCyclist.html', context)
    else:
        return render(request, 'SortCyclist.html')


def InputCustomQuery(request):
    return render(request, 'Query.html', {})


def RunQueryEvent(request):
    raw_query = "select \"Event\".\"event_id\",\"Event\".\"event_name\" from \"Event\" "

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'Query.html', {'data': alldata})


def ProcessCustomQuery(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    print(alldata)

    return render(request, 'RunQueryEvent.html', {'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})

def InputCustomQueryForCyclist(request):
    return render(request, 'QueryCyclist.html', {})

def RunQueryCyclist(request):
    raw_query = "select \"Event\".\"event_id\",\"Event\".\"event_name\" from \"Event\"   "

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'QueryCyclist.html', {'data': alldata})

def ProcessCustomQueryForCyclist(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    print(alldata)

    return render(request, 'RunQueryCyclist.html', {'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})