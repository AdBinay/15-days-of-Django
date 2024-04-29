from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_date = models.DateTimeField("user created",auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    age = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True)
    
    class Meta:
        verbose_name = "Peoples"
        verbose_name_plural = "people"

    def __str__(self):
        return self.first_name+" "+self.last_name