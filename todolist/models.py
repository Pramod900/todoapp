from django.db import models

# Create your models here.

class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.text
    
# Tate bohi bohi rod de

# "ali kali jali dim bor pira pari dim

