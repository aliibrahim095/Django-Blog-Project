from django.forms import fields
from django import forms
from posts.models import Badwords, Category, Post


class BadwordsForm(forms.ModelForm):

    class Meta:
        model = Badwords
        fields = ('badword',)
        widgets = {
            'badword': forms.TextInput(attrs={'class': 'form-control'})
        }


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostsForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField()
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=(
        (category.id, category.name) for category in Category.objects.all()))




# user
# title
# image
# publish
# content
# slug
# likes
# dislikes
