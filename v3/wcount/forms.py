from django import forms

class MyColleagues(forms.Form):
      first_name=forms.CharField(max_length = 200 )
      last_name=forms.CharField(max_length = 200 )
      roll_number=forms.IntegerField( help_text = "Digits only" )
      password=forms.CharField( widget = forms.PasswordInput() )


