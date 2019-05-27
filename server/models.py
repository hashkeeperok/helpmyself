from django.db import models
from .models import User

class Category(models.Model)
	name = models.CharFiled(max_length=50)
	description = models.CharFiled(max_length=50)

	def __unicode__(self):
        return unicode(self.name)
 
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Compaign(models.Model)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL)
	name = models.CharFiled(max_length=50)
	description = models.CharFiled(max_length=50)
	main_image = models.ImageField(upload_to='cars')
	goal = models.IntegerField()
	Total = models.IntegerField()
	created_date = models.DateField()

		def __unicode__(self):
        return unicode(self.name)
 
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class DonationType(models.Model)
	name = models.CharFiled(max_length=50)
	Amount = models.IntegerField()

	def __unicode__(self):
        return unicode(self.name)
 
    class Meta:
        verbose_name = 'Тип взноса'
        verbose_name_plural = 'Типы взносов'

class Donation(models.Model)
	compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	donation_type = models.ForeignKey(DonationType, default=None)

	def __unicode__(self):
        return unicode(self.name)
 
    class Meta:
        verbose_name = 'Взнос'
        verbose_name_plural = 'Взносы'
