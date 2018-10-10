var resolveCid = require('bilibili-playurl');
var g= process.argv.splice(2)[0]
resolveCid(g,{quality: 80}).then(function (url) {
  console.log(url);
});


resolveCid(g, { season_type: 4, quality: 80 }).then(function (url) {
  console.log(url);
});

// 46049038