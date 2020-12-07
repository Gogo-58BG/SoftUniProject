from django.shortcuts import render

from app.models import Traxxas


def index(request):
    if Traxxas.objects.exists():
        articles = Traxxas.objects.all()
        # expenses = Expense.objects.all()
        # expenses_cost = sum(expense.price for expense in expenses)
        # profile.budget_left = profile.budget - expenses_cost
        context = {
            'articles': articles,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
