
from blog.models import Tag, Category

def data_list(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return {"tags" : tags, "categories" : categories}
