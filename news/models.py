from django.db import models
from django.contrib.auth.models import User


class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    author_rating = models.IntegerField(default=0)

    def update_rating(self, update_rating):
        self.author_rating = update_rating
        self.save()


class Category (models.Model):
    category_name = models.TextField(max_length=255, unique=True)


article = 'PS'
news = 'NW'

PUBLICATIONS = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Post (models.Model):
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    news_or_articles = models.CharField(max_length=2, choices=PUBLICATIONS)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header_of_publication = models.TextField(max_length=255)
    publication_text = models.TextField()
    publication_rating = models.IntegerField(default=0)

    def like(self):
        self.publication_rating += 1
        self.save()

    def dislike(self):
        self.publication_rating -= 1
        self.save()

    def preview(self):
        size = 124
        if len(self.publication_text) > 124:
            return self.publication_text[:size] + '...'
        else:
            len(self.publication_text)


class PostCategory (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment (models.Model):
    com_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    com_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.publication_rating = int

    def like(self):
        self.publication_rating += 1
        self.save()

    def dislike(self):
        self.publication_rating -= 1
        self.save()
