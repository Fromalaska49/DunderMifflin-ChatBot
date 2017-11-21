$(document).ready(function(){
    $("#success-div").hide();
    $('#registrationForm').submit(function(e){
        e.preventDefault();
        console.log("submitting");
        $("#errmsg").html("");

        console.log($("#registrationForm").serialize());

        $.ajax({
            url: '/registration',
            type: 'POST',
            data: $("#registrationForm").serialize() + "&ACCOUNT_TYPE=ADMIN",
            success: function(data){
                console.log(data);

                if(data['ERROR'] === true){
                    $("#errmsg").html(data['MESSAGE']);
                }
                else{
                    $("#registration-div").hide();
                    $("#success-div").show();
                }
            }

        })
    });
});
