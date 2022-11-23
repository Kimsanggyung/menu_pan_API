from django.db import models

class Menu(models.Model):
  image = models.TextField()
  name = models.TextField()
  info = models.CharField(max_length=200)
  facts = models.CharField(max_length=500)
  price = models.CharField(max_length=5)
  allergy = models.CharField(max_length=50)
  kategorie = models.TextField()
  release_date = models.CharField(max_length=30)
  update_at = models.DateTimeField(auto_now=True)
