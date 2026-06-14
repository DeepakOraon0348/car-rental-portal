const cars = window.cars;
console.log(window.cars);
console.log(window.cars.length);
// const cars = [
//     {
//         id: 1,
//         name: "Swift",
//         brand: "Maruti",
//         price: 1200,
//         fuel: "Petrol",
//         seats: 5,
//         ac: true,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 2,
//         name: "Creta",
//         brand: "Suzuki",
//         price: 2000,
//         fuel: "Diesel",
//         seats: 5,
//         ac: true,
//         transmission: "Automatic",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 3,
//         name: "Bolero",
//         brand: "Mahindra",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 4,
//         name: "Bolero",
//         brand: "Toyoto",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 5,
//         name: "Bolero",
//         brand: "Mahindra",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 6,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 7,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 8,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 9,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 10,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 11,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 12,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 13,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     },
//     {
//         id: 14,
//         name: "Bolero",
//         brand: "Toyota",
//         price: 1500,
//         fuel: "Diesel",
//         seats: 7,
//         ac: false,
//         transmission: "Manual",
//         image: "/static/image/honda-HR-removebg-preview.png"
//     }
// ];
console.log("Hellow DeepaK I AM WORKIGN!");

const container = document.getElementById("car-cards");

function viewDetails(id) {
    const selectedCar = cars.find(car => car.id === id);
    // store in sessionStorage
    sessionStorage.setItem("car", JSON.stringify(selectedCar));
    // redirect to detail page
    window.location.href = "/car-detail/";
}

cars.forEach(car => {
    const card = `
    <div class="col-md-4 col-sm-6 col-12 mb-4">
        <div class="card h-100" onclick="viewDetails(${car.id})">
            <img src="${car.image}" class="card-img-top" alt="${car.name}">
            
            <div class="card-body">
                <h5 class="card-title">${car.brand} ${car.name}</h5>
                <h6 class="card-subtitle mb-2 text-muted">${car.brand}</h6>

                <div class="features">
                    <span>⛽ ${car.fuel}</span>
                    <span>👥 ${car.seats} Seats</span>
                    <span>⚙️ ${car.transmission}</span>
                    <span>❄️ ${car.ac ? "AC" : "Non-AC"}</span>
                </div>

                <div style="display:flex; justify-content:space-between; align-items:center; padding-top:10px;">
                    <div>₹${car.price}/day</div>
                    <button class="btn btn-primary view-btn" onclick="viewDetails(${car.id})"><a>View Detail</a></button>
                </div>
            </div>
        </div>
    </div>
    `;

    container.innerHTML += card;
});

// =================Gsap-section ====================
