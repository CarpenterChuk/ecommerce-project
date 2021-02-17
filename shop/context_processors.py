from .models import Category, Product


def menu_links(reguest):
    links = Category.objects.all()
    return dict(links=links)