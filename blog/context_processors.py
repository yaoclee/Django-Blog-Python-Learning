
from blog.models import Tag, Category, Post

def data_list(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    hot_posts = Post.objects.filter(hot_rec=True).order_by('-modified')[:10]
    return {
        "tags" : tags, 
        "categories" : categories,
        "hot_posts" : hot_posts
    }
