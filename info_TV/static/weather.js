////////////////////////////////////

const WEATHER_API_ENDPOINT = 'http://127.0.0.1:5000/weather'

async function getWeather() {
  try {
    // Fetches data from the server
    const response = await fetch(WEATHER_API_ENDPOINT);

    // Checks if the connection is okay
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    // Converts the "promise" to JSON format
    const data = await response.json();

    // Stores JSON data in the jsonData object
    jsonData = data;

    console.log('Weather data fetched successfully:', data);  // Logs success message to console

  } catch (error) {
    // If there's an issue with the code, this error message is displayed
    console.error('There was a problem with the fetch operation:', error);
  }
}

function show_weather() {
  var now = new Date();
  var hour = now.getHours();
  const weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  let date = now.getDate();
  let month = now.getUTCMonth() + 1;
  let year = now.getFullYear();

  day_in_numbers.innerHTML = date + "." + month + "." + year;

  // Checks if data is ready
  if (jsonData && jsonData.hourly) {
    console.log(jsonData);
    jsonData.hourly.temperature_2m.forEach((index) => {
      document.getElementById("weather_now").innerHTML = (`Temperature: ${jsonData.hourly.temperature_2m[hour]}°C`);
    });
    // If data is not ready
  } else {
    console.log("No weather data available yet.");
  }
  //////////////////
  document.getElementById("week_day").innerHTML = weekday[now.getDay()];
  //////////////////
  document.getElementById("uv_radiation").innerHTML = "UV Index" + ":" + " " + jsonData.daily.uv_index_max;
}

async function loadAndShowWeather() {
  // Waits until data is fetched from the server and converted into the desired JSON format
  await getWeather();
  show_weather();
}

// Fetch weather data after 5 seconds
setTimeout(loadAndShowWeather, 5000);
