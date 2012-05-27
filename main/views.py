# Create your views here.
from django.http import HttpResponse
from main.models import Student, Faculty
from django.template import RequestContext
from django.shortcuts import render_to_response

### Other ###
def notfound(request):
    return render_to_response('404.html', [], context_instance=RequestContext(request))

def home(request): 
    return render_to_response('index.html', [], context_instance=RequestContext(request))

### About ###
def about(request):
    print "test"
    return render_to_response('about/about.html', [], context_instance=RequestContext(request))

### Prospective Students
def programinfo(request):
    return render_to_response('programinfo.html', [], context_instance=RequestContext(request))

def prospective_students(request):
    return render_to_response('prospective_students/prospective_students.html', [], context_instance=RequestContext(request))

### Students ###
def student_profiles(request):
    return render_to_response('students/profiles.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def student_intranet(request):
    return render_to_response('students/intranet.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def photos(request):
    return render_to_response('students/photos.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def courses(request):
    return render_to_response('students/courses.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def calendar(request):
    return render_to_response('students/calendar.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

def news(request):
    return render_to_response('students/news.html', {'students': Student.objects.all()}, context_instance=RequestContext(request))

### Faculty ###
def faculty_profiles(request):
    return render_to_response('faculty/profiles.html', {'faculty': Faculty.objects.all()}, context_instance=RequestContext(request))


