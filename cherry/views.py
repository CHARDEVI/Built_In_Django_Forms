from django.shortcuts import render
from cherry.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_data(request):
    IDO=TopicForm()
    d={'IDO':IDO}
    if request.method=='POST':
        SFD=TopicForm(request.POST)
        if SFD.is_valid():
            tn=SFD.cleaned_data['topic_name']
            to=Topic.objects.get_or_create(topic_name=tn)[0]
            to.save()
            return HttpResponse(f'{tn} data is inserted')

    return render(request,'insert_data.html',d)




def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            n=WFDO.cleaned_data['name']
            e=WFDO.cleaned_data['email']
            to=Topic.objects.get(topic_name=tn)
            wo=Webpage.objects.get_or_create(topic_name=to,name=n,email=e)[0]
            wo.save()
            return HttpResponse(f'{tn} data is inserted')
    return render(request,'insert_webpage.html',d)





def insert_access(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            a=AFDO.cleaned_data['author']
            d=AFDO.cleaned_data['date']
            wo=Webpage.objects.get(name=n)
            ao=AccessRecord.objects.get_or_create(name=wo,author=a,date=d)[0]
            ao.save()
            return HttpResponse(f'{n} data is inserted')
    return render(request,'insert_access.html',d)