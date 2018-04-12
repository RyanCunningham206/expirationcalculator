from django.db import models

# Create your models here.
class Text_box(models.Model):
    weeks = models.CharField('Weeks', max_length=10)

    def get_id(self):
        return self.id

    def get_weeks(self):
        return self.weeks
