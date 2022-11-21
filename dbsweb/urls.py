"""dbsweb URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain, name = "showMain"),

    path('insertTable1', views.insertionTable1, name = "insertionTable1"),
    path('insertTable2', views.insertionTable2, name = "insertionTable2"),
    path('insertTable3', views.insertionTable3, name = "insertionTable3"),
    path('insertTable4', views.insertionTable4, name = "insertionTable4"),
    path('insertTable5', views.insertionTable5, name = "insertionTable5"),
    path('insertTable6', views.insertionTable6, name = "insertionTable6"),
    path('insertTable7', views.insertionTable7, name = "insertionTable7"),
    path('insertTable8', views.insertionTable8, name = "insertionTable8"),
    path('insertTable9', views.insertionTable9, name = "insertionTable9"),

    path('delete/<int:id>', views.deleteRecordTable1,name ="deleteRecordTable1"),  
    path('delete/<str:id>', views.deleteRecordTable2,name ="deleteRecordTable2"),
    path('deletet3/<str:id>', views.deleteRecordTable3,name ="deleteRecordTable3"),
    path('deletet4/<int:id>', views.deleteRecordTable4,name ="deleteRecordTable4"),  
    path('deletet5/<str:id>', views.deleteRecordTable5,name ="deleteRecordTable5"),
    path('deletet6/<int:id>', views.deleteRecordTable6,name ="deleteRecordTable6"), 
    path('deletet7/<int:id>', views.deleteRecordTable7,name ="deleteRecordTable7"),
    path('deletet8/<int:id>', views.deleteRecordTable8,name ="deleteRecordTable8"), 
    path('deletet9/<int:id>', views.deleteRecordTable9,name ="deleteRecordTable9"),   

    path('editTable1/<int:id>', views.editTable1,name ="editTable1"),
    path('updateTable1/<int:id>', views.updateTable1,name ="updateTable1"),   
    path('editTable2/<str:id>', views.editTable2,name ="editTable2"),
    path('updateTable2/<str:id>', views.updateTable2,name ="updateTable2"),  
    path('editTable3/<str:id>', views.editTable3,name ="editTable3"),
    path('updateTable3/<str:id>', views.updateTable3,name ="updateTable3"), 
    path('editTable4/<int:id>', views.editTable4,name ="editTable4"),
    path('updateTable4/<int:id>', views.updateTable4,name ="updateTable4"),   
    path('editTable5/<str:id>', views.editTable5,name ="editTable5"),
    path('updateTable5/<str:id>', views.updateTable5,name ="updateTable5"),
    path('editTable6/<int:id>', views.editTable6,name ="editTable6"),
    path('updateTable6/<int:id>', views.updateTable6,name ="updateTable6"),
    path('editTable7/<int:id>', views.editTable7,name ="editTable7"),
    path('updateTable7/<int:id>', views.updateTable7,name ="updateTable7"), 
    path('editTable8/<int:id>', views.editTable8,name ="editTable8"),
    path('updateTable8/<int:id>', views.updateTable8,name ="updateTable8"),  
    path('editTable9/<int:id>', views.editTable9,name ="editTable9"),
    path('updateTable9/<int:id>', views.updateTable9,name ="updateTable9"),                           
]
