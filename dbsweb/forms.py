from django import forms

from dbsweb.models import diseaseTypeModel
from dbsweb.models import countryModel
from dbsweb.models import diseaseModel
from dbsweb.models import discoverModel
from dbsweb.models import usersModel
from dbsweb.models import publicservantModel
from dbsweb.models import doctorModel
from dbsweb.models import specializeModel
from dbsweb.models import recordModel


class diseaseTypeForms(forms.ModelForm) :
    class Meta:
        model = diseaseTypeModel
        fields="__all__"

class countryForms(forms.ModelForm) :
    class Meta:
        model = countryModel
        fields="__all__"

class diseaseForms(forms.ModelForm) :
    class Meta:
        model = diseaseModel
        fields="__all__"

class discoverForms(forms.ModelForm) :
    class Meta:
        model = discoverModel
        fields="__all__"

class usersForms(forms.ModelForm) :
    class Meta:
        model = usersModel
        fields="__all__"      

class publicservantForms(forms.ModelForm) :
    class Meta:
        model = publicservantModel
        fields="__all__"

class doctorForms(forms.ModelForm) :
    class Meta:
        model = doctorModel
        fields="__all__"       

class specializeForms(forms.ModelForm) :
    class Meta:
        model = specializeModel
        fields="__all__"    

class recordForms(forms.ModelForm) :
    class Meta:
        model = recordModel
        fields="__all__"   