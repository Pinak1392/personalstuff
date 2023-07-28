//Loads in home screen for initial load in and refreshes
$('#container').load('pages/Homepage.html');

//Initialises a few global variables
var search = '';
var timeout;

//Creates filter storage if you dont have a filter on your system
if(('filter' in window.localStorage) === false){
    window.localStorage.setItem('filter', JSON.stringify(['a',[], 0]));
}

//If you don't have any data yet, this looks through the default .json file and takes the data from it
if(('data' in window.localStorage) === false){
    window.localStorage.setItem('data', JSON.stringify({}));
    //This gets the json and sends it to form submit
    $.getJSON('defaults/defaultData.json', function(data){
        for(i in data){
            formSubmit(data[i], true);
        }
    });
}

//Gets the templates
var template = $('#template').html();
var filterTag = $('#box').html();

$('nav>div>a').click(function(){
    //Hides container
    $('#container').hide();
    //Gets href value
    var contentPage = $(this).attr('href');
    
    //loads the containers based on what you clicked
    $('#container').load('pages/'+contentPage + '.html', function(){
        //Loads games and sets up filters and filter section
        loadGames();

        var check = JSON.parse(window.localStorage.getItem('filter'));
        $('#' + check[0]).prop('checked',true);
        for(i in check[1]){
            $('#filters').append(filterTag.replace('<!--repl-->', check[1][i]));
        }
        $('.slider').val(String(check[2]));
        $('.slidecontainer').children('p').text(String(check[2]));
    });

    //Fades in after loading is done
    $('#container').fadeIn();

    return false;
});

