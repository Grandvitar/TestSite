from django import forms


class MyForm(forms.Form):
    image_input = forms.ImageField(required=False)
    image_name = forms.TextInput()
