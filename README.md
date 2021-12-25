# Light_on_mars
## :alien: What's the weather like up there?
Its December in England. Wouldn't it be nice to see a different type of weather? Lets simulate some real Martian weather! Using data from [NASA's public API](https://api.nasa.gov/) from the [InSight mission](https://mars.nasa.gov/insight/) this project will control a [WiFi enabled colour LED smart bulb from LIFX](https://lifxshop.eu/products/lifx-colour-a60-b22) to bring home the weather on mars. 

## :bulb: Let there be light!
The smart bulbs from LIFX do not require to be connected to the cloud and work on the local network. They are controlled using "LIFX Packets": A protocol that uses binary packets sent over UDP/IP. The documentation on how to encode/decode can be found [here](https://lan.developer.lifx.com/docs). 

## :umbrella: Sad (and wet) robot noises.
The InSight Mars lander is currently parked on Mars at Elysium Planitia near the planets equator. The API provides per-Sol weather data such as atmospheric temperature,horizontal wind speed and, atmospheric pressure. The documentation of the API can be found [here](https://api.nasa.gov/assets/insight/InSight%20Weather%20API%20Documentation.pdf).

-Jacob Nash
