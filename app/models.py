from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()
MODEL_CHOICES = (
    ('monster_trucks', 'MONSTER TRUCKS'),
    ('on_road_cars', 'ON ROAD CARS'),
    ('short_course_trucks', 'SHORT COURSE TRUCKS'),
    ('stadium_trucks', 'STADIUM TRUCKS'),
)


class Traxxas(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=MODEL_CHOICES, default='monster_trucks')
    image = models.ImageField(upload_to='pics',)
    description = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)






