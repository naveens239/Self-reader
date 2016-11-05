from django.db import models

# Create your models here.
class Passage(models.Model):
    passage_name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    passage = models.TextField(blank=False,null=False)
    words = models.IntegerField(blank=False,null=False)
    #time_taken = models.IntegerField(blank=False, null=False)
    #speed = models.IntegerField(blank=False, null=False)
    def __unicode__(self):
        return str(self.id)
class Subject(models.Model):
    subject_name =  models.CharField(max_length=150, blank=False, null=False, unique=False)
    passage_read = models.ForeignKey('Passage',unique=False)
    time_per_word = models.TextField(blank=False,null=False)

    def __unicode__(self):
        return str(self.subject_name)
