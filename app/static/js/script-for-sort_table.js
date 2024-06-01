$(document).ready(function(){
    // Funkcija za sortiranje
    function sortTable(columnIndex) {
        var rows = $('tbody > tr').get();
        rows.sort(function(a, b) {
            var A = $(a).children('td').eq(columnIndex).text().toUpperCase();
            var B = $(b).children('td').eq(columnIndex).text().toUpperCase();
            if(A < B) {
                return -1;
            }
            if(A > B) {
                return 1;
            }
            return 0;
        });
        $.each(rows, function(index, row) {
            $('tbody').append(row);
        });
    }

    // Dodavanje strelica i dodavanje funkcionalnosti sortiranja
    $('th').each(function(index){
        $(this).append('<span class="sort-icon">&#9660;</span>');
        $(this).click(function(){
            $('th .sort-icon').not(this).html('&#9660;');
            var sortOrder = $(this).data('sort-order') || 'asc';
            if(sortOrder === 'asc') {
                $(this).find('.sort-icon').html('&#9650;');
                sortTable(index);
                $(this).data('sort-order', 'desc');
            } else {
                $(this).find('.sort-icon').html('&#9660;');
                sortTable(index);
                $(this).data('sort-order', 'asc');
            }
        });
    });
});