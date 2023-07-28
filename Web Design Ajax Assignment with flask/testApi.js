$.ajax({
    url: 'http://127.0.0.1:5000/give?q=' + JSON.stringify({'Game':'League of Legends'}),
    type: 'GET',
    dataType:"jsonp",
}).fail((resp)=>{
    console.log(resp);
})
