from django.contrib import admin
from .models import Question, Choice

# Register your models here.

admin.site.register(Question) # Question 모델을 admin 에서 관리할 수 있도록 등록
admin.site.register(Choice) 