from django.db import models
import datetime

class Student(models.Model):
		firstname = models.CharField(max_length = 20)
		lastname = models.CharField(max_length = 20)
		email = models.CharField(max_length = 30)
		image = models.CharField(max_length = 30)
		lab = models.CharField(max_length = 50)
		labwebsite = models.CharField(max_length = 100)

		def __unicode__(self):
				return self.firstname + " " + self.lastname

class Theme(models.Model):
		theme = models.CharField(max_length = 3)
		fulltheme = models.CharField(max_length = 30)

		def __unicode__(self):
				return self.fulltheme

class Faculty(models.Model):
		firstname = models.CharField(max_length = 20)
		lastname = models.CharField(max_length = 20)
		degree = models.CharField(max_length = 20)
		website = models.CharField(max_length = 100)
		title = models.CharField(max_length = 20)
		department = models.CharField(max_length = 50)
		email = models.CharField(max_length = 30)
		blurb = models.CharField(max_length = 4000)
		tagline = models.CharField(max_length = 100)
		themes = models.ManyToManyField(Theme)

		def __unicode__(self):
				return self.firstname + " " + self.lastname

class Alumnus(models.Model):
		firstname = models.CharField(max_length = 20)
		lastname = models.CharField(max_length = 20)
		advisor = models.CharField(max_length = 40)
		currentpos = models.CharField(max_length = 250)
		links = models.CharField(max_length = 250)

		def __unicode__(self):
				return self.firstname + " " + self.lastname

class Course(models.Model):
		QUARTER_CHOICES = (
						(1,'Autumn'),
						(2,'Winter'),
						(3,'Spring'),
						(4,'Summer'),
						)
		CONCENTRATION_CHOICES = (
						(1,'Cellular/Molecular/Developmental'),
						(2,'Translational'),
						(3,'Systems/Behavioral/Computational'),
						)
		YEAR_CHOICES = (
						(0,'This Year'),
						(1,'Both this and next year'),
						(2,'Next Year')
						)
		department = models.CharField(max_length=10)
		number = models.CharField(max_length=4)
		title = models.CharField(max_length=80)
		concentration = models.IntegerField(choices = CONCENTRATION_CHOICES)
		quarter = models.IntegerField(choices = QUARTER_CHOICES)
		schoolyear = models.IntegerField(choices = YEAR_CHOICES)
		professors = models.CharField(max_length=50)
		description = models.CharField(max_length=2000)
		
		def __unicode__(self):
				return self.department + " " + self.number
		
		def get_year(self):
				year = datetime.datetime.now().year
				month = datetime.datetime.now().month
				if month < 9:
						if self.schoolyear <= 1:
								return str(year-1) + "-" + str(year)
						else:
								return str(year) + "-" + str(year+1)
				else:
						if schoolyear <= 1:
								return str(year) + "-" + str(year+1)
						else:
								return str(year+1) + "-" + str(year+2)

		def get_quarter(self):
				if self.quarter == 1:
						return "Autumn"
				elif self.quarter == 2:
						return "Winter"
				elif self.quarter == 3:
						return "Spring"
				elif self.quarter == 4:
						return "Summer"

		def get_concentration(self):
				if self.concentration == 1:
						return "Cellular/Molecular/Developmental"
				elif self.concentration == 2:
						return "Translational"
				elif self.concentration == 3:
						return "Systems/Behavioral/Computational"

class FAQ(models.Model):
		question = models.TextField()
		answer = models.TextField()

		def __unicode__(self):
				return self.question
