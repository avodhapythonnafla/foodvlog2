from django.contrib import admin
from . models import *
from . models import logn
from . models import regs


# Register your models here.
admin.site.register(logn)
admin.site.register(regs)
