from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from stark.models import KirModel, CourseModel
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    cources = CourseModel.objects.all()
    context = {
        "x":cources
    }
    return render(request, 'index.html', context=context)

def c(request, c):
    cc = CourseModel.objects.get(name=c)
    context = {
        'cc':cc
    }
    return render(request, 'meeting-details.html', context=context)
def newtime(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        kir = KirModel(name=name, phone=phone, subject=subject, text=message)
        kir.save()
        return HttpResponseRedirect(reverse(index))


def co(request):
    posts = CourseModel.objects.all().order_by('v')
    p = Paginator(posts, 9)
    nop = request.GET.get("page", 1)
    page = p.page(nop)
    context = {
        "p": page,
        "x": p,
        'no':int(nop)
    }
    return render(request, 'meetings.html', context=context)
