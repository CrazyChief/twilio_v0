from django.conf import settings
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from twilio.twiml.voice_response import VoiceResponse, Say
from twilio.rest import Client
from django_twilio.decorators import twilio_view


@csrf_exempt
@twilio_view
def incoming(request, action=None, method='POST', timeout=None,
           finish_on_key=None, max_length=None, transcribe=None,
           transcribe_callback=None, play_beep=None):
    r = VoiceResponse()
    r.record(action=action, method=method, timeout=timeout,
             finishOnKey=finish_on_key, maxLength=max_length,
             transcribe=transcribe, transcribeCallback=transcribe_callback,
             playBeep=play_beep)
    print('\n\n\nDEBUG:')
    print(request)
    print(r)
    return r


class RecordView(TemplateView):

    def get(self, request, *args, **kwargs):
        print('\n\n\nDEBUG FROM RecordView:')
        print(request)
        print(self.args)
        print(self.kwargs)


class CheckView(TemplateView):

    def get(self, request, *args, **kwargs):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to='+380932812462',
            from_='+12017205869'
        )
        print(call)
        return HttpResponse()
