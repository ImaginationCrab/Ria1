from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(default='No description available')
    image = models.ImageField(upload_to='movies/', default='movies/placeholder.png')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    
    def __str__(self):
        return self.title
'''
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField(default='No review available')
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.movie.title} ({self.quantity})"

# class Searchbar(models.Model):
 #   search_text = models.CharField(max_length=200)
 #   description = models.TextField()

 #   def __str__(self):
 #       return self.name
'''