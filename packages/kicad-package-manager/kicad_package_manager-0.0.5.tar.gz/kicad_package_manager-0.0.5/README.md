# KiCad Package Manager


This is a package manager for KiCad symbols, footprints, 3d models, simulation files, and hierarchical sheets.



Goal
----

Create a format for distributing the following kind of KiCad features:

* Symbols
* Footprints
* 3D Models
* SPICE Simulation Code
* Sub-sheets
* Unit Tests
* Command Runner
* Plugins

Projects can be created that programmatically generate these files.



Installing KPM
--------------

Open the "KiCad Command Prompt"

```bash
pip3 install kicad-package-manager
```



Usage
-----

```bash
kpm init

kpm install https://github.com/danroblewis/kicad-eurorack-tools.git

kpm install .
```


### kpm.json
```json
{
	"name": "cool-project",
	"version": "0.0.1",
	"author": "danroblewis",
	"homepage": "http://githab.info/magic/stuff",
	"commands": {
		"test": "./fictional-spice-tester"
	},
	"dependencies": {
		"jlcpcb-basics": "0.0.1",
		"eurorack-parts": "0.0.57"
	}
}
```



Refresh Symbols and Footprints
------------------------------

After updating your libraries, the symbols/footprints in your schematic files won't have the latest changes. Do this to synchronize them:

* In `eeschema`, click `Tools > Update Symbols from Library...`, then save
* In `pcbnew`, click `Tools > Update Footprints from Library...`, then save

(If we can find a way to do this within kpm, that would be awesome.)



Package Directory Structure
---------------------------
```
/kpm.json

/symbols/
/symbols/mysymbols.kicad_sym

/footprints/
/footprints/myfootprints.pretty/
/footprints/myfootprints.pretty/myfootprints.kicad_mod

/3dmodels/
/3dmodels/something.step

/plugins/
/plugins/kicad-eurorack-tools/
/plugins/kicad-eurorack-tools/__init__.py

/simulation/
/simulation/mysim.spice

/sheets/
/sheets/mysubsheet.kicad_sch

/tests/
/tests/mytest.py

/scripts/
/scripts/mycommand.py
```

