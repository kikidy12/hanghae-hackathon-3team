

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
        $(".check1").on('click', function (){

        })






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

function signup(){

    let ninkName = ninkname.val()
    let id = ID.val()
    let pw = PW.val()
    let check = userPWcheck.val()
    let check_kor = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/; // 한글체크
    let checK_idpw = /^[a-zA-z0-9]{4,10}$/;


    // 닉네임은 한글만 아이디와 비밀번호는
    if(check_kor.test(ninkName)  && checK_idpw.test(id)   &&checK_idpw.test(pw)   && check === pw){


    // 조건 닉네임 한글만 아이디 영문숫자 4-8글자


     $.ajax({
                type: "POST",
                url: "/api/register",
                data: {
                    idGive: id,
                    pwGive: pw,
                    nickNameGive:ninkName,
                },
                success: function (response) {
                    if (response['result'] === 'success') {
                        alert('회원가입이 완료되었습니다.')
                        // 메인으로 이동
                        window.location.href = '/'
                    } else {
                        alert(response['msg'])
                    }
                }

            })



    }
    //
    else if(!checK_idpw.test(pw)){
      alert('비밀번호 영문과숫자4-10글자이네로 작성해주세요')
    }else if(check !== pw) {
      alert('비밀번호가 일치하지않습니다!')
    }else {
        alert('오류 다시 시도 하세요!');
        window.location.reload();
    }
    // else if(id_duplicate_check !==true){
    //     alert('아이디 중복체크 하시고 회원가입해주세요!')
    // }
    // else if(nink_duplicate_check!==true){
    //     alert('닉네임 중복체크 하시고 회원가입해주세요!')
    // }



}

