$(document).ready(function() {
    // Realiza a requisição GET para a URL
    $.getJSON('/get_walpapers', function(data) {
        // Itera sobre cada item no JSON
        $.each(data, function(id, item) {
            // Cria o elemento de wallpaper
            var wallpaperDiv = $('<div>', { id: 'walpapper' });
            wallpaperDiv.attr('wpp-id', id);

            // Cria o elemento de imagem e adiciona ao wallpaper
            var img = $('<img>', {
                src: 'preview/' + id + '/' + item.preview,
                id: 'preview'
            });
            wallpaperDiv.append(img);

            // Cria o div de informações
            var informDiv = $('<div>', { id: 'inform' });

            // Cria o título e adiciona
            var title = $('<h1>', { id: 'title', text: item.title });
            informDiv.append(title);

            // Cria o tipo e adiciona
            var type = $('<p>', { id: 'type', text: item.type });
            informDiv.append(type);

            // Cria a descrição e adiciona
            var description = $('<p>', { id: 'description', text: item.description });
            informDiv.append(description);

            // Adiciona o informDiv ao wallpaperDiv
            wallpaperDiv.append(informDiv);

            // Adiciona o wallpaperDiv ao corpo ou a algum outro elemento da página
            $('#walpapers').append(wallpaperDiv); // Supondo que você tenha um container para isso
        });
    });
});


$('#searchinput').on('input', function() {
    var valor = $(this).val();
    console.log(valor); 
    
    $.getJSON('/get_walpapers', function(data) {
        $('#walpapers').empty();
        $.each(data, function(id, item) {
            if (item.title.toLowerCase().includes(valor.toLowerCase()) || 
            item.description.toLowerCase().includes(valor.toLowerCase()) || 
            item.type.toLowerCase().includes(valor.toLowerCase()) || valor == "") {
                var wallpaperDiv = $('<div>', { id: 'walpapper' });
                wallpaperDiv.attr('wpp-id', id);

                var img = $('<img>', {
                    src: 'preview/' + id + '/' + item.preview,
                    id: 'preview'
                });
                wallpaperDiv.append(img);

                var informDiv = $('<div>', { id: 'inform' });

                var title = $('<h1>', { id: 'title', text: item.title });
                informDiv.append(title);
                var type = $('<p>', { id: 'type', text: item.type });
                informDiv.append(type);

                var description = $('<p>', { id: 'description', text: item.description });
                informDiv.append(description);

                wallpaperDiv.append(informDiv);

                $('#walpapers').append(wallpaperDiv);
            }
            
        });
    });
});


