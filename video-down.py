import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
opener = urllib.request.build_opener()
opener.addheaders = [
        ('Host', 'tx.acgvideo.com'),
        ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
        ('Accept', '*/*'),
        ('Accept-Language', 'en-US,en;q=0.5'),
        ('Accept-Encoding', 'gzip, deflate, br'),
        ('Range', 'bytes=0-'),  # Range 的值要为 bytes=0- 才能下载完整视频
        ('Referer', 'https://www.bilibili.com/video/av14543079/'),
        ('Origin', 'https://www.bilibili.com'),
        ('Connection', 'keep-alive'),
    ]
urllib.request.install_opener(opener)
# url = 'http://upos-hz-mirrorks3u.acgvideo.com/upgcxcode/21/09/10520921/10520921-1-80.flv?e=ig8euxZM2rNcNbhahwTVhoMa7wRghwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNC8xNEVE9EKE9IMvXBvE2ENvNCImNEVEK9GVqJIwqa80WXIekXRE9IB5QK==&deadline=1539186935&gen=playurl&oi=3526337348&os=ks3u&platform=pc&trid=c3b7a1b46d8e4058ad661ec879ca0ea1&uipk=5&uipv=5&upsig=e6650d9031124df61303c81227228778'
# url = "http://upos-hz-mirrorks3u.acgvideo.com/upgcxcode/93/10/55041093/55041093-1-80.flv?e=ig8euxZM2rNcNbKa7bdVhoMH7WNVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNC8xNEVE9EKE9IMvXBvE2ENvNCImNEVEK9GVqJIwqa80WXIekXRE9IB5QK==&deadline=1539196399&gen=playurl&oi=3526340601&os=ks3u&platform=pc&trid=c07a471c0d654b4d8a13b787be9ddf0f&uipk=5&uipv=5&upsig=7c63b1d34b4a129780cc73f5ca99dcea"
url = "http://upos-hz-mirrorkodo.acgvideo.com/upgcxcode/61/51/48595161/48595161-1-80.flv?e=ig8euxZM2rNcNbhV7zuVhoMjhWUMhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNC8xNEVE9EKE9IMvXBvE2ENvNCImNEVEK9GVqJIwqa80WXIekXRE9IB5QK==&deadline=1539235940&dynamic=1&gen=playurl&oi=720905611&os=kodo&platform=pc&rate=307700&trid=43c963e302d14b298675f4e9b38ee18d&uipk=5&uipv=5&um_deadline=1539235940&um_sign=1f942b9b9a263c90c8622cd7081d60f5&upsig=3e52fdb23eb67753e87f7fc5414f65a1', 'vhead': 'AWQAMv/hABhnZAAyrNnAeAIn5YQAAA+kAALuADxgxngBAAVo6bssiw=="
urllib.request.urlretrieve(url, filename='1.flv')
