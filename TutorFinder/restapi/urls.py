from django.urls import path, include
from . import views
app_name = "Restapi"

urlpatterns = [
	path('api/tutor/page/<int:page>/size/<int:size>', views.getTutors,name='get'),
    path('api/tutor/', views.addTutors,name='post'),
    path('api/tutor/<int:id>', views.deleteTutors,name='delete'),
    path('api/updatetutor/<int:id>', views.updateTutors,name='put'),
]