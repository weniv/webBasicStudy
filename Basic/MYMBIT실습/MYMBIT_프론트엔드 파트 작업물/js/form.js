function scroller(next) {
    const height = $('fieldset').height();

    $('html').animate({
        scrollTop: ((Math.floor($(window).scrollTop() / height) - (next ? -1 : 1)) * height)
    }, 500)
}

$('.btn_next').click((e) => {
    if (e.currentTarget.closest('fieldset').querySelector('input:checked')) {
        scroller(true);
    } else {
        alert('문항을 선택해주세요!');
    }
})

$('.btn_prev').click(() => {
    scroller(false)
})
