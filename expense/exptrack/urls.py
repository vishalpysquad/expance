from django.urls import path

from .views import ExpanseCreate, ExpanseDelete, ExpanseList

urlpatterns = [
    path("createexp", view=ExpanseCreate.as_view(), name="createexp"),
    path("listexp", view=ExpanseList.as_view(), name="listexp"),
    path("deleteexp/<int:pk>", view=ExpanseDelete.as_view(), name="deleteexp"),
]
