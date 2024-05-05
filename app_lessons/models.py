from django.db import models


class Subjects(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'Subjects'

    def __str__(self):
        return self.name


class Lessons(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    topic = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    article = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'Lessons'
