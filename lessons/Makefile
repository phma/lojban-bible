DSSSLLOC=../dsssl/docbook
SOURCE=less1.doc.xml less2.doc.xml less3.doc.xml less4.doc.xml less5.doc.xml less6.doc.xml less7.doc.xml less8.doc.xml less9.doc.xml less10.doc.xml less11.doc.xml lessintro.doc.xml

all: rtf tex html

rtf: lessStart.doc.xml $(SOURCE)
	openjade -E 0 -t rtf -d $(DSSSLLOC)/print/my_docbook.print.dsl xml.dcl lessStart.doc.xml

tex: lessStart.doc.xml $(SOURCE)
	openjade -E 0 -t tex -d $(DSSSLLOC)/print/my_docbook.print.tex.dsl xml.dcl lessStart.doc.xml

html: lessStart.html.doc.xml $(SOURCE)
	openjade -E 0 -t sgml -d $(DSSSLLOC)/html/my_docbook.html.dsl xml.dcl lessStart.html.doc.xml

