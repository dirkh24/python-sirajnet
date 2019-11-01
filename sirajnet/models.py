from django.db import models

# Create your models here.
class hilbert_model(models.Model):
    """ the model for the perfect gaussian door """
    your_text = models.TextField()
    mine_text = models.TextField()
    swap_rate = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

