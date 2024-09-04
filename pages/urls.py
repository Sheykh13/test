from django.urls import path
from pages import views
app_name='pages'
urlpatterns=[
path('',views.home_page,name='home'),
path('about/',views.about_page,name='about'),
path('login/',views.login_page,name='login'),
path('logout/',views.logout_page,name='logout'),
path("signup/", views.signup_page, name='signup'),
path("update_user/", views.update_use_page, name='update_user'),
path("ch_pass/", views.ch_pass_page, name='ch_pass'),


path('catgory/<str:cat>',views.catgory_page,name='catgory'),
path("cart1/",views.cart_page,name="cart1"),
#path("add/",views.carts_add,name="cart_add"),
#path("delete/",views.carts_delete,name="cart_delete"),
#path("update/",views.carts_update,name="cart_update"),
path('merch/<int:pk>',views.merch_page,name='merch'),




] 