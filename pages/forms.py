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
	OPTIONS = (("E", "E"),("I", "I"),)
	extraversion_field = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, label='Extraversion/Introversion')

class IntuitionField(forms.Form):
	OPTIONS = (("S", "S"),("N", "N"),)
	intuition_field = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, label='Sensing/Intuition')

class FeelingField(forms.Form):
	OPTIONS = (("T", "T"),("F", "F"),)
	feeling_field = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, label='Thinking/Feeling')

class PerceptionField(forms.Form):
	OPTIONS = (("J", "J"),("P", "P"),)
	perception_field = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS, label='Judging/Perceiving')
