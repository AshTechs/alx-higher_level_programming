$(document).ready(function() {
    // Function to fetch and display the translation of "Hello"
    function fetchHelloTranslation() {
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
                // Optionally, display an error message in DIV#hello
                $('#hello').text('Error fetching translation.');
            }
        });
    }
    
    // Attach a click event handler to INPUT#btn_translate
    $('#btn_translate').click(fetchHelloTranslation);

    // Attach a keypress event handler to INPUT#language_code
    $('#language_code').keypress(function(event) {
        // Check if the pressed key is Enter (key code 13)
        if (event.which === 13) {
            // Call the function to fetch and display the translation of "Hello"
            fetchHelloTranslation();
        }
    });
});
