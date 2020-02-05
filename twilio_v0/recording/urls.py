from django.urls import path

from .views import incoming, RecordView


urlpatterns = [
    path('welcome/voice/', incoming, {
        'action': '/record/',
        'play_beep': True,
        'timeout': 5,
        'transcribe': True
    }),
    path('record/', RecordView.as_view(), name='record'),
]
