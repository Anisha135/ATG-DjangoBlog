from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from .forms import CaptchaForm
from .forms import BlogForm
from .models import BlogPost,BlogComment
from django.contrib import messages

def register(request):
    if request.method == 'GET':
        form = CaptchaForm()
        return render(request,'register.html',locals())
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
    
            if request.POST['password1'] == request.POST['password2']:
                try:
                    User.objects.get(username = request.POST['username'])
                    return render (request,'register.html', {'error':'Username is already taken!'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                    form = CaptchaForm(request.POST)
                    auth.login(request,user)
                    return redirect('home')
            else:
                return render (request,'register.html', {'error':'Password does not match!'})
        else:
            return render(request,'register.html',locals())        
    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def home(request):
    allPosts= BlogPost.objects.filter(author=request.user.username)
    context={'allPosts': allPosts}
    return render(request, "home.html", context)

def blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user.username
            form.save()
            return redirect("home")
        else:
            return HttpResponse("Invalid")    
    else:
        form = BlogForm()
    return render(request, 'blog.html', {'form' : form})
def usersearch(request):
    if request.method=="POST":
        try: 
            User.objects.get(username = request.POST['search'])
            name=request.POST['search']
            print(name)
            post=BlogPost.objects.filter(author=name).filter(public=True)
            context={'post':post,'name':name}
            print(context)
            return render(request,"usersearch.html",context)
        except User.DoesNotExist:
            return HttpResponse("User not found")       
    return render(request,"home.html")  


def blogPost(request,sno): 
    post=BlogPost.objects.filter(sno=sno).first()
    post.save()
    comments= BlogComment.objects.filter(post=post, parent=None)

    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, "blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= BlogPost.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
    return redirect(f"/blogPost/{post.sno}") 

def logout(request):
    return redirect("login")                

         

