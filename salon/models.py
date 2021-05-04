from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        #return '<Staff:id=' + str(self.id) + ', ' + self.name + '>'

class Contact(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_kana = models.CharField(max_length=30)
    first_kana = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=30)
    ctgry_data = (
        ('reservation', '予約'),
        ('consultation', '相談'),
        ('other', 'その他'),
    )
    ctgry = models.CharField(max_length=30, choices=ctgry_data)
    pcharge = models.ForeignKey(Staff, blank=True, on_delete=models.CASCADE)
    inquiry = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Contact:id=' + str(self.id) + ', ' + self.last_name + self.first_name + '(' + str(self.pub_date) + ')>'
    
    class Meta:
        ordering = ('pub_date',)

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