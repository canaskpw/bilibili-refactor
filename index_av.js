var resolveCid = require('bilibili-playurl');
var g= process.argv.splice(2)[0]
resolveCid(g,{quality: 80}).then(function (url) {
  console.log(url);
});