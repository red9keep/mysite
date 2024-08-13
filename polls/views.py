from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# from django.template import loader

from.models import Question, Choice
# Create your views here.
def index(request):
    #1
    # return HttpResponse ("Hello, world. Djang tutorial.")

    #2
    #order_by('-pub_date')[:5] 로 5개만 가져오고, (기본)오름차순으로 정렬 -넣으면 내림차순으로 
    # latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    # output = ', '.join([q.question_text for q in latest_question_list]) 
    # return HttpResponse(output)

    #3 템플릿 로드
    # latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    #4 
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    context = {'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context) 

def detail(request, question_id):
    #1
    #변수를 문자열과 함께 출력할때 %를 사용 '%s'는 문자열,'%f'실수, '%d'정수
    # return HttpResponse("질문에  %s 를 응답하였습니다." % question_id) 

    #2
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("페이지가 존재하지 않습니다.")
    # return render(request, 'polls/detail.html', {'question': question})
    
    #3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def vote(request, question_id):
    # return HttpResponse("투표한 결과는 %s 입니다.." % question_id)
    
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "선택하신 질문이 존재하지 않습니다.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    response = "질문에 최종 응답한 결과 %s 입니다."
    return HttpResponse(response % question_id)
