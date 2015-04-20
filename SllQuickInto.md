余波、王万清老师和吴长城一起为教育大发现社区的朋友初步搭建了写作平台，这个平台主要是由GoogleCode和SVN组成。大家可以动手来做做。

# 初始化工具 #

按照以下顺序，我们先应用这样几个工具：

1、2、版本控制SVN＋code.google：http://code.google.com/p/sociallearnlab/

3、项目管理 Everydo：http://sociallearnlab.everydo.com

4、实时讨论~ IRC

**请记住以上这些网址。**

## 工具使用快速教程 ##

`以下是针对上面工具的应用手册，大家看着做就可以：`

  1. Code.Google ~ http://code.google.com/p/sociallearnlab/wiki/UsageGooglecode
  1. SVN：http://code.google.com/p/sociallearnlab/wiki/Usage
  1. IRC：http://code.google.com/p/sociallearnlab/wiki/UsageIRC
  1. Everydo：http://code.google.com/p/sociallearnlab/wiki/UsageEverydo

## 任务驱动（边看边做） ##

### code.google ###

#### 1.1 熟悉GoogleCode界面 ####

GoogleCode手册看完后，大家进入Googlecode，能看到的界面主要有6个标签：

Project Home| Downloads| Wiki| Issues| Source| Administrator （注：Administrator只有Project owners才能看 到，Project members看不到） 大家先点点前5个标签，试试吧，看看都有什么东东！
  1. Project Home其实就是我们Googlecode的首页，通过它能链接到各个WIKI页面；
  1. Downloads里面可以存放些资料，供大家下载，一般很少用；
  1. Wiki就是我们写书和发布一些资料的内容，Googlecode的首页就相当于WIKI的目录；
  1. Issues是存放各种需要修改文件的信息，请参看Task；
  1. Source是SVN所在地，也是我们Googlecode的核心，便于对文件版本进行控制，SVN包括以下几个目录：
    * tasks 收集各种和主工程无关的辅助,支持性质任务代码;
    * tangle 对应开辟各种成员目录,收集平时的积累,成熟后就可以合并到trunk中;
    * trunk 主干分支, 所有最新的成果组织在其中，也就是我们的图书 o branches 发布版本分支收集, 收集阶段性成果,并进行针对版本的追维护；
    * wiki 图书维基。

#### 1.2 完成WIKI页面制作，写个自我介绍 ####

大家对GoogleCode有个大概了解后，手痒痒了吧！开始做吧！

第一步：进入WIKI页面：点击左上角的蓝色“New Page”能够创建新的Wiki页面。进入“New Page”页后，一定注意格式 ；

第二步：页面命名Page Name...（您的英文名字）一定要按照我们起草的《文件命名规范手册》来命名，便于管理；

第三步：填写内容Cotent...

我们看到的第一句话就是One-sentence summary of this page.一定在“summary”后的“空格”后输入简单的Summary，这将在Wiki标签内显示“summary＋Lables”。剩下的内容请参考Wiki右侧的WIKI标记语言帮助“WikiMarkup Help”；

第四步：添加标签Labels...

标签便于我们管理，标签请认真填写，详见IssueFlow 选择正确的标签来综合标定问题，请认真理解IssueTags~Issue标签详解；

第五步：保存；记得经常保存WIKI，以免丢失！同时，也可以在编写过程中预览（Preview）；

第六步：完成。

#### 1.3 发表ISSUES ####

第一步：看例子；点击ISSUES标签，进入ISSUES页面，先看Tsak；

第二步：新建ISSUES；自己新建个需要修改的ISSUES；

第三步：发表一个ISSUES评论；

第四步：完成。

做完这些，你理解googlecode是做什么的吗？如果还不明白，请您做SVN，做完就会明白啦！

### 2  SVN ###

#### 2.1 先要下载SVN ####

从这儿下载:
http://www.subversion.org.cn/?action-viewnews-itemid-64

进入后，能看到3个下载文件，下载以下两个文件:

  * TortoiseSVN-1.5.0.13316-win32-svn-1.5.0.msi
  * LanguagePack\_1.5.0.13316-win32-zh\_CN.msi

然后依序安装以上两个文件.（注：你的机子是32位还是64位，以上是32位的安装程序，64位则下载另一个）。

#### 2.2 用SVN上传和下载文件 ####

按这个上面说明进行操作：

http://blog.csdn.net/andylin02/archive/2007/07/06/1681387.aspx

  * 在本地计算机建立一个文件夹，比如我在E盘建立了“SocialLearnLab”文件夹，右键点击该文件夹，就可以使用刚才安装的“TortoiseSVN”。
  * 选择TortoiseSVN菜单下的Export…，接着它会让你输入url；
例如输入https://sociallearnlab.googlecode.com/svn，提示输入用户名和密码（用户名和密码是在http://code.google.com/p/sociallearnlab/source/browse/，左上角的checkout的URL 中自动获取的（When prompted, enter your generated googlecode.com password.））成功之后在本地“SocialLearnLab”文件夹中出现几个子文件夹,分别是：

```
\branches
\tangle
\tasks
\trunk
\wiki
```

(各文件夹说明参看[UsageSVN](UsageSVN.md))

当然,以后编辑可以直接在本地文件中的文件中进行编辑,然后再通过“ commit” 上传即可。

当然还可以直接访问http://code.google.com/p/sociallearnlab/，会看到界面上方有5个标签：Project Home| Downloads| Wiki| Issues| Source|,(这里还有一份说明http://code.google.com/p/sociallearnlab/wiki/UsageGooglecode)。

请记住这几个命令：Export，Commit，Revert，Add，Delete...

#### 2.3 删除你上传的文件（请勿乱删除） ####

关于如何为何需要SVN：

SVN简明介绍：http://code.google.com/p/sociallearnlab/wiki/UsageSVN

进一步参考：http://tortoisesvn.net/

> http://www.subversion.org.cn/svnbook/1.4/index.html

### 其它 ###

IRC，Everydo使用说明，已经很详细啦，大家自己看着做吧!这里就不多说啦！记得不知道的地方用Google，也可以用IRC和在这里和我们讨论啊！Everydo可以后面再了解！前三种工具越快用越好！

# TODO #

  * 提供对应的教程录像...