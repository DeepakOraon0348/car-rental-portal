const car = JSON.parse(sessionStorage.getItem("car"));

const container = document.getElementById("car-detail");

function goToBooking() {
    window.location.href = "/car-detail/";
}

if (!car) {
    container.innerHTML = "<h3>No car selected</h3>";
} else {
    container.innerHTML = `
  <div class="col-md-12 col-sm-12 col-12">
    <div class="card" style="width:100%">
      <img src="${car.image}" class="card-img-top">

      <div class="card-body">
        <h2>${car.brand} ${car.name}</h2>
        
        <div class="features">
        <span><p><b>⛽Fuel:</b> ${car.fuel}</p></span>
        <span><p><b>👥 Seats:</b> ${car.seats}</p></span>
        <span><p><b>⚙️ Transmission:</b> ${car.transmission}</p></span>
        <span><p><b>❄️ AC:</b> ${car.ac ? "Yes" : "No"}</p></span>
        </div>
        <div class="car-book">
           <h4>₹${car.price}/day</h4>
            <button class="btn btn-success" onclick="goToBooking()">Book Now</button>
        </div>
      </div>
    </div>
    </div>
  `;
}