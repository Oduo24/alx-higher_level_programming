$('div#add_item').on('click', function() {
	const newElement = $('<li>Item</li>');
	$('ul.my_list').append(newElement);
});
