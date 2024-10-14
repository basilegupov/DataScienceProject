$(window).on('load', function() { // makes sure the whole site is loaded 
    $('#status').fadeOut(); // will first fade out the loading animation 
    $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website. 
    $('body').delay(350).css({'overflow':'visible'});
})

$(document).ready(function () {
 

  
    // back to top button
    var offset = 300;
    var scroll_top_duration = 700;
    var $back_to_top = $('.backToTop');

    $(window).scroll(function(){
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('backToTop-is-visible') : $back_to_top.removeClass('backToTop-is-visible backToTop-fade-out');
            
    });

    //smooth scroll

//scroll Offset Value
var scrollOffsetVal = 124;

// smaller screen value
if ($(window).width() < 1350) { 
    scrollOffsetVal = 75;
}

//check if hash exist on page
if(window.location.hash) {
    $(window).scrollTop($(window).scrollTop() + -scrollOffsetVal);
} 

//easy scroll

  $(function() {

    $('a[href*="#"]:not([href="#"])').click(function() {

        $('html, body').animate({
        scrollTop: $($(this).attr('href')).offset().top - scrollOffsetVal
        }, 1000);

    });
}); 

    
});


/////////////////////////////////////////
// // Получаем элементы
// const predictionForm = document.querySelector(".prediction-form");
// const predictionResult = document.getElementById("prediction-result");

// // Функция для обновления видимости формы
// function updateFormVisibility() {
//     // Проверяем, виден ли блок с результатом
//     if (predictionResult.style.display === "none") {
//         predictionForm.classList.remove("hidden"); // Показать форму
//     } else {
//         predictionForm.classList.add("hidden"); // Скрыть форму
//     }
// }

// // Инициализация состояния при загрузке страницы
// updateFormVisibility();

// // Пример обработчика события при отправке формы
// predictionForm.addEventListener("submit", function(event) {
//     event.preventDefault(); // предотвращаем отправку формы для демонстрации

//     // Здесь можно добавить логику для обработки формы и получения предсказания
//     // Например, показать результат
//     predictionResult.style.display = "block"; // показать результат
//     document.getElementById("result").textContent = "Ваше предсказание"; // пример текста результата
    
//     // Обновляем видимость формы
//     updateFormVisibility(); 
// });

// // Дополнительная функция для скрытия результата
// function hideResult() {
//     predictionResult.style.display = "none"; // скрыть результат
//     updateFormVisibility(); // обновляем видимость формы
// }

// // Пример, как скрыть результат через 5 секунд (по желанию)
// setTimeout(hideResult, 5000); // скрыть результат через 5 секунд

