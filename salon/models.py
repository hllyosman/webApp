from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '<Staff:id=' + str(self.id) + ', ' + self.name + '>'

'''
class Enq(model.Model):
    pass

class Menu(models.Model):
    cut_ippan = models.IntegerField(default=0)
    cut_gakusei = models.IntegerField(default=0)
    cut_front = models.IntegerField(default=0)

    color_retouch = models.IntegerField(default=0)
    color_full = models.IntegerField(default=0)
    color_uruoi = models.IntegerField(default=0)
    color_dr = models.IntegerField(default=0)
    color_point = models.IntegerField(default=0)
    color_hena = models.IntegerField(default=0)
    color_breach = models.IntegerField(default=0)
    color_tech = models.IntegerField(default=0)
    color_irumina = models.IntegerField(default=0)

    perm_perm = models.IntegerField(default=0)
    perm_uruoi = models.IntegerField(default=0)
    perm_dr = models.IntegerField(default=0)
    perm_digital = models.IntegerField(default=0)
    perm_perm = models.IntegerField(default=0)
    
    perm_perm = models.IntegerField(default=0)
'''