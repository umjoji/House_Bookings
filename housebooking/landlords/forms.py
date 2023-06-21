from django.contrib.auth.forms import UserCreationForm
from home.models import User
from .models import LandLord
from django.db import transaction
from django import forms

ID_CHOICES = [
    ('NIN', 'NIN'),
    ('VIN', "Voter's Card Num"),
]

OPTIONS = (
    ('yes', 'YES'),
    ('no', 'NO'),
)


class UserCreateForm(UserCreationForm):

    identification = forms.CharField(required=True,
                                     label='choose ID',
                                     widget=forms.Select(choices=ID_CHOICES)
    )

    id_number = forms.CharField(required=True, max_length=11)
    DOB = forms.DateField(required=True,
                          widget=forms.DateInput
    )
    # evidence_of_ownership = forms.FileField()
    # # do_you_own_the_home = forms.CharField(required=True,
    #                                  widget=forms.Select(choices=OPTIONS)
    # )
    phone_number = forms.CharField(required=True, max_length=11)

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
        user.is_landlord = True
        user.save()
        landlord = LandLord.objects.create(landlord=user,
                                           DOB=self.cleaned_data.get('DOB'),
                                           id_number=self.cleaned_data['id_number'],
                                           identification=self.cleaned_data['identification'],
                                           phone_number=self.cleaned_data['phone_number'],
                                        #    do_you_own_the_house=self.cleaned_data('do_you_own_the_house')
        )
        # landlord.DOB.add(*self.cleaned_data.get('DOB')) # type: ignore
        # landlord.identification.add(*self.cleaned_data.get('identification')) # type: ignore
        # landlord.id_number.add(*self.cleaned_data.get('id_number')) # type: ignore
        # landlord.evidence_of_ownership.add(*self.cleaned_data.get('evidence_of_ownership')) # type: ignore
        landlord.do_you_own_the_home = self.cleaned_data.get('do_you_own_the_home') # type: ignore
        return user