from django.shortcuts import render
from .forms import PredictionForm
import joblib  # для загрузки модели машинного обучения

def predict_view(request):
    
    return render(request, 'project/prediction_form.html')  # Подключаем твой HTML-файл

def predict_view(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            data = form.cleaned_data
            
            # Загрузка предобученной модели машинного обучения
            model = joblib.load('path_to_your_model.pkl')
            
            # Подготовка данных для модели
            input_data = [[
                data['is_tv_subscriber'],
                data['is_movie_package_subscriber'],
                data['subscription_age'],
                data['bill_avg'],
                data['remaining_contract'],
                data['service_failure_count'],
                data['download_avg'],
                data['upload_avg'],
                data['download_over_limit'],
            ]]
            
            # Прогнозируем
            prediction = model.predict(input_data)[0]
            prediction_proba = model.predict_proba(input_data)[0][1]  # вероятность оттока

            return render(request, 'result.html', {
                'form': form,
                'prediction': 'Отток' if prediction == 1 else 'Не отток',
                'probability': round(prediction_proba * 100, 2),
            })
    else:
        form = PredictionForm()
    return render(request, 'project/prediction_form.html', {'form': form})
