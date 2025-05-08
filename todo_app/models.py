from django.db import models
from django.contrib.auth.models import AbstractUser

priority=(
    ('H','High'),
    ('M','Medium'),
    ('L','Low')
)


class CustomUser(AbstractUser):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=12)
    USERNAME_FIELD='email'
    username=None
    REQUIRED_FIELDS=[]

class Todo(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField()
    priority=models.CharField(max_length=1,choices=priority)


    def __str__(self):
        return self.title



























































