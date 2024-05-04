$(document).ready(function() {
    // URL to fetch the translation of "hello" in French
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    
    // Fetch the translation of "hello" using jQuery's AJAX function
    $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            // If the request is successful, display the value of "hello" in DIV#hello
            $('#hello').text(data.hello);
        },
        error: function() {
            // Handle any errors that occur during the request
            console.error('Failed to fetch data from the API');
        }
    });
});
