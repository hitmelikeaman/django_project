from django.utils import timezone
from .models import Post, Question
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .utilities import parse_for_checked, apply_priorities, form_result


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            you = form.cleaned_data['you']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(you, message, from_email, ['dnaumova1997@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, "project/contact.html", {'form': form})


def success(request):
    return render(request, "project/success.html")


def index(request):
    return render(request, 'project/index.html', {})


def lessons(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'project/lessons.html', {'posts': posts})


def tuitor(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'project/tuitor.html', {'post': post})


def choose(request):
    if request.method == 'POST':
        checked = parse_for_checked(request)
        objects = Question.objects.all().values_list()
        prioritised_objects = apply_priorities(objects, checked)
        dcs_cat = form_result(prioritised_objects)
        return render(request, 'project/results.html', {'dcs_cat': dcs_cat})
    return render(request, 'project/choose.html')
