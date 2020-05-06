
from blog.models import Tag, Category, Post

def data_list(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    hot_rank_posts = Post.objects.all().order_by('-visited_num')[:10] #list top 10 on right sidebar
    hot_rec_posts = Post.objects.filter(hot_rec=True).order_by('-modified')[:10]
    return {
        "tags" : tags, 
        "categories" : categories,
        "hot_rank_posts" : hot_rank_posts,
        "hot_rec_posts" : hot_rec_posts,
    }
