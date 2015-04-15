from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from box.models import Box

# Create your views here.
from django.forms import ModelForm
class BoxForm(ModelForm):
    class Meta:
        model = Box
        fields = ["uid", "location", "description", "rows", "cols"]

def home(request):
    return HttpResponse("Hello World!")


def edit(request, box_id):
    pass

def add(request):
    if request.method == "POST":
        form = BoxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("box:list")
    else:
        form = BoxForm()

    return render(request, "box/add.html", {'form' : form })

def delete(request, box_id):
    pass

def show(request, box_id):
    box = get_object_or_404(Box, pk = box_id)
    row_numbers = ""
    col_numbers = ""
    for i in range(box.rows):
        row_numbers += chr(i + ord("A"))
    for i in range(box.cols):
        col_numbers += str(i + 1)
    return render(request, "box/show.html", {'box': box, 
        'row_numbers':row_numbers,
        'col_numbers':col_numbers,
        })

def list(request):
    boxes = Box.objects.all()
    if len(boxes) == 0:
        b = Box()
        b.save()
        boxes = Box.objects.all()
    return render(request, "box/list.html", {"boxes":boxes})
