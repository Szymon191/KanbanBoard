var stat = "show"

function check_width(){
    var obj = document.getElementById('right')

    if(stat == "show" ){
        obj.style.width = "100%"
        
        stat = "close"
        console.log(stat)
    }else if(stat == "close"){
        obj.style.width = "80%"
        stat = "show"
        console.log(stat)
    }
}