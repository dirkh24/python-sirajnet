from django import forms

from .models import hilbert_model

class HilbertForm(forms.ModelForm):
    class Meta:
        model = hilbert_model
        fields = ['your_text', 'swap_rate']
        labels = {'your_text': '',
                  'swap_rate' : 'Swap Rate (default: 1)'}
        widgets = {'your_text': forms.Textarea(attrs={'cols': 80})}
