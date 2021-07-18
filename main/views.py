from .models import Author, Comment
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json

def home(request):
    comments = Comment.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        message = json.load(request)['message']

        comment = Comment.objects.create(content=message, author=Author.objects.get(user=request.user))
        comment.save()
        
        data = {
            "author": comment.author.fullname.title(),
            "image":comment.author.image.url,
            "content": comment.content,
            #"date": f"{comment.date:%m, %d, %Y}"
            "date": f"{comment.date.strftime('%b')},"+ f"{comment.date: %d, %Y}"
        }
        print(data)
        return JsonResponse(data, status=200)

    context = {
        "comments":comments,
    }
    return render(request, "home.html", context)