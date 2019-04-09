function marcaHoraExtra(id) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({

        type: 'POST',
        url:'/hora_extra/marcada/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            $("#mensagem").text('Hora extra marcada como utilizada');
        }

    });
}