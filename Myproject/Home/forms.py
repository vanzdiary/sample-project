from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type='date'
class BookingForms(forms.ModelForm):
    class  Meta:
        model=Booking
        fields='__all__'
        widgets={
            'bookingdate':DateInput()
        }
        label={
            'p_name':"patient name",
            'p_phone':"patient phone",
            'p_email':"patient email",
            'doc_name':"doctor name",
            'bookingdate':"booking date",
        }