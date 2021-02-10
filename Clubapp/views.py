from django.shortcuts import render, get_object_or_404

from.models import Meeting, Meeting_Minutes, Resource ,Event
# Create your views here.
from django.urls import reverse_lazy

def index (request):
    return render(request, 'Clubapp/index.html')
def base(request):
    return render(request, 'Clubapp/.html')

def meeting(request):
    meeting=Meeting.objects.all()
    return render(request, 'Clubapp/meetings.html', {'meeting':meeting})





def meetingDetail(request, id ):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'Clubapp/meetingdetail.html', {'meeting':meeting})

