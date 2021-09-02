from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list, name="snippet_list"),
    path('snippet/<int:snippet_id>/', views.snippet_details, name="snippet_details"),

]
