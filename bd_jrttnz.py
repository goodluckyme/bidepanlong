"""
————————需要py3.10版本，新版青龙可运行————————
版本: 7.15内置ck版
cron: 1 7-22 * * *
new Env('今日头条内置ck版');
今日头条刷视频，非黑号一天4块左右
抓包：点击宝箱，开宝箱看视频，连续看两三个都可以。
返回找这个url: https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?
url参数 = ？后面的所有内容
cookie参数 = cookie所有内容
x-argus和x-ladon和user-agent在请求头里面找，格式如下
环境变量：bd_jrtt = url?后的所有内容#cookie#x-argus#x-ladon#user-agent
例如，环境变量名称填写：bd_jrtt  值：luck******#excgd***#x-argus的参数#x-ladon的参数#user-agent的参数
注：url不要前面域名那一节，只要问号？后面的内容，从luck开始
卡密环境变量名：bd_km

白号宝箱视频正常140+个固定300金币，连续是330个固定300金币。
半黑号宝箱140+，连续50左右。
一来就几个金币的直接换号，养两天在跑试试
"""

# 默认刷广告次数一个小时30次一个号够用，多账号自己设置定时时间。
nums = 30

# 格式下面这样填
# bd_jrtt = 'luck******#excgd***#x-argus的参数#x-ladon的参数#user-agent的参数'
bd_jrtt = ''

