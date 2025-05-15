from django.contrib import admin
from . models import Question, Choice

# admin login credentials 
# username - alwinth007
# password - alwin@3785

admin.site.register(Question)
admin.site.register(Choice)

# Register your models here.
