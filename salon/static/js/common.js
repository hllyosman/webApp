$(function(){
    let startPos = 0,winScrollTop = 0;
    $(window).on('scroll',function(){
        winScrollTop = $(this).scrollTop();
        if (winScrollTop >= startPos) {
            if(winScrollTop >= 200){
                $('header').addClass("hide");
            }
        } else {
            $('header').removeClass("hide");
        }
        startPos = winScrollTop;
    });

    window.name = "parentWin"
})

function admin(){
    let dsply = document.getElementById('adminFrame').style
    if(dsply.display == "none"){
        dsply.display = "inline-block"
    }
}

function pwChk(){
    let pw = 'pass'
    let chkData = document.getElementById('pwField').value

    if(pw == chkData){
        window.open('http://localhost:8000/salon/contact/message/', '_self');
    }else{
        document.getElementById('msg').innerText = 'パスワードが違います！【pass】です！'
    }
}