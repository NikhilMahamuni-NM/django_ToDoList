var task = document.querySelectorAll('.task');
var icon = document.querySelector('.icon');
var form = document.querySelector('.todoform')

if (icon){
  icon.addEventListener("click", function(){
    form.classList.toggle('hide')
  })
}
