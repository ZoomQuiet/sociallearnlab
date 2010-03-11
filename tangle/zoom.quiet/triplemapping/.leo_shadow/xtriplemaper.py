#@+leo-ver=4-thin
#@+node:zoomq.20090409122718.2:@shadow triplemaper.py
# -*- coding: utf-8 -*-
'''triplemaper.py
usage Graphviz dot to gen can click map for 学生定义
    - 100311 creat for base way
usage:
    $ python triplemaper.py 100310-all-sample.txt

reverions::
    __author__  = "$Author: zoomq $"
    __date__    = "$Date: 2009-12-04 09:00:41 +0800 (五, 2009-12-04) $"
    __revision__= "$Rev: 11788 $"
    __url__     = "$URL: http://svn.rdev.kingsoft.net/matter/tangle/zoom.quiet/hackminds.leo $"
'''
VERSION = "moinmaper.py v9.04.17"

#@<<define>>
#@+node:zoomq.20090409122718.3:<<define>>
import os,sys
import time,datetime

NOW = "%s"%(time.strftime("%y%m%d",time.localtime()))
NOWTIME = "%s"%(time.strftime("%y%m%d %H:%M:%S",time.localtime()))
LOG_FILENAME = '_log/mapping-%s.log'%NOW

#import logging
#import logging.config
'''
logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]%(levelname)-8s"%(message)s"',
                    datefmt='%Y-%m-%d %a %H:%M:%S',
                    filename='logs/yksitemap-%s.log'%daylog,
                    filemode='a+')
'''
#@-node:zoomq.20090409122718.3:<<define>>
#@nl

