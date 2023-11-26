from django.db import models

# Create your models here.

class note(models.Model):
    noteId = models.BigAutoField(primary_key=True)
    noteTitle = models.CharField(max_length=100)
    noteText = models.TextField()

    def __str__(self):
        return self.noteTitle
    