var myLocation = document.getElementById("myLocation")
const mainBody = document.getElementById("main")

mainBody.onload = () => {
    console.log("check")
    if (navigator.geolocation) {
        myLocation.innerText = "detecting the loaction...."
        navigator.geolocation.getCurrentPosition(onSuccess, onError)
    } else {
        myLocation.innerText = "your browser is not suported"
    }
}
function onSuccess(position) {
    myLocation.innerText = "Detecting your location...";
    let { latitude, longitude } = position.coords; //getting latitude and longitude properties value from coords obj
    //sending get request to the api with passing latitude and longitude coordinates of the user position
    fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=f0073ab6412943c6a8903c04b200bf58`)
        //parsing json data into javascript object and returning it and in another then function receiving the object that is sent by the api
        .then(response => response.json()).then(response => {
            let allDetails = response.results[0].components; //passing components object to allDetails variable
            console.table(allDetails);
            let { road, postcode, neighbourhood, college, county, country } = allDetails; //getting country, postcode, country properties value from allDetails obj
            myLocation.innerText = `Your Location is: Around $ ${neighbourhood}, ${county} ${postcode}, ${country}`; //passing these value to the myLocation innerText
        }).catch(() => { //if error any error occured
            myLocation.innerText = "Something went wrong";
        });
}

function onError() {
    if (error.code == 1) { //if user denied the request
        myLocation.innerText = "You denied the request";
    } else if (error.code == 2) { //if location in not available
        myLocation.innerText = "Location is unavailable";
    } else { //if other error occured
        myLocation.innerText = "Something went wrong";
    }
    myLocation.setAttribute("disabled", "true");
}