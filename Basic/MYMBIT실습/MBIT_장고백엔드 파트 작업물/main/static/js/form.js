function scroller(next) {
    const height = $('fieldset').height();
    $('html').animate({
        // scrollTop : 스크롤 바의 위치를 나타냅니다.
        // 전체 높이에서 뷰포트만큼 나눈 값에 -1, 혹은 +1을 해서 뷰포트 넓이만큼 곱하면 이동해야하는 길이가 나옵니다.
        scrollTop: ((Math.floor($(window).scrollTop() / height) - (next ? -1 : +1)) * height)
    }, 500);
}

$('.btn_next').click((e) => {
    console.log('clicked');
    if (e.currentTarget.closest('fieldset').querySelector('input:checked')) {
        scroller(true);
    } else {
        alert('문항을 선택해주세요.');
    }

})

$('.btn_prev').click((e) => {
    scroller(false);
})