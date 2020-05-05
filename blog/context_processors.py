
from blog.models import Tag

def tag_list(request):
    tags = Tag.objects.all()
    return {"tags" : tags}