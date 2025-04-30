from django.db import models
from django.contrib.auth.models import User

priority=(
    ('H','High'),
    ('M','Medium'),
    ('L','Low')
)

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    deadline=models.DateTimeField()
    priority=models.CharField(max_length=1,choices=priority)


    def __str__(self):
        return self.title



























































