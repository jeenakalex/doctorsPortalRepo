
$( document ).ready(function() {
    console.log( "sign in ready!" );

});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$("#btnIdSignIn").click(function(event){
    event.preventDefault();
    //fun for validation
    var arrLoginCredentials = {};
    
    arrLoginCredentials={
        "strUname": $.trim($("#IdStrUserEmail").val()),
        "strPassword": $.trim($("#idStrPassword").val())
    }

    $.ajax({
        type: 'POST',
        url: 'checkSignin',
        dataType: 'json',
        data: {'jsnLoginCredentials': JSON.stringify({'arrLoginCredentials':arrLoginCredentials})},
        async:false,
        success: function (response) {
            //code
            console.log("success-response : "+JSON.stringify(response))
            $(location).attr('href','www.google.com')
        },
        error:function(response){
            console.log("error-response : "+ JSON.stringify(response))
            console.log("error-status : "+JSON.stringify(status))
        }
    });
}); 

