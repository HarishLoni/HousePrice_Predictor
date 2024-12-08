from django.shortcuts import render
from .forms import PredictForm
from joblib import load 
import numpy as np 

def predict(request):
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            model = load('predictor/ml_model/Dragon.joblib')

            features = np.array([[form.cleaned_data['CRIM'],
                                  form.cleaned_data['ZN'],
                                  form.cleaned_data['INDUS'],
                                  form.cleaned_data['CHAS'],
                                  form.cleaned_data['NOX'],
                                  form.cleaned_data['RM'],
                                  form.cleaned_data['AGE'],
                                  form.cleaned_data['DIS'],
                                  form.cleaned_data['RAD'],
                                  form.cleaned_data['TAX'],
                                  form.cleaned_data['PTRATIO'],
                                  form.cleaned_data['B'],
                                  form.cleaned_data['LSTAT']]])

            prediction = model.predict(features)[0]
            return render(request, 'result.html', {'prediction': prediction})

    else:
        form = PredictForm()

    return render(request, 'predict.html', {'form': form})
