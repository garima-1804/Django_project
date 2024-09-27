
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="index.html"),
    path('about',views.about,name="about.html"),
    path('insert',views.insertdata,name="insertdata"),
    path('update/<id>',views.updateData,name="updatedata"),
    path('delete/<id>',views.deleteData,name="deletedata"),
]
