from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from entry.models import Entry
from box.models import Box
from django.forms import ModelForm
from django.core.urlresolvers import reverse

# Create your views here.


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ["uid", "box", "row","col","entry_type", "description"]

def home(request):
    return HttpResponse("Hello World!")


def edit(request, entry_id):
    pass

def add(request):
    if request.method == "POST":
        if "from_url" in request.POST:
            from_url = request.POST.get('from_url')
            from_name = request.POST.get('from_name')
        else:
            from_url = reverse("entry:list")
            from_name = "list"
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            return redirect("box:show", entry.box.id)
        else:
            return render(request, "entry/add.html", {"form":form, "from_url":from_url, "from_name":from_name})
    else:
        copyid = request.GET.get('copy', '')
        if copyid != "":
            bid = int(copyid)
            entry = Entry.objects.get(pk=bid)
            entry.pk = None
            form = EntryForm(instance = entry)
        else:
            form = EntryForm()
        return render(request, "entry/add.html", {"form":form})

def delete(request, entry_id):
    pass

def show(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    return render(request, "entry/show.html", {"entry":entry})

def list(request):
    pass

def get_next_row_col(request):
    bid = request.GET.get('bid', "")
    result = {'err' : 0}
    if bid == "":
        result['row'] = 1
        result['col'] = 1
        return JsonResponse(result)
    bid = int(bid)
    try:
        box = Box.objects.get(pk=bid)
    except Box.DoesNotExist:
        result['err'] = 1
        return JsonResponse(result)
    mrow = box.rows
    mcol = box.cols
    entries = box.entry_set.all().order_by('-row', '-col')
    row = 1
    col = 1
    if len(entries) > 0:
        row = entries[0].row
        col = entries[0].col
    col += 1
    if col > mcol:
        col = 1
        row += 1
    if row > mrow:
        col = -1
        row = -1
    result['col'] = col
    result['row'] = row
    return JsonResponse(result)
    

def get_max_row_col(request):
    bid = request.GET.get('bid', "")

    result = {'err' : 0}
    if bid == "":
        result['row'] = 1
        result['col'] = 1
        return JsonResponse(result)
    bid = int(bid)
    try:
        box = Box.objects.get(pk=bid)
    except Box.DoesNotExist:
        result['err'] = 1
        return JsonResponse(result)
    entries = box.entry_set.all().order_by('-row', '-col')
    row = 1
    col = 1
    if len(entries) > 0:
        row = entries[0].row
        col = entries[0].col
    result['row'] = row
    result['col'] = col
    return JsonResponse(result)

    
