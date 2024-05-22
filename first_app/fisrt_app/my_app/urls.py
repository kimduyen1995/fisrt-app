from django.urls import path

from my_app.my_http.views.info_file_views import InfoFileView

urlpatterns = [
    path('info-file', InfoFileView.as_view({'get': 'api_get_info_file'})),
    path('insert-file', InfoFileView.as_view({'post':'api_insert_file'}))


]
