function toggle_hidden(event){
    var activeInfo = document.querySelector('.info-content.active')
    if(activeInfo){
        document.querySelector('.info-content.active').classList.remove('active');
    }
    event.target.parentElement.classList.toggle("active");
}