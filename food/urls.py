from django.urls import path
from . import views


app_name = "food"
urlpatterns = [
    path('', views.IndexClassView.as_view(), name="index"),
    path('detail/<pk>', views.DetailClassView.as_view(), name='detail'),

    # create Item
    path('create_item/', views.CreateItemView.as_view(), name='create_item'),

    # update Item
    path('update_item/<pk>/', views.UpdateItemView.as_view(), name='update_item'),

    # delete Item
    path('delete_item/<pk>', views.DeleteItemView.as_view(), name='delete_item')
]
