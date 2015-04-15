
from django.http import HttpResponse, JsonResponse
from {{resource_name}}.models import {{model_name}}
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404

class {{model_name}}Form(ModelForm):
    class Meta:
        model = {{model_name}}

def create(request):
    form = {{model_name}}Form
    return render(request, "{{resource_name}}/create.html", {"form":form})

def read(request, {{resource_name}}_id):
    {{resource_name}} = {{model_name}}.objects.get(pk={{resource_name}}_id)
    return render(request, "{{resource_name}}/read.html", {"{{resource_name}}":{{resource_name}} })

def update(request, {{resource_name}}_id):
    if request.method == "POST":
        form = {{model_name}}Form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "{{resource_name}}/update_succeed.html", {'redirect_to' : reverse("{{model_name}}:list")})
        else:
            return render(request, "{{resource_name}}/update.html", {"form":form})
    else:
        form = {{model_name}}Form()
        return render(request, "{{resource_name}}/update.html", {"form":form})

def delete(request, {{resource_name}}_id):
    {{resource_name}} = {{model_name}}.objects.get(pk={{resource_name}}_id)
    return render(request, "{{resource_name}}/confirm_delete.html")
