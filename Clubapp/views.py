from django.shortcuts import render

from.models import Meeting, Meeting_Minutes, Resource ,Event
# Create your views here.
def index (request):
    return render(request, 'Clubapp/index.html')

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'Clubapp/meetings.html', {'meeting_list':meeting_list})

    # this will contain all the meetngs //



