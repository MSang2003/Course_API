from rest_framework import pagination


class CoursesPanigator(pagination.PageNumberPagination):
    page_size = 1
