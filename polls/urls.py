from django.urls import path
from.import views

app_name = 'polls'  # app 이름을 먼저 정의
urlpatterns = [
    # URL pattern for /polls/
    path('', views.IndexView.as_view(), name='index'),
    # URL pattern for /polls/<int:question_id>/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # URL pattern for /polls/<int:question_id>/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # URL pattern for /polls/<int:question_id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]