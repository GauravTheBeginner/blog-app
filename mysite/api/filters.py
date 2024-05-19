import django_filters
from .models import BlogPost


class BlogPostFilter(django_filters.FilterSet):
    o = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('categories', 'categories'),
        )
    )

    class Meta:
        model = BlogPost
        fields = {
            'categories': ['exact'],
        }
