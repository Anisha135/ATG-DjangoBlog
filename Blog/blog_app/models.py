from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author=author=models.CharField(max_length=14)
    public=models.BooleanField(default=False)
    content=models.TextField()
    image=models.ImageField(upload_to="images/")
    written_on = models.DateTimeField(auto_now= True)
    sno=models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.title

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username        
