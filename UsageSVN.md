# SVN简明介绍 #

在团队合作项目中，你是否遇到过这样的情况：当你正在修改一个文件，却出现另一个人作了同样的事情。你是否曾因为这种巧合而导致了你的修改付之东流？

你是否曾经在文件保存之后，又想恢复到文件保存之前？你是否想过要去查看一个文件几天前的内容？

当你发现一个项目中的bug，你是否想知道它是何时出现在你的项目中？

如果你对上面任何一个问题回答“Yes”，那么SVN就是你所需要的！

SVN是Subversion的简写，它是一个自由/开源版本控制系统，可以跨越时间管理文件和目录，记录每一次文件和目录的修改，这便使你可以取得数据以前的版本，从而可以检查所作的更改。

Subversion可以通过网络访问它的版本库，从而使用户可以在不同的电脑上使用。一定程度上可以说，允许用户在各自的地方修改同一份数据是促进协作。进展可能非常的迅速，并没有一个所有的改变都会取得效果的通道，由于所有的工作都有历史版本，你不必担心由于失去某个通道而影响质量，如果存在不正确的改变，只要取消改变。

这只是一个粗略的介绍，详细资料请查阅：

版本管理与SVN为核心的快速开发环境 http://www.zoomquiet.org/share/s5/0707-SVNnTrac

使用Subversion进行版本控制 http://www.subversion.org.cn/svnbook/1.4/index.html

和其它版本管理系统的对比  http://wiki.woodpecker.org.cn/moin/DistributedScm

# TortoiseSVN快速上手 #

我们的项目是在Google Code下完成，Google Code对SVN有很好的支持，于是，对于每一位参与项目编写的朋友来说，只需要在电脑上安装一个SVN客户端就够了。而对大多数人来说，使用命令来完成操作是很头疼的事，于是很多MS客户端应运而生，其中，小乌龟TortoiseSVN就是很优秀的一款。我们以TortoiseSVN为例，介绍如何使用。

TortoiseSVN功能丰富，但是我们只需要学会2个简单的操作即可，第一就是下载文件，第二是上传。下面针对各个功能作出说明。

### 操作命令1：Checkout... ###

1、下载TortoiseSVN的安装版。TortoiseSVN的官方主页http://tortoisesvn.tigris.org。英文不好的朋友可以在Subversion中文站http://www.subversion.org.cn 寻找合适的中文版本下载。安装后，你不会看到任何可执行的程序，因为TortoiseSVN是嵌在windows里面的。

2、在电脑中新建一个空的文件夹，右键点击它，可以看到TortoiseSVN菜单以及上面的SVN Checkout。

3、Checkout的意思签出，可以把svn中的目录文件下载过来，但不同于export下载的是，它具有验证的功能，Checkout到某处的文件、代码将会被TortoiseSVN监视，里面的文件可以享受各种SVN的服务。选择Checkout，就表示这个目录将与这个SVN地址关联，这里的修改可以提交到SVN服务器。但是，首先，你需要具有权限。

4、获取SVN密码。登录我们的教育大发现项目页，进入Source页面，你会看到

```
# Project members authenticate over HTTPS to allow committing changes.
svn checkout https://sociallearnlab.googlecode.com/svn/trunk/ sociallearnlab --username xxx   
```

username后面的xxx就是你的用户名，而https://sociallearnlab.googlecode.com/svn就是我们的SVN地址，点击这段文字下方的 _When prompted, enter your generated googlecode.com password._你就可以拿到SVN密码了。

5、Checkout，将目录与这个SVN地址关联。右键选择SVN Checkout后，会跳出一个页面，在URL中填写我们的SVN地址，其他选项不需要更改，Omit externals不要勾选，HEAD Revision选中表示最新的代码版本，接着点击OK，在跳出的页面填写用户名和密码即可。

6、全部文件checkout之后，目录上会有一个绿色的勾，表示目录与文件为最新（与之相应的，如果是红色叹号则表示该文件已被修改）。这个目录中所有带勾的文件目前都在Tortoise的监视之下了，可以尝试右键单击文件，你会发现可以执行很多操作。接下来我会挑选一些比较常用的来讲解。

### 操作命令2:Commit... ###

假如你更新了目录中的文件，那么就可以用到commit功能。这个功能就是将你本地的文件修改记录上传到服务器上面，可以理解为上传。

但是commit的功能不仅仅是上传，他会和服务器上面的文件进行对比，假如你更新了某个文件而服务器上面也有人更新了这个文件，并且是在你checkout之后做的更新，那么它会尝试将你的更新和他人的更新进行融合（merge），假如自动merge不成功，那么报告conflict，你必须自己来手动merge，也就是把你的更新和别人的更新无冲突的写在一起。

commit的时候，最好填写Log信息，这样保证别人可以看到你的更新究竟做了写什么。这就相当于上传文件并且说明自己做了那些修改，多人合作的时候log非常重要。

### 操作命令3:Add... ###

TortoiseSVN的commit只会上传原先 checkout然后又被修改了的文件，假如你新加入了某些文件，需要右键点击文件选择Add，然后文件上面会出现一个加号，在下次commit的时候它就会被upload并且被标记为绿色对勾。没有绿色对勾的文件不会被commit。

假如你需要给带有绿色对勾文件改名或者移动它的位置，请不要使用windows的功能，右键点击它们，TortoiseSVN都有相应的操作。想象这些文件已经不在是你本地的东西，你的一举一动都必须让Tortoise知道。

### 操作命令4:Revert... ###

假如修改了某个文件但是你后悔了，可以右键点击它选择Revert，它将变回上次checkout时候的情况。或者Revert整个工程到任意一个从前的版本。

### 操作命令5:Update... ###

假如是多人合作的项目，自己不做修改的话别人也要修改，这时候就需要使用update来同步本地和服务器上的代码。同样是右键选择update，所有的更改就会从服务器端传到你的硬盘。注意，假如别人删除了某个文件，那么更新之后你在本地的也会被删除。

如果本地的代码已经被修改，和commit一样会先进行merge，不成功的话就会报告conflict。

### 其他…… ###

假如有的文件不想让别人修改，还可以进行Lock操作。
还有用于查看所有log的show log菜单，现实版本更新图示的Revision graph，查看服务器端目录结构的Repo-browser。
另外还有创建tag操作，相当于把当前的代码版本复制一份到其他地方，然后以这个地方为出发点进行新的开发，与原来位置的版本互不干扰。

## 相关资源： ##
TortoiseSVN的官方主页 http://tortoisesvn.tigris.org

Subversion中文站 http://www.subversion.org.cn

TortoiseSVN 简明使用（插图版） http://fairyfish.net/2007/09/08/tortoisesvn-introduce/

# SVN目录结构 #

SVN/

+-- tasks   推广软文，团队组织定义／流程等

+-- tangle   项目收集（tangle ~ 混乱的,专门用以收藏成员自行设计的项目,如果通过评估就可以合并到主线成为正式功能! ）

+-- trunk    主干分支, 所有最新的成果组织在期中

> |+-- 图书项目名称

> |+-- 图书项目名称

> |+-- 图书项目名称

+-- branches  发布版本分支收集, 收集阶段性成果,并进行针对版本的追踪维护

+-- wiki     工程维基，图书的 beta 版本，以及存放一些编写说明，规则，技术文档，会谈纪要，成员介绍等等