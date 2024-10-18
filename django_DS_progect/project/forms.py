from django import forms
import random

class PredictionForm(forms.Form):

    id = forms.IntegerField(
        label="ID",
        initial=random.randint(0, 100000),
        required=True,
        help_text="Случайный ID, сгенерированный автоматически."
    )

    is_tv_subscriber = forms.BooleanField(
        required=False,
        label="Чи є підписка на ТБ?",
        help_text="Вкажіть, чи є у клієнта підписка на телебачення."
    )
    is_movie_package_subscriber = forms.BooleanField(
        required=False,
        label="Чи є підписка на фільми?",
        help_text="Вкажіть, чи підписаний клієнт на пакет фільмів."
    )
    subscription_age = forms.FloatField(
        required=True,
        label="Тривалість підписки (місяці)",
        help_text="Введіть кількість місяців з моменту початку підписки."
    )
    bill_avg = forms.FloatField(
        required=True,
        label="Середній рахунок",
        help_text="Введіть середню суму щомісячного рахунку."
    )
    reamining_contract = forms.FloatField(  # Исправлено название поля
        required=True,
        label="Залишок контракту (місяці)",
        help_text="Введіть кількість місяців, що залишилися до завершення контракту."
    )
    service_failure_count = forms.IntegerField(
        required=True,
        label="Кількість збоїв у сервісі",
        help_text="Введіть кількість збоїв у наданні послуг."
    )
    download_avg = forms.FloatField(
        required=True,
        label="Середня швидкість завантаження (Mbps)",
        help_text="Вкажіть середню швидкість завантаження даних в Mbps."
    )
    upload_avg = forms.FloatField(
        required=True,
        label="Середня швидкість вивантаження (Mbps)",
        help_text="Вкажіть середню швидкість вивантаження даних в Mbps."
    )
    download_over_limit = forms.BooleanField(
        required=False,
        label="Чи перевищено ліміт завантаження?",
        help_text="Вкажіть, чи перевищено встановлений ліміт завантаження даних."
    )
