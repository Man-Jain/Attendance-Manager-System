a=1;
$(document).ready(function(){
    $("#add-option-g1").click(function(){
        $("fieldset").append("<div id='field-"+a+"' class='form-group'><label>Poll Choice</label> <input class='form-control' placeholder='Choice' required type='text' name='choice-"+a+"'> </div>");
        a++;
    });
    $("#remove-option-g1").click(function(){
        $("#field-"+a).remove();
        a--;
    });
});

$(function(){
    $('.content-box-large').on("click","#btn-group1", function(){
        $.ajax({
            url: '/group1',
            data: $('#form-group').serialize(),
            type: 'POST',
            success: function(){
            $("#alert-g1").show();
            $("#alert-g1").fadeOut(3000);
            //$('.content-box-large').load(document.URL +  ' .content-box-large');
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});

$(function(){
    $('#polls-row').on("click", '.vote-btn',function(){
        $.ajax({
            url: '/vote',
            data: $(this).parent().serialize(),
            type: 'POST',
        }).done(function(response){
            console.log(response);
            //location.reload(true);
            $('#polls-row').load(document.URL +  ' #polls-row');
        });
    });
});