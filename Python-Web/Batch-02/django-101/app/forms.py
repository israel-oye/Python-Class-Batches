from decimal import Decimal

from django import forms
from django.core.validators import MinLengthValidator

GENRE_CHOICES = [
    ("g1", "Drama"),
    ("g2", "Prose"),
    ("g3", "Poetry"),
]


def must_start_with_a(value: str):
    if not value.lower().startswith('a'):
        raise forms.ValidationError("Author name start with 'a'")

class BookForm(forms.Form):
    title = forms.CharField(
        label='Title',
        validators=[MinLengthValidator(3, "Must be 3 or more characters")],
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    author = forms.CharField(validators=[must_start_with_a])
    price = forms.DecimalField(decimal_places=2, initial=Decimal('0.00'), required=False)
    is_available = forms.BooleanField(required=False)
    genre = forms.ChoiceField(choices=GENRE_CHOICES, initial='g2')
