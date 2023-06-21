from django import forms
from .models import HouseImages, House, Amenity
from multiupload.fields import MultiImageField

class HouseRegistration(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            'name', 'address', 'state_id', 'city_id', 'amenities',
            'number_of_beds', 'number_of_bath', 'pet_allowed', 'smoking_allowed', 'description'
                  ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 20})
        }

class ImageUpload(forms.ModelForm):
    upload_pictures = MultiImageField(min_num=1, max_num=4, max_file_size=1024*1024*5)

    class Meta:
        model = HouseImages
        fields = ['upload_pictures']

class AddAmenity(forms.ModelForm):
    model = Amenity
    fields = ['name'] # type: ignore