//Loads the games
function loadGames(){
    //quickly fades out. Hide failed for some reason.
    $('#library').fadeOut(1);

    //Clears library to add more stuff in again
    $('#library').html(''); 

    //Gets filter and library data
    filter = JSON.parse(window.localStorage.getItem('filter'));
    library = JSON.parse(window.localStorage.getItem('data'));

    //Appends data into library
    for(i in library){
        $('#library').append(library[i]['html'])
    }

    //Sort function
    function sortMe(a, b) {
        if(filter[0] === 'a'){
            return a.className > b.className;
        }
        else if(filter[0] === 'z'){
            return a.className < b.className;
        }
        else if(filter[0] === 'da'){
            aScore = a.className.split(' ')[1]
            bScore = b.className.split(' ')[1]
            return aScore > bScore;
        }
        else if(filter[0] === 'dz'){
            aScore = a.className.split(' ')[1]
            bScore = b.className.split(' ')[1]
            return aScore < bScore;
        }
        else if(filter[0] === '0'){
            aScore = a.className.split(' ')[2]
            bScore = b.className.split(' ')[2]
            return parseInt(aScore) > parseInt(bScore);
        }
        else if(filter[0] === '9'){
            aScore = a.className.split(' ')[2]
            bScore = b.className.split(' ')[2]
            return parseInt(aScore) < parseInt(bScore);
        }
    }

    //sorts library
    var elem = $('#library').children('div').sort(sortMe);
    $('#library').append(elem);

    //The filtering section
    for(x in filter[1]){
        //Uses regex to remove all white space in filter input
        x = filter[1][x].replace(/\s/g, '_')

        //creates a regex pattern
        var reg = new RegExp('^' + x, 'i');

        //looks at all divs in library and removes those which don't have a 
        //class which matches with regex pattern
        $('#library').children().each(function(){
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

    //Checks if the score class of the game is greater than set min score. Remove the games which are too low score.
    //To be fair I probably could have used attributes instead of doing crazy stuff with the classes
    $('#library').children().each(function(){
        if($(this).attr('class')){
            var classes = $(this).attr('class').split(' ');

            if(parseInt(classes[2]) < filter[2]){
                $(this).remove();
            }
        }
    });

    //Takes care of searching uses same technique as the filter
    var sReg = new RegExp('^' + window.search, 'i');

    $('#library').children().each(function(){
        if($(this).attr('class')){
            var classes = $(this).attr('class').split(' ');
            var found = false;

            for(i in classes){
                if(classes[i].match(sReg)){
                    found = true;
                }
            }
            
            if(!found){
                $(this).remove();
            }
        }
    });

    //Fades in library
    $('#library').fadeIn();
    
    return false;
}

function formSubmit(event, arg=false) {
    //arg is true if i give in data manually such as when entering default data
    if(!arg){
        // Stop the browser from submitting the form.
        event.preventDefault();

        //Puts form vals into dict
        var dict = {};
    
        $(event.target).find('input').each(function(){
            if($(this).attr('name')){
                dict[$(this).attr('name')] = $(this).val();
                $(this).val('');
            }
        });        
    } else {
        //makes dict into the manually inputted dictionary
        var dict = event;
    }

    //creates regex pattern
    var comments = /!--(.*)--/g;

    var gameSlot = template;

    var matches = [];
    
    var m;

    /*I use regular expressions to find comments and replace em with what 
    I want from a dictionary made out of the form.*/
    do{
        //finds all the regex matches and adds the returned values to a list m
        m = comments.exec(gameSlot);
        if(m){
            matches.push(m[1]);
        }
    } while (m);

    //creates the classes for the game div
    function createClasses(list){
        list = Object.create(list);
        for(i in list){
            //replaces white spaces with '_'
            var adding = dict[list[i]].replace(/\s/g,'_');
            //adding = adding.replace(/'/,"\\\'");
            list[i] = adding;
        }
        //Joins the classes with space so i can insert in into div
        return list.join(' ');
    }

    //Inserts the classes into div by replacing classEdit
    gameSlot = gameSlot.replace("classEdit", createClasses(matches));
    
    //Looks through your all the places needed to be replaced and replaces them with their dictionary equivalent.
    for(i in matches){
        i = matches[i];
        gameSlot = gameSlot.replace('<!--' + i + '-->', dict[i]);
    }

    $.getJSON("https://en.wikipedia.org/w/api.php?action=query&format=json&gsrlimit=1&generator=search&origin=*&gsrsearch=" + dict['Game'] + '(game)', function(res){
        var page_id = Object.keys(res.query.pages)[0];
        var title = res.query.pages[page_id].title.replace(/\s/g,'_');
        $.ajax({
            url: 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=' + title,
            dataType:'jsonp',
            success: function(data) {
                //gets wikipedia data on your game and stores it along with your game div in to local storage
                var page_id = Object.keys(data.query.pages);
                var summary = data.query.pages[page_id].extract;
                var library = JSON.parse(window.localStorage.getItem('data'));
                library[dict['Game']] = {};
                library[dict['Game']]['html'] = gameSlot;
                library[dict['Game']]['descript'] = String(summary);
                window.localStorage.setItem('data',JSON.stringify(library));
                loadGames();
            }
        });
    });
}

//Is called on remove button press of a game div and removes it from local storage and the library
function erase(event){
    var targ = $(event.target).parent().parent().parent();
    var key = targ.attr('class').split(' ')[0].replace(/_/g,' ');
    var library = JSON.parse(window.localStorage.getItem('data'));
    delete library[key];
    window.localStorage.setItem('data', JSON.stringify(library));
    targ.remove();
}

//activated when a checkbox is checked in filter section and it send the value to filter in local storage
function check(e){
    var change = e.target.id;
    console.log(change);
    $('input:radio').prop('checked',false);
    $('#' + change).prop('checked',true);
    var filt = JSON.parse(window.localStorage.getItem('filter'));
    filt[0] = e.target.id;
    window.localStorage.setItem('filter', JSON.stringify(filt));
    loadGames();
}

//adds a filter
function addFilter(){
    var addVal = $('#filterBox').val();
    if(addVal !== ''){
        var filt = JSON.parse(window.localStorage.getItem('filter'));
        filt[1].push(addVal);
        console.log(filt);
        window.localStorage.setItem('filter', JSON.stringify(filt));

        $('#filters').append(filterTag.replace('<!--repl-->', addVal));
        loadGames();
    }
    $('#filterBox').val('');
}

//removes a filter
function remFilt(event){
    var remVal = $(event.target).html();
    var filt = JSON.parse(window.localStorage.getItem('filter'));
    var index = filt[1].indexOf(remVal);

    if (index > -1) {
        filt[1].splice(index, 1);
    }

    window.localStorage.setItem('filter', JSON.stringify(filt));
    $(event.target).remove();
    loadGames();
}

//responsible for the slider
function range(event){
    var value = $(event.target).val();
    $('.slidecontainer').children('p').text(value);

    //makes it so that the below function will only activate if the slider
    //doesn't change for a certain amount of time
    clearTimeout(timeout);

    timeout = setTimeout(function () {
        var filt = JSON.parse(window.localStorage.getItem('filter'));
        filt[2] = parseInt(value);
        window.localStorage.setItem('filter', JSON.stringify(filt));

        loadGames();
    }, 250);
}

function searching(event){
    //makes it so that the below function will only activate if the search
    //doesn't change for a certain amount of time
    clearTimeout(timeout);

    timeout = setTimeout(function () {
        var value = $(event.target).val();
        value = value.replace(/\s/g,'_');
        window.search = value;
        loadGames();
    }, 500);
}

//Drops down the info which it dynamically gets from local storage. It isn't
//ajax but it does the same thing as ajax. I really didn't want files. and wikipedia
//api takes times. So I initialise and data during the form submit stage and insert
//the initialised data, so that divs and info will display quickly on the page.
function info (event) {
    var self = $(event.target).parent('div').parent('div').parent('div');
    //If info is open, it will close. If info is closed it will open.
    if($(self).parent('#library').length > 0){
        if($(self).children('div').children('p').length > 0){
            $(self).children('div').children('p').slideUp('fast');
            var self = $(self);
            setTimeout(function () {
                self.children('div').children('p').remove();
            }, 100);
            $(self).css('margin-bottom','1%');
        } else {
            var data = window.localStorage.getItem('data');
            data = JSON.parse(data);
            key = $(self).attr('class').split(' ')[0].replace(/_/g,' ');
            $(self).children('div').append("<p style='margin-bottom:2%; margin-top:-1%; display:none;'>" + data[key]['descript'] + "</p>");
            $(self).children('div').children('p').slideDown();
            $(self).css('margin-bottom','8%');
        }
    }
};    
