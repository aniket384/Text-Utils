# I have created this file - Aniket
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html');

def about (request):
    return  HttpResponse("About");

def analyze (request):

# Get Text
    djtext= request.POST.get('text', 'default')

# Checkbox Value
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')

# Check Which Checkbox in "ON":-

# Remove Puncuations:
    if removepunc == "on":
        puncations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in puncations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


#Change To Upper Case:
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.capitalize()
        params = {'purpose': 'Chaged to Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

# New Line Remover:
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

# Extra Space Remover:
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


#Defualt Case:
    else:
        return HttpResponse("Error")

