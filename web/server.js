const express = require('express');
const app = express()
const path = require("path");
const bodyParser = require("body-parser");

app.set("view engine", "pug");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(__dirname + '/public'));

var jsonParser = bodyParser.json()

var temperature = 70;
var setpoint = 75;
var ac = false;
var heat = false;

app.get('/', (req, res) => {
    res.render("index",
    {
        temperature: temperature,
        setpoint: setpoint,
        ac: ac,
        heat: heat
    })
})

app.get('/up', (req, res) => {
    res.sendStatus(200);
    setpoint++
})

app.get('/down', (req, res) => {
    res.sendStatus(200);
    setpoint--
})

app.get('/setpoint', (req, res) => {
    res.send({
        setpoint: setpoint
    })
})

app.post('/update', jsonParser, (req, res) => {
    console.log(req.body);
    temperature = req.body.temperature;
    setpoint = req.body.setpoint;
    ac = req.body.ac;
    heat = req.body.heat;
    res.sendStatus(200);
})

app.listen(5656, () => {
    console.log('http://localhost:5656')
})
