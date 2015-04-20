

SEE::[SLL项目流程](SllProjectFlows.md)/**[仨儿之建议集](SllPrjZQ.md)**
# code.google #
**这是 Google 提供的免费轻量级项目管理环境,,,**

**简介：**
```
配合有 SVN 版本管理后台的，
自动渲染发布环境，
通过WIKI 进行索引，通过SVN 进行协同发布，
通过列表进行沟通，
通过Issue 进行问题追踪...
```

## 配置 ##

首页::
  * http://code.google.com/p/sociallearnlab/
  * 没有在 wiki 目录中有反应,所以,只能人工编辑,俺重构了一下,
  * 建议,这个工程首页,应该作为一个根索引页,作为所有其它页面的总入口,
  * 另外,俺建议,在组织所有维基页面时,有个基本准则,就是任何一个维基页面从首页进行点击访问时,不应该超过3次点击!

联动::
  * 接下来，应该将 code.google 和列表联动，
  * 在工程的 admin. 标签中 Activity Notifications 一节有描述:
    * codesite-noreply@google.com
  * 是工程的自动通告邮箱，将其加入到列表订阅中，配置成只 web 查阅，但是允许发送邮件，
  * 就可以在 code.google 中设定，
  * 将所有SVN 检入活动或是Issue 的提交情况，自动汇报给列表了....

出自:_[关于“教育大发现”社区功能架构的一点建议](https://groups.google.com/group/sociallearnlab-members/browse_thread/thread/f077f2c27486beb2/6b631001b5344f64?lnk=gst&q=%E6%B2%A1%E6%9C%89%E5%9C%A8+wiki+%E7%9B%AE%E5%BD%95%E4%B8%AD%E6%9C%89%E5%8F%8D%E5%BA%94%2C%E6%89%80%E4%BB%A5%2C%E5%8F%AA%E8%83%BD%E4%BA%BA%E5%B7%A5%E7%BC%96%E8%BE%91%2C%E4%BF%BA%E9%87%8D%E6%9E%84%E4%BA%86%E4%B8%80%E4%B8%8B#6b631001b5344f64)_ <sup>- SocialLearnLab-Members:“教育大发现”核心成员列表 | Google 网上论坛</sup>
### Issue追踪系统 ###

可惜，code.google 作为一个完备的项目管理环境，大家用的并不完全，Issue 是一个非常简洁好用的追踪系统，
可以进行任务分配/问题追踪/缺陷记录/需求设计<sub>,, 配合维基 更加可以完善的记录项目的进度</sub>,

出自:_[我将在Chandler过程中的经验总结了一下，写了一篇文章出来](https://groups.google.com/group/sociallearnlab-members/browse_thread/thread/1a55e1d7dcadba8b#)_ <sup>- SocialLearnLab-Members:“教育大发现”核心成员列表 | Google 网上论坛</sup>


`> 我想肯定有一部分人，跟我一样，没有弄清楚Googelcode中Issue如何用。`

感谢 xiuli 勇敢品尝螃蠏！
  * 不过，从很久之前，以下两个专项说明页面，就是在工程首页的了:
    1. [Issue 提案流程概述](http://code.google.com/p/sociallearnlab/wiki/IssueFlow)
    1. [Issue 提案标签详解](http://code.google.com/p/sociallearnlab/wiki/IssueTags)

请大家查阅后，对比 xiuli 老师的操作，自个儿也尝试一下，
开始将大任务分解成可追踪的小任务，开始追踪/流通/分配吧,,,,
  * 发现 Issue 的个性, 不是维基语法,对 URL 不进行自动解析,

但是对 Issue 相关的行动都有对应的自动解析了, 从我们创建 Issue 开始到完成任务:
  1. 创建提案后, [最后的 id= 的数字就是全球唯一的任务编号,,](http://code.google.com/p/sociallearnlab/issues/detail?id=5)
  1. 在Issue 中 任何地方使用 " [Issue 5](https://code.google.com/p/sociallearnlab/issues/detail?id=5) " 这种格式的字串,就可以自动解析成提案的链接!
  1. 在我们为此任务进行SVN 检入时的注释中就可以使用! 这样在 SVN 的Changeset 中,就可以自动解析出任务的链接:
    * 例如: [r525](http://code.google.com/p/sociallearnlab/source/detail?r=525)
    * Changeset 列表在:[Changeset list](http://code.google.com/p/sociallearnlab/source/list)
  1. 最后我们回到 Issue 页面,可以使用 " [r525](https://code.google.com/p/sociallearnlab/source/detail?r=525) " 格式的字串来说明SVN的操作, 一样这将自动解析成链接,指向[source r525](http://code.google.com/p/sociallearnlab/source/detail?r=525)

由此,一个具体任务的 创建/指派/完成/关闭 的整体过程的所有信息形成了完整的封闭循环!
```
Issue->认领->SVN检入解决
 ^            |
 |            |
 +--注释说明---+
```

出自:_[我将在Chandler过程中的经验总结了一下，写了一篇文章出来](https://groups.google.com/group/sociallearnlab-members/browse_thread/thread/7a714474b8bbb02e/c25a353750bc0497?lnk=gst&q=%E6%84%9F%E8%B0%A2+xiuli+%E5%8B%87%E6%95%A2%E5%93%81%E5%B0%9D%E8%9E%83%E8%A0%8F%EF%BC%81#c25a353750bc0497)_ <sup>- SocialLearnLab-Members:“教育大发现”核心成员列表 | Google 网上论坛</sup>


## 版本管理 ##

对于任何協作团队来讲，核心要命的支持管理就是"版本管理"

`> >简单可行最好，如果需求工具太多，怕大家应付不过来。`

是也乎,SVN 这个版本管理工具是任何对自个儿知识负责的人都应该学习和使用的,
这样才能够进入有版本管理的知识管理境界,
  * [SVN + Trac 以及知识管理](http://www.zoomquiet.org/share/s5/0707-SVNnTrac/)～一次培训的资料:

SVN, 可以方便统一的作到:
  1. 将所有成员的工作，通过中央仓库的形式进行同步和安全的分发
  1. 将成员所有交付成果，进行了版本管理，可以安全回溯到历史任何一个时间点
  1. 对文本的冲突，进行了自动化的提醒，可以精确的汇报出差异，类似:
    * [r146和r145差异](http://wiki.woodpecker.org.cn/moin/TrustedGroup?action=diff&rev2=146&rev1=145)
    * 或是: http://tinyurl.com/5axbxs
    * [原始链接](http://trac.edgewall.org/changeset?new=7440%40trunk%2Ftrac%2Fwiki%2Fdefault-pages%2FTracModPython&old=7422%40trunk%2Ftrac%2Fwiki%2Fdefault-pages%2FTracModPython)
  1. 可以通过分支的管理，对工程发行版本，进行并行维护...

总之对于团队工作的项目管理:
```
需求／变更／版本／发布 管理是有机结合在一起的，统称配置管理，
没有 CM ~ configure manage 配置管理，工程的进度，就无从控制，
```

出自:_[关于项目管理经验与平台](https://groups.google.com/group/sociallearnlab-members/browse_thread/thread/a7be4c641236762e/3901e9fbc0f45cca?lnk=gst&q=%E6%B2%A1%E6%9C%89+CM+~+configure+manage+%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%EF%BC%8C%E5%B7%A5%E7%A8%8B%E7%9A%84%E8%BF%9B%E5%BA%A6%EF%BC%8C%E5%B0%B1%E6%97%A0%E4%BB%8E%E6%8E%A7%E5%88%B6%EF%BC%8C#3901e9fbc0f45cca)_ <sup>- SocialLearnLab-Members:“教育大发现”核心成员列表 | Google 网上论坛</sup>

～～～～

### SVN 仓库策略 ###
SVN 版本仓库,可以想象成一个中央存储,智能化的将所有人的成果合理合法的保存下来,所有人的工作,以SVN仓库为准,进行版本更替;
  * SVN 版本管理是来自CVS 等等更早的系统策略的,
  * 比较经典的 :[FreeBSD 版本发布策略](http://www.freebsd.org/doc/en_US.ISO8859-1/articles/releng/release-proc.html)

所以,code.google 提供的 SVN 目录内含的版本策略是:
```
/ 仓库根
 +-- wiki 工程维基
 +-- tag  标签版本
 +-- trunk 主干分支
 +-- branches 版本分支
```
其中 tagu和branches 和从CVS 时代继承下来的习惯,但是在SVN中,俺建议:

[开源模式项目SVN规约](http://wiki.woodpecker.org.cn/moin/OssSvnRule)
```
/ 仓库根
 +-- wiki     工程维基
 +-- tasks    任务分支收集
 +-- tangle   试验代码收集
 +-- trunk    主干分支
 +-- branches 发布版本分支收集
```
这样SVN 的目录使用就根据不同的代码,或是文本性质进行了明确的分类:
```
+-- tasks    收集各种和主工程无关的辅助,支持性质任务代码
+-- tangle   对应开辟各种成员目录,收集平时的积累,成熟后就可以合并到 trunk 主干代码中
+-- trunk    主干分支, 所有最新的成果组织在期中
+-- branches 发布版本分支收集, 收集阶段性成果,并进行针对版本的追踪维护,比如说:
 +-- Ss4student_0.1_tadpole   v0.1 蝌蚪 版 图书稿和样例
 +-- Ss4student_0.2_frog      v0.2 青蛙 版 图书稿和样例
```

出自:_[关于“教育大发现”社区功能架构的一点建议](https://groups.google.com/group/sociallearnlab-members/browse_thread/thread/f077f2c27486beb2/759eda8141b0e376?lnk=gst&q=%E6%89%80%E4%BB%A5%2Ccode.google+%E6%8F%90%E4%BE%9B%E7%9A%84+SVN+%E7%9B%AE%E5%BD%95%E5%86%85%E5%90%AB%E7%9A%84%E7%89%88%E6%9C%AC%E7%AD%96%E7%95%A5%E6%98%AF%3A#759eda8141b0e376)_ <sup>- SocialLearnLab-Members:“教育大发现”核心成员列表 | Google 网上论坛</sup>

### code.google 的维基 ###

  * 其实 code.google 提供的维基,就已经是非常吻合最小原则的有自动化版本协同的发布系统了;
  * 因为 code.google 的维基和SVN 是联动的
    * http://openbookproject.googlecode.com/svn/wiki/
  * 通过 SVN 对 维基的中的文本进行修订就可以直接获得 web 方面的修订!

**e.g::**
  * 进行[r1382](http://code.google.com/p/openbookproject/source/detail?r=1382)的SVN 提交,就自然的修订了:
    * http://code.google.com/p/openbookproject/wiki/ZoomQuiet

而且已经有一些项目直接使用 这个简单维基进行了图书的撰写:
  * [ByteOfZhpy](http://code.google.com/p/zhpy/wiki/ByteOfZhpy)

出自:_[关于“教育大发现”社区功能架构的一点建议](https://groups.google.com/group/sociallearnlab-members/browse_thread/thread/f077f2c27486beb2/759eda8141b0e376?lnk=gst&q=%E5%B0%B1%E5%B7%B2%E7%BB%8F%E6%98%AF%E9%9D%9E%E5%B8%B8%E5%90%BB%E5%90%88%E6%9C%80%E5%B0%8F%E5%8E%9F%E5%88%99%E7%9A%84%E6%9C%89%E8%87%AA%E5%8A%A8%E5%8C%96%E7%89%88%E6%9C%AC%E5%8D%8F%E5%90%8C%E7%9A%84%E5%8F%91%E5%B8%83%E7%B3%BB%E7%BB%9F%E4%BA%86#759eda8141b0e376)_ <sup>- SocialLearnLab-Members:“教育大发现”核心成员列表 | Google 网上论坛</sup>

～～～～

咔咔咔,这也是 code.google 在 Guido 加入后给出的完美解决方案:
```
[https://sociallearnlab.googlecode.com/svn/wiki/]
 + <-> [http://code.google.com/p/sociallearnlab/w/list]
 + <-> 用户本地 svn 工作复本
```
关系如上,对于code.google的维基 和 通过SVN 检入 wiki 目录, 是完全一样的,没有任何差别,
  * SVN 仓库, 对这两种表现都是个版本仓库,
  * 不过,一个是在线编辑,一个是离线编辑;
  * 在线的必须有网络,而且只能使用网页的输入框,
  * 离线的,可以在任何地方放心的进行编辑,而且可以使用自个儿喜欢的编辑器进行!

**再次建议!!!**
  * 在所有图书维基页面发布之前,先在 trunk 中创建组织好文档,维基发布出来后,就可以进行公众评阅了!
  * 俺建议文件命名规范:
```
ZhGshAccountHowto.wiki
|  |  |           +-- wiki 后缀的纯 utf-8 文本文件,可以直接复制到 wiki 目录自动发布的
|  |  +-- 章节E文名,使用WikiName 格式
|  +-- 图书工程缩写
+-- 语言地域缩写 Zh|En|Tw|Fr ...
```

出自:_[关于“教育大发现”社区功能架构的一点建议](https://groups.google.com/group/sociallearnlab-members/browse_thread/thread/f077f2c27486beb2/c2fe9328e1a998e9?lnk=gst&q=%E5%92%94%E5%92%94%E5%92%94%2C%E8%BF%99%E4%B9%9F%E6%98%AF+code.google+%E5%9C%A8+Guido+%E5%8A%A0%E5%85%A5%E5%90%8E%E7%BB%99%E5%87%BA%E7%9A%84%E5%AE%8C%E7%BE%8E%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88%3A#c2fe9328e1a998e9)_ <sup>- SocialLearnLab-Members:“教育大发现”核心成员列表 | Google 网上论坛</sup>

# Discuss #
`还有什么想法?持续聚集哪,,,`
