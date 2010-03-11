digraph mainmap {
/*图片生成命令:: need:: apt-get install graphviz-cairo
$ dot test.dot -Tpng -o test.png -Tcmapx -o test.map
        style=filled,fillcolor=lightyellow,
        shape=plaintext,        
        ranksep=1.2,size="12,32"
        overlap=false,splines=true,
*/
    graph [label="%(dotmapname)s",
        labelloc="b",labeljust="r",
        fontsize=12.0,
        fontname="VeraSansYuanTi-Regular.ttf",
        ratio=compress,
        rankdir=LR,
        ranksep=0.2,
        ];
    node[fontsize=10.5,color=gray70,
        target="new",shape=plaintext,
        style=filled,fillcolor=lightyellow,
        height=0.1,
        ];
    /*dir=both,plaintext		arrowType=vee,
        */
    edge [fontsize=8.0,fontcolor=gray15,
        color=gray40,
        arrowsize=0.5,arrowhead=vee,arrowtail=none,
        len=2.1,
        ];
    /*关系
        len=1.7,
    KUP->PEM    [arrowhead=normal,style="setlinewidth(4)"]; 
    */    
%(dotnodes)s

    /*页面
    Td    [label="Toad\n未来特性管理视图",shape=component,URL=""];
    */

%(dotrelats)s

}
