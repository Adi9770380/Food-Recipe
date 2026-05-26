from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recipe_name=models.CharField(max_length=50)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to='recipe_iamge')
    models.SlugField(unique='TRUE')
    
    def __str__(self):
        return self.recipe_name

# Create your models here.
