from django.urls import path
from.import views

app_name = 'polls'  # This app's name is the module name.
urlpatterns = [
    # URL pattern for /polls/
    path('', views.index, name='index'),
    # URL pattern for /polls/<int:question_id>/
    path('<int:question_id>/', views.detail, name='detail'),
    # URL pattern for /polls/<int:question_id>/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # URL pattern for /polls/<int:question_id>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]