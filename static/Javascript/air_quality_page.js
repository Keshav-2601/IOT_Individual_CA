const pubnub = new PubNub({
    publishKey: env.PUB_KEY,
    subscribeKey: env.SUB_KEY,
    uuid: "testuser",
    cipherKey: env.CIPHER_KEY, 
});

pubnub.subscribe({
    channels: ["airquality"],
});

pubnub.addListener({
    message: function (messageEvent) {
        const { temperature, pressure, aqi, alert } = messageEvent.message;
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