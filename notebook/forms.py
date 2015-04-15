from django.forms import ModelForm, CharField, PasswordInput
from notebook.models import Article, ForumUser

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']

class LoginForm(ModelForm):
    password = CharField(widget = PasswordInput()) 
    class Meta:
        model = ForumUser
        fields = ['name', 'password']
