from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

router =DefaultRouter()
router.register('/contact',ContactViewSet)


urlpatterns = [

    path('',views.base1.as_view(),name='base1'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path( 'api/' , include(router.urls))

]