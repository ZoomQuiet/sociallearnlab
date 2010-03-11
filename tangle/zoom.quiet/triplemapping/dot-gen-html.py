# -*- coding: utf-8 -*-
'''dot-gen-html.py
    v0.9 090413 append others Graphviz export
    v0.8 090312 forpy.kingsoft.net 增补网页标题参数
    v0.7 090312 for KUP.rdev dot mapping gen html
usage:
    $ python dot-gen-html.py py-k-idx.dot "py.kingsoft.net 数据地图" index.html
reverions::
    __author__  = "$Author$"
    __date__    = "$Date$"
    __revision__= "$Rev$"
    __url__     = "$URL$"
'''
VERSION = "dot-gen-html v9.04.13"

import os,sys,time
import popen2

GENTIME = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
TPL = "res/index.tpl"
DODOT = "dot %s.dot -Tpng -o %s.png -Tcmapx -o %s.map"
TPLDOT = "%s %s.dot -Tpng -o %s-%s.png -Tcmapx -o %s.map"
FOOTCSS="css/stickyfooter/footer.css"


def gen(dotoolname,dotf,titp,wxpf):
    """usage dot exp png+img map,auto usage html tpl writ out idenx page!
    """
    script = VERSION
    gentime = GENTIME
    dotmap = dotf.split(".")[0]
    #print dotmap
    mapdot = dotmap
    dotool = dotoolname
    #TPLDOT = "%s %s.dot -Tpng -o %s-%s.png -Tcmapx -o %s.map"
    genmap = TPLDOT%(dotool
        ,mapdot
        ,mapdot
        ,dotool
        ,mapdot)
    title = titp
    print genmap
    r, w, e = popen2.popen3(genmap)
    print e.readlines()
    print r.readlines()
    r.close()
    e.close()
    w.close()

    cmapx = open("%s.map"%dotmap).read()
    css = open(FOOTCSS).read()
    open(wxpf,"w").write(open(TPL).read() % locals())
    print "%s done gen mapping @%s"%(VERSION,GENTIME)



if __name__ == '__main__':      # this way the module can be
    if 5 != len(sys.argv):
        print """ %s usage::
$ python dot-gen-html 'u.dot' "PageTitle" exPageNam[like index.html) dotool
        """
    else:
        dotf = sys.argv[1]
        titp = sys.argv[2]
        expf = sys.argv[3]
        mapn = dotf.split(".")[0]
        dotool = sys.argv[4]
        #print dir()
        gen(dotool,dotf,titp,expf)
    #open(exrep,"w").write(open(tpl).read() % locals())









