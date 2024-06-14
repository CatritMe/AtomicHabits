from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Пагинатор для списка привычек, показывать по 5 на странице"""
    page_size = 5
