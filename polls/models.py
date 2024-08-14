import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    # admin에 등록할 변수값
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    # 데이터 등록일 함수
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # 필드 정렬을 발행일로 변경
    was_published_recently.admin_order_field = 'pub_date'
    # 아이콘 모습으로 옵션
    was_published_recently.boolean = True
    # 타이틀을 변경으로 옵션
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # admin에 등록할 변수값 CharField: 최대길이정의가 필요, TextField: 다중행적용
    choice_text = models.CharField(max_length=200)
    # 정수값만 받는 입력 필드
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
