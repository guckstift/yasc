
include localMakefile

LLMODS = view
LLLIBS = $(foreach llmod,$(LLMODS),bin/lowlevel/lib$(llmod).so)

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
	# somehow the new blender produces shity filenames, when using the # as placeholder
	# for the framenumber of the render-output
	# dear Blender developers, please fix this! :)
	#$(BLENDER) -b "$^" -o "$(subst .png,#.png,$@)" -f 1
	$(BLENDER) -b "$^" -o "$(subst .png,,$@)" -f 1
	mv "$(subst .png,0001.png,$@)" "$@"

render/protosettler/noshd-0001.png: blender/protosettler/protosettler.blend
	mkdir -p "$(dir $@)"
	#$(BLENDER) -b "$^" -o "$(subst 001.png,###.png,$@)" -P blender/protosettler/ConfOnlySettler -s 1 -e 156 -a
	$(BLENDER) -b "$^" -o "$(subst 0001.png,,$@)" -P blender/protosettler/ConfOnlySettler -s 1 -e 156 -a

render/protosettler/onlshd-0001.png: blender/protosettler/protosettler.blend
	mkdir -p "$(dir $@)"
	#$(BLENDER) -b "$^" -o "$(subst 0001.png,###.png,$@)" -P blender/protosettler/ConfOnlyShadow -s 1 -e 156 -a
	$(BLENDER) -b "$^" -o "$(subst 0001.png,,$@)" -P blender/protosettler/ConfOnlyShadow -s 1 -e 156 -a

cbin: $(LLLIBS)

bin/lowlevel/lib%.so: csrc/lowlevel/%.c
	mkdir -p "$(dir $@)"
	gcc -ansi -o "$@" -fPIC -shared "$^" `sdl-config --cflags` -lGL

pybin: $(PYBINS)

pybin/%.pyc: pysrc/%.py
	mkdir -p "$(dir $@)"
	python pyc.py "$^" "$@"

clean:
	-rm -r gfx
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
