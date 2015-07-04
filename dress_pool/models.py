from django.db import models

# Create your models here.
class SkirtType(models.Model):
	skirtTypeName = models.CharField('裙子類型' ,max_length=200)
	
	def __str__(self):
		return self.skirtTypeName

	class Meta:
		verbose_name = '裙子類型'
		verbose_name_plural = '裙子類型'
    
class DressType(models.Model):
	dressTypeName = models.CharField('禮服類型' ,max_length=200)
	
	def __str__(self):
		return self.dressTypeName

	class Meta:
		verbose_name = '禮服類型'
		verbose_name_plural = '禮服類型'

class Purpose(models.Model):
	purposeName = models.CharField('用途', max_length=200)

	def __str__(self):
		return self.purposeName

	class Meta:
		verbose_name = '用途'
		verbose_name_plural = '用途'


class Dress(models.Model):
	number = models.CharField('編號 ', max_length=200)
	rent = models.IntegerField('租金 ', default=0)
	additional = models.IntegerField('禮服加價', default=0)
	dressType = models.ForeignKey(DressType, verbose_name='禮服類型')
	skirtType = models.ForeignKey(SkirtType, verbose_name='裙子類型')
	purpose = models.ForeignKey(Purpose, verbose_name='用途')
	vendor = models.CharField('廠商 ', max_length=200)
	amount = models.IntegerField('總價 ', default=0)
	color = models.CharField('顏色 ', max_length=200)
	image = models.ImageField('禮服照片 ', upload_to='pic')

	def image_tag(self):
		return u'<img src="%s" width="300px" />' % self.image.url
	image_tag.short_description = "預覽 "
	image_tag.allow_tags = True

	def __str__(self):
		return self.number

	class Meta:
		verbose_name = '禮服'
		verbose_name_plural = '禮服'


class RentRecord(models.Model):
	dress = models.ForeignKey(Dress, verbose_name='禮服')
	rentDate = models.DateField('租借時間')

	class Meta:
		verbose_name = '租借記錄'
		verbose_name_plural = '租借記錄'

	def __str__(self):
		return u'%s    %s' % (str(self.rentDate), str(self.dress))
