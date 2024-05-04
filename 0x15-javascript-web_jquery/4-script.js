$(document).ready(function() {
    // Attach a click event handler to the DIV#toggle_header element
    $('#toggle_header').click(function() {
        // Select the <header> element
        const header = $('header');
        
        // Check the current class of the <header> element
        if (header.hasClass('red')) {
            // If the current class is 'red', remove 'red' and add 'green'
            header.removeClass('red').addClass('green');
        } else {
            // If the current class is not 'red', it must be 'green', remove 'green' and add 'red'
            header.removeClass('green').addClass('red');
        }
    });
});
