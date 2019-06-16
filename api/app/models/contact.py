import uuid
from django.db import models
from django.utils import timezone

# class CategoryManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().annotate(
#             article_count=models.Count('article')
#         ).order_by('-article_count')

# class Category(models.Model):
#     class Meta:
#         db_table = 'category'

#     name = models.CharField(max_length=40)
#     objects = CategoryManager()

#     def __str__(self):
#         if hasattr(self, 'article_count'):
#             return f'{self.name}({self.article_count})'
#         else:
#             return self.name

class Contact(models.Model):
    class Meta:
        db_table = 'contact'

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 30, null = False)
    name = models.CharField(max_length = 30, null = False)
    email = models.EmailField(null = False)
    text = models.TextField(null = False)
    tell = models.TextField(max_length=12,null=False)
    # category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,)

    def __str__(self):
        return self.title