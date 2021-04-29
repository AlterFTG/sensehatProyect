let penColour = 'black';

function setPixelColour(pixel){
  pixel.style.backgroundColor = penColour;
}

function setPenColour(color) {
  penColour = color;
}

function setTextColor(color) {
  document.getElementById("textColor").value = color;
  console.log(color);
}