.SUFFIXES:
.SUFFIXES: .z5 .inf

.PHONY: default run all clean

#default: run
default: all

run: all
	frotz sudyfoi.z5

all: sudyfoi.z5

clean:
	-rm -f sudyfoi.z5

.inf.z5:
	inform +language_name=Lojban $<
