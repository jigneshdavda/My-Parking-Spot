from django.db import models

# Create your models here.

class Slot_status(models.Model):
	# Model represents the status of the individual slot

	slot_id = models.CharField(max_length=5, help_text="Enter the Parking slot id (eg. s_01, s_02, etc.)")

	status = models.BinaryField(max_length=1, help_text="1 for slot available and 0 for not availabel or blocked or reserved")

	def get_absolute_url(self):
		# Returns the url to access a detail record for this slot
		return reverse('slot_status', args=[str(self.id)])