function login() {
   if($("#userPW").val().length>3 && $("#userID").val().length>3){

           $.ajax({
                type: "POST",
                url: "/api/login",
                data: {
                    idGive: $('#userID').val(), pwGive: $('#userPW').val()
                },
                success: function (response) {
                    console.log(response)
                    // 지금여기가 안되는 부분인가 !!
                    if (response['result'] == 'success') {
                        alert('로그인 완료!!')
                       $.cookie('mytoken', response['token']);
                        // 메인으로 이동
                        window.location.href = '/register'
                    } else {
                        alert(response['msg'])
                    }
                }

            })




   }
}