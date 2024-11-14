# main/views.py
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail  # Optional: to send email notifications
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponseRedirect

def main_view(request):
    return render(request, 'main/index.html')  # Render your main template here

def about_redirect(request):
    return HttpResponseRedirect('/#about') 

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.POST)

        
        if form.is_valid():
            # Retrieve form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name = request.POST.get('name')

            form.save()
            
            # Attempt to send email
            try:
                # send_mail(
                #     f"Contact Form Submission from {name}",
                #     message,
                #     email,
                #     ['manishtimilsina7@gmail.com'],
                # )
                messages.success(request, 'Your message has been sent!')
            except Exception as e:
                messages.error(request, 'An error occurred while sending the email. Please try again later.')
                # Optionally, log the error here

            return redirect('contact')  # Redirect to the contact page
    else:
        form = ContactForm()
    
    return render(request, 'main/index.html', {'form': form})
