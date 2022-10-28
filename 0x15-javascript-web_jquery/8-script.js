$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(response) {
	for (elem in response) {
		$('ul#list_movies').append(`<li>${elem}</li>`);
	}
});
