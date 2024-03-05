"""
URL configuration for interest_group_activation_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

import advertiser.views
import bidder.views
import interest_group.views

router = routers.DefaultRouter()

router.register(r'advertisers', advertiser.views.AdvertiserViewSet, basename='advertiser')
router.register(r'bidders', bidder.views.BidderViewSet, basename='bidder')
router.register(r'interest_groups', interest_group.views.InterestGroupViewSet, basename='interest_group')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    # path('login/', user.views.LoginView.as_view(), name='login'),
    # path('logout/', user.views.LogoutView.as_view(), name='logout'),
]
