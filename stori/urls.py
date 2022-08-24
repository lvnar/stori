from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls')),
    path('input', include('reader.urls')),
    path('mail', include('mailer.urls')),
]
