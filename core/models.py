from django.db import models


class Expense(models.Model):
    name = models.CharField(u'Name', max_length=255, null=True, blank=True)
    description = models.CharField(u'Description', max_length=255, null=True, blank=True)
    amount = models.DecimalField(
        u"Amount",
        max_digits=9,
        decimal_places=2,
        default=00.00
    )
    updated_at = models.DateTimeField(u'Update Date', auto_now_add=True)

    def __unicode__(self):
        return "{0}".format(self.user)
