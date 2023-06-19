from django.contrib import admin

# Register your models here.
from .models import Courses, Order, Lesson, Comment

admin.site.register(Courses)
admin.site.register(Order)
admin.site.register(Lesson)
admin.site.register(Comment)
