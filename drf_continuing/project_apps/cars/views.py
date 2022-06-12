from django.shortcuts import render


def index(request):
    return render(request, 'cars/index.html', {'title': 'Hello, cars'})


"""
config breadcrambs
        context['breadcrumbs'] = (
            {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
            {'position': 2, 'name': 'Все отзывы', 'url': 'reviews', 'resolved': True},
            {'position': 3, 'name': 'Добавить отзыв', 'resolved': False},
        )

"""
