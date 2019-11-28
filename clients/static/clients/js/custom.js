$(document).ready(function(){

    $("#search_btn").on("click keydown", function() {
        var value = $('#search_txt').val();
        $.ajax({
            type: "GET",
            url: "/clients/",
            contentType: "application/json; charset=utf-8",
            data: {'search_val': value},
            success: function(result) {
            $('#contact_table').html(result.html);
            },
            error: function(result) {
            alert('error');
            }
        });

    });

    $('#search_txt').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){
            $('#search_btn').click();
        }
    });

});
