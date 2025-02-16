document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const moviesList = document.getElementById('moviesList');
    const movies = moviesList ? moviesList.getElementsByTagName('li') : [];

    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            const filter = searchInput.value.toLowerCase();
            for (let i = 0; i < movies.length; i++) {
                const movie = movies[i].textContent || movies[i].innerText;
                if (movie.toLowerCase().indexOf(filter) > -1) {
                    movies[i].style.display = '';
                } else {
                    movies[i].style.display = 'none';
                }
            }
        });
    }
});