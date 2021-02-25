from django.shortcuts import render, get_object_or_404

from.models import Meeting, Meeting_Minutes, Resource ,Event
# Create your views here.
from django.urls import reverse_lazy

# here to import the form 
from .forms import MeetingForm

from django.contrib.auth.decorators import login_required






def index (request):
    return render(request, 'Clubapp/index.html')
def base(request):
    return render(request, 'Clubapp/.html')

def meeting(request):
    meeting=Meeting.objects.all()
    return render(request, 'Clubapp/meetings.html', {'meeting':meeting})
# @login_requited means you cant access the form unless you have log in info
@login_required 

def meetingDetail(request, id ):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'Clubapp/meetingdetail.html', {'meeting':meeting})





# // here the form start to see if the post or not and save  // 

def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'Clubapp/newmeeting.html', {'form': form})

def loginmessage(request):
    return render(request, 'Clubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'Clubapp/logoutmessage.html')