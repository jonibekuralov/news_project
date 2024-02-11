from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Category, News
from .forms import ContactForm
# Create your views here.

def news_list(request):
    # default manager orqali
    # news_list = News.published.all()
    # Yaratgan menejerimiz orqali
    news_list =News.objects.filter(status=News.Status.Published)
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)


# def news_detail(request, id):
#     news = get_object_or_404(News, id=id, status=News.Status.Published)
#     context = {
#         "news": news
#     }
#
#     return render(request, 'news/news_detail.html', context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }

    return render(request, 'news/news_detail.html', context)


# context protsessor




#funkisya orqali
# def HomePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:5]
#     local_one = News.published.all().filter(category__name="O'zbekiston").order_by("-publish_time")[:1]
#     local_news = News.published.all().filter(category__name="O'zbekiston").order_by("-publish_time")[1:6]
#
#
#     context = {
#         "news_list": news_list,
#         "categories": categories,
#         "local_one": local_one,
#         "local_news": local_news
#     }
#
#     return render(request, "news/index.html", context)


#class orqali
class homePageView(TemplateView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')
        # context['local_one'] = News.published.all().filter(category__name="O'zbekiston").order_by("-publish_time")[:1]
        context['local_news'] = News.published.all().filter(category__name="O'zbekiston")[:6]
        context['world_news'] = News.published.all().filter(category__name="Jahon")[0:4]
        context['sport_news'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[:6]
        # context['sport_news2'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[1:5]
        context['techno_news'] = News.published.all().filter(category__name="Fan-texnika").order_by("-publish_time")[:6]
        # context['techno_news2'] = News.published.all().filter(category__name="Fan-texnika").order_by("-publish_time")[1:5]
        context['economy'] = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[:6]
        # context['economy2'] = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[1:6]
        context['galery'] = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[0:6]


        return context

# requets turlari
# POST
# GET

# def ContactPageView(request):
#     # print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Ma'lumotlaringiz jo'natildi </h2>")
#     context ={
#         "form" : form
#     }
#     return render(request, 'news/contact.html', context)


class ContactPageView(TemplateView):
    templates_name = 'news/contact.html'

    def get(self, request,  *args, **kwargs):
        form = ContactForm()
        context = {
            'form' : form
        }
        return render(request, "news/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Xabaringiz yuborildi </h2>")
        context = {
            "form": form
        }

        return render(request, "news/contact.html", context)




class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'localnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="O'zbekiston")
        return news

class WorldNewsView(ListView):
    model = News
    template_name = 'news/world.html'
    context_object_name = 'worldnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Jahon")
        return news

class SubjectNewsView(ListView):
    model = News
    template_name = 'news/fan.html'
    context_object_name = 'fannews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Fan-texnika")
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sportnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news

class IqtisodNewsView(ListView):
    model = News
    template_name = 'news/iqtisodiyot.html'
    context_object_name = 'iqtisodnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Iqtisodiyot")
        return news