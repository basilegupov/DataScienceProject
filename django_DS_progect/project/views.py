import logging
from django.shortcuts import render
from .forms import PredictionForm
import joblib  # для загрузки модели машинного обучения

# Настройка логирования
logger = logging.getLogger(__name__)

def predict_view(request):
    # Инициализация переменных для отображения результата
    prediction = None
    probability = None

    # Обрабатываем POST-запрос
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            data = form.cleaned_data
            
            # Логируем полученные данные
            logger.info("Полученные данные из формы: %s", data)
            
            # Загрузка модели машинного обучения
            model = joblib.load('project/XGBClassifier.pkl')
            
            # Загрузка масштабировщика
            scaler = joblib.load('project/scaler.pkl')

            # Подготовка данных для модели
            input_data = [[
                data['id'],
                data['is_tv_subscriber'],
                data['is_movie_package_subscriber'],
                data['subscription_age'],
                data['bill_avg'],
                data['reamining_contract'],
                data['service_failure_count'],
                data['download_avg'],
                data['upload_avg'],
                data['download_over_limit'],
            ]]

            # Масштабирование данных
            input_data_scaled = scaler.transform(input_data)
            
            # Логируем масштабированные данные
            logger.info("Подготовленные и масштабированные данные: %s", input_data_scaled)
            
            # Прогноз
            prediction = model.predict(input_data_scaled)[0]
            prediction_proba = model.predict_proba(input_data_scaled)[0][1]  # вероятность оттока
            
            # Логируем результат
            logger.info("Результат: %s, вероятность: %s", prediction, prediction_proba)

            # Форматирование вероятности в проценты
            probability = "{:.0f}".format(prediction_proba * 100)

            # Очищаем форму после успешного предсказания
            form = PredictionForm()

        else:
            # Логируем ошибки валидации
            logger.warning("Ошибки валидации формы: %s", form.errors)
            return render(request, 'project/prediction_form.html', {
                'form': form,
                'errors': form.errors,
            })

    else:
        # Создаем пустую форму при GET-запросе, сбрасываем prediction и probability
        form = PredictionForm()

    # При GET-запросе (например, после перезагрузки страницы) prediction и probability будут равны None
    return render(request, 'project/prediction_form.html', {
        'form': form,
        'prediction': 'Клієнт покине компанію' if prediction == 1 else 'Клієнт залишиться з компанією' if prediction is not None else None,
        'probability': probability if probability is not None else None,
    })
