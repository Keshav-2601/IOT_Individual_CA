import { env } from "./env.js";
const pubnub = new PubNub({
    publishKey: env.PUB_KEY,
    subscribeKey: env.SUB_KEY,
    uuid: env.UUID,
    cipherKey: env.CIPHER_KEY, 
});

pubnub.subscribe({
    channels: ["airquality"],
});

pubnub.addListener({
    message: function (messageEvent) {
        console.log("Full message received:", messageEvent.message);
        const { temperature, pressure, aqi, alert } = messageEvent.message;
        document.getElementById("para1").value = temperature; // Use `.value` (lowercase) to set input field value
        document.getElementById("para2").value = pressure;
        document.getElementById("para3").value = aqi;
        
        console.log(`Temperature: ${temperature}°C`);
        console.log(`Pressure: ${pressure} hPa`);
        console.log(`Air Quality Index: ${aqi}`);
        console.log(`Alert: ${alert}`);
    },
    status: function (statusEvent) {
        if (statusEvent.category === "PNConnectedCategory") {
            console.log("Successfully subscribed to airquality channel.");
        }
    },
});