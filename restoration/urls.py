
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
admin.site.site_header = "Great Hills Admin"
admin.site.site_title = "Great Hills"
admin.site.index_title = "Welcome to Great Hills Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('greathills.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('Member',include('membership.urls'))
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


