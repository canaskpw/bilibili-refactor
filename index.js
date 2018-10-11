var resolveCid = require('bilibili-playurl');

resolveCid(46049038,{quality: 80}).then(function (url) {
  console.log(url);
});

resolveCid(46049038, { season_type: 4, quality: 80 }).then(function (url) {
  console.log(url);
});