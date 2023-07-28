//loads page
function loadPage(role){
    $("body").fadeIn();
    // When role is received and document is loaded, it'll go through and check if any of these pages were the page that was last open.
    var frontpagelastopen = window.localStorage.getItem('frontpageopen')
    var librarylastopen = window.localStorage.getItem('libraryopen')
    var aboutpagelastopen = window.localStorage.getItem('aboutpageopen')
    var tacticalpagelastopen = window.localStorage.getItem('tacticspageopen')
    var commandpagelastopen = window.localStorage.getItem('commandpageopen')
    var helmpagelastopen = window.localStorage.getItem('helmpageopen')
    var adminpagelastopen = window.localStorage.getItem('adminpageopen')
    var operationspagelastopen = window.localStorage.getItem('operationspageopen')
    var sciencepagelastopen = window.localStorage.getItem('sciencepageopen')
    if (window.localStorage.getItem('frontpageopen')  != 'yes') {
        if (window.localStorage.getItem('libraryopen') != 'yes') {
            if (window.localStorage.getItem('aboutpageopen') != 'yes') {
                if (window.localStorage.getItem('tacticspageopen') != 'yes' || role !== 'tactics') {
                    if (window.localStorage.getItem('commandpageopen') != 'yes' || role !== 'command') {
                        if (window.localStorage.getItem('helmpageopen') != 'yes' || role !== 'helm') {
                            if (window.localStorage.getItem('adminpageopen') != 'yes' || role !== 'admin') {
                                if (window.localStorage.getItem('operationspageopen') != 'yes' || role !== 'operations') {
                                    if (window.localStorage.getItem('sciencepageopen') != 'yes' || role !== 'science') {
                                        $("#container").load("static/ajax-elements/frontpage.html");
                                        // First loads the front page if nothing else was loaded prior.
                                    }
                                }
                            }
                        }
                    }
                }
            } 
        }
    }
    // If one of the pages read as 'yes' and was loaded in a prior session, fade in that page.
    if (frontpagelastopen == 'yes') {
        $("#container").load("static/ajax-elements/frontpage.html").fadeIn();
    }
    if (librarylastopen == 'yes') {
        $.getJSON(window.location.href + "/libraryLoad", 
        function(data) {
            console.log(data)
            $("#container").hide().html(data).fadeIn();
        });
    }
    if (aboutpagelastopen == 'yes') {
        $("#container").load("static/ajax-elements/aboutpage.html").fadeIn();
    }
    // All of the role last open pages have checks to see if their current role matches up. Otherwise, it will not fade in, and will
    // instead go to the front page.
    if (tacticalpagelastopen == 'yes' && role === 'tactics') {
        $("#container").load("static/ajax-elements/tactics.html").fadeIn();
    }
    if (commandpagelastopen == 'yes' && role === 'command') {
        $("#container").load("static/ajax-elements/command.html").fadeIn();
    }
    if (helmpagelastopen == 'yes' && role === 'helm') {
        $("#container").load("static/ajax-elements/helm.html").fadeIn();
    }
    if (adminpagelastopen == 'yes' && role === 'admin') {
        $("#container").load("static/ajax-elements/admin.html").fadeIn();
    }
    if (operationspagelastopen == 'yes' && role === 'operations') {
        $("#container").load("static/ajax-elements/operations.html").fadeIn();
    }
    if (sciencepagelastopen == 'yes' && role === 'science') {
        $("#container").load("static/ajax-elements/science.html").fadeIn();
    }
    $("#frontpagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-dodger-blue-bg');
            $("#header_2").addClass('lcars-dodger-blue-bg');
            $("#header_3").addClass('lcars-dodger-blue-bg');
            $("#footer_1").addClass('lcars-dodger-blue-bg');
            $("#footer_2").addClass('lcars-dodger-blue-bg');
            $("#footer_3").addClass('lcars-dodger-blue-bg');
            $("#left_bar").addClass('lcars-dodger-blue-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-dodger-blue-bg');
            $("#header_2").removeClass('lcars-dodger-blue-bg');
            $("#header_3").removeClass('lcars-dodger-blue-bg');
            $("#footer_1").removeClass('lcars-dodger-blue-bg');
            $("#footer_2").removeClass('lcars-dodger-blue-bg');
            $("#footer_3").removeClass('lcars-dodger-blue-bg');
            $("#left_bar").removeClass('lcars-dodger-blue-bg');
        }
    );
    $("#librarybutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-rust-bg');
            $("#header_2").addClass('lcars-rust-bg');
            $("#header_3").addClass('lcars-rust-bg');
            $("#footer_1").addClass('lcars-rust-bg');
            $("#footer_2").addClass('lcars-rust-bg');
            $("#footer_3").addClass('lcars-rust-bg');
            $("#left_bar").addClass('lcars-rust-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-rust-bg');
            $("#header_2").removeClass('lcars-rust-bg');
            $("#header_3").removeClass('lcars-rust-bg');
            $("#footer_1").removeClass('lcars-rust-bg');
            $("#footer_2").removeClass('lcars-rust-bg');
            $("#footer_3").removeClass('lcars-rust-bg');
            $("#left_bar").removeClass('lcars-rust-bg');
        }
    );
    $("#aboutpagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-eggplant-bg');
            $("#header_2").addClass('lcars-eggplant-bg');
            $("#header_3").addClass('lcars-eggplant-bg');
            $("#footer_1").addClass('lcars-eggplant-bg');
            $("#footer_2").addClass('lcars-eggplant-bg');
            $("#footer_3").addClass('lcars-eggplant-bg');
            $("#left_bar").addClass('lcars-eggplant-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-eggplant-bg');
            $("#header_2").removeClass('lcars-eggplant-bg');
            $("#header_3").removeClass('lcars-eggplant-bg');
            $("#footer_1").removeClass('lcars-eggplant-bg');
            $("#footer_2").removeClass('lcars-eggplant-bg');
            $("#footer_3").removeClass('lcars-eggplant-bg');
            $("#left_bar").removeClass('lcars-eggplant-bg');
        }
    );
    $("#tacticspagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-tamarillo-bg');
            $("#header_2").addClass('lcars-tamarillo-bg');
            $("#header_3").addClass('lcars-tamarillo-bg');
            $("#footer_1").addClass('lcars-tamarillo-bg');
            $("#footer_2").addClass('lcars-tamarillo-bg');
            $("#footer_3").addClass('lcars-tamarillo-bg');
            $("#left_bar").addClass('lcars-tamarillo-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-tamarillo-bg');
            $("#header_2").removeClass('lcars-tamarillo-bg');
            $("#header_3").removeClass('lcars-tamarillo-bg');
            $("#footer_1").removeClass('lcars-tamarillo-bg');
            $("#footer_2").removeClass('lcars-tamarillo-bg');
            $("#footer_3").removeClass('lcars-tamarillo-bg');
            $("#left_bar").removeClass('lcars-tamarillo-bg');
        }
    );
    $("#adminpagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-navy-blue-bg');
            $("#header_2").addClass('lcars-navy-blue-bg');
            $("#header_3").addClass('lcars-navy-blue-bg');
            $("#footer_1").addClass('lcars-navy-blue-bg');
            $("#footer_2").addClass('lcars-navy-blue-bg');
            $("#footer_3").addClass('lcars-navy-blue-bg');
            $("#left_bar").addClass('lcars-navy-blue-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-navy-blue-bg');
            $("#header_2").removeClass('lcars-navy-blue-bg');
            $("#header_3").removeClass('lcars-navy-blue-bg');
            $("#footer_1").removeClass('lcars-navy-blue-bg');
            $("#footer_2").removeClass('lcars-navy-blue-bg');
            $("#footer_3").removeClass('lcars-navy-blue-bg');
            $("#left_bar").removeClass('lcars-navy-blue-bg');
        }
    );
    $("#commandpagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-atomic-tangerine-bg');
            $("#header_2").addClass('lcars-atomic-tangerine-bg');
            $("#header_3").addClass('lcars-atomic-tangerine-bg');
            $("#footer_1").addClass('lcars-atomic-tangerine-bg');
            $("#footer_2").addClass('lcars-atomic-tangerine-bg');
            $("#footer_3").addClass('lcars-atomic-tangerine-bg');
            $("#left_bar").addClass('lcars-atomic-tangerine-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-atomic-tangerine-bg');
            $("#header_2").removeClass('lcars-atomic-tangerine-bg');
            $("#header_3").removeClass('lcars-atomic-tangerine-bg');
            $("#footer_1").removeClass('lcars-atomic-tangerine-bg');
            $("#footer_2").removeClass('lcars-atomic-tangerine-bg');
            $("#footer_3").removeClass('lcars-atomic-tangerine-bg');
            $("#left_bar").removeClass('lcars-atomic-tangerine-bg');
        }
    );
    $("#operationspagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-medium-carmine-bg');
            $("#header_2").addClass('lcars-medium-carmine-bg');
            $("#header_3").addClass('lcars-medium-carmine-bg');
            $("#footer_1").addClass('lcars-medium-carmine-bg');
            $("#footer_2").addClass('lcars-medium-carmine-bg');
            $("#footer_3").addClass('lcars-medium-carmine-bg');
            $("#left_bar").addClass('lcars-medium-carmine-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-medium-carmine-bg');
            $("#header_2").removeClass('lcars-medium-carmine-bg');
            $("#header_3").removeClass('lcars-medium-carmine-bg');
            $("#footer_1").removeClass('lcars-medium-carmine-bg');
            $("#footer_2").removeClass('lcars-medium-carmine-bg');
            $("#footer_3").removeClass('lcars-medium-carmine-bg');
            $("#left_bar").removeClass('lcars-medium-carmine-bg');
        }
    );
    $("#helmpagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-bourbon-bg');
            $("#header_2").addClass('lcars-bourbon-bg');
            $("#header_3").addClass('lcars-bourbon-bg');
            $("#footer_1").addClass('lcars-bourbon-bg');
            $("#footer_2").addClass('lcars-bourbon-bg');
            $("#footer_3").addClass('lcars-bourbon-bg');
            $("#left_bar").addClass('lcars-bourbon-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-bourbon-bg');
            $("#header_2").removeClass('lcars-bourbon-bg');
            $("#header_3").removeClass('lcars-bourbon-bg');
            $("#footer_1").removeClass('lcars-bourbon-bg');
            $("#footer_2").removeClass('lcars-bourbon-bg');
            $("#footer_3").removeClass('lcars-bourbon-bg');
            $("#left_bar").removeClass('lcars-bourbon-bg');
        }
    );
    $("#sciencepagebutton").hover(
        function () { // If any of these buttons are hovered over, it will add a colour class to each of the border elements.
            $("#header_1").addClass('lcars-bahama-blue-bg');
            $("#header_2").addClass('lcars-bahama-blue-bg');
            $("#header_3").addClass('lcars-bahama-blue-bg');
            $("#footer_1").addClass('lcars-bahama-blue-bg');
            $("#footer_2").addClass('lcars-bahama-blue-bg');
            $("#footer_3").addClass('lcars-bahama-blue-bg');
            $("#left_bar").addClass('lcars-bahama-blue-bg');
        },
        function () { // When the hover ceases, it will then remove the colour class from each of the border elements.
            $("#header_1").removeClass('lcars-bahama-blue-bg');
            $("#header_2").removeClass('lcars-bahama-blue-bg');
            $("#header_3").removeClass('lcars-bahama-blue-bg');
            $("#footer_1").removeClass('lcars-bahama-blue-bg');
            $("#footer_2").removeClass('lcars-bahama-blue-bg');
            $("#footer_3").removeClass('lcars-bahama-blue-bg');
            $("#left_bar").removeClass('lcars-bahama-blue-bg');
        }
    );
    $("#frontpagebutton").click(function () { // If this button is pressed, fades in the Front Page.
        window.localStorage.setItem('frontpageopen', 'yes')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'no')
        window.localStorage.setItem('tacticspageopen', 'no')
        window.localStorage.setItem('commandpageopen', 'no')
        window.localStorage.setItem('adminpageopen', 'no')
        window.localStorage.setItem('helmpageopen', 'no')
        window.localStorage.setItem('operationspageopen', 'no')
        window.localStorage.setItem('sciencepageopen', 'no')
        $("#container").hide().load("static/ajax-elements/frontpage.html").fadeIn();
    });
    $("#aboutpagebutton").click(function () { // If this button is pressed, fades in the About Page.
        window.localStorage.setItem('frontpageopen', 'no')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'yes')
        window.localStorage.setItem('tacticspageopen', 'no')
        window.localStorage.setItem('commandpageopen', 'no')
        window.localStorage.setItem('adminpageopen', 'no')
        window.localStorage.setItem('helmpageopen', 'no')
        window.localStorage.setItem('operationspageopen', 'no')
        window.localStorage.setItem('sciencepageopen', 'no')
        $("#container").hide().load("static/ajax-elements/aboutpage.html").fadeIn();
    });
    $("#tacticspagebutton").click(function () { // If this button is pressed, fades in the Tactics Page.
        window.localStorage.setItem('frontpageopen', 'no')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'no')
        window.localStorage.setItem('tacticspageopen', 'yes')
        window.localStorage.setItem('commandpageopen', 'no')
        window.localStorage.setItem('adminpageopen', 'no')
        window.localStorage.setItem('helmpageopen', 'no')
        window.localStorage.setItem('operationspageopen', 'no')
        window.localStorage.setItem('sciencepageopen', 'no')
        $("#container").hide().load("static/ajax-elements/tactics.html").fadeIn();
    });
    $("#commandpagebutton").click(function () { // If this button is pressed, fades in the Command Page.
        window.localStorage.setItem('frontpageopen', 'no')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'no')
        window.localStorage.setItem('tacticspageopen', 'no')
        window.localStorage.setItem('commandpageopen', 'yes')
        window.localStorage.setItem('adminpageopen', 'no')
        window.localStorage.setItem('helmpageopen', 'no')
        window.localStorage.setItem('operationspageopen', 'no')
        window.localStorage.setItem('sciencepageopen', 'no')
        $("#container").hide().load("static/ajax-elements/command.html").fadeIn();
    });
    $("#adminpagebutton").click(function () { // If this button is pressed, fades in the Admin Page.
        window.localStorage.setItem('frontpageopen', 'no')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'no')
        window.localStorage.setItem('tacticspageopen', 'no')
        window.localStorage.setItem('commandpageopen', 'no')
        window.localStorage.setItem('adminpageopen', 'yes')
        window.localStorage.setItem('helmpageopen', 'no')
        window.localStorage.setItem('operationspageopen', 'no')
        window.localStorage.setItem('sciencepageopen', 'no')
        $("#container").hide().load("static/ajax-elements/admin.html").fadeIn();
    });
    $("#helmpagebutton").click(function () { // If this button is pressed, fades in the Helm Page.
        window.localStorage.setItem('frontpageopen', 'no')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'no')
        window.localStorage.setItem('tacticspageopen', 'no')
        window.localStorage.setItem('commandpageopen', 'no')
        window.localStorage.setItem('adminpageopen', 'no')
        window.localStorage.setItem('helmpageopen', 'yes')
        window.localStorage.setItem('operationspageopen', 'no')
        window.localStorage.setItem('sciencepageopen', 'no')
        $("#container").hide().load("static/ajax-elements/helm.html").fadeIn();
    });
    $("#operationspagebutton").click(function () { // If this button is pressed, fades in the Operations Page.
        window.localStorage.setItem('frontpageopen', 'no')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'no')
        window.localStorage.setItem('tacticspageopen', 'no')
        window.localStorage.setItem('commandpageopen', 'no')
        window.localStorage.setItem('adminpageopen', 'no')
        window.localStorage.setItem('helmpageopen', 'no')
        window.localStorage.setItem('operationspageopen', 'yes')
        window.localStorage.setItem('sciencepageopen', 'no')
        $("#container").hide().load("static/ajax-elements/operations.html").fadeIn();
    });
    $("#sciencepagebutton").click(function () { // If this button is pressed, fades in the Science Page.
        window.localStorage.setItem('frontpageopen', 'no')
        window.localStorage.setItem('libraryopen', 'no')
        window.localStorage.setItem('aboutpageopen', 'no')
        window.localStorage.setItem('tacticspageopen', 'no')
        window.localStorage.setItem('commandpageopen', 'no')
        window.localStorage.setItem('adminpageopen', 'no')
        window.localStorage.setItem('helmpageopen', 'no')
        window.localStorage.setItem('operationspageopen', 'no')
        window.localStorage.setItem('sciencepageopen', 'yes')
        $("#container").hide().load("static/ajax-elements/science.html").fadeIn();
    });
}

