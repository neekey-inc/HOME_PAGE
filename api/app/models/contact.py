import uuid
from django.db import models
from django.utils import timezone

class Contact(models.Model):
    class Meta:
        db_table = 'contact'

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 150, null = False)
    email = models.EmailField(null = False, unique=True)
    phone = models.CharField(max_length=64,null=False)
    subject = models.CharField(max_length = 300, null = False)
    detail = models.TextField(null = False)
    status = models.IntegerField(null = False, default=0)

    deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)    # category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,)

    def __str__(self):
        return self.subject
