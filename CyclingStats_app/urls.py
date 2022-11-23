"""CyclingStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from CyclingStats_app import views

urlpatterns = [
    path("", views.index, name='index'),
    path('InsertEvent', views.InsertEvent, name="InsertEvent"),
    path('ShowEvent', views.ShowEvent, name="ShowEvent"),
    # path('EditEvent/<int:id>',views.EditEvent, name="EditEvent"),
    # path('Update/<int:id>', views.updateEvent, name="updateEvent"),

    path('EditEvent/<int:id>', views.EditEvent, name="EditEvent"),
    path('updateEvent/<int:id>', views.updateEvent, name="updateEvent"),
    path('DelEvent/<int:id>', views.DelEvent, name="DelEvent"),
    path('ShowCyclist', views.ShowCyclist, name="ShowCyclist"),
    path('InsertCyclist', views.InsertCyclist, name="InsertCyclist"),
    path('EditCyclist/<int:id>', views.EditCyclist, name="EditCyclist"),
    path('updateCyclist/<int:id>', views.updateCyclist, name="updateCyclist"),
    path('DelCyclist/<int:id>', views.DelCyclist, name="DelCyclist"),
    path('SortEvent', views.SortEvent, name="SortEvent"),
    path('SortCyclist', views.SortCyclist, name="SortCyclist"),
    path('RunQueryEvent', views.RunQueryEvent, name="RunQueryEvent"),
    path('ProcessCustomQuery/', views.ProcessCustomQuery, name="ProcessCustomQuery"),
    path('InputCustomQuery/', views.InputCustomQuery, name="InputCustomQuery"),
    path('RunQueryCyclist', views.RunQueryCyclist, name="RunQueryCyclist"),
    path('ProcessCustomQueryForCyclist/', views.ProcessCustomQueryForCyclist, name="ProcessCustomQueryForCyclist"),
    path('InputCustomQueryForCyclist/', views.InputCustomQueryForCyclist, name="InputCustomQueryForCyclist"),

]