$("body").hide();
//connects to socket which is on the flask port
var socket = io.connect(window.location.href);
console.log(window.location.href)

//A blank initial role, also instantiates as a global
var role = '';

//To log that we connected, role is made blank again just incase
socket.on('connect', function(){
    $("#adminpagebutton").hide();
    $("#commandpagebutton").hide();
    $("#tacticspagebutton").hide();
    $("#operationspagebutton").hide();
    $("#helmpagebutton").hide();
    $("#sciencepagebutton").hide();
    role = '';
});

//The handshake gives us our role data and then it is used to get the display.
socket.on('handshake', function(val){
    if(role === ''){
        role = JSON.parse(val);
        $("#" + role + "pagebutton").show();
        loadPage(role);
    }
});

//Closes chat sections
function closeForm(){
    $('#chatForm').hide();
}

//Opens chat
function openForm(){
    $('#chatForm').show();
}

//submits the chat message to the chat
function formSubmit(){
    var inputVal = $('#chatMessageInp').val();
    $('#chatMessageInp').val('');
    console.log(inputVal)
    if(inputVal !== ''){
        inputVal = role + ': ' + inputVal;
        socket.emit('chatadd', inputVal);  
    }
    return true
}

//sends a private chat message, so its to a specific person
function chat(sendTo){
    console.log(sendTo)
    if($('.chatSend' + sendTo).val() !== ''){
        socket.emit('chatpriv', JSON.stringify([$('.chatSend' + sendTo).val(), sendTo, role]));
        $('.chatSend' + sendTo).val('');
    }
}

