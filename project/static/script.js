let penColour = 'black';

function setPixelColour(pixel){
  pixel.style.backgroundColor = penColour;
  document.getElementById(pixel.id).setAttribute("value",penColour);
}

function setPenColour(color) {
  penColour = color;
}

function sendDraw(){

  const x = document.getElementsByClassName("pixel");
  let colors = [];

  for (let i = 0; i < x.length; i++) {

    x[i].getAttribute("value") == null
      ? colors.push("blank")
      : colors.push(x[i].getAttribute("value"))
  }

  console.log(colors);

  const URL = '/profile'
  const xhr = new XMLHttpRequest();
  sender = JSON.stringify(colors)
  xhr.open('POST', URL);
  xhr.send(sender);

}