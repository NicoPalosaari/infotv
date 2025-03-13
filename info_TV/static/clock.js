
let clock = document.getElementById("digiclock")
let jsonData = {};

setInterval(function clockwork() {
  // TIME DATA
  var T = new Date();

  let hour = T.getHours();
  let minute = T.getMinutes();
  let second = T.getSeconds();

  if (minute < 10) {
    clock.innerHTML = hour + "." + 0 + minute + "." + second;
  } else {
    clock.innerHTML = hour + "." + minute + "." + second;
  }
}, 1000);


let day_in_numbers = document.getElementById("day_in_numbers")
