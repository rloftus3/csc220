export REPO = csc220
SUBDIRS = 00-lab 01-lab

all: $(SUBDIRS)

.PHONY: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@