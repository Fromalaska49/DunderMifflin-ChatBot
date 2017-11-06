from django.db import models

#This is the section where database tables are defined in the form of class definitions (where ORM starts)


#sample definitions (not used, will be removed once real development begins)

#Django will handle the autoincrementing IDs

#class Notification(models.Model):
#   title = models.CharField(max_length=64)
#   play_count = models.IntegerField(default=0)
#   director = models.ForeignKey(Director)         #sample foreign key relationship


#class Director(models.Model):
#   first_name = models.CharField(max_length=64)
#   last_name = models.CharField(max_length=64)
