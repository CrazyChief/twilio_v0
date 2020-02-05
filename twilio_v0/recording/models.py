from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Record(models.Model):
    """
    Model for storing call records
    """
    account_sid = models.CharField(max_length=50, null=True, blank=True)
    call_sid = models.CharField(max_length=50, null=True, blank=True)
    call_status = models.CharField(max_length=20, null=True, blank=True)
    called = PhoneNumberField(null=True, blank=True)
    called_city = models.CharField(max_length=30, null=True, blank=True)
    called_country = models.CharField(max_length=4, null=True, blank=True)
    called_state = models.CharField(max_length=4, null=True, blank=True)
    called_zip = models.CharField(max_length=10, null=True, blank=True)
    caller = PhoneNumberField(null=True, blank=True)
    caller_city = models.CharField(max_length=30, null=True, blank=True)
    caller_country = models.CharField(max_length=4, null=True, blank=True)
    caller_state = models.CharField(max_length=4, null=True, blank=True)
    caller_zip = models.CharField(max_length=10, null=True, blank=True)
    digits = models.CharField(max_length=50, null=True, blank=True)
    direction = models.CharField(max_length=20, null=True, blank=True)
    call_from = PhoneNumberField(null=True, blank=True)
    from_city = models.CharField(max_length=30, null=True, blank=True)
    from_country = models.CharField(max_length=4, null=True, blank=True)
    from_state = models.CharField(max_length=4, null=True, blank=True)
    from_zip = models.CharField(max_length=10, null=True, blank=True)
    recording_duration = models.CharField(max_length=10, null=True, blank=True)
    recording_sid = models.CharField(max_length=50, null=True, blank=True)
    recording_url = models.URLField(null=True, blank=True)
    call_to = PhoneNumberField(null=True, blank=True)
    to_city = models.CharField(max_length=30, null=True, blank=True)
    to_country = models.CharField(max_length=4, null=True, blank=True)
    to_state = models.CharField(max_length=4, null=True, blank=True)
    to_zip = models.CharField(max_length=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Call from: {self.call_from} to {self.call_to}'
