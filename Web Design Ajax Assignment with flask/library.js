var filter = ['Bethesda'];

$('#container').load('Homepage.html');

if(('data' in window.localStorage) === false){
    window.localStorage.setItem('data', JSON.stringify([]));
}

var template = $('#template').html();

$('nav>div>a').click(function(){
    //Gets href value
    var contentPage = $(this).attr('href');
    
    $('#container').load(contentPage + '.html', function(){
        loadGames(filter);
    });

    return false;
});

function loadGames(filter){
    $('#Games').html('<h3>Your Games</h3>');
    var library = JSON.parse(window.localStorage.getItem('data'));
    for(i in library){
        $('#Games').append(library[i]);
    }

    //The filtering section
    for(x in filter){
        var reg = new RegExp('^' + filter[x], 'i');

        $('#Games').children().each(function(){
            console.log($(this).attr('class'));

            if($(this).attr('class')){
                var classes = $(this).attr('class').split(' ');
                var found = false;

                for(i in classes){
                    if(classes[i].match(reg)){
                        found = true;
                    }
                }
                
                if(!found){
                    $(this).remove();
                }
            }
        });
    }

    return false;
}

function formSubmit(event) {
    // Stop the browser from submitting the form.
    event.preventDefault();

    var dict = {};

    $(event.target).find('input').each(function(){
        if($(this).attr('name')){
            dict[$(this).attr('name')] = $(this).val();
            $(this).val('');
        }
    });

    var comments = /!--(.*)--/g;
    var gameSlot = template;

    var matches = [];
    
    var m;

    /*I use regular expressions to find comments and replace em with what 
    I want from a dictionary made out of the form.*/
    do{
        m = comments.exec(gameSlot);
        if(m){
            matches.push(m[1]);
        }
    } while (m);

    function createClasses(list){
        list = Object.create(list);
        for(i in list){
            var adding = dict[list[i]].replace(' ','_');
            list[i] = adding;
        }
        return list.join(' ');
    }

    gameSlot = gameSlot.replace("classEdit", createClasses(matches));
    
    for(i in matches){
        i = matches[i];
        gameSlot = gameSlot.replace('<!--' + i + '-->', dict[i]);
    }

    var library = JSON.parse(window.localStorage.getItem('data'));
    library.push(gameSlot);
    window.localStorage.setItem('data',JSON.stringify(library));
    loadGames(filter);
}
