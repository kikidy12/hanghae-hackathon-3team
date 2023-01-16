let id_duplicate_check = false;
let nink_duplicate_check = false;

let ninkname = $("#userNinkName");
let ID = $("#userID");
let PW = $("#userPW");
let userPWcheck = $("#userPWcheck");

// 닉네임 input 창
ninkname.on('input', function (){

    if(ninkname.val().length >=2){

         $('.check1').css('opacity','1')

     $(".check1").on('click', function (){
             let check_kor = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/; // 한글체크
             let nink1 = ninkname.val()
             if(check_kor.test(nink1) ){
               $.ajax({
               type: "POST",
               url: "/ninkcheck",
               data: { nickNameGive:  ninkname.val()},
               success: function (response) {
                   console.log(response)

               console.log(response['msg'])
               $('.check1').css('background','#fa5252')
               $('.check1').text(response["msg"])

               nink_duplicate_check = response["nink_duplicate_check"]
               console.log(nink_duplicate_check)
                     }
                 })

             }
             else {
                $(".show1").addClass('show');
                window.location.reload()
             }


 })






    } else{
     $(".check1").css('opacity', '0.2')
    }

});


ID.on('input', function (){
    if(ID.val().length >=2){
    $(".check2").css('opacity', '1')

          $(".check2").on('click', function (){
             let checK_idpw = /^[a-zA-z0-9]{4,10}$/; //정규식 아이디
             let ID1 = ID.val()

             if(checK_idpw.test(ID1)){
                   $.ajax({
               type: "POST",
               url: "/idcheck",
               data: {idGive:  ID.val()},
               success: function (response) {
                   console.log(response)
              console.log(response['msg'])
               $('.check2').css('background','#fa5252')

               $('.check2').text(response["msg"])
               id_duplicate_check = response["id_duplicate_check"]
               console.log(id_duplicate_check)
                     }
                 })

             }
             else {
                $(".show2").addClass('show');
                window.location.reload()
             }



 })





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
    if(nink_duplicate_check==true  && id_duplicate_check==true   &&checK_idpw.test(pw)   && check === pw){


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
    }
    else if(id_duplicate_check !==true){
         alert('아이디 중복체크 하시고 회원가입해주세요!')
     }
     else if(nink_duplicate_check!==true){
         alert('닉네임 중복체크 하시고 회원가입해주세요!')
     }
    else {
        alert('오류 다시 시도 하세요!');
        window.location.reload();
    }



}