from django.views import View
from django.shortcuts import render
from .forms import MyForm

class MyView(View):

    def get(self, request):
        return render(request, template_name='index.html')

    def post(self, request):
        post_form = MyForm(request.POST)

        print(post_form.data.get('image_name'))

        return render(request, template_name='index.html')
