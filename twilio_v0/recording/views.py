from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from twilio.twiml.voice_response import VoiceResponse
from django_twilio.decorators import twilio_view

from .models import Record


@csrf_exempt
@twilio_view
def incoming(request, action=None, method='POST', timeout=None,
           finish_on_key=None, max_length=None, transcribe=None,
           transcribe_callback=None, play_beep=None):
    r = VoiceResponse()
    r.say(
        'Please leave a message at the beep.\nPress the star key when finished.'
    )
    r.record(action=action, method=method, timeout=timeout,
             finishOnKey=finish_on_key, maxLength=max_length,
             transcribe=transcribe, transcribeCallback=transcribe_callback,
             playBeep=play_beep)
    return r


class RecordView(TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # get values from params
        account_sid = request.POST.get('AccountSid', '')
        call_sid = request.POST.get('CallSid', '')
        call_status = request.POST.get('CallStatus', '')
        called = request.POST.get('Called', '')
        called_city = request.POST.get('CalledCity', '')
        called_country = request.POST.get('CalledCountry', '')
        called_state = request.POST.get('CalledState', '')
        called_zip = request.POST.get('CalledZip', '')
        caller = request.POST.get('Caller', '')
        caller_city = request.POST.get('CallerCity', '')
        caller_country = request.POST.get('CallerCountry', '')
        caller_state = request.POST.get('CallerState', '')
        caller_zip = request.POST.get('CallerZip', '')
        digits = request.POST.get('Digits', '')
        direction = request.POST.get('Direction', '')
        call_from = request.POST.get('From', '')
        from_city = request.POST.get('FromCity', '')
        from_country = request.POST.get('FromCountry', '')
        from_state = request.POST.get('FromState', '')
        from_zip = request.POST.get('FromZip', '')
        recording_duration = request.POST.get('RecordingDuration', '')
        recording_sid = request.POST.get('RecordingSid', '')
        recording_url = request.POST.get('RecordingUrl', '')
        call_to = request.POST.get('To', '')
        to_city = request.POST.get('ToCity', '')
        to_country = request.POST.get('ToCountry', '')
        to_state = request.POST.get('ToState', '')
        to_zip = request.POST.get('ToZip', '')

        # create record
        record = Record(
            account_sid=account_sid, call_sid=call_sid, call_status=call_status,
            called=called, called_city=called_city, called_country=called_country,
            called_state=called_state, called_zip=called_zip, caller=caller,
            caller_city=caller_city, caller_country=caller_country,
            caller_state=caller_state, caller_zip=caller_zip, digits=digits,
            direction=direction, call_from=call_from, from_city=from_city,
            from_country=from_country, from_state=from_state, from_zip=from_zip,
            recording_duration=recording_duration, recording_sid=recording_sid,
            recording_url=recording_url, call_to=call_to, to_city=to_city,
            to_country=to_country, to_state=to_state, to_zip=to_zip
        )
        record.save()

        # When call finished
        response = VoiceResponse()
        response.say('Thanks for your message')
        return HttpResponse(response)

