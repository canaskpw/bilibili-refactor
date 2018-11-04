var resolveCid = require('bilibili-playurl');
var list = process.argv.splice(0)
var cid = list[2]
var s_id = list[3]
resolveCid(cid, { season_type: s_id, quality: 80 }).then(function (url) {
  console.log(url);
});

// 46049038