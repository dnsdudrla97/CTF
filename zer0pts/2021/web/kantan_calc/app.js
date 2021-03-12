const express = require('express');
const path = require('path');
const vm = require('vm');
const FLAG = 'zer0pts{eproeproeporeoreoroepoproeopo}'

const app = express();

// app.set('views', path.join(__dirname, 'views'));
// app.set('view engine', 'pug');

// app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function (req, res, next) {
  let output = '';
  const code = req.query.code + '';

  console.log(code.length);
  if (code && code.length < 30) {
    try {
      const result = vm.runInNewContext(`'use strict'; (function () { return ${code}; /* ${FLAG} */ })()`, Object.create(null), { timeout: 100 });
      console.log(result)
      output = result + '';
      if (output.includes('zer0pts')) {
        output = 'Error: please do not exfiltrate the flag';
      }
    } catch (e) {
      console.log(e)
      output = 'Error: error occurred';
    }
  } else {

    output = 'Error: invalid code';
  }
  console.log(output)
  // res.render('index', { title: 'Kantan Calc', output });
});

app.get('/source', function (req, res) {
  res.sendFile(path.join(__dirname, 'app.js'));
});

var port = 3000
app.listen(port, () => {
  console.log("SERVER ON")
})

process