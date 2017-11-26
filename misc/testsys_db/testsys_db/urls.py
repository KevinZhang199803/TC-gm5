from django.conf.urls import url
from django.contrib import admin

from testbank.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/(?P<quiz_id>[0-9]+)/problems/$', TakeQuizView),
    url(r'^sentence/$', QuizHandinView),
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quiz', QuizListViewForExaminee, base_name='quiz')
urlpatterns += router.urls
