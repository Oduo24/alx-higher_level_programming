$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(response) {
	$('div#character').html(response.name);
}
);
