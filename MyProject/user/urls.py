from django.urls import path

from . import views

urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('alumni/',views.alumni),
    path('contact/',views.contact),
    path('cources/',views.cources),
    path('faculty/',views.faculty),
    path('feedback/',views.feedback),
    path('gallery/',views.gallery),
    path('infra/',views.infra),
    path('recruiters/',views.recruiters),
    path('principal/',views.principal),
    path('portfolio/',views.portfolio),

]