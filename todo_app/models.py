from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

priority=(
    ('H','High'),
    ('M','Medium'),
    ('L','Low')
)

"""
DOes not work because createsuperuser command requires username
Solution : Create a CustomUserManager() for createsuperuser to use 
"""
#class CustomUser(AbstractUser):
#    name=models.CharField(max_length=200)
#    email=models.EmailField(unique=True)
#    password=models.CharField(max_length=12)
#    username=None
#    USERNAME_FIELD='email'
#    REQUIRED_FIELDS=[]

class CustomUserManager(BaseUserManager):
    def create_superuser(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address") 
        
        user=self.create_user(email=email,password=password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
        
    
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        user=self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.is_staff=True
        user.is_superuser=False
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    name=models.CharField(max_length=200,blank=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=500)
    username=None
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()


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



























































