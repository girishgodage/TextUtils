# I have create this file - Girish
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    #get checkbox value
    removepunc= request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')

    purpose = ""
    # Check checkbox value
    if removepunc == "on":
        # define punctuation
        punctuations = '''!()-[]{};:'"\,|<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # Analyze the text
        purpose += '|Remove Punctuation'
        djtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        # Analyze the text
        purpose += '|Change to Uppercase'
        djtext = analyzed
    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r" :
                analyzed = analyzed + char
        # Analyze the text
        purpose += '|Remove new line'
        djtext = analyzed
    if extraspaceremove == "on":
        analyzed = ""
        for index , char in enumerate(djtext)   :
            if not(djtext[index] == " " and djtext[index + 1] == " "):
               analyzed = analyzed + char
        # Analyze the text
        purpose += '|Remove Extra Space'
    if ( removepunc != "on" and newlineremove != "on" and extraspaceremove != "on" and  fullcaps != "on"):
        return HttpResponse("Please select amy operation and try again")
    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)







