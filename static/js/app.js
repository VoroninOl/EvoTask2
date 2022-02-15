


$('#btn-hello').on('click', () => {
    if  ($('#name').val() && $('#surname').val()){
        $.ajax({
            url: 'checkUser',
            method: 'POST',
            dataType: 'json',
            data: JSON.stringify({'name': $('#name').val(), 'surname': $('#surname').val()}),
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
