from django import forms
from .models import SupporterFeedback

class SupporterFeedbackForm(forms.ModelForm):
    class Meta:
        model = SupporterFeedback
        fields = ['supporter_name', 'gift', 'comment', 'proof_image']
        widgets = {
            'supporter_name': forms.TextInput(attrs={
                'class': 'form-control w-100 py-2 px-3 rounded-3',
                'placeholder': 'Enter your name (e.g. Jerin)'
            }),
            'gift': forms.Select(attrs={
                'class': 'form-select w-100 py-2 px-3 rounded-3'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control w-100 p-3 rounded-3',
                'rows': 4,
                'placeholder': 'Write your thoughts or feedback here...'
            }),
            'proof_image': forms.FileInput(attrs={
                'class': 'form-control w-100 py-2 px-3 rounded-3'
            }),
        }