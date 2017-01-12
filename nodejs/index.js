var redis = require('redis');
var express = require('express');
var app = express();
var server = require('http').createServer(app);
var socketio = require('socket.io')(server);
var argv = require('minimist')(process.argv.slice(2));

var redis_port = argv['redis_port'];
var redis_host = argv['redis_host'];
var redis_channel = argv['redis_channel'];

console.log("DEBUG : start redis")
var redis = redis.createClient(redis_port, redis_host);
redis.subscribe(redis_channel);
redis.on('message', function(channel, message) {
    console.log(message);
    socketio.emit("stock", message);    
})

app.use(express.static(__dirname + '/public'));
app.use('/jquery', express.static(__dirname + '/node_modules/jquery/dist'));
app.use('/smoothie', express.static(__dirname + '/node_modules/smoothie/'));


server.listen(3000);


