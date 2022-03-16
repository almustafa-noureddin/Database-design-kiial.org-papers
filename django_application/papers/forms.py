from django import forms
from papers.models import Paper, Researcher, Supervisor


class PaperModelForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = (
            'title',
            'researcher',
            'supervisor',
            'degree',
            'date_of_publishing',
            'paper_number',
        )


class ResearcherModelForm(forms.ModelForm):
    class Meta:
        model = Researcher
        fields = (
            'first_name',
            'second_name',
            'third_name',
            'fourth_name',
            'alternative_name',
            'title',
        )


class SupervisorModelForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = (
            'first_name',
            'second_name',
            'third_name',
            'fourth_name',
            'alternative_name',
            'title',
        )






#from django import forms
#
#class SearchForm(forms.ModelForm):
#    name = forms.CharField(max_length=200, required=True,
#		    widget=forms.TextInput(attrs={
#			'placeholder': '*search',
#			'class': 'form-control'
#			}))