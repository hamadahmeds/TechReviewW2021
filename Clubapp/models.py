from django.db import models

from django.contrib.auth.models import User

class Meeting(models.Model):
    MeetingTittle=models.CharField(max_length=255)
    MeetingDate=models.DateField()
    MeetingTime=models.TimeField()
    Location=models.CharField(max_length=255)
    Agenda=models.TextField()

    def __str__(self):
        return self.MeetingTittle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'


class Meeting_Minutes(models.Model):
    MeetingID=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    Attendance=models.ManyToManyField(User)
    Minutes=models.TextField()

    def __str__(self):
        return self.MeetingID
    
    class Meta:
        db_table='meeting minutes'
        verbose_name_plural='meeting_minutes'




class Resource (models.Model):
    ResourceName=models.CharField(max_length=255)
    ResourceType=models.CharField(max_length=255)
    URL=models.URLField()
    DateEntered=models.DateField()
    UserID=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Description=models.TextField()


    def __str__(self):
        return self.ResourceName
    
    class Meta:
        db_table='resources'


class Event (models.Model):
    EventTitle= models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    Date=models.DateField()
    Time=models.TimeField()
    Description=models.TextField()
    UserID=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    

    def __str__(self): 
        return self.EventTitle
    class Meta:
         db_table='event'


