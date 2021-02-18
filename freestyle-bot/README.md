# README

## ffmpeg

据说可以直接用`ffmpeg`捕获`m3u8`并存成文件，测试一下吧，下面是AG Player的地址

`https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8`

```bash
ffmpeg -i https://fms2.uniqueradio.jp/agqr10/aandg1.m3u8 -t 60 output.mp4
```

卧槽...牛逼疯了，这样就可以写一个简单的自动录制了。用一个自动启动的命令，在六点半的时候启动并录制30分钟，然后等时间一过拿文件就行了。

