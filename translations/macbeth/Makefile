# Makefile

DOC=		macbeth
DOCPS=		$(DOC).ps
DOCPDF=		$(DOC).pdf
DOCHTML=	$(DOC)/$(DOC).html
DOCDVI=		$(DOC).dvi
DOCSRC=		$(DOC).tex

#test: $(DOCDVI)
#	xdvi $(DOCDVI)

all: $(DOCPS) $(DOCPDF) $(DOCHTML)

viewall: all
	xdvi $(DOCDVI)
	gv $(DOCPS)
	xpdf $(DOCPDF)

clean:
	-rm -f $(DOCPS) $(DOCPDF) $(DOCDVI)
	-rm -f $(DOC).aux $(DOC).log
	-rm -fr $(DOC)/

$(DOCPS): $(DOCDVI)
	dvips $(DOCDVI) -o $(DOCPS)

$(DOCPDF): $(DOCDVI)
	dvipdf $(DOCDVI) $(DOCPDF)

$(DOCHTML): $(DOCSRC)
	latex2html $(DOCSRC)

$(DOCDVI): $(DOCSRC)
	latex $(DOCSRC)

$(DOCSRC): act1.tex act2.tex act3.tex act4.tex act5.tex
