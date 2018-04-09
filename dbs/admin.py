from django.contrib import admin
from .models import AbstractTools,Square,Diamond,Circle,Parabola, Workflow, Steps
# Register your models here.

#admin.site.register(AbstractTools)
admin.site.register(Workflow)
admin.site.register(Circle)
admin.site.register(Diamond)
admin.site.register(Square)
admin.site.register(Parabola)
admin.site.register(Steps)