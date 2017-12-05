$(document).ready(function(){
    $('#registrationForm').submit(function(e){
        e.preventDefault();
        console.log("submitting");
        $("#errmsg").html("");

        console.log($("#registrationForm").serialize());
        var account_type = "";
        if(document.getElementById("admin-checkbox").checked){
            account_type = "&ACCOUNT_TYPE=ADMIN";
        }

        $.ajax({
            url: '/registration',
            type: 'POST',
            data: $("#registrationForm").serialize() + account_type,
            success: function(response){
                console.log(response);
                if(response['ERROR'] == false){
                    //successful login
                    $("#registration-message-container").addClass("alert-success");
                    $("#registration-message-container").html("Succes: " + response['MESSAGE']);
                    $("#registration-message-container").css("display", "inline-block");
                    //window.location.replace("/chatbot");
                }
                else if(response['ERROR'] == true){
                    //failed login
                    $("#registration-message-container").addClass("alert-danger");
                    $("#registration-message-container").text("Error: " + response['MESSAGE']);
                    $("#registration-message-container").css("display", "inline-block");
                } 
                else{
                    //response.ERROR undefined, error on server implied
                    $("#registration-message-container").addClass("alert-danger");
                    $("#registration-message-container").text("Error: unknown server error");
                    $("#registration-message-container").css("display", "inline-block");
                }
            },
            error: function(jqXHR, response){
                //server error
                $("#registration-message-container").addClass("alert-danger");
                $("#registration-message-container").text("Error: server error (" + jqXHR + ")");
                $("#registration-message-container").css("display", "inline-block");
            }
        });
    });
});