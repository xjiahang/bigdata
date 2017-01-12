$(function () {

	var smoothie = new SmoothieChart();
	smoothie.streamTo(document.getElementById("StockChart"), 1000)

	var line1 = new TimeSeries()

	smoothie.addTimeSeries(line1, {
		strokeStyle:'rgb(0, 255, 0)',
		fillStyle:'rgba(0, 255, 0, 0.4)',
		lineWidth:3
	});


    var socket = io();

    // - Whenever the server emits 'data', update the flow graph
    socket.on('stock', function (stock) {
    	parsed = JSON.parse(stock)
    	line1.append(Math.trunc(parsed['timestamp'] * 1000), parsed['average_price'])
    });
});
