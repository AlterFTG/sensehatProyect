colorDict = {"rgb(128, 0, 0)": "maroon", "rgb(165, 42, 42)": "brown", "rgb(160, 82, 45)": "sienna", "rgb(210, 105, 30)": "chocolate", "rgb(220, 20, 60)": "crimson", "rgb(255, 0, 0)": "red", "rgb(250, 128, 114)": "salmon", "rgb(255, 140, 0)": "darkorange", "rgb(255, 165, 0)": "orange",
"rgb(255, 255, 0)": "yellow", "rgb(240, 230, 140)": "khaki","rgb(128, 128, 0)": "olive", "rgb(128, 0, 128)": "purple", "rgb(255, 0, 255)": "fuchsia", "rgb(255, 105, 180)": "hotpink", "rgb(255, 192, 203)": "pink", 
"rgb(255, 255, 255)": "white", "rgb(173, 255, 47)": "greenyellow", "rgb(0, 128, 0)": "green", "rgb(0, 0, 128)": "navy", 
"rgb(0, 0, 255)": "blue", "rgb(0, 255, 255)": "aqua", "rgb(0, 128, 128)": "teal", "rgb(192, 192, 192)": "silver", "rgb(172, 158, 158)": "blank"};

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
  
  selectedDraw == 1 
  ?  draw = drawOne
  :  draw = drawTwo; 

  const URL = '/profile'
  const xhr = new XMLHttpRequest();
  sender = JSON.stringify(drawOne);
  senderTwo = JSON.stringify(drawTwo);
  xhr.open('POST', URL);
  xhr.send(sender, senderTwo);

}

function addDraw() {
  if($('#buttonList').find('button').length < 3) 
    $('#buttonList').append('<button class="button" onclick="selectDraw(this)">2</button>');
  else 
    alert('Ya no caben más dibujos!');
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
