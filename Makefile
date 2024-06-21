export REPO = csc220
SUBDIRS = 00-lab 01-lab 02-lab 04-lab 05-lab

all: $(SUBDIRS)

.PHONY: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

clean:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done
