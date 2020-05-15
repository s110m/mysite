from django.shortcuts import render
#from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
#from django.http import HttpResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income
from datetime import datetime
#from django.utils import timezone
# Create your views here.


@csrf_exempt
def submit_expense(request):
    """ submit an expense """

    # TODO: revise validation for the amount
    # this_date = request.POST['date'] if 'date' in request.POST else timezone.now()
    # this_text = request.POST['text'] if 'text' in request.POST else ""
    # this_amount = request.POST['amount'] if 'amount' in request.POST else "0"
    # this_token = request.POST['token'] if 'token' in request.POST else ""
    # this_user = get_object_or_404(User, token__token=this_token)
    #
    # Expense.objects.create(user=this_user, amount=this_amount,
    #                        text=this_text, date=this_date)
    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date=datetime.now()
    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)  # return {'status':'ok'}


@csrf_exempt
def submit_income(request):
    """ submit an income """

    # TODO: revise validation for the amount
    # this_date = request.POST['date'] if 'date' in request.POST else timezone.now()
    # this_text = request.POST['text'] if 'text' in request.POST else ""
    # this_amount = request.POST['amount'] if 'amount' in request.POST else "0"
    # this_token = request.POST['token'] if 'token' in request.POST else ""
    # this_user = get_object_or_404(User, token__token=this_token)
    #
    # Expense.objects.create(user=this_user, amount=this_amount,
    #                        text=this_text, date=this_date)
    this_token=request.POST['token']
    this_user=User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date=datetime.now()
    Income.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)  # return {'status':'ok'}