document.addEventListener('DOMContentLoaded', function () {
        const searchBar = document.querySelector('.search-bar');
        const searchButton = document.querySelector('.search-button');
        const tableRows = document.querySelectorAll('.table tbody tr');

        const initialRowsDisplay = Array.from(tableRows).map(row => row.style.display);

        searchButton.addEventListener('click', function () {
            const searchTerm = searchBar.value.trim().toLowerCase(); // Dohvati vrijednost i pretvori u mala slova

            // Provjeri je li pretraga prazna
            if (searchTerm === '') {
                alert('Unesite pojam za pretragu.');
                return;
            }

            // Iteriraj kroz svaki red
            tableRows.forEach(function (row) {
                const author = row.querySelector('td:nth-child(1)').textContent.trim().toLowerCase();
                const title = row.querySelector('td:nth-child(2)').textContent.trim().toLowerCase();
                const key = row.querySelector('td:nth-child(3)').textContent.trim().toLowerCase();
                const genre = row.querySelector('td:nth-child(4)').textContent.trim().toLowerCase();

                // Provjeri je li pojam za pretragu prisutan u bilo kojoj od kolona reda
                if (author.includes(searchTerm) || title.includes(searchTerm) || key.includes(searchTerm) || genre.includes(searchTerm)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });

        // Resetuje prikaz na pocetno stanje kada se ukloni pretraga
        searchBar.addEventListener('input', function () {
            if (searchBar.value.trim() === '') {
                tableRows.forEach(function (row, index) {
                    row.style.display = initialRowsDisplay[index];
                });
            }
        });
    });