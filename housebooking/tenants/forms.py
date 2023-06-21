from django.contrib.auth.forms import UserCreationForm
from home.models import User
from .models import Tenant
from django.db import transaction
from django import forms

ID_CHOICES = [
    ('NIN', 'NIN'),
    ('VIN', "Voter's Card Num"),
]

class UserCreateForm(UserCreationForm):

    identification = forms.CharField(required=True,
                                     label='choose ID',
                                     widget=forms.Select(choices=ID_CHOICES)
    )

    id_number = forms.CharField(required=True, max_length=11)
    DOB = forms.DateField(required=True,
                          widget=forms.DateInput
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name',
              'last_name',
              'email',
              'username',
        ]
        exclude = ['password', 'password']



        @transaction.atomic
        def save(self):
            user = super().save(commit=False) # type: ignore
            user.is_tenant = True
            user.save()
            tenant = Tenant.objects.create(user=user)
            tenant.DOB.add(*self.cleaned_data.get('DOB')) # type: ignore
            tenant.identification.add(*self.cleaned_data.get('identification')) # type: ignore
            tenant.id_number.add(*self.cleaned_data.get('id_number')) # type: ignore
            return user