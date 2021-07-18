from django.contrib import admin
from .models import Comment,Author

admin.site.register(Comment)
admin.site.register(Author)