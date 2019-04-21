from django import forms

# from django.forms import ModelForm
# from .models import TwitterUser, TextBox

# class TextInputField(ModelForm):
# 	text = forms.CharField(widget=forms.Textarea, label='')
# 	class Meta:
# 		model = TextBox
# 		fields = ['text']

# class TwitterHandleField(forms.ModelForm):
# 	twitter_handle = forms.CharField(label='')
# 	class Meta:
# 		model = TwitterUser
# 		fields = ['twitter_handle']

class TextInputField(forms.Form):
	text_field = forms.CharField(widget=forms.Textarea, label='', required=None)

class TwitterHandleField(forms.Form):
	twitter_handle = forms.CharField(label='', required=None)

class ExtraversionField(forms.Form):
	extraversion_field = forms.CharField(label='', required=None)

class IntuitionField(forms.Form):
	intuition_field = forms.CharField(label='', required=None)

class FeelingField(forms.Form):
	feeling_field = forms.CharField(label='', required=None)

class PerceptionField(forms.Form):
	perception_field = forms.CharField(label='', required=None)
