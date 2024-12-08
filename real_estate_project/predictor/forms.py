from django import forms

class PredictForm(forms.Form):
    CRIM = forms.FloatField(label="CRIM")
    ZN = forms.FloatField(label="ZN")
    INDUS = forms.FloatField(label="INDUS")
    CHAS = forms.IntegerField(label="CHAS")  # Binary input (0 or 1)
    NOX = forms.FloatField(label="NOX")
    RM = forms.FloatField(label="RM")
    AGE = forms.FloatField(label="AGE")
    DIS = forms.FloatField(label="DIS")
    RAD = forms.FloatField(label="RAD")
    TAX = forms.FloatField(label="TAX")
    PTRATIO = forms.FloatField(label="PTRATIO")
    B = forms.FloatField(label="B")
    LSTAT = forms.FloatField(label="LSTAT")
