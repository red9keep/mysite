from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# class를 만들어 QuestionAdimin 에서 Choice Inline 로 등록, Taular~ : 입력필드를 일자로 노출
class ChoiceInline(admin.TabularInline): 
    model = Choice
    extra = 2 # Choice 2개를 생성 , 입력필드 갯수 

class QuestionAdmin(admin.ModelAdmin):
    #질문내용과, 등록일 일필드 등록
    fieldset = [
        ( None,       {'fields':['question_text']}),
        ( '등록일',   {'fields':['pub_date']})
        ] 
    inlines = [ChoiceInline] #  QuestionAdmin 에 추가로 등록
    list_display = ('question_text', 'pub_date', 'was_published_recently') # admin 에서 list로 보여짐
    list_filter = ['pub_date'] # admin 에서 필터링 추가
    search_fields = ['question_text'] # admin 에서 검색기능 추가
    
admin.site.register(Question, QuestionAdmin) # Question 모델을 admin 에서 관리할 수 있도록 등록