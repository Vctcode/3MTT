const express = require('express');
const app = express();

app.get('/', (req, res) => res.send("This is a simple node app running on a  Docker Container"))
app.listen(3000, () => console.log("This server is running on port 3000"))
