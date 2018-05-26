from django.db import models

# Create your models here.
class Mod(models.Model):
    title = models.CharField(max_length=264)
    body = models.TextField()

    def __str__(self):
        return self.title

# class Webpage(models.Model):
#     mod = models.ForeignKey(Mod,on_delete=models.CASCADE)
#     name = models.CharField(max_length=264,unique=True)
#     url = models.URLField(unique=True)
#
#     def __str__(self):
#         return self.name
#
# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
#     date = models.DateField()
#
#     def __str__(self):
#         return str(self.date)
