setTimeout(reload, 5000);

function reload(){
    location.reload();
    setTimeout(reload, 5000);
}

function up(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/up", true );
    xmlHttp.send( null );
    location.reload()
}

function down(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/down", true );
    xmlHttp.send( null );
    location.reload()
}