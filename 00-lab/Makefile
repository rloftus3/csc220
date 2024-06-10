# Makefile with multiple targets
dirname = $(notdir $(CURDIR))
htmldir = ~/public_html/$(REPO)/$(dirname)

# Default target
all: publish

publish:
	if test -d ~/public_html; then \
	  mkdir -p $(htmldir); \
	  cp -f --remove-destination *.py $(htmldir); \
	  chmod +x $(htmldir)/*.py; \
	fi

clean:
	rm $(htmldir)/*.py
