import folium
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import PostForm, LoginForm, UserRegistrationForm, ClientForm, HistoryForm
from .models import Post, Client, History


def start(request):
    return render(request, 'start.html', {})


def post_list(request):
    return render(request, 'main.html', {})


def about(request):
    return render(request, 'firstapp/about.html', {})


def mainproject(request):
    return render(request, 'project/main.html', {})


def test(request):
    return render(request, 'project/test.html')


def read_client(request):
    result = History.objects.all()
    paginator = Paginator(result, 5)
    page = request.GET.get('page')
    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)
    return render(request, "firstapp/client_list.html", {"result": result})


def readPost(request):
    text = Post.objects.all()
    paginator = Paginator(text, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "firstapp/index.html", {'text': text, 'page': page, 'posts': posts})


def search(request):
    text = Post.objects.filter(author=1)
    paginator = Paginator(text, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "firstapp/index.html", {'text': text, 'page': page, 'posts': posts})


def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index_list')
    else:
        form = PostForm()
    return render(request, 'firstapp/newPost.html', {'form': form})


def updatePost(request, id):
    try:
        posts = Post.objects.get(id=id)
        if request.method == "POST":
            posts.title = request.POST.get("title")
            posts.text = request.POST.get("text")
            posts.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "firstapp/update.html", {"posts": posts})
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Posts not found</h2>")


def deletePost(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Posts not found</h2>")


def about(request):
    return render(request, 'firstapp/about.html', {})


def readClient(request):
    text = Client.objects.all()
    return render(request, "firstapp/client_list.html", {"text": text})


def createClient(request):
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('index_list')
    else:
        form = HistoryForm()
        return render(request, 'firstapp/newClient.html', {'form': form})


def updateClient(request, id):
    try:
        clients = Client.objects.get(id=id)
        if request.method == "POST":
            clients.name = request.POST.get("name")
            clients.lastname = request.POST.get("lastname")
            clients.pol = request.POST.get("pol")
            clients.age = request.POST.get("age")
            clients.mail = request.POST.get("mail")
            clients.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "firstapp/update_client.html", {"clients": clients})
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Clients not found</h2>")


def deleteClient(request, id):
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return HttpResponseRedirect("/")
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Clients not found</h2>")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/main')
                else:
                    return HttpResponse('Учетная запись недействительна')
            else:
                return HttpResponse('Неверный логин')
    else:
        form = LoginForm()
    return render(request, 'firstapp/login.html', {'form': form})


def registr(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            return render(request, 'start.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'firstapp/registr.html', {'user_form': user_form})


def map(request):
    folium_map = folium.Map (location=[55.779864, 49.215766], zoom_start=70, tiles="Stamen Terrain")
    folium_map
    folium.CircleMarker ([55.72641, 52.3886], radius=40, popup="SmartGym", color='red', fill='red').add_to (
        folium_map)

    folium_map
    folium_map.save ('maps.html')
    return render (request, 'firstapp/maps.html', {'folium_map': folium_map})