from django.forms import ModelForm
from .models import *
from django import forms


class AddBabe(ModelForm):
    class Meta:
        model = Babesform
        fields = '__all__'
        widgets = {
            'timein': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class AddSitter(ModelForm):
    class Meta:
        model = Sittersform
        fields = '__all__'

class AddBdeparture(ModelForm):
    class Meta:
        model = B_departure
        fields = '__all__'
        widgets = {
            'timeout': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AddBpayment(ModelForm):
    class Meta:
        model = Bpayment
        fields = '__all__'

        

class AddSpayment(ModelForm):
    class Meta:
        model = Spayment
        fields = '__all__'
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['amount'].disabled = True
   

class AddSarrival(ModelForm):
     class Meta:
        model = Sarrival
        fields = '__all__'

class  DollForm(ModelForm):
     class Meta:
        model = Doll
        fields = '__all__'

class Addform(ModelForm):
     class Meta:
        model = Doll
        fields = ['received_quantity']

class SalesrecordForm(ModelForm):
     class Meta:
        model= Salesrecord
        fields = ['quantity_sold', 'amount_received', 'payee']  



class  AddShop(ModelForm):
     class Meta:
        model = Shopform
        fields = '__all__'

        from django import forms



class SitterSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)


class BabySearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)



