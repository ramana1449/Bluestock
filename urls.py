urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ipo_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
