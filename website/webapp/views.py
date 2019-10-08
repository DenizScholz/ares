from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.


class Home(View):
    title = 'Home'

    def get(self, request):
        context = {
            'title': self.title,
        }
        return render(request, 'webapp/index.html', context=context)


class Pricing(View):
    title = 'Pricing'

    def get(self, request):
        context = {
            'title': self.title,
        }
        return render(request, 'webapp/pricing.html', context=context)


class About(View):
    title = 'About'

    def get(self, request):
        context = {
            'title': self.title,
        }
        return render(request, 'webapp/about.html', context=context)
