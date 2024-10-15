from django import forms

class PredictionForm(forms.Form):
    is_tv_subscriber = forms.BooleanField(required=False)
    is_movie_package_subscriber = forms.BooleanField(required=False)
    subscription_age = forms.IntegerField(required=True)
    bill_avg = forms.FloatField(required=True)
    remaining_contract = forms.IntegerField(required=True)
    service_failure_count = forms.IntegerField(required=True)
    download_avg = forms.FloatField(required=True)
    upload_avg = forms.FloatField(required=True)
    download_over_limit = forms.BooleanField(required=False)