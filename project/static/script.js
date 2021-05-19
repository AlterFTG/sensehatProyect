let penColour = 'black';
let selectedDraw = 1;
let drawOne = [];
let drawTwo = [];
let actualDraw = [];

function setPixelColour(pixel){

  if(pixel.style.backgroundColor == penColour){
    pixel.style.backgroundColor = "";
  }else{
    pixel.style.backgroundColor = penColour;
  }
  document.getElementById(pixel.id).setAttribute("value",penColour);
}

function setPenColour(color) {
  penColour = color;
  document.getElementById("actualColor").style.backgroundColor = penColour;
}

function getDraw(){
  const x = document.getElementsByClassName("pixel");

  let draw = [];


  for (let i = 0; i < x.length; i++) {

    x[i].getAttribute("value") == null
      ? draw.push("blank")
      : draw.push(x[i].getAttribute("value"))
  }

  return draw;
}

function sendDraw(){

  draw = getDraw();

  console.log(draw);

  const URL = '/profile'
  const xhr = new XMLHttpRequest();
  sender = JSON.stringify(draw)
  xhr.open('POST', URL);
  xhr.send(sender);

}

function addDraw() {
  if($('#buttonList').find('button').length < 3) 
    $('#buttonList').append('<button class="button" onclick="selectDraw(this)">2</button>');
  else 
    alert('Ya no caben más items en el contenedor!');
  return false;  
}

function selectDraw(button) {

  deleteDraw();

  selectedDraw = button.innerHTML;

  selectedDraw == 1 
  ?  actualDraw = drawOne
  :  actualDraw = drawTwo; 

  var x = document.getElementsByClassName("pixel");
  for (let i = 0; i < x.length; i++) {
    x[i].style.backgroundColor = actualDraw[i];
  }

}

function getActualDraw(){
  let actualDraw = [];

  $( "#art .pixel" ).each(function( index, elem ) {

    $(elem).css("background-color") == null
    ? actualDraw.push("blank")
    : actualDraw.push($(elem).css("background-color"))


  });

  console.log(actualDraw);

  return actualDraw;
}


function saveDraw(){

  savedDraw = getActualDraw();

  selectedDraw == 1 ? drawOne = savedDraw : drawTwo = savedDraw;
}

function deleteDraw(){
  var x = document.getElementsByClassName("pixel");
  for (let i = 0; i < x.length; i++) {
    x[i].style.backgroundColor = "";
    x[i].setAttribute("value","blank");
  }
}
