var template = $("#table-time-template").html();
var templateForm = $("#time-input-template").html();
var resetTemplate = $("#reset-template").html();
var divTemplate = $("#div-template").html();
var tasks = [];

$('#AddTask').hide();

function setDates(date = ''){
    n =  new Date();

    if(date !== ''){
        n = new Date(date);
    }

    day = n.getDay() - 1
    
    if(day === -1){
        day = 6
    }

    n.setDate(n.getDate() - day);

    y = n.getFullYear();
    m = n.getMonth() + 1;
    d = n.getDate();

    nd = new Date();
    nd.setDate(n.getDate() + 6);

    yn = nd.getFullYear();
    mn = nd.getMonth() + 1;
    dn = nd.getDate();

    var date = d + "/" + m + "/" + y + ' - ' + dn + "/" + mn + "/" + yn;

    document.getElementById("date").innerHTML = date;
}

setDates();

function create(){
    for (var i = 0; i < 12; i++) {
        var taskHTML = template.replace("<!-- TASK_NAME -->", String(i) + ' AM');
        $('#Table').append(taskHTML);
        $('#Mon').attr('id','Mon_' + String(i));
        $('#Tue').attr('id','Tue_' + String(i));
        $('#Wed').attr('id','Wed_' + String(i));
        $('#Thu').attr('id','Thu_' + String(i));
        $('#Fri').attr('id','Fri_' + String(i));
        $('#Sat').attr('id','Sat_' + String(i));
        $('#Sun').attr('id','Sun_' + String(i));
    }
    
    for (var i = 0; i < 12; i++) {
        var taskHTML = template.replace("<!-- TASK_NAME -->", String(i) + ' PM');
        $('#Table').append(taskHTML);
        $('#Mon').attr('id','Mon_' + String(i + 12));
        $('#Tue').attr('id','Tue_' + String(i + 12));
        $('#Wed').attr('id','Wed_' + String(i + 12));
        $('#Thu').attr('id','Thu_' + String(i + 12));
        $('#Fri').attr('id','Fri_' + String(i + 12));
        $('#Sat').attr('id','Sat_' + String(i + 12));
        $('#Sun').attr('id','Sun_' + String(i + 12));
    }
}

create();

function getFormData(){
    var Taskname = $('#Task').val();
    var Color = $('#Color').val();

    if(Taskname === '' || Color === ''){
        return([Taskname,Color,[]]);
    }

    var timeSlots = [];

     $('.times').each(function(){
        var time = [];
        time.push($(this).find('#day').val());
        time.push($(this).find('#time1').val());
        time.push($(this).find('#time2').val());

        if(time[0] === '' || time[1] === '' || time[2] === ''){
            return([Taskname,Color,[]]);
        }

        timeSlots.push(time);
    });

    $('#inputs').html(resetTemplate);
    $('#AddTask').toggle();
    return([Taskname,Color,timeSlots]);
}

$('#add').on('click', function(event) {
    $('#AddTask').toggle();
});

$('#Addtime').click(function(event) {
    $('#inputs').append(templateForm);
});

$('#Submit').click(function(event) {
    var data = getFormData();
    var storeIn = data[0];
    var col = data[1];
    var timeFrames = data[2];

    for(i in timeFrames){
        var a = new CreateTask(storeIn, col, timeFrames[i]);
        a.drawTask();
    }
});

class CreateTask{
    constructor(label,color,time){
        this.label = label;
        this.color = color;
        this.time = time;
        this.x = 0;
        this.y = 0;
    }

    drawTask(){
        var taskDay = this.time[0];
        var time1 = this.time[1].split(':');
        var time2 = this.time[2].split(':');
        var id1 = $('#' + taskDay + '_' + String(parseInt(time1[0])));
        var id2 = $('#' + taskDay + '_' + String(parseInt(time2[0])));

        var divHTML = divTemplate.replace("<!-- TASK_NAME -->", this.label);
        
        $('body').append(divHTML);

        var addedY = parseInt(id1.outerHeight())/60;
        this.y = parseInt(id1.offset().top) + (parseInt(time1[1])*addedY);
        this.x = id1.offset().left;
        var botY = parseInt(id2.offset().top) + (parseInt(time2[1])*addedY);
        var height = botY - this.y;
        
        $('.edit > h4').css({'text-align':'center','color':'white','font-size':'100%'});
        $('.edit').css('width',id1.outerWidth() +'px');
        $('.edit').css('height',height +'px');
        $('.edit').css('left',this.x + 'px');
        $('.edit').css('top',this.y + 'px');
        $('.edit').css('background',this.color);
        $('.edit').css('border-radius','1%');
        $('.edit').removeClass('edit').addClass('task');
    }
}

