from django import forms

from .models import User, Vacation


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='E-MAIL')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'position']


class VacationUpdateForm(forms.ModelForm):
    # vacation_days = forms.IntegerField(label='Количество дней отпуска')
    vacation_date_start = forms.DateField(
        label='Начало отпуска',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )
    vacation_date_end = forms.DateField(c
            label='Конец отпуска',
            widget=forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        )

    class Meta:
        model = Vacation
        fields = ['vacation_date_start', 'vacation_date_end']

    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('vacation_date_end') < self.cleaned_data.get('vacation_date_start'):
            raise forms.ValidationError('Дата окончания отпуска должна быть больше даты начала')
        return self.cleaned_data
