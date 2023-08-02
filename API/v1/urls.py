from django.urls import path

from API.v1.safo_eshiklar.auth.views import RegisView, LoginView
from API.v1.safo_eshiklar.basket.views import BasketView
from API.v1.safo_eshiklar.contact.views import CntView
from API.v1.safo_eshiklar.ctg.views import CtgView
from API.v1.safo_eshiklar.like_dislike.like_dislike import Dislike_LikeView

urlpatterns = [
    path("regis/", RegisView.as_view()),
    path("login/", LoginView.as_view()),

    path("cnt/", CntView.as_view()),
    path('cnt/<int:_id>/', CntView.as_view()),

    path("ctg/", CtgView.as_view()),
    path('ctg/<int:_id>/', CtgView.as_view()),

    path('basket/', BasketView.as_view()),

    path('like/', Dislike_LikeView.as_view()),
]