from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from cmbs.models import Deal, Loan, Property, Article, Publisher, Keyword, Lease
from django.forms.models import model_to_dict


class MainView(View):
    def get(self, request):
        deals = Deal.objects.all()
        loans = Loan.objects.all()
        properties = Property.objects.all()
        context = {'deals':deals,'loans':loans,'properties':properties}
        return render(request, 'cmbs/index.html', context)

class AllView(View):
    def get(self, request):
        articles = [model_to_dict(article) for article in Article.objects.all()]
        context = {'articles': articles}
        return JsonResponse(context)

class DealView(View):
    def get(self, request, term):
        deal = Deal.objects.get(deal_name=term)
        loans = Loan.objects.filter(deal=deal)
        articles = []
        for loan in loans:
            properties = Property.objects.filter(loan_link_id=loan)
            for prop in properties:
                new_articles = [model_to_dict(article) for article in Article.objects.filter(property=prop)]
            for article in new_articles:
                articles.append(article)
        context = {'articles': articles}
        return JsonResponse(context)

class LoanView(View):
    def get(self, request, term):
        loan = Loan.objects.get(loan_name=term)
        properties = Property.objects.filter(loan_link_id=loan)
        articles = []
        for prop in properties:
            new_articles = [model_to_dict(article) for article in Article.objects.filter(property=prop)]
        for article in new_articles:
            articles.append(article)
        # articles = [model_to_dict(article) for article in articles_build]
        context = {'articles': articles}
        # context = {'loan':model_to_dict(loan),'properties':properties}
        return JsonResponse(context)

class PropertyView(View):
    def get(self, request, term):
        prop = Property.objects.get(property_name=term)
        articles = [model_to_dict(article) for article in Article.objects.filter(property=prop)]
        context = {'articles': articles}
        return JsonResponse(context)
