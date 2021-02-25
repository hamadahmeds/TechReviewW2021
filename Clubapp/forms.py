from django import forms

from .models import Meeting, Meeting_Minutes, Resource ,Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model= Meeting
        fields='__all__'