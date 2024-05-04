$(document).ready(function() {
    // Attach a click event handler to INPUT#btn_translate
    $('#btn_translate').click(function() {
        // Get the language code entered in INPUT#language_code
        const langCode = $('#language_code').val();
        
        // URL to fetch the translation of "Hello" based on the language code
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
        
        // Fetch the translation of "Hello" using jQuery's AJAX function
        $.ajax({
            url: apiUrl,
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                // If the request is successful, display the translation in DIV#hello
                $('#hello').text(data.hello);
            },
            error: function() {
                // Handle any errors that occur during the request
                console.error('Failed to fetch data from the API');
                // Optionally, you can display an error message in DIV#hello
                $('#hello').text('Error fetching translation.');
            }
        });
    });
});
