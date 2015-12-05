from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from cmbs.models import Deal, Loan, Property, Article, Publisher, Keyword, Lease
from django.forms.models import model_to_dict


def get_articles(prop):
    prop = Property.objects.get(property_name=prop)
    articles = [model_to_dict(article) for article in Article.objects.filter(property=prop)]
    return articles

def get_keywords(articles):
    for article in articles:
        keywords_list = [Keyword.objects.get(id=key).word for key in article['key_words']]
        article['key_words'] = ', '.join(keywords_list)
    return articles

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
        get_keywords(articles)
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
                articles += get_articles(prop)
        articles = get_keywords(articles)
        context = {'articles': articles}
        return JsonResponse(context)

class LoanView(View):
    def get(self, request, term):
        loan = Loan.objects.get(loan_name=term)
        properties = Property.objects.filter(loan_link_id=loan)
        articles = []
        for prop in properties:
            articles += get_articles(prop)
        articles = get_keywords(articles)
        context = {'articles': articles}
        return JsonResponse(context)

class PropertyView(View):
    def get(self, request, term):
        articles = get_articles(term)
        articles = get_keywords(articles)
        context = {'articles': articles}
        return JsonResponse(context)
