function login(){
let a = $('#userID').val();
        console.log(a);

    $.ajax({
                type: "POST",
                url: "/api/login",
                data: {
                    idGive:  $('#userID').val(),
                    pwGive: $('#userPW').val(),
                },
                success: function (response) {
                    if (response['result'] == 'success') {
                        alert('회원가입이 완료되었습니다.')
                        // 메인으로 이동
                        window.location.href = '/'
                    } else {
                        alert(response['msg'])
                    }
                }

            })
}