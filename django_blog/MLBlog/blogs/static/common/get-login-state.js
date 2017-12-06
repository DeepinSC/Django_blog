function get_login_state() {
    function is_login_or_username(){
        var return_state;
        $.ajax({
            async:false,
            url:"/api/rest-auth/user",
            type:"GET",
            datatype:"json",
            success:function (data) {
                return_state = data.username;
            },
            error:function(XMLHttpRequest, textStatus, errorThrown) {
                  return_state = false;
              }
        });
        return return_state;
    }

    function sign_out(){
        $.ajax({
            async:false,
            url:"/api/rest-auth/logout/",
            type:"POST",
            datatype:"json",
            headers:{"X-CSRFToken":getCookie('csrftoken')},
            success:function () {
                location.reload();
            },
            error:function(XMLHttpRequest, textStatus, errorThrown) {
                console.log(textStatus.responseText);
                alert(XMLHttpRequest.status);
              }
        });
    }

    var user_content_div = document.getElementById("usercontent");
    var state = is_login_or_username();
    var title = document.createElement("h4");
    // 如果未登录,提示用户登录
    if (state == false){

        title.append("Please Sign in or Sign up:");

        var container = document.createElement("div");

        var signin = document.createElement("button");
        signin.className = "btn btn-info btn-sm";
        signin.append("Sign In");
        signin.onclick = function () {
            window.location.href = "/login";
        };
        var signup = document.createElement("button");
        signup.className = "btn btn-default btn-sm";
        signup.append("Sign Up");

        container.appendChild(signin);
        container.appendChild(signup);

        user_content_div.appendChild(title);
        user_content_div.appendChild(container);
    }
    else{
        title.append("Welcome: "+state);

        var signout = document.createElement("button");
        signout.className = "btn btn-primary btn-sm";
        signout.append("Sign Out");
        signout.onclick = function (ev) { sign_out(); };

        user_content_div.appendChild(title);
        user_content_div.appendChild(signout);
    }

}