


$('#btn-hello').on('click', () => {
    if  ($('#input-fname').val() && $('#input-sname').val()){
        $.ajax({
            url: 'checkUser',
            method: 'POST',
            dataType: 'json',
            data: JSON.stringify({'name': $('#input-fname').val(), 'surname': $('#input-sname').val()}),
            success:  function (data){
                $('#div-warning').fadeIn()
                $('#lb-answer').text(data['answer'])
            }
        })
    }
    else{
        $('#div-warning').fadeIn()
        $('#lb-answer').text('Ви забули щось ввести')
    }
    
})


$('#btn-submit').on('click', () => {
    $('#div-warning').fadeOut()
})