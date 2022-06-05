from django.urls import path, re_path, include, register_converter
from . import views, converters

# extra_patterns = [
#     path("reports/", credit_views.report),
#     path("reports/<int:num>/", credit_views.report),
#     path('charges/', credit_views.charge)
# ]

register_converter(converters.FourDigitalYearConverter, "yyyy")


app_name = 'poll'
urlpatterns = [
#     path('credit/', include(extra_patterns)),
#     re_path(r'^(?P<year>[0-9]{4})/$', views.index),
#     re_path(r'articles/(?:page-(?P<page_number>\d+)/)?$', views.index)
    # re_path(r'^articles/(?P<name>\w+)/$')
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path("credit/<yyyy:year>", views.index)

    path('<int:question_id>/result', views.result, name='result'),
    path('<int:question_id>/vote', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/result', views.result, name='result'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]