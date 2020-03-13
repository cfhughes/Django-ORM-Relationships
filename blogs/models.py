from django.db import models

class User(models.Model):
    username = models.TextField()
    #blogs
    #comments

class Blog(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="blogs",blank=True, null=True)
    users_who_liked = models.ManyToManyField(User,related_name="blogs_liked")
    #entries

    def __str__(self):
        return f"Blog id {self.id} description: {self.description}"


class BlogEntry(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name="entries")
    #comments

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="comments")
    blogEntry = models.ForeignKey(BlogEntry,on_delete=models.CASCADE,related_name="comments")