import logging
from django.shortcuts import render
from .forms import PredictionForm
import joblib  # для загрузки модели машинного обучения

# Настройка логирования
logger = logging.getLogger(__name__)

def predict_view(request):
    # Создаем пустую форму при GET-запросе
    form = PredictionForm()
    prediction = None  # Изначально результат пустой
    probability = None  # Изначально вероятность пустая

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            data = form.cleaned_data
            
            # Логируем данные, полученные из формы
            logger.info("Полученные данные из формы: %s", data)
            
            # Загрузка предобученной модели машинного обучения
            model = joblib.load('project/model.pkl')
            
            # Подготовка данных для модели
            input_data = [[
                data['id'],
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
            
            # Логируем подготовленные данные для предсказания
            logger.info("Подготовленные данные для модели: %s", input_data)
            
            # Прогнозируем
            print(input_data)
            prediction = model.predict(input_data)[0]
            prediction_proba = model.predict_proba(input_data)[0][1]  # вероятность оттока

            # Логируем результат предсказания
            logger.info("Результат предсказания: %s, вероятность: %s", prediction, prediction_proba)
            print(f"Prediction: {prediction}, Probability: {prediction_proba}")

            # Обновляем значение для отображения в шаблоне
            probability = "{:.2f}".format(prediction_proba * 100)

        else:
            # Логируем ошибки валидации
            logger.warning("Ошибки валидации формы: %s", form.errors)
            return render(request, 'project/prediction_form.html', {
                'form': form,
                'errors': form.errors,
            })

    # Возвращаем результат на ту же страницу
    return render(request, 'project/prediction_form.html', {
        'form': form,
        'prediction': 'Отток' if prediction == 1 else 'Не отток' if prediction is not None else None,
        'probability': probability,
    })

