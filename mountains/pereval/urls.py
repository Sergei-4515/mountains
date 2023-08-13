from django.urls import path

from .views import SubmitData, SubmitDetailsData

urlpatterns = [
    path('api/v1/submitData/', SubmitData.as_view(), name='submitData'),
    path('api/v1/submitData/<int:pk>/', SubmitDetailsData.as_view(), name='SubmitDetailsData'),
]