DSSSLLOC=../../dsssl/docbook
DOCBOOKTOOLS=../docbooktools
SOURCE=less1.doc.xml less2.doc.xml less3.doc.xml less4.doc.xml less5.doc.xml less6.doc.xml less7.doc.xml less8.doc.xml less9.doc.xml less10.doc.xml less11.doc.xml less12.doc.xml less13.doc.xml less14.doc.xml less15.doc.xml lessinfo.doc.xml lessintro.doc.xml
all: rtf paperback tex html

paperback: lessons.index.doc.xml
	openjade -E 0 -wno-valid -t rtf -o lessons.tmp.rtf -d $(DSSSLLOC)/print/my_docbook.paperback.dsl $(DOCBOOKTOOLS)/xml.dcl lessStart.doc.xml
	perl $(DOCBOOKTOOLS)/rtf2rtf.pl < lessons.tmp.rtf > lessons.paperback.rtf
	echo "Don't forget to index the text in Word (Ctrl-A, F9 on PC.)"

rtf: lessons.index.doc.xml
	openjade -E 0 -o lessons.tmp.rtf -t rtf -d $(DSSSLLOC)/print/my_docbook.print.dsl $(DOCBOOKTOOLS)/xml.dcl lessStart.doc.xml
	perl $(DOCBOOKTOOLS)/rtf2rtf.pl < lessons.tmp.rtf > lessons.doc.rtf
	echo "Don't forget to index the text in Word (Ctrl-A, F9 on PC.)"


tex: lessons.index.doc.xml
	openjade -E 0 -t tex -d $(DSSSLLOC)/print/my_docbook.print.tex.dsl $(DOCBOOKTOOLS)/xml.dcl lessStart.doc.xml

lessons.index.doc.xml: HTML.index
	perl $(DSSSLLOC)/bin/collateindex.pl -p -o lessons.index.doc.xml HTML.index

HTML.index: $(SOURCE)
	perl $(DSSSLLOC)/bin/collateindex.pl -N -o lessons.index.doc.xml
	openjade -E 0 -wno-valid -t sgml -d $(DSSSLLOC)/html/my_docbook.html.dsl -V html-index $(DOCBOOKTOOLS)/xml.dcl lessStart.doc.xml

html: lessStart.html.doc.xml $(SOURCE)
	openjade -E 0 -t sgml -d $(DSSSLLOC)/html/my_docbook.html.dsl $(DOCBOOKTOOLS)/xml.dcl lessStart.html.doc.xml

