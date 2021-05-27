#i have created this one - Sachi shome
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    #getting the text and analyzing the text
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    uppercase=request.POST.get('uppercase', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')

    if (removepunc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
        paras={'purpose':'Removed punctuation','analyzed_text':analyzed}
        djtext=analyzed

    if(uppercase=='on'):
        analyzed=""
        for i in djtext:
            analyzed=analyzed+i.upper()
        paras = {'purpose': 'Upper cased letter', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=='on'):
        analyzed=""
        for i in djtext:
            if i != "\n" and i!='\r':
                analyzed=analyzed+i
        paras = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        paras = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}

    if (removepunc!='on' and uppercase!="on" and newlineremover!="on" and extraspaceremover != "on"):
        return HttpResponse("Error 404 \n please select an option")



    return render(request, 'analyze.html', paras)