#@+others
#@+node:zoomq.20090409202326.3:initlog
def initlog():
    '''base Limodou blog easy creat logger obj.
    '''
    import logging
    logger = logging.getLogger()
    hdlr = logging.FileHandler(LOG_FILENAME)
    formatter = logging.Formatter("[%(asctime)s]%(levelname)-8s`%(message)s`")
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return logger
#@-node:zoomq.20090409202326.3:initlog
#@+node:zoomq.20090409122718.4:class mapper
class mapper:
    """main class for mapping moinmoin pages
    """
    #@	@+others
    #@+node:zoomq.20090409142411.20:__init__
    def __init__(self,pagenamefile):
        """ini all
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")
        logger.critical("critical message")
        """
        self.logger = initlog()
        self.logdo = 0
        self.MM = MM
        self.data = pagenamefile
        self.mapli = []
        self.mapdots = []
        self.gendots = []
        self.dotnodes = ""
        #print open(pagenamefile).read()
        self.xmltree = []
        self.xmlnodes = ""
        #@    @+others
        #@+node:zoomq.20090409142411.21:abtFile
        self.pathlog = "_logs/"
        self.pathtpl = "_tpls/"

        self.tplmain = "moinmaper.tpl"
        self.tplitem = "moinpage.tpl"
        self.tpldot = "moindot.tpl"
        self.tpldotitem = open("%s/%s"%(self.pathtpl,self.tplitem)).read()

        self.tmpdotpages = "dotpages.tmp"
        open(self.tmpdotpages,"w").write("")

        self.expdot = "moinmaper.dot"
        #@-node:zoomq.20090409142411.21:abtFile
        #@+node:zoomq.20090414113944.1:xmlfiles
        self.tplxml = "moinxml.tpl"
        self.expxml = "index.xml"

        self.xmlroot = lE.Element("node")
        self.xmlroot.set("ID","ID_0")
        self.xmlroot.set("TEXT",XML['ROOTXT'])
        self.xmlroot.set("ALT","{%s @%s}"%(VERSION,NOWTIME))
        self.xmlroot.set("PATH","NULL")
        self.xmlroot.set("LINK","#")
        #@-node:zoomq.20090414113944.1:xmlfiles
        #@-others


        #print self.MM

    #@-node:zoomq.20090409142411.20:__init__
    #@+node:zoomq.20090415093541.1:_parentfix
    def _parentfix(self,crtnode,path,deep,fpli,urli):
        '''fixed all deep parent nodes
        '''
        base64code = base64.b64encode(path).replace("=","")
        url = "/".join(urli[:deep])
        root = self.xmlroot
        print path,"\n",XML['XPATH']%path
        #print "join(fpli::%s"%"/".join(fpli[:deep-1])
        if "" == "/".join(fpli[:deep-1]):
            crtnode = root
        else:
            xpath = XML['XPATH']%"/".join(fpli[:deep-1])
            if XML["XPROOT"] == xpath:
                crtnode = root
                #@            <<new node>>
                #@+node:zoomq.20090414204327.3:<<new node>>
                node = lE.SubElement(crtnode, "node")
                node.set("ID","ID_%s"%base64code)
                #node.set("TEXT",path)
                label=self._getitle(fpath)
                node.set("TEXT",label[0].decode('utf8'))
                if "" !=label[1]:node.set("STATE",label[1].decode('utf8'))

                node.set("PATH",path)
                node.set("LINK","%s/%s"%(MM['URL'],url))

                #@-node:zoomq.20090414204327.3:<<new node>>
                #@nl
            else:
                xparent = lE.XPath(xpath)
                print "try xparent::\n\t%s"%xpath
                print xparent(root)
                if [] == xparent(root):
                    crtnode = self._parentfix(crtnode,path,deep-1,fpli,urli)
                else:
                    print "match xparent::\n\t%s"%xpath
                    crtnode = xparent(root)[0]
                    #@                <<new node>>
                    #@+node:zoomq.20090414204327.3:<<new node>>
                    node = lE.SubElement(crtnode, "node")
                    node.set("ID","ID_%s"%base64code)
                    #node.set("TEXT",path)
                    label=self._getitle(fpath)
                    node.set("TEXT",label[0].decode('utf8'))
                    if "" !=label[1]:node.set("STATE",label[1].decode('utf8'))

                    node.set("PATH",path)
                    node.set("LINK","%s/%s"%(MM['URL'],url))

                    #@-node:zoomq.20090414204327.3:<<new node>>
                    #@nl
            #print lE.tostring(xparent(root)[0],pretty_print=True)
        #print lE.tostring(root,pretty_print=True)
        return crtnode

    #@-node:zoomq.20090415093541.1:_parentfix
    #@+node:zoomq.20090409142411.24:mapall
    def mapall(self):
        """main action for do all mapping
        .write(open(self.whatIdx).read() % locals())
        """
        self.urlanalyze();
        dotmapname = self.MM["MAPNAME"]
        dotpages = self.dotnodes    #.encode('unicode_escape').decode('string_escape')
        #open(self.tmpdotpages).read()
        dotdigraph = "\n".join(self.mapli)
        #print dotpages
        #print unicode(self.dotpages,'ascii','cjk_replace').encode('utf8')
        open(self.expdot,"w").write(open("%s/%s"%(self.pathtpl,self.tplmain)).read() % locals())
    #@-node:zoomq.20090409142411.24:mapall
    #@+node:zoomq.20090414113944.21:gen_dotmap
    def gen_dotmap(self,realPath):
        """gen dot uage MoinMoin page items
        - dot node and map gen in diff loop
        - from raw url get node label  urllib2.urlopen('http://wiki.s.kingsoft.net/moin/AutoTest/AutoTestMembersList?action=raw').readlines()
        - usage file dir path name through Base64 as dot node
        """
        fpath = realPath[:-2]
        wikiurl = wikiutil.unquoteWikiname(fpath)
        #print "dirname:%s"%realPath[:-2]
        #print "unquoteWikiname:%s"%wikiutil.unquoteWikiname(realPath[:-2])
        #print "quoteWikinameURL:%s"%wikiutil.quoteWikinameURL(realPath[:-2])
        subs = fpath.split("(2f)")
        if int(self.MM["DEEP"]) < len(subs):
            pass
        else:
            # one by one gen. all mapping
            #@        <<intermap>>
            #@+node:zoomq.20090414113944.22:<<intermap>>
            self.gen_dotitem(fpath)
            #print subs
            #lwidth=self.MM["LWIDTH"]-(self.MM["LWSTEP"]*deep) COLORSEED COLORSTEP
            dotwikiname =  ["(2f)".join(subs[:i+1]) for i in range(len(subs))]
            for node in dotwikiname:
                base46node = base64.b64encode(node).replace("=","")
                if base46node not in self.mapdots:
                    self.mapdots.append((base46node,node))
                else:
                    pass

            dotbase64 = ""
            dottpl = open("%s/%s"%(self.pathtpl,self.tpldot)).read()

            #@<<try mapping>>
            #@+node:zoomq.20090414113944.23:<<try mapping>>
            try:
                dotbase64 = [base64.b64encode(i).replace("=","") for i in dotwikiname]
                for i in range(len(dotbase64)):
                    lwidth=self.MM["LWIDTH"]-(self.MM["LWSTEP"]*i)
                    if lwidth<=0:
                        lwidth=0.1
                    color = self.MM["COLORSEED"]-(self.MM["COLORSTEP"]*i)
                    if lwidth<=0:
                        color=self.MM["COLORSEED"]

                    if i+1 >= len(dotbase64):
                        break
                    else:
                        intermap = dottpl%(dotbase64[i],dotbase64[i+1],lwidth,color)
                        #print intermap
                        if intermap not in self.mapli:
                            self.mapli.append(intermap)
            except UnicodeEncodeError:
                self.logger.debug("UnicodeEncodeError : %s"%realPath)
            except:
                self.logger.warn("others code bad ")
            #@-node:zoomq.20090414113944.23:<<try mapping>>
            #@nl



            #@-node:zoomq.20090414113944.22:<<intermap>>
            #@nl
        #self.dotpages += dotnode



    #@-node:zoomq.20090414113944.21:gen_dotmap
    #@+node:zoomq.20090410145521.2:gen_dotitem
    def gen_dotitem(self,fpath):
        '''ask wiki found the first title as node label
        dotlabel = self._getitle(rawurl)
        \return file self.tmpdotpages include all dot node define
        \return self.gendots as list recoded all node gen. for gen_lostnodes
        '''
        #print fpath
        wikiname = wikiutil.unquoteWikiname(fpath)
        wikiurl = wikiutil.quoteWikinameURL(wikiname)
        ##for right export Chinese
        #print fpath.encode('unicode_escape').decode('string_escape')
        dotitem = base64.b64encode(fpath).replace("=","")

        self.gendots.append(dotitem)
        #print dotitem
        #dotlabel = dotitem[:7]
        dotlabel = self._getitle(fpath)
        '''test what mis in _getitle()
        if "NULL" == dotlabel:
            print "gen_dotitem:%s"%wikipath
            return 
        '''
        doturl = "%s/%s"%(self.MM["URL"],wikiurl)
        #wikipath.encode('unicode_escape').decode('string_escape'))
        #self.logger.debug("all picked : %s"%dotitem)
        #print self.tpldotitem%locals()
        self.dotnodes += self.tpldotitem%locals()




    #@-node:zoomq.20090410145521.2:gen_dotitem
    #@+node:zoomq.20090410145521.12:gen_lostnodes
    def gen_lostnodes(self):
        '''gen that not real creat pages in path relation
        '''
        #print self.mapdots
        #print self.gendots
        lose = []
        for i in self.mapdots:
            if i[0] not in self.gendots:
                lose.append(i)
        #print lose
        dotlosed = ""
        for node in lose:
            wikipath = wikiutil.unquoteWikiname(node[1])
            dotitem = node[0]
            dotlabel = wikipath.encode('unicode_escape').decode('string_escape')
            doturl = "#"
            dotlosed += self.tpldotitem%locals()
        #print "dotlosed::>%s<::dotlosed"%dotlosed
        #self.logger.debug("dotlosed::%s"%dotlosed)
        self.dotnodes += dotlosed



    #@-node:zoomq.20090410145521.12:gen_lostnodes
    #@-others

#@-node:zoomq.20090409122718.4:class mapper
#@-others

#@<<__main__>>
#@+node:zoomq.20090409142411.22:<<__main__>>
if __name__ == '__main__':      # this way the module can be
    if 2 != len(sys.argv):
        print """ %s usage::
$ python triplemaper.py DataFile [like: 00310-all-sample.txt]
        """ % VERSION
    else:
        begin = time.time()
        df = sys.argv[1]
        mm = mapper(df)
        #mm.mapall()
        #mm.mapxml()
        #mm._treelist(pf)
        end = time.time()

        info = ">>>runing time=%.2fs<<<"%(end - begin)
        print info
        mm.logger.info("^_^: %s"%info)
        info = ">>>chked nodes=%s<<<"%mm.logdo
        print info
        mm.logger.info("^_^: %s"%info)

        info = ";-) export MoinMoin pages mapping \n by %s"%VERSION
        print info
        mm.logger.info("^_^: %s"%info)

#@-node:zoomq.20090409142411.22:<<__main__>>
#@nl


#@-node:zoomq.20090409122718.2:@shadow triplemaper.py
#@-leo
