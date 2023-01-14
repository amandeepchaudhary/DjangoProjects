from django import forms
from core.models import Visitor


class VisitorInfo(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['visitor_name', 'email', 'subject', 'message']
