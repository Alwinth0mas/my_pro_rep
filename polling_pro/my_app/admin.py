from django.contrib import admin
from . models import Question, Choice

# admin login credentials 
# username - alwin001
# password - alwin@2331

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
