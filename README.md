#Pelican Qiniu

This plugin allows you to use [qiniu](http://www.qiniu.com/) to serve your static files.

##Dependency
- [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/)
- [sevencow](https://github.com/yueyoum/seven-cow)

```
$ pip install sevencow beautifulsoup4
```

##Settings

| Setting name | What does it do? |
| :----------: | ---------------- |
| QINIU_AK | qiniu access key |
| QINIU_SK | qiniu secret key |
| QINIU_BUCKET | Which bucket do you want the files to save in? |
| QINIU_PRE | url prefix |

##LICENSE
[GPL](https://github.com/mtunique/pelican_qiniu/blob/master/LICENSE)
