from django.shortcuts import render
from southflalerts.forms import EmpInsertForm
from southflalerts.forms import EmpDeleteForm
from southflalerts.forms import Contact
from southflalerts.models import EmpDelete
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage, get_connection

def Insertvalue(request):
    if request.method == "POST":
        form = EmpInsertForm(request.POST)
        if form.is_valid():
            form.URL = request.POST.get('URL')
            form.email = request.POST.get('email')
            form.save()
            messages.success(request,'Info saved. Be on the lookout for a confirmation e-mail within 10 minutes.')
        elif not form.non_field_errors():
            messages.error(request,'Captcha not cleared. Please try again.')
        return render(request,'Index.html',{"form":form})
    else:
        form = EmpInsertForm()
        return render(request,'Index.html',{"form":form})

def Deletevalue(request):
    if request.method == "POST":
        form = EmpDeleteForm(request.POST)
        if form.is_valid():
            form.email = request.POST.get('email')
            emailToDelete = EmpDelete.objects.filter(email = form.email)
            if emailToDelete:
                emailToDelete.delete()
                messages.success(request,'You have been unsubscribed from our services and won\'t receive any emails from us.')
            else:
                messages.error(request,'We don\'t have that email address in our database.')
        else:
            messages.error(request,'Captcha not cleared. Please try again.')
        return render(request,'Unsubscribe.html',{"form":form})
    else:
        form = EmpDeleteForm()
        return render(request,'Unsubscribe.html',{"form":form})

def ContactUs(request):
    if request.method == "POST":
        form = Contact(request.POST)
        if form.is_valid():
            with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
            ) as connection:
                subject = request.POST.get("subject")
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [settings.EMAIL_HOST_USER]
                message = request.POST.get("message")
                EmailMessage(subject, message, email_from, recipient_list, reply_to=[request.POST.get("email")], connection=connection).send()
            messages.success(request,'Email sent!')
        else:
            messages.error(request,'Captcha not cleared. Please try again.')
        return render(request,'Contact.html',{"form":form})
    else:
        form = Contact()
        return render(request,'Contact.html',{"form":form})

def My404(request,exception):
    return render(request,'errors/404.html', {})

def My500(request,exception):
    return render(request,'errors/500.html', {})


