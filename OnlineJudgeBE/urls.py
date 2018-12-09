"""OnlineJudgeBE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from problems.views import ProblemsListViewSet
from contests.views import ContestsListViewSet
from submissions.views import SubmissionsListViewSet, SubmissionTokenListViewSet
from user_operation.views import UserCollectListViewSet, UserAcceptedProblemListViewSet,UserChallengingProblemListViewSet
from users.views import UserRegViewSet,UserViewSet,UserProfileListViewSet

router = DefaultRouter()
router.register(r'problems', ProblemsListViewSet, base_name="problems")
router.register(r'contests', ContestsListViewSet, base_name="contests")
router.register(r'register', UserRegViewSet, base_name="register")
router.register(r'users', UserViewSet, base_name="users")
router.register(r'userprofile', UserProfileListViewSet, base_name="userprofile")
router.register(
    r'submissions',
    SubmissionsListViewSet,
    base_name="submissions")
router.register(
    r'submissiontoken',
    SubmissionTokenListViewSet,
    base_name="submissiontoken")
router.register(
    r'usercollect',
    UserCollectListViewSet,
    base_name="usercollect")
router.register(
    r'useracceptedproblems',
    UserAcceptedProblemListViewSet,
    base_name="useracceptedproblems")
router.register(
    r'userchallengingproblems',
    UserChallengingProblemListViewSet,
    base_name="userchallengingproblems")

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # jwt的认证接口
    url(r'^api/login/', obtain_jwt_token),
    url(r'^api/', include(router.urls)),
    url(r'docs/', include_docs_urls(title="OnlineJudgeBE")),

]
