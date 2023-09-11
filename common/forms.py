from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, NormalUser

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'agree']

class NormalUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = NormalUser
        fields = ['age', 'sex', 'weight', 'height', 'activity_level', 'goal', 'dietary_restrictions']

    SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    ACTIVITY_LEVEL_CHOICES = [
        ('S', 'Sedentary (little or no exercise)'),
        ('LA', 'Lightly active (light exercise/sports 1-3 days/week)'),
        ('MA', 'Moderately active (moderate exercise/sports 3-5 days/week)'),
        ('VA', 'Very active (hard exercise/sports 6-7 days a week)'),
        ('EA', 'Extra active (very hard exercise/sports, physical job, or training twice a day)'),
    ]
    GOAL_CHOICES = [('L', 'Lose Weight'), ('M', 'Maintain Weight'), ('G', 'Gain Weight')]
    DIETARY_RESTRICTIONS_CHOICES = [
        ('V', 'Vegetarian'),
        ('VG', 'Vegan'),
        ('GF', 'Gluten-free'),
        ('DF', 'Dairy-free'),
        ('NF', 'Nut-free'),
        ('SF', 'Shellfish-free'),
        ('EF', 'Egg-free'),
    ]

    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=False,
        error_messages={'required': 'Please select your gender.'}
    )
    age = forms.IntegerField(
        min_value=18,
        max_value=100,
        required=False,
        help_text='Must be at least 18 years old.',
        error_messages={'invalid': 'Please enter a valid age.', 'min_value': 'You must be at least 18 years old.'}
    )
    weight = forms.DecimalField(
        min_value=20,
        max_value=500,
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 68.5'}),
        error_messages={'invalid': 'Please enter a valid weight.', 'min_value': 'Weight must be at least 20 kg.'}
    )
    height = forms.DecimalField(
        min_value=50,
        max_value=300,
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 175'}),
        error_messages={'invalid': 'Please enter a valid height.', 'min_value': 'Height must be at least 50 cm.'}
    )
    activity_level = forms.ChoiceField(
        choices=ACTIVITY_LEVEL_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=False,
        error_messages={'required': 'Please select your activity level.'}
    )
    goal = forms.ChoiceField(
        choices=GOAL_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=False,
        error_messages={'required': 'Please select your fitness goal.'}
    )
    dietary_restrictions = forms.MultipleChoiceField(
        choices=DIETARY_RESTRICTIONS_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        weight = cleaned_data.get('weight')
        height = cleaned_data.get('height')
        activity_level = cleaned_data.get('activity_level')

        if age and age < 18:
            self.add_error('age', 'You must be at least 18 years old.')

        if weight and weight < 20:
            self.add_error('weight', 'Weight must be at least 20 kg.')

        if height and height < 50:
            self.add_error('height', 'Height must be at least 50 cm.')

        if not activity_level:
            self.add_error('activity_level', 'Please select your activity level.')
