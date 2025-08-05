from .models import Category


def add_categories_to_layout(request):
    category_list = Category.objects.all().order_by('name')[:10].values_list('id', 'name')
    return {
        'category_list':category_list,
    }

