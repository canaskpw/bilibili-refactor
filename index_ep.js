var resolveCid = require('bilibili-playurl');
var g= process.argv.splice(2)[0]

resolveCid(g, { season_type: 1, quality: 80 }).then(function (url) {
  console.log(url);
});

// 46049038