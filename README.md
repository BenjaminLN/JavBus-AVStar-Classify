# Python爬虫+Everything按女优名称整理本地AV资源（需要富强上网）

### 情景：
是这样的，我的一个朋友是大法师，手中施法材料由于在收集的时候没有按施主进行分类，日积月累之后，施法材料多达几个T。为了让各位施主尽快找到归宿，他让我想一个方案进行分类。

### 原理如下：
**每次使用Python爬虫从某东瀛网站Javbus上爬取小姐姐的全部作品番号，用 `| `间隔开，将结果用Windows本地搜索之王 Everything 搜索即可。其中设置一个cookies`cookiesDit = {'existmag':'all'}`，将搜索内容设置为`全部影片`。


### 使用方法：
1. 需要富强上网，小飞机直接开全局，或者修改`request.proxies = {"https": ''}`即可，我是直接把PAC URL填进去。
2. 将url修改成女优的Javbus的首页，如https://www.javbus.com/star/tyv 运行即可，得到番号和去掉了"-"的番号。
3. 将其填入Everything搜索即可得到这个女优在你本地磁盘中的所有资源，剪切放到同一个文件夹整理。

### 为方便使用，已打包https://github.com/BenjaminLN/AVstar-Classify/releases

![TIM图片20190919013123.png](https://i.loli.net/2019/09/19/ZjikYPrtNv64Ahd.png)

![TIM图片20190919013558.png](https://i.loli.net/2019/09/19/KwkxgM5413iyGcI.png)
