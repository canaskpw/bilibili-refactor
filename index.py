import os
import execjs

# os.environ["EXECJS_RUNTIME"] = "Node"
os.environ["NODE_PATH"] = os.getcwd()+"/node_modules"
print(execjs.get().name)

parser = execjs.compile("""
    var gurl = ''
    var resolveCid = require("bilibili-playurl");
    resolveCid(46049038,{quality: 80}).then(function (url) {
          gurl =url;
        });
        function sleep(sleepTime) {
    for(var start = +new Date; +new Date - start <= sleepTime; ) { } 
}
        function parse(text) {
        return gurl;
    }


""")

if __name__ == "__main__":
    obj = parser.call("parse",46049038)
    print(obj)
    # pass