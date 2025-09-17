 
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import Book
# from .models import User


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'status', 'rating', 'review']
#         labels = {
#             'rating': 'Rating (1-5)',
#             'review': 'Your Review (optional)'
#         }

# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)  # Add email field

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user