//Adds chat message to chat, this chat message is from the server so it can be from anyone not just you
socket.on('chat', function(val){
    $('#chatList').append('<li>' + val + '</li>')
    $('#chatList').find('li:first').remove();
    $("#chatList").animate({ scrollTop: $('#chatList').prop("scrollHeight")}, 1000);
});

//Send your screen over to server
socket.on('screenreq', function(val){
    socket.emit('screen',JSON.stringify([role,$('#container').html()]));
});

//Puts a screen value of someone else in the slot they belong. This is only used for admin and command who can survey screens
socket.on('screenVal', function(val){
    var value = JSON.parse(val);
    console.log(value)
    $('.screen' + value[0]).each(function(){$(this).html(value[1])});
    $('#mod' + value[0] + 'screen').each(function(){$(this).html(value[1])});
});

//Adds to private chat when the value of the message and of who is receiving are acquired
socket.on('chatpriv', function(val){
    var lis = JSON.parse(val)
    console.log(lis)
    $('.chatList' + lis[1]).each(function(){$(this).append('<li class="flow-text">' + lis[2] + ': ' + lis[0] + '</li>')});
    $('.chatList' + lis[1]).each(function(){$(this).find('li:first').remove()});
});

//opens modal
function openModal(id){
    $('#modalCont').html($('.' + id).html());
    $('#screenMod').css('z-index', 1000).show();
}

