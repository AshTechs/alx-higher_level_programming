$(document).ready(function() {
    // Attach a click event handler to the DIV#add_item element
    $('#add_item').click(function() {
        // Create a new <li> element with the text 'Item'
        const newItem = $('<li>').text('Item');
        
        // Add the new <li> element to the UL.my_list element
        $('ul.my_list').append(newItem);
    });
});
