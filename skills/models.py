from django.db import models

# Create your models here.

class Skill(models.Model):
    TRACK_CHOICES = [
        ('DS', 'Data Science'),
        ('DA', 'Data Analysis'),
        ('FE', 'FrontEnd'),
        ('BE', 'BackEnd'),
    ]

    track = models.CharField(
        max_length=30,
        choices=TRACK_CHOICES,
        default='DS',
        verbose_name='Track'
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_track_display()})"
    



class UserInput(models.Model):
    TRACK_CHOICES = [
        ('DS', 'Data Science'),
        ('DA', 'Data Analysis'),
        ('FE', 'FrontEnd'),
        ('BE', 'BackEnd'),
    ]

    track = models.CharField(
        max_length=100,
        choices=TRACK_CHOICES,
        default='DS',
        verbose_name='Chosen Track'
    )
    description = models.TextField()  

    def __str__(self):
        return f"User Input for {self.get_track_display()}"
    