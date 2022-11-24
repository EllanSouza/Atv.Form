from django import forms
from painel.models import Estudante


class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields= '__all__'   

        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.TimeInput(attrs={'type': 'date'}),
        }