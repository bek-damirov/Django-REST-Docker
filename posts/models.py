from django.db import models
from accounts.models import Author


class Post(models.Model):
    text = models.TextField()
    data_joined = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author

    def get_status(self):
        statuses = PostStatus.objects.filter(post=self).values('status')
        result = {}
        num = 0
        ser = 0
        for i in statuses:
            num = num + i['status']
            ser = ser + 1
        if num != 0:
            result['оценка'] = num / ser
            return result
        result['оценка'] = num
        return result


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    data_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.id}-{self.author.user.username}'

    def get_status_com(self):
        statuses = CommentStatus.objects.filter(comment=self).values('status')
        result = {}
        num = 0
        ser = 0
        for i in statuses:
            num = num + i['status']
            ser = ser + 1
        if num != 0:
            result['оценка'] = num / ser
            return result
        result['оценка'] = num
        return result


class Status(models.Model):
    status_choice = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    status = models.IntegerField(choices=status_choice)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class PostStatus(Status):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['author', 'post']

    def __str__(self):
        return f'{self.post.id}-{self.author.id}-{self.status}'


class CommentStatus(Status):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['author', 'comment']

    def __str__(self):
        return f'{self.comment.id}'



