
from django.db import models
from django.utils import timezone

class Categorystay(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


   
class Sittersform(models.Model):
    s_name = models.CharField(max_length=200,)
    age = models.CharField(max_length=200, default=0)
    contact = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=200)
    level_of_education = models.CharField(max_length=50)
    nin = models.CharField(max_length=200)
    date_of_birth = models.DateField(max_length=200, default=0)

    def __str__(self):
        return self.s_name

class Sarrival(models.Model):
    s_names = models.ForeignKey(Sittersform,on_delete=models.CASCADE)
    timein = models.TimeField(default=timezone.now)
    sittersno = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now) 

    def __str__(self):
        return self.s_names

  

class Spayment(models.Model):
    name = models.CharField(max_length=100, null= True, blank= False)
    amount = models.DecimalField(max_digits=10, decimal_places=0, default=3000)
    date = models.DateField(default=timezone.now)
    numbers_of_babies_attended_to = models.IntegerField(default=0)

    def __str__(self):
        return str(self.amount)

    @property
    def total_amount_paid(self):
        # print("Amount:", self.amount)
        # print("Number of Babies Attended To:", self.numbers_of_babies_attended_to)
        return self.amount * self.numbers_of_babies_attended_to
    

class Babesform(models.Model):
    # c_stay = models.ForeignKey(Categorystay,on_delete=models.CASCADE,max_length=200)
    c_stay=models.CharField(max_length=200)
    b_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200, default=0)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=50, null=True, default=None)
    sponsor = models.CharField(max_length=200)
    parentsname = models.CharField(max_length=200)
    babysno = models.CharField(max_length=200, default=0)
    timein = models.DateTimeField()
    brought_by = models.CharField(max_length=200)
    # Assigning_babies = models.ForeignKey(Sitterslist,on_delete=models.CASCADE)

    def __str__(self):
        return self.b_name

class B_departure(models.Model):
    b_names = models.ForeignKey(Babesform,on_delete=models.CASCADE)
    person_taking_baby = models.CharField(max_length=200)
    telephone_no = models.CharField(max_length=200)
    timeout = models.DateTimeField()
    babyno = models.IntegerField(default=0)
    comments = models.TextField(max_length=500)

    def __str__(self):
        return self.b_names
class Bpayment(models.Model):
    c_payment_id = models.ForeignKey(Categorystay, on_delete=models.CASCADE, max_length=200)
    Payno = models.IntegerField(default=0)
    currency = models.IntegerField(default=0, choices=[(10000, '10000'), (15000, '15000'), (300000, '300000'), (450000, '450000')])
    amount_paid = models.IntegerField(default=0)
    payee=models.ForeignKey(Babesform,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.payee

    def get_balance(self):
        return self.currency - self.amount_paid

        


class Category_doll(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name      

class Doll(models.Model):
    c_doll = models.ForeignKey(Category_doll, on_delete=models.CASCADE, null=True, blank=True)
    name_of_the_doll = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    issued_quantity = models.IntegerField(default=0, blank=True, null=True) 
    received_quantity = models.IntegerField(default=0, null=True, blank=True)
    Unit_price = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def _str_(self):
        return self.name_of_the_doll

class Salesrecord(models.Model):    
    doll = models.ForeignKey(Doll, on_delete=models.CASCADE, null=False, blank=False)
    payee = models.ForeignKey(Babesform, on_delete=models.CASCADE, null=False, blank=False)
    quantity_sold = models.IntegerField(default=0)
    amount_received = models.IntegerField(default=0)
    sale_date = models.DateField(default=timezone.now)
    unit_price = models.IntegerField(default=0)
        
    def get_total(self):
        total = self.quantity_sold * self.unit_price
        return int(total)

    def get_change(self):
        change = self.get_total() - self.amount_received
        return int(change)
      

class Shopform(models.Model):
    item_name = models.CharField(max_length=100, choices=( 
        ('Fruits', 'Fruits'),
        ('Diapers', 'Diapers'),
        ('Milk', 'Milk'),
        ('Toys', 'Toys')))
    quantity = models.IntegerField(default=0, null=True, blank=True)
    quantity_received = models.IntegerField(default=0, null=True, blank=True)
    Total_amount = models.IntegerField(default=0, null=True, blank=True)
    Date_of_purchase = models.DateField(default=timezone.now())
    quantity_issued_out = models.IntegerField(default=0, null=True, blank=True)
    stock_at_hand = models.IntegerField(default=0, null=True, blank=True)
    
def total_quantity(self):
    total = self.quantity + self.quantity_received
    return total


    def _str_(self):
        return self.item_name