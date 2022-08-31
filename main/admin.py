from django.contrib import admin

from .models import *
# signin your models here.
admin.site.register(teachers)
admin.site.register(Answer)
admin.site.register(questions)
admin.site.register(users)
