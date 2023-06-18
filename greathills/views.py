from django.shortcuts import render,get_object_or_404
from .models import ContactTable, FutureEvents,LatestEvents
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.

# fetching from db
events = LatestEvents.objects.all()
futurevents = FutureEvents.objects.all()
# send to user
context = {
 'event': events,
 'futureEV':futurevents,
}

def home(request):
    events = LatestEvents.objects.all().order_by('-posted_date')[:3]
    return render(request, "home.html",{'event': events})

def about(request):
    return render(request, "about.html",{})

def events(request):
    event = LatestEvents.objects.all()
    futurevents = FutureEvents.objects.all().order_by('-posted_date')
    p = Paginator(event, 10)
    page_number = request.GET.get('page', 1 )
   
    try:
        page = p.page(page_number)
    except PageNotAnInteger:
        page= p.page(1)
    except EmptyPage: 
       page = p.page(p.num_pages)
        
    context ={'event':page}

    return render(request, "events.html", context)

def contact(request):
    if request.method == 'POST':
        post = ContactTable()
        post.FullName = request.POST.get('fullname')
        post.EmailAddress = request.POST.get('email')
        post.Subject = request.POST.get('subject')
        post.Message = request.POST.get('message')
        post.save()

        messages.error(request,'Thanks, Your message have been sent successfully.')
        return render(request, "contact.html",{})
    else:
        return render(request, "contact.html",{})

def events_details(request, pk):
    details = get_object_or_404(LatestEvents, pk = pk)

    return render(request, "events_details.html",{'events_details':details})
    
def future_events(request, pk):
    future_details = get_object_or_404(FutureEvents, pk = pk)

    return render(request, "futurevents_detais.html",{'future':future_details})
