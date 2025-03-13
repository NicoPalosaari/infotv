// List of images
const frog_array = [];

// Defines the channel from which we receive the desired image data
var eventSource = new EventSource('/stream-images');

// When a connection to the channel is established
eventSource.onmessage = function (event) {
    var imageName = event.data;
    frog_array.push("/static/SAMMAKKO/" + imageName);
};

// When the connection to the channel fails
eventSource.onerror = function () {
    console.log("SSE connection lost, attempting to reconnect...");
};

// Determines the display time for an image
function ShowImageTime(string) {
    if (isNaN(string)) {
        return 2000;
    } else {
        return string * 1000;
    }
}

let timeInterval = 2000;
let i = 0;

const loop = (i) => {
    setTimeout(() => {
        // Extracts time information from the image name if available
        let path = frog_array[i];
        let position = path.search("O/");
        let name = path.slice(position + 2, path.length);
        let imageTime = name.slice(0, 2);

        timeInterval = ShowImageTime(imageTime);

        // Updates the displayed image
        document.getElementById("imagePlayer").src = frog_array[i];
        i++;

        // Loops through the images
        if (i !== frog_array.length) {
            loop(i);
        } else {
            i = 0;
            loop(i);
        }
    }, timeInterval);
};

loop(i);
