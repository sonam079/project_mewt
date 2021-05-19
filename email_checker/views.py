import smtplib
from django.shortcuts import render
from .models import Emails


def index(request, email):
    bank_domain_names = {
        'bankofbaroda.com': 'Bank of Baroda',
        'bankofindia.co.in': 'Bank of India',
        'mahabank.co.in': 'Bank of Maharashtra',
        'canarabank.com': 'Canara Bank',
        'centralbank.co.in': 'Central Bank of India',
        'iobnet.co.in': 'Indian Overseas Bank',
        'psb.co.in': 'Punjab and Sind Bank',
        'pnb.co.in': 'Punjab National Bank',
        'ucobank.co.in': 'Uco Bank',
        'unionbankofindia.com': 'Union Bank of India',
        'axisbank.com': 'Axis Bank',
        'bandhanbank.com': 'Bandhan Bank',
        'cityunionbank.com': 'City Union Bank',
        'csb.co.in': 'Catholic Syrian Bank',
        'dcbbank.com': 'DCB Bank',
        'dhanbank.co.in': 'Dhanlaxmi Bank',
        'federalbank.co.in': 'Federal Bank',
        'hdfcbank.com': 'HDFC Bank',
        'idfcfirstbank.com': 'IDFC FIRST Bank',
        'indusind.com': 'IndusInd Bank',
        'jkbmail.com': 'Jammu and Kashmir Bank',
        'ktkbank.com': 'Karnataka Bank',
        'kvbmail.com': 'Karur Vysya Bank',
        'Ivbank.in': 'Lakshmi Vilas Bank',
        'nainitalbank.co.in': 'Nainital Bank',
        'rblbank.com': 'RBL Bank',
        'sib.co.in': 'South Indian Bank',
        'tmbank.in': 'Tamilnad Mercantile Bank',
        'yesbank.in': 'Yes Bank',
        'ujjivan.com': 'Ujjivan Small Finance Bank',
        'aubank.in': 'AU Small Finance Bank',
        'capitalbank.co.in': 'Capital Small Finance Bank',
        'esafbank.com': 'ESAF Small Finance Bank',
        'suryodaymf.com': 'Suryoday Small Finance Bank',
        'utkarsh.bank': 'Utkarsh Small Finance Bank',
        'finobank.com': 'Fino Payments Bank'
    }
    user_name, domain_name = email.split('@')
    if domain_name in bank_domain_names.keys():
        response = 'The sender is ' + bank_domain_names[domain_name]
        existing_email = Emails.objects.filter(email=email)
        total_email_count = Emails.objects.all().count()
        if not existing_email and total_email_count < 100:
            Emails.objects.create(email=email)
        elif total_email_count == 100:
            send_email()
    else:
        response = 'Please try another email'
    return render(request, 'template.html', {'result': response})


def send_email():
    message = 'Hi, we have reached the limit'
    audience = 'xyz@gmail.com'
    user = 'abc@gmail.com'
    password = 'abcxyz123'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.sendmail(user, audience, message)
    server.quit()
    return 1
