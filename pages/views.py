from .models import Post , Contact
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from accounts.models import Profile
from django.shortcuts import render ,redirect ,get_list_or_404 ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages , auth
from accounts.models import Comment



def index(request):
    return render(request , 'pages/index.html')


def contact(request):
    return render(request , 'pages/contact.html')    

def blog(request):
    posts = Post.objects.order_by('date').filter(is_published=True)
    posts2 = posts[:4]
    paginator = Paginator(posts , 5)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    context = {
        'posts' : paged_posts ,
        'posts2' : posts2 ,
    }
    return render(request , 'pages/blog.html',context) 

def post(request,post_id):
    comments = Comment.objects.all().filter(post_id=post_id).filter(is_published=True)
    cou = comments.count()
    posts = Post.objects.order_by('date').filter(is_published=True)[:4]
    post = get_object_or_404(Post,pk=post_id)
    profile = Profile.objects.get(user=post.auther)
    context = {
        'post' : post ,
        'posts' : posts ,
        'profile' : profile ,
        'comments' :comments ,
        'count' : cou ,
    }
    return render(request , 'pages/post.html',context)    

def gcontact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['name']
        subject = request.POST['subject']
        text = request.POST['text']
        contact = Contact(name=name , email=email , subject=subject , text=text)
        contact.save()
        messages.success(request, ": " + "Thanks for Contacting Will Seen Soon") 
        return redirect('contact')
    return render(request , 'pages/contact.html')




def gcomment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        user_id = request.POST['user_id']
        name = request.POST['name'] 
        text = request.POST['text']
        comment = Comment(post_id=post_id , user_id=user_id,name=name,text=text)
        comment.save()
        messages.success(request, ": " + "Thanks for Commenting After Sccepting will Show") 
        return redirect('/blog/posts/'+post_id)

