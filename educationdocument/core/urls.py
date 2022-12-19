from django.urls import path
from .views import *

urlpatterns=[
    path('home/',FormView.as_view(),name="home"),
    path('detail/',DetailView.as_view(),name="detail"),
    path('export_pdf/user/<int:pk>/',GeneratePdf.as_view(),name="export_pdf"),
]