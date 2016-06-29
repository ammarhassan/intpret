from django.db import models

# Create your models here.




class QueriesStore(models.Model):
	query = models.TextField(help_text='Query string')
	group = models.IntegerField(help_text='group identifier', null=True, blank=True)

	def __unicode__(self):
		return self.query