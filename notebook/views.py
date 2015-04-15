from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.forms import ModelForm
from django.db.models import Q, F
from django import template
from django.core.urlresolvers import reverse
# Create your views here.
from notebook.models import Article, Forum, hash_uid, Attachment
from notebook.forms import ArticleForm, LoginForm

import os

def index(request):
    # list all forums
    # basically retrieve top level forum here, and then loop through the sub forum in template
    forums = Forum.objects.all().filter(parent = None)
    data = {}
    data['forums'] = forums
    return render(request, 'notebook/list_forum.html', data)

def article(request, article_id):
    '''
        Shor one article. with reply articles
    '''
    article = get_object_or_404(Article, pk = article_id)
    if request.GET.get('mode', 'new') == 'delete':
        main_article = article
        while not main_article.main_article:
            main_article = main_article.reply_to
        main_deleted = False
        if main_article.id == article.id:
            main_deleted = True
            forum_id = main_article.forum.id
        article.delete()

        if not main_deleted:
            return redirect('notebook:view_article', main_article.id)
        else:
            return redirect('notebook:view_forum', forum_id)
    data = {}
    data['main_article'] = article
    data['articles'] = article.articles.all().exclude(id = article.id).order_by('-id')
    data['navs'] = get_navs(article)
    return render(request, 'notebook/article.html', data)

def new_article(request):
    
    data = {}
    article = Article()
    if request.method == "GET":
        if not request.GET.get('forum',''):
            raise Http404("Forum id must be provided")
        forum = get_object_or_404(Forum, pk=int(request.GET.get('forum','-1')))
        data['mode'] = request.GET.get('mode', 'new')
        if request.GET.get('mode', 'new') == 'edit':
            if not request.GET.get('article', ''):
                raise Http404("Artice id must be provided in edit mode")
            article_id = int(request.GET.get('article'))
            article = get_object_or_404(Article, pk=article_id)
            data['reply_to'] = article.reply_to

            data['article_id'] = article.id
        if request.GET.get('reply_to', None):
            reply_to = int(request.GET.get('reply_to', None))
            reply_to = get_object_or_404(Article, pk=reply_to)
            article.title = "Re: %s" % reply_to.title
            data['reply_to'] = reply_to
        if request.GET.get('title', None):
            article.title = request.GET.get('title','')
        data['form'] = ArticleForm(instance = article)
        data['forum'] = forum
        data['editor'] = True
        data['navs'] = get_navs(forum)

        return render(request, 'notebook/new_article.html', data)
    # POST DATA AFTER HERE
    mode = request.POST.get('mode','new')
    if mode == 'edit':
        article_id = request.POST.get('article_id','')
        if not article_id:
            raise Http404("article id must be provided while using edit mode")
        article = get_object_or_404(Article, pk=int(article_id))
    elif mode == 'new':
        article = Article()
    forum_id = request.POST.get('forum', '')
    reply_to = request.POST.get('reply_to', '')


    if not forum_id:
        # should be reply mode
        if reply_to:
            reply_article = get_object_or_404(Article, pk=int(reply_to))
            forum = article.forum
    else:
        forum = get_object_or_404(Forum, pk=int(forum_id))

    if reply_to and article.id != int(reply_to):
        article.reply_to = get_object_or_404(Article, pk=int(reply_to))
        article.main_article = False
        article.forum = get_object_or_404(Forum, pk=int(request.POST.get('forum', '-1')))
    else:
        article.forum = forum
    articleForm = ArticleForm(request.POST, instance = article)
    
    valid = True
    if not articleForm.is_valid():
        valid = False

    # handle file upload
    if valid:
        # save main article first
        articleForm.save()
        if not reply_to:
            article.reply_to = article
            article.save()
        files = request.FILES
        if len(files) > 0:
            for f_id in files:
                f = files[f_id]
                fname = f.name
                uid = hash_uid(fname)
                attachment = Attachment(name=fname, uid=uid, article=article)
                fpath = attachment.path()
                fdir = os.path.dirname(fpath)
                if not os.path.exists(fdir):
                    os.makedirs(fdir)
                print fpath
                with open(fpath, 'wb+') as dest:
                    for chunk in f.chunks():
                        dest.write(chunk)
                attachment.save()
                
    if request.is_ajax():
        if not valid:
            return JsonResponse({"error": ["Form is invalid..."]})
        else:
            return  JsonResponse({"error": []})
    if valid:
        main_article = article
        while not main_article.main_article:
            main_article = main_article.reply_to
        return redirect("notebook:view_article", main_article.id)
    else:
        data['forum'] = article.forum
        data['editor'] = True
        data['form'] = articleForm

        return render(request, 'notebook/new_article.html', data)

def list_article(request):
    forum_id = request.GET.get('forum','')
    if not forum_id:
        forum = Forum.objects.all()[0]
    else:
        forum = get_object_or_404(Forum, pk=int(forum_id))
    articles = forum.articles.all()
    data = {}
    data['articles'] = articles
    data['forum'] = forum
    navs = get_navs(forum)
    data['navs'] = navs
    return render(request, 'notebook/list_article.html', data)

def get_navs(ins):
    '''
        get navegation hericy
    '''
    navs = []
    if isinstance(ins, Article):
        navs.append({'url': reverse('notebook:view_article', args=[ins.id]), 'name': ins.title})
        forum = ins.forum
    else:
        forum = ins
    while forum is not None:
        print forum.parent
        navs.insert(0, {'url': reverse('notebook:view_forum', args=[forum.id]), 'name':forum.title})
        forum = forum.parent
    print navs
    return navs
def forum(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    articles = forum.articles.all().filter(main_article=True)
    articles_per_page = 10
    per_page = request.GET.get("per_page", '10')
    per_page = int(per_page)
    # no less than 10 per page
    if per_page > 10:
        articles_per_page = per_page
    page_number = request.GET.get("page", '1')
    page_number = int(page_number)
    total_pages =  len(articles) / per_page
    if len(articles) % per_page > 0:
        total_pages += 1
    
    articles = articles[(page_number - 1) * per_page : page_number * per_page]
    navs = []
#    navs.append({'url' : reverse('notebook:view_forum', args=[forum.id]), 'name':forum.title})
    navs = get_navs(forum)
    data = {
            'page_number'   : page_number,
            'total_pages'   : total_pages,
            'articles'      : articles,
            'forum'         : forum,
            'navs'          : navs,
            'opts'          : Forum._meta,
            }
    return render(request, 'notebook/view_forum.html', data)
