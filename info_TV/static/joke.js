///////////////////////////////////////////////////////////////////////////////////////////
const JOKE_API_ENDPOINT = 'http://127.0.0.1:5000/joke'
jsonData = {}

async function getJokes() {
  try {
    // Fetches data from the server
    const response = await fetch(JOKE_API_ENDPOINT);

    // Checks if the connection is okay
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    // Converts the "promise" to JSON format
    const data = await response.json();

    // Stores JSON data in the jsonData object
    jsonData = data;

    console.log('Joke data fetched successfully:', data);  // Logs success message to console

  } catch (error) {
    // If there's an issue with the code, this error message is displayed
    console.error('There was a problem with the fetch operation:', error);
  }
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function fireball() {
  let fireBall_move = -1000;
  let fireBall_size = 100;
  var fireBall = document.getElementById("fireBall");

  // Creates a cool fireball effect, still in progress
  let The_interval = setInterval(
    function fire() {
      fireBall_move++;
      fireBall.style.left = fireBall_move + "px";

      if(fireBall_move == 8000) {
        clearInterval(The_interval);
      }

    }, 1
  );
};

function tell_joke() {
  const setupcontainer = document.getElementById("setup")
  const deliverycontainer = document.getElementById("punchline")

  var joke = jsonData[0]

  setupcontainer.innerHTML = joke["setup"]
  deliverycontainer.innerHTML = joke["punchline"]
  console.log(jsonData[0])
}

async function crack_a_joke() {
  await getJokes();
  tell_joke();
}

crack_a_joke();

// Fetch a new joke every 30 minutes
setInterval(crack_a_joke, 1800000)

if (crack_a_joke) {
  fireBall_move = "-500px"
  fireball();
}
