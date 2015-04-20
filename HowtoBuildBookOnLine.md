#summary 如何组织在线图书工程 经验组织.
#labels Phase-Support

# 如何组织在线图书工程 #

啄木鸟/CPyUG 几年来主持组织了不少[Py技术图书的翻译/原创工程](http://wiki.woodpecker.org.cn/moin/OpenBookProject), 但是能力有限，不可能出面组织所有图书的翻译，所以有必要分享**在线图书工程**的组织经验了

  * 参考: [写作心得分享\_董越老师文章：我是怎样写作《理解软件配置管理》的](http://groups.google.com/group/BVtougao/browse_thread/thread/b600341d1bf15838)

## 兴趣 ##
**态度决定一切!**
  * 在线分布式团队的构成,更加要求臭味相投,最好是一个稳固的社区中的老朋友们
  * 选题的有趣和有用,也是图书成功的绝对必要条件

## 资源 ##
**图书也是工程!**
  * 就按照软件工程的方式来组织大家都习惯且有效!
  * 网络中的对应免费服务是齐全的:
    * 版本控制~ code.google 等等免费工程管理服务
    * 日常沟通~ groups.google 等等免费列表服务
    * 知识积累~ wikidot.com 等等免费维基服务
    * 实时讨论~ IRC at freenode.org  等等聊天服务
    * 项目管理~ Everydo 等等免费管理服务
      * 进度计划~  google.com/calendar 等等在线日历服务

## 技巧 ##
**没有规矩不成方圆**
  * 定期的IRC会议非常有助于鼓励士气,協商进度,调节任务
  * 一定要有热心的核心人物来協調和决定所有变更(前期应该是发起人,后期由编辑分担比较合理)
  * 200页以内的小书,团队有多少人是没有关系的,因为任何偏差都可以快速修订
  * 大于300页的图书,写作团队应该控制在5人以内,否则,沟通将是没有尽头的事儿了:
    * 合理的团队构成:
      * 2~5人的撰写成员
      * 3~10 人的校对成员
      * 随便多少人的关注/宣传成员
      * 1~2 个稳定的跟随编辑
  * 一定不要使用任何 Office 格式文档来进行交互组织!这是无法进行版本控制的二进制东西!
    * 结构化文本
    * 纯文本
    * HTML
    * TeX文本
    * 等等都是可以良好的通过版本控制环境进行充分管理的格式!一定要坚持使用!
    * 即使在交付前统一倒入 Word 之流来统计字数,也要坚持使用!

## 原则 ##
**所有人知道所有事儿！**
  * 这是社区化分布式协同的最重要原则! 防止误会/误解/偏差,令所有人都在正确的信息基础上进行工作/思考/创新;并可以立即分享到所有人的进步!
  * 但是,这也是有技巧的哪:

**任何事儿,得通过恰当的渠道令所有人舒服的获得;**
  * 类似列表这种异步信息沟通,如果不是所有人一直积累浏览邮件,将形成各种"惊奇",,,特别是列表的使用礼节没有都习惯时;
  * IRC 这种实时沟通渠道,对大家的时间要求非常高,而且到点如果手头有事儿的,也不可能很好的接受讨论信息,,,

所以,就俺的体验,一定要将各种渠道合理配合使用:
  1. 维基作为唯一的正式决议通告方式,每个方面的决议使用独立的页面进行收集,整理,形成全球唯一的URL 标识的信息节点;
    * (以免决议形成不同版本,形成噪音)
  1. 列表作为有证据记载的讨论中心,大家可以在不同的时间分别相互理解和发表意见,最终形成决议,正式发布到维基中
  1. IRC/MSN/好看/主页/日历<sub>,</sub>各种灵活的信息发布渠道,作为提醒渠道,将决议维基URL 不断的通告给所有人

这样,社区事务的正式发布/变更讨论/通告传播 就有机结合起来了,,,

## 出版 ##
**出版是不比撰写轻松的复杂工程!**
  * 国家法令法规,行业潜则,市场反应,目标人群,流行模式,排版风格... 都是出版方面的专业知识,不是软件行业行者可以轻易体悟的到的!
  * 有技术背景的编辑是个宝!
  * 固定的编辑是永远的朋友!
  * 固定的编辑追随进行田间管理是种幸福,否则是很郁闷的事儿~你得将相同的话,不断的反复说给不同的负责编辑
  * 不使用 M$ Office 的编辑在中国是神话!

教训::
  * 一定要有合同，有社区背景中，出版社对署名的理解是不同的，一定要事先沟通好，否则，会有解释不清的麻烦，对社区贡献也是个隐患
  * 签定合同时,一定要有法人资格的社区出面来交涉,出版社会比较重视...

---

转载:**OBP** ~ Open Book Project：http://code.google.com/p/openbookproject/wiki/HowToBuildBookOnline