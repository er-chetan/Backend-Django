import datetime  

# Create your views here.  
from django.http import HttpResponse  
from django.shortcuts import render


def index(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse  

def services(request):
    return render(request, 'services.html')

def card(request):
    return render(request, 'card.html')

def about(request):
    html='''

    <style>
    *{
    margin: 0%;
    padding: 0%;
    box-sizing: border-box;
    font-family: 'Gowun+Batang';
}
 
.color-yellow{
    color: #FFBF00;
}
.back-yellow{
    background-color: #FFBF00;
}
 
.color-gray{
    color: #716D6E;
}
.back
.back-gray{
    background-color: #E3E2E2;
}
.drop-menu{
    z-index: 10;
    width: 14%;
}
.gray-border{
    border: 1px solid #cac5c6;
}
.drop-down-item img{
    width: 12%;
}
.drop-down-item:hover{
    background-color: rgba(230, 220, 220, 0.884);
}
.navbar a:hover{
    background-color: #e7e7e7;
}
.navbar a span::before{
    content: "";
    width: 5px;
    height: 40%;
    background-color: #FFBF00;
    position: absolute;
    transform: translate(-10px,6px);
}
.reserve-input{
    color: #716D6E;
    padding: 1px !important;
    background-color: #EFE9E9;
    border: 1px solid #cac5c6;
    /* width: 70%; */
}
.reserve-input label i{
    color: #716D6E;
}
.reserve-input input::placeholder{
    opacity: 1;
}
.reserve-input input.city{
    padding: 10px;
    width: 71%;
}
.reserve-input input.date{
    width: 48%;
}
.car-slider .item img{
    width: 580px !important;
}
.car-slider .owl-nav{
    position: absolute;
    z-index: 4;
    right: 60px;
    bottom: -60px;
}
.car-slider .owl-nav .owl-prev{
    color: #FEE18B !important;
    font-weight: 900 !important;
    font-size: 80px !important;
    background: none !important;
}
.car-slider .owl-nav .owl-next{
    color: #FEE18B !important;
    font-weight: 900 !important;
    font-size: 80px !important;
    background: none !important;
}
.car-slider .owl-nav .owl-prev:hover,.car-slider .owl-nav .owl-next:hover{
    color: white !important;
}
.reserve::before{
    content: "";
    background-color:#FFBF00;
    position: absolute;
    z-index: 10;
    width: 80px;
    bottom: 0px;
    height: 30px;
    left: 48%;
    transform: translateY(-100px);
    rotate: 180deg;
}
.cust-service h1::before{
    content: "";
    width: 10%;
    height: 4px;
    background-color: #FFBF00;
    position: absolute;
    z-index: -1;
    transform: translate(60%,60px);
}
.cust-service .col-5 p{
    font-size: 17px;
}
.cust-service .col-5 span{
    font-size: 30px;
    font-weight: 900;
    padding: 5px 12px;
}
.offers .col-2 i{
    width: 60px;
    height: 58px;
}
.offers .col-2 i.fa-twitter{
    background-color: #36A4CF;
}
.offers .col-2 i.fa-google-plus-g{
    background-color: #D41332;
}
.offers .col-2 i.fa-facebook-f{
    background-color: #365595;
}
.offers .col-4 .email-btn{
    background-color: white;
    padding: 6px;
    margin-left: -4px;
}
.vehicles .col-3 button{
    margin-bottom: 1px;
    text-transform: uppercase;
}
.vehicles .col-3 button.select-btn::after{
    content: "";
    background-color:#FFE599;
    position: absolute;
    z-index: 10;
    width: 25px;
    height: 25px;
    left: 281px;
    transform: rotateX(75deg);
    rotate: 90deg;
}
.vehicle-btn-color{
    background-color: #FFE599;
}
.cars-info .col-4 div.d-flex{
    border-bottom: 1px solid gray;
}
 

    
    </style>


    <div class="container-fluid language">
        <div class="row">
            <div class="col-9">
                <span class="fw-bold h5 float-end mt-2 text-secondary color-gray">Contact:(562) 498-4600</span>
            </div>
            <div class="col-3 positon-relative">
                <button class="px-3 py-2 back-yellow text-white border-0 fw-bold" id="lang-btn">Select your language <i class=" fa-solid fa-square-caret-down"></i></button>        
                <div class="border border-1 mt-1 drop-menu position-absolute bg-white">
                    <div class="col-12 drop-down-item"><img src="./img/united-states-of-america.png" alt=""><span class="ms-2">English</span></div>
                    <div class="col-12 drop-down-item"> <img src="./img/india.png" alt=""><span class="ms-2">Hindi</span></div>
                    <div class="col-12 drop-down-item"><img src="./img/german.png" alt=""><span class="ms-2">German</span></div>
                </div>    
            </div>
        </div>
    </div>

    <nav class="navbar navbar-expand-lg">
        <div class="container">
                <a class="h1 fw-bold positon-relative text-decoration-none color-gray" href="#">CAR<span class="ms-3">RENTAL</span><h6 class="mt-1">TOP CAR RENTAL DEALS-SAVE BIG!</h6></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            <div class="row color-gray">
                <div class="col">
                    <div class="collapse navbar-collapse" id="navbarSupportedContent ">
                        <ul class="navbar-nav me-auto mb-2 mb-lg-0 float-end">
                            <li class="nav-item h5 me-2 ">
                                <a class="nav-link active" aria-current="page" href="#">Home</a>
                            </li>
                            <li class="nav-item h5 me-2">
                                <a class="nav-link" href="#">Services</a>
                            </li>
                            <li class="nav-item h5 me-2">
                                <a class="nav-link" href="#">Vehicle Models</a>
                            </li>
                            <li class="nav-item h5 me-2 dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                Blog
                                </a>
                                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a class="dropdown-item" href="#">Action</a></li>
                                <li><a class="dropdown-item" href="#">Another action</a></li>
                                <li><hr class="dropdown-divider"></li>
                                <li><a class="dropdown-item" href="#">Something else here</a></li>
                                </ul>
                            </li>
                            <li class="nav-item h5 me-2">
                                <a class="nav-link">Location</a>
                            </li>
                            <li class="nav-item h5 me-2">
                                <a class="nav-link" href="#">Contact</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
      </nav>


    <div class="container-fluid back-yellow p-5 reserve positon-relative">
        <div class="row d-flex justify-content-center align-item-center ">
            <div class="col-4 bg-white p-4 g-5">
                <div class="reserve-input">
                        <select name="" id="" class="w-100 p-3 border-0 bg-white ">
                            <option value="" class="px-5">Select Your Car Type</option>
                            <option value="">a</option>
                            <option value="">b</option>
                            <option value="">c</option>
                            <option value="">d</option>
                            <option value="">e</option>
                            <option value="">f</option>
                            <option value="">g</option>
                            <option value="">h</option>
                            <option value="">i</option>
                            <option value="">j</option>
                        </select>
                </div>
                <div class="mt-3 reserve-input ">
                    <label for="" class="px-3 py-2 "><i class="fa-solid fa-location-dot me-2"></i>Pick-up</label>
                    <input type="text" name="" id="" class="d-inline-block border-0 color-yellow city " placeholder="Enter a city or Airport">
                </div>
                <p>Need a different drop-off location?</p>
                <div class=" mt-4 d-flex">
                    <div class="reserve-input  w-75">
                        <label for="" class="px-3 py-2 w-50"><i class="fa-solid fa-calendar-days me-2"></i>Pick-up</label>
                        <input type="date" name="" id="" class="px-2 py-2 border-0 color-yellow date">
                    </div>
                    <select name="" id="" class="p-2 ms-1 border-1 gray-border bg-white color-yellow time">
                        <option value="">12:00 AM</option>
                        <option value="">01:00 AM</option>
                        <option value="">02:00 AM</option>
                        <option value="">03:00 AM</option>
                        <option value="">04:00 AM</option>
                        <option value="">05:00 AM</option>
                        <option value="">06:00 AM</option>
                        <option value="">07:00 AM</option>
                        <option value="">08:00 AM</option>
                        <option value="">09:00 AM</option>
                        <option value="">10:00 AM</option>
                        <option value="">11:00 AM</option>
                        <option value="">12:00 PM</option>
                        <option value="">01:00 PM</option>
                        <option value="">02:00 PM</option>
                        <option value="">03:00 PM</option>
                        <option value="">04:00 PM</option>
                        <option value="">05:00 PM</option>
                        <option value="">06:00 PM</option>
                        <option value="">07:00 PM</option>        
                        <option value="">08:00 PM</option>
                        <option value="">09:00 PM</option>
                        <option value="">10:00 PM</option>
                        <option value="">11:00 PM</option>                                
                    </select>
                </div>
                <div class=" mt-3 d-flex ">
                    <div class="reserve-input w-75">
                        <label for="" class="px-3 py-2 w-50"><i class="fa-solid fa-calendar-days me-2"></i>Drop-off</label>
                        <input type="date" name="" id="" class=" p-2 border-0 color-yellow date">
                    </div>                       
                    <select name="" id="" class="p-2 ms-1 border-1 gray-border bg-white color-yellow time">
                        <option value="">12:00 AM</option>
                        <option value="">01:00 AM</option>
                        <option value="">02:00 AM</option>
                        <option value="">03:00 AM</option>
                        <option value="">04:00 AM</option>
                        <option value="">05:00 AM</option>
                        <option value="">06:00 AM</option>
                        <option value="">07:00 AM</option>
                        <option value="">08:00 AM</option>
                        <option value="">09:00 AM</option>
                        <option value="">10:00 AM</option>
                        <option value="">11:00 AM</option>
                        <option value="">12:00 PM</option>
                        <option value="">01:00 PM</option>
                        <option value="">02:00 PM</option>
                        <option value="">03:00 PM</option>
                        <option value="">04:00 PM</option>
                        <option value="">05:00 PM</option>
                        <option value="">06:00 PM</option>
                        <option value="">07:00 PM</option>
                        <option value="">08:00 PM</option>
                        <option value="">09:00 PM</option>
                        <option value="">10:00 PM</option>
                        <option value="">11:00 PM</option>
                    </select>                            
                </div>
                <button class="h2 fw-bold w-100 mt-5 p-2 border-0 back-yellow text-white">Continue Car Reservation</button>
            </div>
            <div class="col-6 g-5">
                <div class="row ">
                    <div class="col-11 ms-5 owl-carousel owl-theme car-slider positon-relative">
                        <div class="item">
                            <h2 class="text-white fw-bold">GET 15% OFF PERCENTILE</h2>
                            <h3 class="color-gray">Plain your trip</h3>
                            <img src="./img/car1.png" alt="" >
                        </div>
                        <div class="item">
                            <h2 class="text-white fw-bold">LUXURY CAR FROM FROM $28 DAY</h2>
                            <h3 class="color-gray">Treat Yourself in USA</h3>
                            <img src="./img/car2.png" alt="" >
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <div class="container-fluid my-5 cust-service">
        <div class="row py-5">
            <h1 class="text-center mb-5 positon-relative color-gray fw-bold ">Customer Service</h1>
            <div class="row d-flex justify-content-center align-item-center gap-4 mt-4">
                <div class="col-5 back-gray p-4">
                    <span class="back-yellow   text-white">+</span><h3 class="d-inline-block ms-3 color-gray fw-bold ">Special rates on car booking</h3>
                    <p class="mt-3 lh-base text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum aspernatur enim laboriosam, quam excepturi, voluptas dolores veritatis fuga, non unde repudiandae ab reprehenderit quaerat. Aspernatur reiciendis ipsum ad blanditiis architecto.</p>
                </div>
                <div class="col-5 back-gray p-4 ">
                    <span class="back-yellow   text-white">+</span><h3 class="d-inline-block ms-3 color-gray fw-bold">Mobile Phone Reservation</h3>
                    <p class="mt-3 lh-base text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum aspernatur enim laboriosam, quam excepturi, voluptas dolores veritatis fuga, non unde repudiandae ab reprehenderit quaerat. Aspernatur reiciendis ipsum ad blanditiis architecto.</p>
                </div>
            </div>
            <div class="row d-flex justify-content-center align-item-center mt-5 gap-4">
                <div class="col-5 back-gray p-4">
                    <span class="back-yellow text-white">+</span><h3 class="d-inline-block ms-3 color-gray fw-bold">Unlimited Miles Car Rental</h3>
                    <p class="mt-3 lh-base text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum aspernatur enim laboriosam, quam excepturi, voluptas dolores veritatis fuga, non unde repudiandae ab reprehenderit quaerat. Aspernatur reiciendis ipsum ad blanditiis architecto.</p>
                </div>
                <div class="col-5 back-gray p-4">
                    <span class="back-yellow  text-white">+</span><h3 class="d-inline-block ms-3 color-gray fw-bold">One Way Car Rentals</h3>
                    <p class="mt-3 lh-base text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum aspernatur enim laboriosam, quam excepturi, voluptas dolores veritatis fuga, non unde repudiandae ab reprehenderit quaerat. Aspernatur reiciendis ipsum ad blanditiis architecto.</p>
                </div>
            </div>
        </div>    
    </div>

    <div class="container-fluid back-yellow py-5 offers my-5">
        <div class="row d-flex justify-content-center align-item-center text-uppercase py-3">
            <div class="col-4">
                <h3 class="text-white">Sign up for amazing offers</h3>
                <h6 class="color-gray">exclusive access for offers and promotions</h6>
            </div>
            <div class="col-4 ms-4">
                <input type="text" name="" id="" class="w-75 p-3 border-0 mt-1" placeholder="Enter Your Email Address">
                <div class="email-btn d-inline-block">
                    <button class="p-2 border-2 border-secondary text-uppercase fw-bold color-gray">send</button>
                </div>
            </div>
            <div class="col-2 text-center mt-1">
                <a href=""><i class="fa-brands fa-twitter text-white fs-3 p-3"></i></a>
                <a href=""><i class="fa-brands fa-google-plus-g text-white fs-3 p-3 mx-1"></i></a>
                <a href=""><i class="fa-brands fa-facebook-f text-white fs-3 p-3"></i></a>
            </div>
        </div>
    </div>


    <div class="container-fluid vehicles">
        <h1 class="color-gray"><span class="fw-bold">Vehicle Models -</span> Our rental fleet at a glance</h1>
        <div class="row justify-content-center align-item-center gap-4">
            <div class="col-3" id="veh">
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold  positon-relative vehicle-btn" value="1" id="vehicle-btn1">hundai</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn" value="2" id="vehicle-btn2">suzuki</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn" value="3" id="vehicle-btn3">volwo</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn" value="4" id="vehicle-btn4">audi</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn"
                value="5" id="vehicle-btn5">jaguar</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn"
                value="6" id="vehicle-btn6">bugati</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn" value="7" id="vehicle-btn7">marceedes</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn"
                value="8" id="vehicle-btn8">BMW</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn"
                value="9" id="vehicle-btn9">toyota</button>
                <button class="w-75 p-2 back-gray color-gray border-0 fw-bold positon-relative vehicle-btn"
                value="10" id="vehicle-btn10">tesla</button>
            </div>
            <div class="col-8 cars-info">
                <!-- vehicle-1 -->
                <div class="row cars" id="vehicle1" >
                    <div class="col-8">
                        <img src="./img/vehicle1.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehcile 2 -->
                <div class="row cars" id="vehicle2">
                    <div class="col-8">
                        <img src="./img/vehicle2.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>3</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>4 Suitcases / 1 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>no</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>20 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle-3 -->
                <div class="row cars" id="vehicle3">
                    <div class="col-8">
                        <img src="./img/vehicle3.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle 4 -->
                <div class="row cars" id="vehicle4">
                    <div class="col-8">
                        <img src="./img/vehicle2.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle-5 -->
                <div class="row cars" id="vehicle5">
                    <div class="col-8">
                        <img src="./img/vehicle3.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle-6 -->
                <div class="row cars" id="vehicle6">
                    <div class="col-8">
                        <img src="./img/vehicle1.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle-7 -->
                <div class="row cars" id="vehicle7">
                    <div class="col-8">
                        <img src="./img/vehicle3.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle -8 -->
                <div class="row cars" id="vehicle8">
                    <div class="col-8">
                        <img src="./img/vehicle1.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle-9 -->
                <div class="row cars" id="vehicle9">
                    <div class="col-8">
                        <img src="./img/vehicle3.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- vehicle-10 -->
                <div class="row cars" id="vehicle10">
                    <div class="col-8">
                        <img src="./img/vehicle2.jpg" alt="">
                    </div>
                    <div class="col-4 color-gray">
                        <div class="row">
                            <h4 class="back-yellow py-3 px-3">$100.50 <span class="h5">rent per day</span></h4>
                        </div>
                        <div class="row d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Models</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Doors</span>
                            </div>
                            <div class="col">
                                <span>4</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Seats</span>
                            </div>
                            <div class="col">
                                <span>5</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Luggage</span>
                            </div>
                            <div class="col">
                                <span>2 Suitcases / 2 Bags</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Transmission</span>
                            </div>
                            <div class="col">
                                <span>Automatic</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col">
                                <span>Air conditioning</span>
                            </div>
                            <div class="col">
                                <span>Yes</span>
                            </div>
                        </div>
                        <div class="row  d-flex justify-content-center align-item-center px-3 py-1">
                            <div class="col-5">
                                <span>Minimum age</span>
                            </div>
                            <div class="col">
                                <span>25 years</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>



'''
    return HttpResponse(html)

def contact(request):
    html="<h1> my name number is 987655678</h1>"
    return HttpResponse(html)

