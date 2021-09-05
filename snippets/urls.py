from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name="snippet_list"),
    path('snippet/<int:snippet_id>/', views.SnippetDetails.as_view(),name="snippet_details"),

]
format_suffix_patterns(urlpatterns)
