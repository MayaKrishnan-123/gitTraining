from django.shortcuts import render



from django.views.generic import TemplateView

class base(TemplateView):
    template_name = "easyTodo/base.html"