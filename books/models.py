from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Book(models.Model):
    STATUS_CHOICES = [
        ('want_to_read', 'Want to Read'),
        ('reading', 'Currently Reading'),
        ('read', 'Read'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='want_to_read')
    rating = models.IntegerField(null=True, blank=True, help_text="Rate 1-5 stars")
    review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):  # Fixed indentation
        return reverse('book-detail', kwargs={'book_id': self.id})
    
    class Meta:
        ordering = ['-date_added']