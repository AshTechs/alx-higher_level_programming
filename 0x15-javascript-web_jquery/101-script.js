$(document).ready(function() {
    // Attach a click event handler to DIV#add_item
    $('#add_item').click(function() {
        // Create a new <li> element with the text 'Item'
        const newItem = $('<li>').text('Item');
        
        // Append the new <li> element to UL.my_list
        $('ul.my_list').append(newItem);
    });

    // Attach a click event handler to DIV#remove_item
    $('#remove_item').click(function() {
        // Select UL.my_list and find the last <li> element
        const lastItem = $('ul.my_list').children('li').last();
        
        // Remove the last <li> element from the list
        lastItem.remove();
    });

    // Attach a click event handler to DIV#clear_list
    $('#clear_list').click(function() {
        // Remove all elements from UL.my_list
        $('ul.my_list').empty();
    });
});
