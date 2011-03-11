
include localMakefile

# FUNCTIONS

# arg1 = c-source-filename
CSRC2CLIB = $(patsubst csrc/%.c,bin/%.so,$(dir $(1))lib$(notdir $(1)))

# arg1 = c-source-filename, arg2 = lib-filename
define CRULE
$(2): $(1)
	mkdir -p "$(dir $(2))"
	gcc -ansi -o "$(2)" -fPIC -shared "$(1)" `sdl-config --cflags` -lGL
endef

# VARIABLES

CMODS := $(wildcard csrc/*.c) $(wildcard csrc/*/*.c)
CLIBS := $(foreach cmod,$(CMODS),$(call CSRC2CLIB,$(cmod)))

PYMODS = $(subst ./,,$(shell cd pysrc; find . -name \*.py; cd ..))
PYBINS = $(foreach pymod,$(PYMODS),pybin/$(pymod)c)

.PHONY : yasc gfx cbin pybin clean totalclean

yasc: gfx cbin pybin

gfx: gfx/terrain/grass.png gfx/protosettler.png

gfx/terrain/grass.png: render/terrain/grass.png
	mkdir -p "$(dir $@)"
	python scripts/postprocess_texture.py "$^" "$@"

gfx/protosettler.png: render/protosettler/noshd-0001.png render/protosettler/onlshd-0001.png
	mkdir -p "$(dir $@)"
	python scripts/postprocess_settler.py "$(dir $<)" "$@" 1 156

render/terrain/grass.png: blender/terrain/grass.blend
	$(BLENDER) -b "$^" -o "$(subst .png,,$@)" -f 1
	mv "$(subst .png,0001.png,$@)" "$@"

render/protosettler/noshd-0001.png: blender/protosettler/protosettler.blend
	mkdir -p "$(dir $@)"
	$(BLENDER) -b "$^" -o "$(subst 0001.png,,$@)" -P blender/protosettler/ConfOnlySettler -s 1 -e 156 -a

render/protosettler/onlshd-0001.png: blender/protosettler/protosettler.blend
	mkdir -p "$(dir $@)"
	$(BLENDER) -b "$^" -o "$(subst 0001.png,,$@)" -P blender/protosettler/ConfOnlyShadow -s 1 -e 156 -a

cbin: $(CLIBS)

$(foreach cmod,$(CMODS),$(eval $(call CRULE,$(cmod),$(call CSRC2CLIB,$(cmod)))))

pybin: $(PYBINS)

pybin/%.pyc: pysrc/%.py
	mkdir -p "$(dir $@)"
	python pyc.py "$^" "$@"

clean:
	-rm -r bin
	-rm -r pybin

totalclean:
	-rm -r render
	-rm -r gfx
	-rm -r bin
	-rm -r pybin
	-rm -r doc/pysrc

epydoc:
	mkdir -p doc
	epydoc --html pysrc -o doc/pysrc --config epydoc.conf --parse-only
