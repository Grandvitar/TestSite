from django.views import View
from django.shortcuts import render
from .forms import MyForm
from .models import SaveModel


class MyView(View):

    def get(self, request):
        return render(request, template_name='index.html')

    def post(self, request):
        post_form = MyForm(request.POST)
        SaveModel.objects.create(image=request.FILES.get('image_input'), name=post_form.data.get('image_name'))
        print(post_form.data.get('image_input'))
        return render(request, template_name='index.html')


        return render(request, template_name='index.html')
