$(document).ready(function() {
    // URL to fetch the list of movies
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    
    // Fetch the list of movies using jQuery's AJAX function
    $.ajax({
        url: apiUrl,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            // If the request is successful, list the movie titles in UL#list_movies
            const movies = data.results; // Access the results array from the data object
            
            // Iterate through each movie in the results array
            movies.forEach(function(movie) {
                // Create a new <li> element with the movie title
                const listItem = $('<li>').text(movie.title);
                
                // Append the new <li> element to UL#list_movies
                $('#list_movies').append(listItem);
            });
        },
        error: function() {
            // Handle any errors that occur during the request
            console.error('Failed to fetch data from the API');
        }
    });
});
