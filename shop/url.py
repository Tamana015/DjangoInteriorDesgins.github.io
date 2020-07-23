# shop.....................
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='www.VaayuInterior.in'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('office/',views.office,name='office'),
    path('homedecore/',views.homedecore,name='homedecore'),
    path('search/',views.search,name='search'),
    path('home/',views.home,name='home'),
    path('checkout/',views.checkout,name='checkout'),
    path('tracker/',views.tracker,name='tracker'),
    path('blog/', include('blog.urls')),
    path('productview/<int:myid>',views.productview,name='productview')

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