try:
    import marshal, lzma, gzip, bz2, binascii, zlib;

    exec(marshal.loads(lzma.decompress(
        b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x17Xc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00sH\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x01l\x03Z\x03d\x00d\x01l\x04Z\x04d\x00d\x01l\x05Z\x05e\x06e\x00\xa0\x07e\x01\xa0\x08d\x02\xa1\x01\xa1\x01\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nst\x16\x00\x00\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0\x16G\x162]\x001\x802\xa0hC"m;\xa5S\x08\\\xd8\xf7\x17\xa0\x87@\x96\xe0\xf8\xe5/9\xf0\xa2\x10\xfd\xbeM\xf9\x12\xa5\xc3\xaf\xd6\x9b\xa7\x98\x82\xb06\xb0Z$g#3:\x04.\xd3\xe1\'\x8d `\x04\xaa\x1d\xcf\xa4)\x1b\x1b\xfa\x12\x05\x024D!\x95\xa6Ia\x86cC\xd4\xd0 \xb7\xe8i;qV3]\x0b|\x12\xab\xeb\x84\xc6zC\xcc/A\xf6\xc5\xe81\x0e`\x84\x83\x02\xff\xafvVLa\xfa\x92O\xe3\xac\x04\xd4\\\xfb\x15\xe0\xee\n[\x00\xe9Y:<X\xc4\x9bUO\xb8\x14&\xe3\xf3\x86\x99\xf4m/\xcb\\\xb8\xa5~.\x809\xab\x9e\x03S;\xddhb\x84|\xaa)\xcdFI\xc6\x91\xab\xe8\x03&\xce\x1a7dK\xaa\x12\x91\x16q\x97K-\xf2\xecb0\x16\x9a\x80\x13.o\xa1\x83i\x0e\x19)\xf1!\xff\xcb\xd9\x1b\xaao`\xa7M\xbfo\xf0\xd5\xd7\xe6}j\xe6\x0b\x8a4.I\xe1O\xe7lO\x85M\xc4r{\x9a\xc9\xb9\x032#f&\x8bQ\xd67\xb7\x02hzX\x93p\x87\xd7\x16\x99;\xd1\xa1G\x17\x18\x91{+\xa2\xd7\xbe\x0f\xb3X\x06\x8e\x12\n\x04E\xcd\xf90\xc7\x085z\xcf7\xf7\x1f\x16\xf7\xa8\xef\r\x9d\xbf\xf1\xfbs\x10O\xafMe#\xe2\x15\x86WU\xea-\xb1R\xae\xb6\xe4\x12\xf12\x80<\x9e6,\xf3d\xad?\x15\\\xca\xa6\x966\xd4\xcd-]<\x1d@\x05\xce\xfe\xaf2\xa9\x11k\xbb\xc1\xf8\x06R\xf4\xc7\x16\x1c\xdc\xe9\x04?\x98\xb9y\xa8\x81\x93;\x13\xd0\x02\xe0\x10\xb9Bv\xb4\x7f5\xd7W}idPr\xbc\xd0\xbbt\x10\x8af>\xf8\xf5\x8cV\xac\xbeJ\x98\x94ra\x8f\xf9\xd0\x0f/\xafV&-\xcd)\xb5\x07B\x91$\xeaj.\x9e\xd7\xc9\r1\xb9%\xb2\x88\x81t\x8a\xcd\x14\xe4P\xf7\xa3\xb4UhB\xd5\xf3\xf1K\xbb\x1d\xe83\x0f*\x97\x87\x10BR\x11\xa6\x86\x90n\x85/d\x110DK\x01\xa1\\\x84U)8Z\xe3\x90\xd0\x7f\xfc0\t\xd6\xad=\\\xf3\xb3\x7f/e\xe8\r\xd59k%3e5\x9cd\n\xbe\xbd\xbbtB\xabB\xc7k\xa2i\xadayU\xf2\x7f\x91\x96\xbd8\xe1\xb8\x900\x1b|\xa8\xfa\xe0\x17&\x06\xec\xe7\xa9\x05\xc2\x9c!\xa5I\xc4\x8b\xc4q\xc6ey)\x89\x85\x9e\xee\xad\xb02I\x9b\xb1,\x94\xe1`\xf7\x088L\xb5A\x1e\xa3\x9dPf\xc3s_M\xb6\x93\xc6\xca\xc6r\x13\xc9\x1c\xed\x18\xbfg#\x98\xbeFu8_\xa8\xf8\xd0Q\xe3\'q\xc9\x89lM\xe1\xf3^\xe2c3T \xb2\n\x8f\x8a\x8bTsLwr\xf7\r\xc8\xa8F\xd9\xb5\xd6O\x82O^@\xc1\xf2\x8e\xf8~\xb6\x1c\nH\xbc\xc0z\x0c=w\xa0\xa3\x1e\xc0\x08\xaf\xea\x9eC\x19\xa0\xaa\xf6G\xaa\xc1.w"\xf9\x96\xdd\x86\xdf\xc4\x88\\h\xd0\x91\x11?\x17\xa7\xb8z&\xa1N\x8eN\x0e[)u\x08E\x92\xb6\xacG\x01\x10\xf09\xf1.\xce\xd17\xfcL\xf6\xa5\xed\xd8\xd3\x0cV\xee\x91mtcmf\xe0b\xd3\xa6@w\xd4\xe5mK\r\xb3\x98`\x16\x91\xf7\xed\x9eAXL2\xef\x0e\xfb=O\xb9\xc6\xe8\xaf\xf3\xd1s\x1f\x08\n<\xbe\xc7.H\xfe\x8b\xcf\xc3\x9e:\xcavg\xcagq@\xf9\xfb~@\x86\x987\x0f\xfa)\xaf\x94B\x96\x858P\x98\xb2\xbfa\x9b\xf8\xd6\xf8T\xbd\x17\xf1\x1a^\x81\xa9c\x0e|\xc4\x86\x14d\x8a\x86\xe0\x95\xab}L(n\xaaq\xdf\xa23^\x94eSx\x04\xf9N\x8eW\xb4-\x8c\xee\xf1\xc5\xc1\xd5M\xa9tG+\x8e\xdcX\xeb\xe2\xbbE\x8eE\xceVx\x1b;4,n4\xd1{\x8b\xe9ED\x00@\x98\x1f\xe2\x8ex<\r\xd3$P\x17\n\xe0%\xfdtLYW\x92\xc0W\xadD\xcb\x92\xc4k\x96\xa7:\xfe\xbe\x05\\\x17\x0cr\xd9w\x1e\x00\xba\xdbB\x8c}\xa1\x9b\xd1\xff4!r\x08\x0e\xd2\xc2\xd3(\xd8\xa0{T\x99\xd7\xed\xae\x01#%Dm\xcb,\xb4l0\xf4rYGb\xc3\xb0\xa4\xd4\xc4\x19S\xad\x9c\x99\x0f\xce\xdeT\xf5\xf9\xf6\x13\xa2\x04jb\xda\xe7Bs\x97\x02\xd1\x8e\xd2\x1a\xf3G\xf0\t|`\xa9\xda\xdd\xc7\xce\xf1\xc8o\xae\x97\xc9\xff\xe1\x94 \xdf\xf1\xf8\x0c\x88A\xf1\xa7\xb8xFw\x12\x18\xfb\x89\xe0-\xc3\x19\x0b7\x95\xd7\x90\xcb\xbc?\xce\'f0\x1a\x1a\xa9\xeb\xe6\x86\xce\x9c\xd9+\x8f\x07]\xc4\x9ag\x1dG9\xcb\x18\xd3y\xe0\xc6\xc2/\x9c\xf6\xc1\x1eR\xef\x8d2\xea\x84\xe2[,\x1d}\xc2\xd0\xee\x96\xa4$G|\x9a\xbc\xee\x1e\x80\xbcQ\xd6Q\x07\xa4h\x8f\x90\\UQ\x8eB\xdc5\xd37\x13\xd4\xa9\x9fq\xc5\xdf\xee\xd1\xea{[\xe6]Y2\x8e\x80\xfbz\xd2e\xdd\xe3JS\xa6\xc0\xa7\xb6{p\xdb\x8e\x881\xd23\xc9E.\x11\xf5\xbc\xbe\xfd\x12r\r\xfb1-\x99\xfalO\xe3\x9d\xc4\xbd\xef\x07\xe0b\xe3t;\xa8\xe75>S\xaa\x06P\x13\xee\x7fD\x89\xd3h\x8a\xe6\xbf\x0b\xb1n\x8d\x9a?\xbb\xa6\xa7\xac\x97\xc6\x8b\xe7[#=\xef.\x16\x1c\x98\xbdbh\xa2\x17\x94\xe3yN\xee\x89\xe0Z\xcfY\x01\x0f\xae\x16\x9cm)\x00\x0e\xd6\xdc\xd4\xfe\x8c6:Z+\x1dY\x92\x02$\xbc7dy\xdb\xd1\xe5\xdfw\xbbE\xf6\x8f\x1b\x9ei4\x8a\xf16\x8f@\x9f\xe3\xc8\xac\x19\xc2 \x97\xce@?Z\xa3\x03\xddt\xe0\x18\\\xb3"\x8b\x91\x8b\xb3f\x89\x10\x8d\x06\xe4\xec\xa4\x9e\xc2\xcf}\x08\xdc\xb6\x9e\xc8A>0<\xa9\x7f\xf1\xb4\x83ro+\xed\xe8\xece\x7fV\x9f\x11GXY(\x0c=\xe9Fa\xb7\x05\xda\xcd\x9f\xc9X\x85\x0f\x8b\xa5f%\xdc\x87\xccUn\x7fMT!nx\xf8-\xc6\x8f\xee\x05\xa1\xad\xa9\xe9\x08p\x93F\xda\xaey0\xd6\x11\xfd\x00\x12\x89B\xd7\xdf\x98t\xbc\x00\xccA\xdf\xfd\x05Y\xfe2rj\xbf+\x06x\xf2\xa9\xfe\x7f\xca\xd8\xfcA\x02\xb5\xde1[\x8a\x7fE\x86|\xbdB4\xe1\xa8\xbe\x0cV\x9a\xfats\xcckB\x0f-\xe3\xe8\x15/\xe4\x0b\xc7\xd1\xce\xe8b\xaa2\xc7qd\xab\x06\xc3z\xbdH\xc5#\xf4\x91*t\x06\x81\x8a\xc6?\x87\xac+Ylw\xb82`\x8fL\xca\xfaZ\xfe\x97\xc7\xa7>LP;\xfa\x7f\x9b\xfa;&Ax\x08\x0b\xf7\xc5\xbe\xdb\xe9\'/\xd3n\xde\x02z\x00c\x88\xfd4$}\xff\x91\xb1\xc1\xbc\xc7OY\x82\xa1K-\x81B\xb7\x93O,\xefR\x9a\xd4\xde\xb0=}\xc1Re\xd6\x8f<ie\x7f\x9c\xe1\xcd\x9c\x1bw\x99]&\xf3\x91<\xbb\x03^\n\r\xce\xa8\x9c\x1cg\xd1\x81\x1d\x9aAuj`\xb1\xdao\xef\x1a\x0c\xce\xbb\xa8\x88k\x83\x16\xecWW\xb2\xd7\x0cBT\xb8\xfb\xdfO\x05\x13\xf0u]\xf3\n\x1cf\xdd\x01\xe9j\x13s\x19\x91w\xfdv\xa8B\xeb\x13\xd2\x9d\xac*\xa8\xcd|`\x1f\x80\xb6\xd7:\x0f\xde\xfa\xdcT\xb9Q\x1f\xe3X\x90\x80adS{\xcc\x83^f\xf8:\x06b\x16{\xc4\xa8J\xf7`\xa5\xc2\xb0CR\x8b\x86\xf8\xbb\x10\x02\x81\xe0t\xb8\x96\x18\xdb}n\xa3\xe8\x19\x95\xda\xf2\xcf\x18;\xb2\t5\x05fi\xd5\xe7\xe9K\xddk\xf9\xd4\xbby\xbd\x93N\xa0#\xcaT\xef\xdc4\xa2\xf1\xdc\xc7\t\x15\xe4\x14\x8b\xe2\xd9J\xcf\x90\x99"e\x0f\xff4x=\xbb\xdbA"{\x0b7*\xce\x0e\xb5c\x97\xec\xd4\xca\xf9\xe8Y\xab\xf7\xd3e\xe4\xb83\x85V\xa3P\xb2\x8f\xbe\xe1E\xf3\xe9\xee\xc6\x18\xf0\xd3\xb1maW\x8b\x88\t\x8db\xf8\xf0\xf6-\xa3\xe4\xf5\xd7><3h\xcfT_\xeb\xd0\xb1Q\x9d\x81\xcd`\x98\xba\xf2\xf7\xa0\xae); :55\x96\xfb\x80r\x9a9?-\xfe\x107\xa9g\xa5\x92v%0\x15&\xc9\xf9\xfe#t\x15\xf6\x91\x9bK\x0e/\x98a\x06\x89q\xfd\x96\x8d7\xf9\xe3\xde\x11\x1b\x0b\x93\x9d\x08\r|\xb8\x06+\xb6T\xd0\x91\xef\x8e\xce4\xa8\x13\xf7\xd8;\x83q\x13\xcc\xca\xf7\xd4\x1dZ\xdf\x81\x8d\x81\x84\x9a\x96u\xc5\x1eD\xc9\'\xe9\xa5/\xa4I4\x892\xa0\x10\x86]\x93V=\xec\x98}:\x84BY\xc1.\xd2\xc2\xe7\x10m"vO\xdac\xea\xd9\x16I\xb5\x84t\xd1[M\x0fB"\xe0\xc93e\x84 ~(\x7fp\x18\xc2\xd0\x11\xd5\xbdk\xee\xa1\xf4]\x90\xc1\xceW\xd1}`\xe5\xbb\xd1\x1c\xe5\x1eA\xebU\x1f\xd9!\xd4\x9c\xc9:\xce\xfa\x16\xf8\x13\xdb\xb1\xda\x8e\xee^\x0eKk\xe6\xac\x17\xe5=N#`\xb0\xa52|l\xb2S\x0c\x94#c2\xd2\xfc\x84\xab\x01#\x86`\x17,d\x16D\xdc\xb1\xc2\x84\xbfy`F\xe0\x81BuF\xd5\xbd,L\xc5iwA\x1cu\x16\xfe\x99X\r_p>\x15\xf0\xc1\x15\x04\x8e\xdaf\x8c\xd6W\xc6\xb2\xfe\xf3\x0b\x8d\\(\xa8\x1c\xde\xe8\xba\xb1\xf0\xdav\x03\xaf>,\x90\xbdV\xe2\xdct\xb5\xb7\x87t\xa6\x11\r\xf4z\xc1`\xe6\xe1DZ\xcfz:}\x9b\xbex\xbd81-J*\x88\x84\x87\x15\xe2\xe3\xf3\xdfr\xdd\xf9\xe1\xf7yY\xd1\x98q\xce}\xe4b\xea\xf6\x9cf\xf1\xae\x05\x94\xc2\x06\xa0\x19.\xd5\xcf\x17pZ\x905\x04\xaa\x03\xf6qS\xc0\xa6\xcb\x10\x03\x1e\x80\xdd\xa2\x19\x87\xc04@\xb6\xfc\xb5tv\xba\x80\xb7\xeeK\xd1\xea83\xa8\xea\xa4\xef\x13\\\xc6\x88\xf2\xd9CX\xe0\xb8\xbf\xba#\xa2f\x8e.%\xc2\xc2C\xd7\xd7\xf33\x05\xb7\xd4p\x88\x82n\x80;\xf4\xd9\xc5\xf8w\xfbW3\x9d\x8e\x8a\xb38\xc4@\x9fjjC\x98<S\xe08\xfe\xe2\x9f[9\x9c\'M@7}\xaaG"I\xe4$u!0\x1f\xca3\xde\xb4.\xaf\x96\xa2u{\x90&\xbes\x03\xa8*\xfb\xe0\x11\x0b\x10\x05\xf0\xb4M\x05\x11,\xdd\xda\xa4\xdcMc\xa5\xd7\xd0\xacz\x9e\x14\xce\'\xaf\x9f\x1a\xd1"\xe7\t\x1c\xf5a\xf9F\xf6\x19\xe1\x9d\x12\xa2\x02]\xcc\xeb\xd9\x8a\xd54H\x9ez\x00\x00\x1f\x1c\tIW\xb4[\xd7\x8a\'\xaa\xfd*\xa4\xd5\xd9\xd6\xc2\x06_\xd0\xa8\xf8\xa44\x1b\x0c\xdc\xd8Nc\xb3\x8d6\x19\\5\x86Re\xd8\xf9\x18\xc0\xd7\xea\x83\xc7\x0b\xbfq\x03\xa3\xf3\n\xaf\n6|\x99\x0c\x1eH\x85\xa5tt9l\x04\xee?%R[\xce\x12\x0c\x9f\xe6\xd8S\xe5\xb9\xc1+.\x86\x8d\xf3\x07\xd6\x19\xbd\x96\xed\xbeW\x91.\xa3/[\xdd\xdb\xc2\x86\x01\x8f\x19\x08\xa0\x1eC\xact\xac\xddU\x8b\xc6\xf8SZ7-_\xe7\x08\x1d79\xcb\xd1h\x9f\xd37\xf7\x9dY+\x18O\x17C\xb4\xbf\x83\xb8\x88\xa8\x84$\xfb\x046\t\x16\x08XC3\xad{\x06\xf0\xdf\xbd\xdc\xd1\xb9-U\x12C\xac\x90(\xb0q$\x1d=\x95K\xb1w$\xb7r\xe5\xc0\x85S~\x01\x12y\xa5\x9fkg\x98\xee\xa4\x14\xa0\xbdM%\xdfn\x886\x80\x91\x03\xa5\xcaEF4\r\xb8\x07z\xc09:\x1c\xd3\xf2>\xaa\xa6bs\xb5\x18 \xf6\xe2\xc8\xdfY\xf9\x96\xbf\xdf\x00J\x05\xc2\x1b;\xcd\x9e\xf9\x93\xeerD\xb8\xe5r\x10\xfd\xa0\x0f\xd0A\xc1?\xca<~\xae5\x94\x9f\x05[m\xf3\x95\xcb\xe7:w\xad_e\x89\xd0\xf6\xe3\xb9\xbc\xff\xac\x99\x1e\'\x8c\x80j (z\x87\x07\xfe\x0e\n\xcf\x81\x1c\x7f^\x179\x95\x93YN\xb9\x04`\x8f\x82\xff_\xd5\x82\x97T\xdbI\xea\x07\x9f\xe9\x84\x1c\xa3\xde\xca#\xc2\xecTZm\xda\xe4\xc7\xe2\'\x9a\xcc`\xf0\xde\xe6\x94\xd5\x8a\x96\x17\xfc\x9fb3\xd52\x0f\n\x8eW\xe9\xbe\x07\x80\xe3y\rt*\xcbw`\xad\xe5\x0e!\xab\x15T\x84\xf6\x0f\xc5\x06\r\\\xb0\x98\xe2\xa8H&\x86\xe4\xe0\x1f/`\xc0*em\xb5\x0fa\xcc\xf9\x8e\x0e\x96;h\xa8C\x01\xf9}81\xb7\xc4\xec\xd6-\xe6\xc0L\x16 \x07\xf2\xc1n\x83:\x8d)\xb9C\x9b\x1ci\xb8-\xacfP\x8d\x97:\xd2XP\x1b_o\xa0\x05?r\x9c\x15j\xc7k\xc92\xcf}\x96p\xbdZ\xfb\xa23\xb5\x0e+k|\xd7\x04\x08\x1b\x89Yr\xb7\x95\x8f\xaa\x13\xd4\xf8SFO\xb4\xb7\xba\x0c\xe3\xa2\xf6~\x0c\xd7\xce\xa1\xc2Z\xd2\xb5\x05c.\xd7\x04&_!(zh\xd1\xde\x81>\x1ba\xce\xc2[p<axg\x04\xf8\xa9\xa1\xd9\xdfZ\xcfL\xe7\xbd\xcf\xc3\xe3\xb7\x12\x0bg/\r\xe4\xd5<\xac\xdba\x98\xe0\x1e\xd8\x82\xd5\x06\xddq\xce\xcc$\xcf\x13{A\xcb \xcc<\xd2\x93/\xf5=\xe1vk\x97VOJ\xa1\x14\xca\xbc\x00a\xa9\xc6t\xcc]+\x87\xa2\r]/\xac\x17S-ei\x0c_\x12cS\x06\x07\xcf\xd6\x17kv\xad\x8cJ`)J5\xb2\x90C\xc3\xd2\xde\xf1\x87yP\xf9n\x82dd\xc4\x83\x00x\x96\xe4\xd8\xdf\x8d\xd5\xd0MD\x85a|\xe6\xe9\xc2zP\x9c\xebH\x88\r\x85\x94\xa7LT\x83o\x1a,G#\xb2&U\xe3,F\xf1\x99\xcd\x8d\x0c\'>\x85\xbc\xb1m\xd9-\xa7\x9c\xc6\x97\xab\x15\xe2\xfd\x1f5\xd9*\xef\xa6\xa3*\xd5B\x853X\xf9\x18Kf\xacy\xc4E\xae,\x87\xd4\xcb\xf6\x07\xec\x93\xabd\x96\x98\x13\xbe\xbd\xfb\xcb\xd9\x81\xf3WT\x1e\x0c\xd3d\x07\xafgz\x198\xd4!T!k\xe5\xe2\x9b0\x88L\xa5Xz\x17,\x08\x8e\xab\xc5\x03z\xe6(1D\xc4i\x7f\x92\x8dhag\x92$\x84V~$\x89v1\xda\x87\xa3G\x1ct\xf3\xef\x98:\xc3\xc8(\xbf\x19\xe33\xbeA&\x89D%\xee\x7fg\x10\tW\xa3\xfe\xebduq\xacm\xa5\xc4J\xfdR\x81\x05\x1bW3YO\xc3\x13>\xa0:\xe71L\xbe5d\xda.\x8d\xbc\x1c\x13\x1az\xf5\x0c\xb0\xde\xc8\xd6=\x13\xad\xdd\xde\x9a\xc2\xcfR\xa3\xcc\x11{]\x893g\x0e\xdd\xb3\x15\xd8*+=b\xd8?Sy\xf1\x8f\xbc\xc5m\x92\xbf\xec\xba\xb4\xe5\x8c\xf7\x03r\xa1\x82$\x94\xec\xd3\t}\x1cG\xfe\x96\x8e\xa7I\xe1\xa5\xb3u/f\x04\xa8\x1b\x1f\xbab\xd2s\xa3f\xca\x89\x04\x112\xf97\xd0\x06\x0b\x8b\xea\xcd\x1f7\xd3\x83\xb1cZ$\'\xcd\xe3ALG\xbd\xef\xf1\x8f,\x03\x19\xb6\x00)\xf8>d-\x14\xe4\x03\xb8\xd5\x98\xa2\xabsO\x8c\xf0\x87\x835MI\x8fN!\xcaKH\xa8\x94T\xcdbHyD\xfbM\x07"3\xc6b\xb2H\xda\xc7\x05\r\ro\xcb\xaa\xa6T\xdct\xcb\t\xaf\xd7\xf6\xdb\x02\x81\xc6%\xac:x\xa8g\x13\x88\xab\xb5B\x04\xd4a\xe4=\xdc\xf9{\x91~\x08P\r\x7f\x0f\xdcY\x8e\x04\x16d\xea\xf4\x13Z\x88\xb8\x1b\xd9\x14\xe1}E\x8b=\xcd\xd5\xda4\x1e\x92\x8c\x11(\xb8\x87\xfb\xb6p\xda\xa43\x1do\x97\x8c\xdap\xe9\x19\x8c\xde\xca\x07>Y\x04%H\xcb$%\xcf\x90u\xf7\x0bt\xcd\x8f\x16h\x8d\xe5E\xf1\xa6\xe6\x02\xe0\xf7/\xc6\xee;\xc9qi\x98p\x01\xa7%\xe0HG\xca\xb5A\xca\x98c:\rTB\xb5\xc6\x04\x06\x0f\xbd\xa3\xb8\xfd\x96\x1b\xd0\xe4*2\xe9\x0b\x9fEwOM\xb1\x86\xf8(\x03\x9f\xb7\xfe\xef\xa3\x93\xb7\x18V\xd2\x9b\xcdS\xf7\x13R\x0c\x88+_\x08\x97\x90\xa9s\xfd\xc0\xfb\xb4\xf67x\x05ue%\xb86ef\xcb\x1c\xea\xe7\xbf0Z\xee\xe0z\x1b\x8c_\x88L\xad\xc4\xa9\xe3\xdeT\x0fRS\xba7\x021\xbe\xe5\x17\x15\x9c#w>\xba\xf8\xeb-\xd9\xba\x8e Ra\xc5\xfeN\x85\x13\xb9\xbc\xa0\x17\xf8\xb4\xeb\xd1\x8f\xe7\x8c\x85\xf1nb\xc4:\x90,!\xbe\xc2\xcb\x96\x1a\x98d\x18\x19\x13\x061\x8d\xbb\x99B\xf3\x86&\x95\x82\x98\xc6R\xc0\xb5\xf1\x1ad3O\x01s\xe0\xe3N\xbeF\xe6E\xcb\xbea\xf6\x14tM\xea\x80\xe8\x9c\xbd\x89aM\xf6\x91!<p\x84-C\xf1\x8bu\xbbN\x00\xc6d\x93l2\xc0q\x8e\x80\xfc\xe1xc~\xcd\x8f\xc5\x19!\x17\x1f\xb0\xae0\x9c\x88\xb8\x04\x80\x9fr\xe1\x96\x03\xee\x84,\x8e\x14\xb1l\xe3\xc2\xdc\xc5g"\xd2C-\x88I\x05>f=\x8dk\xc5V_y\x93\nGx\xb9I\'\xc5\xff\x7f\x03\x95\xc8\xb8\xba\xfd\xfe\x07\xfb\x05\xc7\xd0LGi\x1d5\xf2BN\xb4\xe9O\xb6B?T+q\x0eK\xfe\x9ad\x8e\xae\xe5Q(*\xc2\x9a\x99\x83\xac\x17Q\x00\x01\x9fUM\xab\x85F%\x0b\xc3\xfc\xbdTz\x1d\x8b\xa6\x8d\':\nj\xba\xdd;\x91\xba\xbbu\x88G\x01/\xe6T\xb0f\xa5\x06\x95\xd0\xe9\xeb\x0f\x93\xf0\xa9\xd3\x08.8\xf7V\xea\xc8\x9fv\xea\xaf\xb2\xd6V\xa1IfF\x8d\x1a\x8c:\xf7\x98V\xdeg\xb2"26H\x17\x90\x8e\xe9\xd7\xa4\x1e;\xf9\x0cY\xd8$\xfe\xb9\xfa\xd8yP\x81\xdb\x99\x04\xc3f\xd4\xb4\x96wc\x1b\xdf\xae\x00CK\x95x9\xf6k\xdb\xa7\xab\x11>A\x9e\x96\x8b\xa1\x1a\x1fX\xbf\x12\\^\xbd\x90\xf3\xff\xf6D\x17T|H\x81\x16\xc0\xbfpc\xf2D\xbfK\xf3\x0c\x8a\xd5l\x8e\xd5\x13\x9e`\xd1*7\x008B\xb4d\xaaV\xa1\x90$\x15m\\\xf2\x87cd\xffd1|O\xeb\xc22\x9d\xeaz\xb7\xc9\xc4\xd8|\xa5\x10\xea\x82\x10\xeb~\xfa\xdaQ=\xacIK\xc8,t\xb5%\x00\xbb\xab\x88>L\xfbj\xe2h\xb3\xdd\x0b\x87~\xf0\xc3\xb5\x18\x88E\xea\x80\x01m}}%\xfd\x9a\xe2A\\\xb6\x82=o\x99KYE\xd7*\xad\xd4\xd4\xd4X\x00\xe3\x1fi\x02\xf0Nf\xad\xac\x12\xd1G\x84p\x7f\x89nc\x81\xc9\\r\x8c`\x80\xa0\xb9w:\x8d\xfc\x1fpv\xf8\xb5\xbf\x8c\xa4\xd6\xca\n\xcdfO\xa3*\xe8\n\x07\x95\x93\x8bB\xd0Y\x0f\xd3\x13z\xbcO\x94\xe6\xbd"2: \xda\x9c\x845lfN\x81\xa3r\xc9\x0ed\xdc?\xd1\xcf\x86\xba\xd2\xef\x88\x196d\xacj\x10\xaf\x9f\xa5K\x87\x99\xb5~\xb2\xd0\x9d\xce\x1b\xae \xbf6l\xae\x9c\xc3\xe67\xf3\x06g\xe00\x8f\x82\x1cCG\x1f\x1dgf\xab\xc5\x15\x83|\x0ed\xc1\xd1F"N\x0fs\x14\xf2\xe4\xa9r\xd2\xd9\x03/\xcb\x0f9\xea\xed\x90c\xd8\x0b\x18\xe8\x17Q\x88\xc3<\xb7\xa0\xc9C (\xba\xf7\xfa\x1d\xdbL\xde\x07\xad\xe8\xf2\xfbc\x92d\x0b\xe6\xf1\xcc\xa0\xd6\x08V\xfa\xd9\xc4I*\x00\x9f\xa7\xba\xe7\x1c]\xc5\x06S\xa4(\xd5\xaf\x96n\x1dX\x19*a\x81K;\x80=\xd2e\xc6\xa1\xc4 -\xc9hKW2E\xad5?\xe7\x8dCV\xd6w\xcc\tA\xf3B\xc1\x0533\x99\n\xb0\x00\xc2<\xbb\xdah\xc8\xc4W\xa59\xbe\x10\xe0\x12\xb4( \x0f\xec|\xe7\x9d\xc1p\xc8\xdcwg\x8cL\xaa\x17\x80H\xa5\xbd\xfcU\xfa\xc9\xe2\x9a!\x95d\xd2\x87X\xd9\x91T\xf9 =\xfc\x8dI\xb4\xd8\xd4\x00U\x8a\n\xb8\'g\xb2\xc3#\\~\xde\xc6F\xfd\xa0\x8f\xf7\xf5\xef\xf4\xce\xc7\xaaOl\xdb\xc3i\xe2b\x91\xbb\x83\xf0|\xbb\x14\xc3\xa9S%+{-\xc6\xd6\xb6\xefR\xba\x8f\x90\n2:H\x19)b\xf8\xb5\x8e%\xd5\x90\xfa\xe2&\xf4\xa8r\x94\x9a\xabM\xfc\xcf\xac@r\xe9\xc9\xc5\xf7A4"\x8b\xcd\x87-Z\x18\x12\x08>0N\xa1^\x8fL\xd5\xa5\x81\x90\xbd\xdb\x95\xc8o\xe0\x1a.#\x8a\x08\x998\x1cz\x9fx\xff\x8ex\xcdY\x1d\xf8\xd5L\xbe\x85R\xf4f\xcaB&^\x18fc-\xa7\xc4\xf4\xfd*\x10\xb1\x9c\x8d\x14\x03\xd7\xb2\x1b\xd6\xa7\xe9T\x91n\x1b\xf9_R,\x0fpdg\xdd\xf4\x0c\x08\xa6\x9e\xb9\xb7h\xd0mP\x04r\x1co\x92\x87\x88\xbf\xc4\x04\xf8\xcb\x94\x91k\xbe(\x81\x11B\xc5\x82\x95\xde\xf2\xbf\xc9\x8b>\xacp\xed\xcc\xa4\x1aI\x9f\xab\xb4.i\xbe f\x07\x1f\xd3\x10\xf5\xb6\xe8\x00\xa7\xac\xa4\xa3\xb5\x9e/5EB\xe6\x81\xa8\xfcs\xef)\xf2\xa1\x8a\xed\xb5\xf3i!\xb8$\xf0h\xd7\xb7\xff\xa4Y\xacS%\xfd\xa9\xc4^\xd9\x9f\xe1\xd4\x05\x95\xf4\x85\x18\x06\xc7\xc26S{\xc4t\x80\x1d/|\xd5\xc7\xd2,iWy\x0f`\xd5\xcc\x03U\xb7\x83)\x84\xdam\xe8T\xeej\xf5\x18\x0b\x83\x00MG\xa7\xc1d\xfb\xf0\xd0B \xf2\xaa\xe0\xe5Le/\x0f\x05Ij\xcf\xf6\xcc\xcf\xf7\x86\xd4-\x83\x12Ka\xa1\x80\xc6\x12\x1b9{\xb4\xab<\xf9\xa4\x98n\xb8MoL!\xfeRE\xf1\x1b\xedM*b\x9a\xe8\x1e\xe1Gg!(\x15\x81\x9cn\xde\xfe\xf4/u\x8d\x96\x9e\xbc0\x8f\xee$\xa2@\xe5[\xd7t\xeb.\xf4\xcc\x15o$\x10(\xab\xf6\xf0_\xa3\x0f\x8c]\xceP\x1cxF\x95\x8b\xd8\xcf\xfa#\xfb\xa2\xc8s\x04(\xca{\xb7/\x95"\xa7L\x06|J{n]Q\xc8\xf7\x8e\x92\xdeg\x81\xdaT\xadwv8 \\i\x00\'[\xf2\xed\x7f\x00\r\x87C\xd8C\x1e\xa0p\xa96\xc2\xd4.?c\xf2\x17\xd3\xef\xd76\x02ND\x80\xda\xe8J=\xe4\xbf\xf8jj\xd7\xbb\xbd1\x03\x12K\t\x1e\x08\xfb\x87\xe2D\t\xf4G\xa2\xa7\xc4\xb6\x84yc\x12\xafp\xef\xc7sPc\xc7\x02\x1a`\xf4-\xa3\xbb\x80p\xdb\xaeS\xbeW\xae\xe5\xea\x92<5\x8e9:n\xf0w`2\xa1\x9c\xebA2/s\x9a\xcb\xe6\x7f?tEZ]\t\xc1\x08&\x98M\xc2\xdaV\x7f\xcf\x00\xe6\xcf\x10\xeaO\xb2\x0cP\x13\x91\xac\xc49X\xfa\x07\xe9\x05\xc0\xc2~Ss\x17\xa5\x0fL\r\xf1N\xca\xb7>\xff/\xdf:H\xab\xcbj~\x82Z\xa1\xb0\xf1T\xa9\x1e\xebf\xe7\n\xd2\x8c\x9fL"Q~|\xf7\x02\x90\x1aK\xfc\xc2\x81\x9e]Vl\xb0\xf41\xb2\x1eJ\xa6t\xe9\xd3\x17N_\xac\xe2\x14\xa5\x92\x9d\xe0"\xdc\x0e\xad\xd2v\x9d\x05\xa2aI\x91D\x08\xfd\x15\x03\xdf\xea8s\x92\xfcJ\xaa\x19\xae*u\x10i\xe5f\xd6\xe9V\xbet$^DS\xf0~\'\x04G\x84\x8ep\xac\x89\xc5\xfd*\'!%vux\x0e?\x91\xd7\x8a\xf7\x13\xee{A\x18\x9eO\xf0\x84a\x02\x05#\xb1y\x11\xd6\xdc\xc9/]\x9d\xbe`\x08\xde\xa1R\nW\xd2\xdbF\xb2\x03\x83\xbe\x98:\x83\xbc8\x8f\xc0\xed\x8f\xc1j\xe3\xcfJ~\t\xdb@\xa8\x97\x1b\x97\xe8qs\x10\xe7g8\xdf\xcd\xb2k\xd5\xc0=\xff\x05\x00P\x11\xdd[\x07K\xbd|\x86\x82k\x9a\xfa\xfd`\xb8\xc7\x9c\x1f\xe4z\xda.\x8b>\xe8\xb6\xed\xac\x19\x1a~\xca\xd0\xf6\xe8\x1f\xc9\x9c\xc18H\xad}:I\x8b\x08#\x11\xad\xe9\xa2\x97:\xdf\x1f\x92\xee\x97{\xa5\xe6\xbb\x94O\xc6\xe5iu\xe7\x18>\x086\x87UU\x1es;\xdd\x0e\x91\xe7\x8d7@I\xbf\xd3\x13:\x04\xbf\xdc\xe5\xac\x1f\x94\xd2(\x04E<:\xc5(\xbd,:;\x0c\xb1K\x8en\xedL\x9c \n\r\x03>z%\x9b\xc8\x99\xa6\xb9\\mU\x1b"2]\xe9,]l\xfb\xb2\xd4e\xcd\xb3\xdf\x9e\x85]\xb5E\xea\x95<\x8cnG\xec\x8dP+p\t\x90\t\x89\x98pWC\xad\xdd\xe2$\xaf\xd7\xe8{U\\\xfb\xf9\xa0\xed\x9co\xc9\xedrU\x84\xa8w\xe6C\xfdR3qm\x03\xb8H\x13\x05\xecwS(6\xeb\xf8\xecoOU.\xfdD\x87\xc8\x00\x00\x00\x00\x00\xe9\x18\xf7\xa4\'t\xd3\xd2\x00\x01\xce,\xc8,\x00\x00q\x10(n\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ)\t\xda\x07marshal\xda\x04lzma\xda\x04gzip\xda\x03bz2\xda\x08binascii\xda\x04zlib\xda\x04exec\xda\x05loads\xda\ndecompress\xa9\x00r\n\x00\x00\x00r\n\x00\x00\x00\xfa\nPy-Fuscate\xda\x08<module>\x01\x00\x00\x00s\x02\x00\x00\x00H\x00\x00\x00\x00\x00)\xbf)o\x81\xb08\x05\x00\x01\xf1.\xd9.\x00\x00\xfd\x12\xe5\n\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))
except KeyboardInterrupt:
    exit()