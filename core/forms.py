from django import forms
from .models import QuizAttempt

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizAttempt
        fields = ['user_name', 'answer_1', 'answer_2', 'answer_3']
        # --- NEW LABELS & PLACEHOLDERS ---
        labels = {
            'user_name': 'Your Name / Nickname:',
            'answer_1': 'Q1 (Midpoint 2D): Find the midpoint of A(3, 9) and B(7, 1). (Answer: x, y)',
            'answer_2': 'Q2 (Distance 2D): What is the distance between P(0, -4) and Q(3, 0)? (Answer: a single number)',
            'answer_3': 'Q3 (Distance Squared 3D): Find the SQUARE of the distance between R(1, 2, 3) and S(4, 2, 0). (Answer: a single number)',
        }
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'answer_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5, 5'}),
            'answer_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5'}),
            'answer_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 18'}),
        }