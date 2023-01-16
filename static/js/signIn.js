function login(){


        let id =  $('#userID').val()
        let pw =  $('#userPW').val()

    $.ajax({
                type: "POST",
                url: "/api/login",
                data: {
                    idGive: id,
                    pwGive: pw,
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