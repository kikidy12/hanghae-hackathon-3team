

let ninkname = $("#userNinkName");
let ID = $("#userID");
let PW = $("#userPW");
let userPWcheck = $("#userPWcheck")

// 닉네임 input 창
ninkname.on('input', function (){
    if(ninkname.val().length >=2){
        $(".check1").css('opacity', '1')
    // 닉네임 2글자 이상이고
    //  중복체크 하기 버튼넣고 맞으면
    } else{
     $(".check1").css('opacity', '0.2')
    }

});

ID.on('input', function (){
    if(ID.val().length >=2){
    $(".check2").css('opacity', '1')
    }
    else {
        $(".check2").css('opacity', '0.2')
    }
})


// 비밀번호 체크 기능
const pwShowHide = document.querySelectorAll('.showHidePw');
const pwInput = document.querySelectorAll('.password');

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener('click', () => {
        pwInput.forEach(pwInput => {
            // icon hide 경우
            if (pwInput.type === "password") {
                pwInput.type = "text";
                // replace 첫번쨰클라스를 두번쨰 클라스로 바꾸라
                pwShowHide.forEach(icon => {
                    icon.classList.replace("fa-eye-slash", "fa-eye")
                })
            } // iocn show 경우
            else {
                pwInput.type = "password";

                pwShowHide.forEach(icon => {
                    icon.classList.replace("fa-eye", "fa-eye-slash")
                })
            }

        })

    })
})
