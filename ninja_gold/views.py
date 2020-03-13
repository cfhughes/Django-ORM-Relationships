from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'gold':request.session['gold'],
        'activities':request.session['activities']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.GET['location'] == 'farm':
        earned = random.randint(10,20)
        request.session['gold'] += earned
    if request.GET['location'] == 'cave':
        earned = random.randint(5,10)
        request.session['gold'] += earned
    if request.GET['location'] == 'house':
        earned = random.randint(2,5)
        request.session['gold'] += earned
    if request.GET['location'] == 'casino':
        earned = random.randint(-50,50)
        request.session['gold'] += earned
    request.session['activities'].append({'earned':earned,'location':request.GET['location'],'abs':abs(earned)})
    return redirect('./')