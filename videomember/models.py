from django.db import models

# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length = 255)
	image = models.FileField()
	description = models.TextField()
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

class Content(models.Model):
	STATUS = (
		('active', 'active'),
		('inactive', 'inactive'),
		)
	lesson = models.CharField(max_length = 255)
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	status = models.CharField(max_length = 25, choices = STATUS)

	def __str__(self):
		return f"{self.lesson} -- {self.course}"