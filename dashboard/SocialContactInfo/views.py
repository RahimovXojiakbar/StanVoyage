from django.shortcuts import render, redirect
from main import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def social(request):
    social = models.Social.objects.filter(is_active=True)
    context = {
        'social': social
    }
    return render(request, 'social_contact_info/social.html', context)

@login_required(login_url='login')
def social_create(request):
    if request.method == 'POST':
        instagram = request.POST.get('instagram')
        telegram = request.POST.get('telegram')
        whatsapp = request.POST.get('whatsapp')
        gmail = request.POST.get('gmail')

        models.Social.objects.create(
           instagram = instagram,
           telegram = telegram,
           whatsapp = whatsapp,
           gmail = gmail
        )
        messages.success(request, 'Ijtimoyi tarmoq muvaffaqiyatli yaratildi!')
        return redirect('social')
        
@login_required(login_url='login')
def social_edit(request, uuid):
    social = models.Social.objects.get(uuid=uuid)
    if request.method == 'POST':
        # Update only provided fields
        instagram = request.POST.get('instagram')
        telegram = request.POST.get('telegram')
        whatsapp = request.POST.get('whatsapp')
        gmail = request.POST.get('gmail')
        
        social.instagram = instagram
        social.telegram = telegram
        social.whatsapp = whatsapp
        social.gmail = gmail
        
        social.save()
        messages.success(request, 'Ijtimoyi tarmoq muvaffaqiyatli yangilandi!')
        return redirect('social')








@login_required(login_url='login')
def company_info(request):
    company_info = models.CompanyInfo.objects.filter(is_active=True)
    context = {
        'company_info': company_info
    }
    return render(request, 'social_contact_info/company_info.html', context)



@login_required(login_url='login')
def company_info_create(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        models.CompanyInfo.objects.create(
           phone = phone,
           email = email
        )
        messages.success(request, 'Bog\'lanish muvaffaqiyatli yaratildi!')
        return redirect('company_info')
    


@login_required(login_url='login')
def company_info_edit(request, uuid):
        
    
    company_info = models.CompanyInfo.objects.get(uuid=uuid)

    if request.method == 'POST':
        # Update only provided fields
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        company_info.phone = phone
        company_info.email = email

        company_info.save()
        messages.success(request, 'Bog\'lanish muvaffaqiyatli yangilandi!')
        return redirect('company_info')


@login_required(login_url='login')
def contact_list(request):
    contact = models.Contact.objects.filter(is_active=True)

    context = {
        "contact":contact
    }
    return render(request, 'social_contact_info/contact.html', context)

@login_required(login_url='login')
def toggle_active(request, uuid):
    if request.method == 'POST':
        try:
            contact = models.Contact.objects.get(uuid=uuid)
            is_read = request.POST.get('is_read') == 'on'
            contact.is_read = is_read
            contact.save()
        except models.Contact.DoesNotExist:
            pass  # Optionally handle missing contact
    return redirect(request.META.get('HTTP_REFERER', 'list_page')) # Fallback to a default URL if HTTP_REFERER is missing  
