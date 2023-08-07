from django.shortcuts import render, redirect
 
 
def chatPage(request):
    return render(request, "chat/chatPage.html")