//closes modal
function closeModal(){
    $('#screenMod').hide();
}

//sends alert
function alertSet(color) {
    socket.emit('sendAlert',color)
}

//sets alert
socket.on('alert', function(val){
    $("#alertslot").css('background', val);
});

//sends role over
socket.on('roleCheck', function(val){
    socket.emit('roleSend', role);
});

//sends notes over
socket.on('getNotes', function(){
    $('.note').each(function(){
        console.log($(this))
        socket.emit('saveNotes', JSON.stringify([$(this).attr('class').split(" ")[0],$(this).val()]));
    });
});

//gets notes from server and replaces the current ones
socket.on('syncNote', function(val){
    value = JSON.parse(val);
    $('.' + value[0]).val(value[1]);
});

function libLoad () { // This will load the library if it is currently active.
    window.localStorage.setItem('frontpageopen', 'no')
    window.localStorage.setItem('libraryopen', 'yes')
    window.localStorage.setItem('aboutpageopen', 'no')
    window.localStorage.setItem('tacticspageopen', 'no')
    window.localStorage.setItem('commandpageopen', 'no')
    window.localStorage.setItem('adminpageopen', 'no')
    window.localStorage.setItem('helmpageopen', 'no')
    window.localStorage.setItem('operationspageopen', 'no')
    window.localStorage.setItem('sciencepageopen', 'no')
    $.getJSON(window.location.href + "libraryLoad", 
        function(data) {
            $("#container").hide().html(data).fadeIn();
    });
}
function textAreaAdjust(o) { // This adjusts the area of all textarea boxes.
    o.style.height = "1px";
    o.style.height = (25 + o.scrollHeight) + "px";
}

//This updates notes
socket.on('updateNotes', function(){
    $('.note').each(function(){
        socket.emit('reqNotes', $(this).attr('class').split(" ")[0]);
    });
});