let penColour;
let color;

let selectedDraw = 1;
let drawOne = [];
let drawTwo = [];
let actualDraw = [];
let randomDraw = [];

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
  
  selectedDraw == 1 
  ?  draw = drawOne
  :  draw = drawTwo; 

  const URL = '/profile'
  const xhr = new XMLHttpRequest();
  sender = JSON.stringify(draw);
  xhr.open('POST', URL);
  xhr.send(sender);

}

function minusDraw() {
  if($('#buttonList').find('button').length > 3){ 
    $('#buttonList button').remove(":contains('2')");
    drawTwo = [];
  }else
    alert('¡No se puede tener menos de un dibujo!');
  return false;  
}


function addDraw() {
  if($('#buttonList').find('button').length < 4) 
    $('#buttonList').append('<button class="pixelButton" onclick="selectDraw(this)">2</button>');
  else 
    alert('¡Ya no caben más dibujos!');
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
    : actualDraw.push(colorDict[$(elem).css("background-color")]);
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

function deleteSavedDraw(){

  selectedDraw == 1 
  ?  drawOne = []
  :  drawTwo = []; 

  deleteDraw()
}

function randomizer(){

  randomNumber = Math.floor(Math.random() * (4 - 1)) + 1;
  console.log(randomNumber);
  randomDraw = randomDict[randomNumber];

  deleteDraw();

  var x = document.getElementsByClassName("pixel");
  for (let i = 0; i < x.length; i++) {
    x[i].style.backgroundColor = randomDraw[i];
  }
}