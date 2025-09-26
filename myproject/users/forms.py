# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:48:28 2025

@author: iyaku
"""

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınızı giriniz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta adresiniz'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 120}),
        }