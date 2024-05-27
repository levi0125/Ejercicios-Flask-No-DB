let tot

window.onload=function(){
    EvFinDocumento()
    tot=document.getElementsByName("total");
    if(tot[1].innerHTML.length<1){
        for(let b=0;b<2;b++){
            tot[b].style.display="none"
        }
    }    
}