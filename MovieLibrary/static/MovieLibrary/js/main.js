document.getElementById('searchInput').addEventListener('input', function() {
    var filter = this.value.toUpperCase();
    var moviesList = document.getElementById('moviesList');
    var movies = moviesList.getElementsByTagName('li');

    for (var i = 0; i < movies.length; i++) {
        var title = movies[i].getElementsByClassName('movie-title')[0];
        if (title.innerHTML.toUpperCase().indexOf(filter) > -1) {
            movies[i].style.display = 'block'; // Ensure the display is set to block
        } else {
            movies[i].style.display = 'none';
        }
    }
});