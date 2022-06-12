from django.shortcuts import render


def index(request):
    return render(request, 'main_app/index.html', {'title': 'Hello, main'})


"""
config breadcrambs
        context['breadcrumbs'] = (
            {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
            {'position': 2, 'name': 'Все отзывы', 'url': 'reviews', 'resolved': True},
            {'position': 3, 'name': 'Добавить отзыв', 'resolved': False},
        )

"""
