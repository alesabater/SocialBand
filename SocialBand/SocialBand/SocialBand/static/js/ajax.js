$(function(){

    $('#search').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "/usuario/search/",
            data: { 
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

$(function(){

    $('#search1').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "/banda/search/",
            data: { 
                'search_text' : $('#search1').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}