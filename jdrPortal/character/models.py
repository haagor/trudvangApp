from django.db import models


class Traits(models.Model):
	charisma = models.IntegerField(default=0)
	constitution = models.IntegerField(default=0)
	dexterity = models.IntegerField(default=0)
	intelligence = models.IntegerField(default=0)
	perception = models.IntegerField(default=0)
	psyche = models.IntegerField(default=0)
	strength = models.IntegerField(default=0)

	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Traits._meta.fields]

class Character(models.Model):
	name = models.CharField(max_length=200)
	traits = models.ForeignKey(Traits, on_delete=models.CASCADE, blank=True, null=True)