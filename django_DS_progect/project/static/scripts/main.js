$(document).ready(function () {
    $(window).on('load', function() { 
        $('#status').fadeOut(); // Скрываем анимацию загрузки
        $('#preloader').delay(350).fadeOut('slow'); // Скрываем белый DIV
        $('body').delay(350).css({'overflow':'visible'});
    });

    // back to top button
    var offset = 300;
    var scroll_top_duration = 700;
    var $back_to_top = $('.backToTop');

    $(window).scroll(function(){
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('backToTop-is-visible') : $back_to_top.removeClass('backToTop-is-visible backToTop-fade-out');
    });

    // smooth scroll
    var scrollOffsetVal = 124;
    if ($(window).width() < 1350) { 
        scrollOffsetVal = 75;
    }
    if(window.location.hash) {
        $(window).scrollTop($(window).scrollTop() + -scrollOffsetVal);
    } 

    $('a[href*="#"]:not([href="#"])').click(function() {
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top - scrollOffsetVal
        }, 1000);
    });

    // Обработка формы предсказания
    $('#prediction-form').on('submit', function(event) {
        event.preventDefault(); // Предотвращаем перезагрузку страницы

        // Получаем CSRF-токен
        const csrftoken = getCookie('csrftoken');

        // Собираем данные формы
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);

        // Логируем собранные данные
        console.log("Собранные данные формы:", data);

        // Отправляем данные на сервер для получения предсказания
        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            body: JSON.stringify(data),
        })
        .then((response) => {
            if (!response.ok) {
                // Обработка ошибки
                return response.json().then(errData => {
                    throw new Error(errData.error || "Неизвестная ошибка");
                });
            }
            return response.json();
        })
        .then((data) => {
            document.getElementById("result").textContent = data.prediction;
            document.getElementById("prediction-result").style.display = "block";
        })
        .catch((error) => {
            console.error("Ошибка при обработке запроса:", error);
            // Отобразите ошибку пользователю
            document.getElementById("result").textContent = `Ошибка: ${error.message}`;
            document.getElementById("prediction-result").style.display = "block";
        });
    });
});
