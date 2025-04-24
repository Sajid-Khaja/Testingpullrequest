from django import forms
from .models import Operation

class formOperation(forms.ModelForm):  # Inherit from ModelForm
    class Meta:
        model = Operation
        fields = '__all__'  # Or specify fields: fields = ['field1', 'field2', ...]
        # exclude = ['field_to_exclude'] #Exclude some fields

#If you don't want to use ModelForm, then you have to define the fields manually
class formOperationManual(forms.Form):
    name = forms.CharField(max_length=255) #Example
    #Add all fields from the model here