from django.shortcuts import render

# Create your views here.
def post(request):
    post_list = Post.objects.all()
    return render(request, "blog/post.html", context= {"post":post_list} )