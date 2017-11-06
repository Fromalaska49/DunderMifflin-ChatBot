$(document).ready(function(){
    $("#success-div").hide();
    $('#registrationForm').submit(function(e){
        e.preventDefault();
        console.log("submitting");
        $("#errmsg").html("");

        console.log($("#registrationForm").serialize());

        $.ajax({
            url: '/register',
            type: 'POST',
            data: $("#registrationForm").serialize(),
            success: function(data){
                console.log(data);

                if(data['error'] === true){
                    $("#errmsg").html(data['msg']);
                }
                else{
                    $("#registration-div").hide();
                    $("#success-div").show();
                }
            }

        })
    });
});
