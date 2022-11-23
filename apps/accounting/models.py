from django.db import models

class Payment(models.Model):
	PAYMENTTYPES = (
		("click","click"),
		("naqd","naqd"),
		("plastik","plastik"),
		)
	student = models.ForeignKey('user.Student',on_delete = models.CASCADE)
	group = models.ForeignKey('course.Group',on_delete = models.SET_NULL,null = True)
	summ = models.PositiveIntegerField()
	date = models.DateField(auto_now_add = True)
	description = models.TextField()
	payment_type = models.CharField(max_length = 8,choices = PAYMENTTYPES)

