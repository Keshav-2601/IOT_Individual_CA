document.addEventListener("DOMContentLoaded", function () {
    var chx = document.getElementById("chart1");
    var chart = new Chart(chx, {
        type: "bar",
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1
            }]
        }
    });
});
