# AIFaceChangingfor1024eecs
小型赛事项目代码, [推送链接](https://mp.weixin.qq.com/s/TuG7VUBKBkHNbs2RvlMGZw)
项目效果是实现对笔记本/PC外接摄像头输入的ai换脸. 搭配OBS这类直播推流软件效果更佳.

### 配置(Windows)
注意不要在中文路径下使用(因为dilb库的路径读取写的唐)
```
scoop install cmake
git clone https://github.com/ICUlizhi/AIFaceChangingfor1024eecs.git
pip install -r requirements.txt
```
### 使用
```
python main.py images/xj.jpg
```
其中 images/xj.jpg 可替换成你想要的人物头像路径
运行程序会弹出一个窗口实时直播换脸后的摄像头画面, 如需用于直播还要借助obs软件

### OBS
- [OBS下载](https://obsproject.com/)
- 运行obs后在"来源"中添加对脚本程序弹出画面的"窗口采集",即可以在画布上看到我们的换脸画面
- 打开虚拟摄像头用于微信聊天or会议展示...
- 或者使用obs的直播推流方法...

[似乎用到了的项目](https://github.com/JeffTrain/face-swap)