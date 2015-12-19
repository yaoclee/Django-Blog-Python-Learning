from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context_data = super(BlogIndex, self).get_context_data(**kwargs)
        alltags = models.Tag.objects.all()
        queryset = models.Entry.objects.published()
        context_data['alltags'] = alltags
        context_data['recent_posts'] = queryset[:5] #limitation for recent posts
        return context_data

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

    def get_client_ip(self):
        ip = self.request.META.get("HTTP_X_FORWARDED_FOR", None)
        if ip:
            ip = ip.split(", ")[0]
        else:
            ip = self.request.META.get("REMOTE_ADDR", "")
        return ip
        
    def get_context_data(self, **kwargs):
    	context_data = super(BlogDetail, self).get_context_data(**kwargs)
    	related_entries = models.Entry.objects.filter(
    		tags__in=list(self.object.tags.all())
    		).exclude(id=self.object.id)
        queryset = models.Entry.objects.published()
        alltags = models.Tag.objects.all()

        context_data['get_client_ip'] = self.get_client_ip
        context_data['alltags'] = alltags
        context_data['count_tags'] = related_entries.count
    	context_data['related_entries'] = related_entries[:5] #limitation for post
        context_data['recent_posts'] = queryset[:5] #limitation for recent posts
    	return context_data

class PageDetail(generic.DetailView):
    model = models.Page
    template_name = "pages.html"