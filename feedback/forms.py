from django import forms
from .models import EnrollmentRequest

class EnrollmentRequestForm(forms.ModelForm):
    class Meta:
        model = EnrollmentRequest
        fields = [
            'child_full_name',
            'child_date_of_birth',
            'program',
            'parent_full_name',
            'parent_contact_phone',
            'parent_contact_email',
            'pfdo_certificate_number',
            'school',
            'grade',
            'school_shift',
            'message',
        ]
        widgets = {
            'child_date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
