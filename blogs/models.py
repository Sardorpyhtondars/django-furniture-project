from django.db import models

from shared.models import BaseModel


class Author(BaseModel):
    full_name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='authors/', default='authors/default-user.jpg')
    about = models.CharField(max_length=255)
    professions = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'authors'
        verbose_name = 'author'
        verbose_name_plural = 'authors'

class Category(BaseModel):
    title = models.CharField(max_length=128)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Tag(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tags'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

class BlogStatus(models.TextChoices):
    PUBLISHED = "PUBLISHED", "Published"
    DRAFT = "DRAFT", "Draft"
    DELETED = "DELETED", "Deleted"

class Blog(BaseModel):
    title = models.CharField(max_length=128)
    short_description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs/', default='blogs/default-blog.jpg')
    long_description = models.TextField()

    status = models.CharField(
        max_length=24,
        choices=BlogStatus.choices,
        default=BlogStatus.DRAFT
    )

    categories = models.ManyToManyField(Category, related_name='blogs')
    tags = models.ManyToManyField(Tag, related_name='blogs')
    authors = models.ManyToManyField(Author, related_name='blogs')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'