from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null= True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = models.TextField

    image = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return self.subject
