$(document).ready(function() {
    // URL to fetch the character data
    const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    
    // Fetch the character data using jQuery's AJAX function
    $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            // If the request is successful, update the text of the DIV#character element
            $('#character').text(data.name);
        },
        error: function() {
            // Handle any errors that occur during the request
            console.error('Failed to fetch data from the API');
        }
    });
});
