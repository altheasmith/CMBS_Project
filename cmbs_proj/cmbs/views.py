from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from cmbs.models import Deal, Loan, Property, Article, Publisher, Keyword, Lease
from django.forms.models import model_to_dict


class MainView(View):
    def get(self, request):
        return render(request, 'cmbs/index.html')

class AllView(View):
    def get(self, request):
        articles = [model_to_dict(article) for article in Article.objects.all()]
        context = {'articles': articles}
        return JsonResponse(context)

class DealView(View):
    def get(self, request, term):
        
        articles = [model_to_dict(Article.objects.get(id=1))]
        context = {'articles': articles}
        return JsonResponse(context)
