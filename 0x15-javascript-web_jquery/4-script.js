$('div#toggle_header').on('click', function() {
	const clsAttr = $('header').attr('class')
	if (clsAttr == 'red') {
		$('header').attr('class', 'green');
	}
	else {
		$('header').attr('class', 'red');
	}
});
