from django.urls import path
from NKO import views

urlpatterns = [
    path("library/", views.LibraryAllApiView.as_view()),
    path("librarycategory/", views.LibraryCategoryAllApiView.as_view()),
    path("libraryfavorites/", views.libraryfavoultes),
    path("librarywitsfavourite/", views.Library_wits_favourite),

]
