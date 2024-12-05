from django import forms
from .models import Property, Community, House, Owner

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'description']

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'property']

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['room_number', 'area']

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'phone'] 