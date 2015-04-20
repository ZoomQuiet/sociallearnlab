SEE: IssueFlow ~ 提案协同流程
# 介绍 #

**Issue(提案)作为软件开发项目中的bug 提供了实用的追踪管理服务.**
  * 然而实际上,在利用 code.google 进行图书工程时,图书的撰写/勘误/校对等等任务的提交/指派/认领/流转/关闭的处理也非常类似，特此定制并约定相关标签进行支持:
  * 提案实例:**[Issue 4: GSH 故事组大纲设计](http://code.google.com/p/sociallearnlab/issues/detail?id=4)**

## 提案模板 ##
**非成员用:**
  1. Defect report from user ~ 问题报告
**成员使用:**
  1. Task report from member ~ 成员任务提案
  1. Defect report from developer ~ 成员意见提案

... 可以根据需要随时追加不同的提案模板

## 活动提案状态 ~ Open Issue Status ##
```
    New                     = 提案刚刚创建没有人复审过
    Accepted                = 提案已经被人确认，并接受进行处理
    Started                 = 提案开始处置ing..
```

## 关闭提案状态 ~ Closed Issue Status ##
```
    Fixed                   = 已修正ed
    Verified                = 已证实ed
    Invalid                 = 无效的
    Duplicate               = 重复的
    WontFix                 = 无为的～ 我们决定暂时不处理
```

## 预定标签 ~ Predefined Issue Labels ##
### 提案类型 ###
```
    Type-Issue           = 文字讨论
    Type-Defect          = 代码／样例 缺陷
    Type-Enhancement     = 改进建议
    Type-Task            = 撰写任务
    Type-Patch           = 补丁
    Type-Other           = 其它
```
### 提案严重度 ###
```
    Priority-Sentence    = 语句有不妥
    Priority-Paragraph   = 段落有不妥
    Priority-Chapter     = 章节有不妥
    Priority-Word        = 字词有不妥
```
### 图书里程碑 ###
```
    Milestone-tangle0.1  = 混乱阶段,收集内容ing
    Milestone-merged0.5  = 合并阶段,融合所有内容
    Milestone-review0.7  = 复审阶段,关注图书整体思想
    Milestone-release1.0 = 发行阶段,发布图书
```

### 图书组件 ###
```
    Component-GSH        = "Google服务应用手册"~ Google Services Handbook
    Component-STM        = "社会性软件工具应用手册" ~ Socialsoftware Tools Manual
    Component-STM4College = 大学生版 for College Usage Socialsoftware Tools Manual
    Component-STM4Teacher = 教师群版 for Teacher Usage Socialsoftware Tools Manual
    Component-STM4Enterprise = 企业员工版 for Enterprise  Usage Socialsoftware Tools Manual
    Component-SEPL       = "社会性网络环境下的教学活动实施案例" ~ Socialnetwork Education Practice Library
    Component-EiSNS      = "社会性参与式网络中的学与教实践" ~Education in SNS net
    Component-Docs       = 其它文章
```

### 系统影响 ###
```
OpSys-All            = 影响所有操作系统
OpSys-Windows        = 影响M$操作系统
OpSys-Linux          = 影响GNU/Linux操作系统
OpSys-OSX            = 影响Mac操作系统
OpSys-student        = 影响学生群体
OpSys-teacher        = 影响教师群体
OpSys-staff          = 影响职员群体
```


---

源自 openbookproject   http://code.google.com/p/openbookproject/wiki/IssueTags