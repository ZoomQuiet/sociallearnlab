# Googlecode介绍 #
Googlecode＋SVN实现集体创作中文件版本控制


教育大发现的Google Code地址：http://code.google.com/p/sociallearnlab/


大家进入以后，能看到的界面主要有6个标签：


Project Home| Downloads| Wiki| Issues| Source| Administrator
（注：Administrator只有Project owners才能看到，Project members看不到）


大家先点点前5个标签，试试吧，看看都有什么东东！～


  * Project Home其实就是我们Googlecode的首页，通过它能链接到各个WIKI页面；

  * Downloads里面可以存放些资料，供大家下载，一般很少用；

  * Wiki就是我们写书和发布一些资料的内容，Googlecode的首页就相当于WIKI的目录；

  * Issues是存放各种需要修改文件的信息，请参看[Task](http://code.google.com/p/sociallearnlab/issues/detail?id=1)；

  * Source是SVN所在地，也是我们Googlecode的核心，便于对文件版本进行控制，SVN包括以下几个目录：


> o  tasks    收集各种和主工程无关的辅助,支持性质任务代码


> o  tangle   对应开辟各种成员目录,收集平时的积累,成熟后就可以合并到trunk中


> o  trunk    主干分支, 所有最新的成果组织在期中，也就是我们的图书

> o branches  发布版本分支收集, 收集阶段性成果,并进行针对版本的追踪维护


> o wiki      图书维基

---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

## Administrator ##
由Administrator来实现以上前5个标签的操作，Administrator中8个子标签，Project Summary| Project Members |Downloads |Wiki |Issue Tracking |Source |Tabs |Advanced ，与上面5个标签配对实现操作,如Project Summary

&lt;--&gt;

Project Home。
#### Project Members... ####
实现对项目成员进行管理
#### Tabs... ####
实现“Downloads | Wiki | Issues | Source”的更改和隐藏，一般不需要操作
#### Advanced... ####
实现删除项目，切勿操作
## Wiki ##
点击左上角的蓝色“New Page”能够创建新的Wiki页面。进入“New Page”页后，一定注意格式
#### Page Name... ####
一定要按照我们起草的《文件命名规范手册》来命名，便于管理
#### Cotent... ####
我们看到的第一句话就是[One-sentence summary of this page.](#summary.md)一定在“summary”后的“空格”后输入简单的Summary，这将在Wiki标签内显示“summary＋Lables”。剩下的内容请参考Wiki右侧的“Wiki Markup Help”
#### Labels... ####
标签便于我们管理，标签请认真填写，详见IssueFlow
选择正确的标签来综合标定问题
## Issues ##
请认真理解IssueTags~Issue标签详解
## Source ##
主要实现与SVN客户端版本控制，TortoiseSVN操作时提示输入用户名和密码http://code.google.com/p/sociallearnlab/source/checkout 中自动获取的，其它应用详见UsageSVN详解