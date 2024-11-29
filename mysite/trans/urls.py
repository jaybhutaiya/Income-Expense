from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('transaction/',views.transaction.as_view(),name='transaction'),
    path('list/',views.list.as_view(),name='list')
]