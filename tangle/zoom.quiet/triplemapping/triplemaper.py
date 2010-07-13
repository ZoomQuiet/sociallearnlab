# -*- coding: utf-8 -*-
'''triplemaper.py
usage Graphviz dot to gen can click map for 学生定义
    - 100311 creat for base way
usage:
    $ python triplemaper.py 100310-all-sample.txt

reverions::
    __author__  = "$Author$"
    __date__    = "$Date$"
    __revision__= "$Rev$"
    __url__     = "$URL$"
'''
VERSION = "triplemaper.py v10.3.11"

import os,sys
import time,datetime
import base64
from cfg import MM


NOW = "%s"%(time.strftime("%y%m%d",time.localtime()))
NOWTIME = "%s"%(time.strftime("%y%m%d %H:%M:%S",time.localtime()))
LOG_FILENAME = '_logs/mapping-%s.log'%NOW

def initlog():
    '''base Limodou blog easy creat logger obj.can logging as:
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")
    '''
    import logging
    logger = logging.getLogger()
    hdlr = logging.FileHandler(LOG_FILENAME)
    formatter = logging.Formatter("[%(asctime)s]%(levelname)-8s`%(message)s`")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return logger
class mapper:
    """main class for mapping moinmoin pages
    """
    def __init__(self,relatdatafile):
        """ini all
        """
        self.cfg = MM
        self.logger = initlog()
        self.logdo = 0  #处理数据行数
        self.data = relatdatafile
        self.pathlog = "_logs/"
        self.pathtpl = "_tpls/"

        self.tplmain = "dotmain.tpl"
        self.tplrelat = "dotrelat.tpl"
        self.tplnode = "dotnode.tpl"
        self.tpldotmain = open("%s/%s"%(self.pathtpl,self.tplmain)).read()

        self.expdot = "triplemaper.dot"
        self.mapdict = {}
        self.mapall()

        #print self.MM

    def mapall(self):
        """主程序图谱节点分析:
            {节点名:{指向节点名:计数
                    ,..}
                ,..}
        """
        rlines = open(self.data).readlines()
        for line in rlines:
            self.logdo +=1
            #print line[:-1]
            self._push2dict(line[:-1].split())
        print self.mapdict
        tv_timstamp = NOWTIME
        tv_rev = VERSION
        dotmapname = self.cfg["MAPNAME"] % locals()
        dotnodes = self.gen_dotnodes()
        dotrelats = self.gen_dotralet()
        open(self.expdot,"w").write(self.tpldotmain % locals())
        #print self.mapdict
        '''
        for key in self.mapdict.keys():
            print key
            #print self.mapdict[key][0],self.mapdict[key][1]
        '''
    def _push2dict(self,relats):
        """行内容字典分配:
        """
        if 3<len(relats):
            # 不处理超过3元的行定义
            return None
        else:
            objnode = relats[0]
            midnode = relats[1]
            endnode = relats[2]
            self._relat2dict(objnode,midnode)
            self._relat2dict(midnode,endnode)
            '''
            for i in range(len(relats)):
                if relats[i] in self.mapdict.keys():
                    self.mapdict[relats[i]][0]+=1
                else:
                    if (i+1) == len(relats):
                        self.mapdict[relats[i]]=[1,None]
                    else:
                        self.mapdict[relats[i]]=[1,relats[i+1]]
            '''
        return self.mapdict
    def _relat2dict(self,fromnode,pointnode):
        """行内容字典元素关系分配:
        """
        if fromnode in self.mapdict.keys():
            if pointnode in self.mapdict[fromnode].keys():
                self.mapdict[fromnode][pointnode] += 1
            else:
                self.mapdict[fromnode][pointnode] = 1
        else:
            self.mapdict[fromnode] = {}
            self.mapdict[fromnode][pointnode] = 1
    def gen_dotralet(self):
        """生成图谱节点关系
        """
        dotrelats = ""
        for key in self.mapdict.keys():
            nodename = key
            dotfrom = nodename #base64.b64encode(nodename).replace("=","")
            for next in self.mapdict[key].keys():
                dotnext = next
                noderank = self.mapdict[key][next]
                #%s->%s [label="%s",style="setlinewidth(%s)",color="#%s"];
                dotrelats += open("%s/%s"%(self.pathtpl
                    ,self.tplrelat)).read()%(dotfrom
                        ,dotnext
                        ,noderank
                        ,self.cfg["LWIDTH"]+noderank*self.cfg["LWSTEP"]
                        ,self.cfg["COLORSEED"]-noderank*self.cfg["COLORSTEP"]
                        )
        print dotrelats
        return dotrelats


    def gen_dotnodes(self):
        """生成图谱节点
        """
        dotnodes = ""
        for key in self.mapdict.keys():
            nodename = key
            #%(dotitem)s [label="%(dotlabel)s",URL="%(doturl)s"];
            dotitem = nodename  #base46node
            dotlabel = nodename
            doturl = "#"
            dotnodes += open("%s/%s"%(self.pathtpl,self.tplnode)).read()% locals()
        return dotnodes




if __name__ == '__main__':      # this way the module can be
    if 2 != len(sys.argv):
        print """ %s usage::
$ python triplemaper.py DataFile [like: 00310-all-sample.txt]
        """ % VERSION
    else:
        begin = time.time()
        df = sys.argv[1]
        tm = mapper(df)
        end = time.time()

        info = ">>>runing time=%.2fs<<<"%(end - begin)
        print info
        tm.logger.info("^_^: %s"%info)
        info = ">>>chked nodes=%s<<<"%tm.logdo
        print info
        tm.logger.info("^_^: %s"%info)

        info = ";-) export data .dot mapping \n by %s"%VERSION
        print info
        tm.logger.info("^_^: %s"%info)



