from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *

# Create your views here.
def loginAccount(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(notes)
        else:
            return render(request, "authentication/login.html", {"denied":True})

    return render(request, "authentication/login.html", {"denied":False})

def logoutAccount(request):
    logout(request)
    return redirect(loginAccount)

@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard.html")

@login_required(login_url="login")
def notes(request):
    
    if "deleteButton" in request.POST:
        deleteNote = request.POST["noteId"]
        
        if len(deleteNote) > 0:
            note.objects.filter(noteId=deleteNote).delete()
            

    elif request.method == "POST":
        newNoteName = request.POST["noteName"]
        newNoteText = request.POST["noteText"]
        newNoteId = request.POST["noteId"]
        newNoteAuthor = request.POST["noteAuthor"]

        if(len(newNoteId) > 0):
            #newNote = note(noteId=newNoteId, )
            note.objects.filter(noteId=newNoteId).update(noteTitle=newNoteName, noteText=newNoteText, noteModifiedDate=timezone.now())
        else:
            newNote = note(noteAuthor_id=newNoteAuthor, noteTitle=newNoteName, noteText=newNoteText)

            newNote.save()

    noteData = note.objects.all()
    name = {"noteData": noteData}
    return render(request, "notes.html", name)