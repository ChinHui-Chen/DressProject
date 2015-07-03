from django.db import models

# Create your models here.
class SkirtType(models.Model):
	skirtTypeName = models.CharField(max_length=200)
	def __unicode__(self):
		return self.skirtTypeName
    
class DressType(models.Model):
	dressTypeName = models.CharField(max_length=200)
	def __unicode__(self):
		return self.dressTypeName

class Purpose(models.Model):
	purposeName = models.CharField(max_length=200)
	def __unicode__(self):
		return self.purposeName

class Dress(models.Model):
	skirtType = models.ForeignKey(SkirtType)
	dressType = models.ForeignKey(DressType)
	purpose = models.ForeignKey(Purpose)
	vendor = models.CharField(max_length=200)
	amount = models.IntegerField(default=0)
	rent = models.IntegerField(default=0)
	additional = models.IntegerField(default=0)
	color = models.CharField(max_length=200)
	number = models.CharField(max_length=200)
	image = models.ImageField(upload_to='pic')

	def __unicode__(self):
		return self.number

class RentRecord(models.Model):
	dress = models.ForeignKey(Dress)
	rentDate = models.DateField('date rent')
