from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        db_table = 'blog_category'
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

class BlogTag(models.Model):
    name = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        db_table = 'blog_tag'
        verbose_name = 'Blog Tag'
        verbose_name_plural = 'Blog Tags'

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs/')
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()

    category = models.ForeignKey('BlogCategory', on_delete=models.PROTECT, null=True, blank=True)
    tags = models.ManyToManyField('BlogTag', blank=True)
    comments_count = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} | {self.title}'

    class Meta:
        db_table = 'blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'