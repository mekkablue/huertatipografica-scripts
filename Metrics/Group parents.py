#MenuTitle: Group parents
# -*- coding: utf-8 -*-
__doc__="""
Goes through the kerning groups of the selected glyphs. Then opens a new tab with all the posible combinations so you can focus only in what you need to kern.
"""

import GlyphsApp

thisFont = Glyphs.font # frontmost font
selectedLayers = thisFont.selectedLayers # active layers of selected glyphs

Glyphs.clearLog()

keys = set([ l.parent.leftKerningGroup for l in selectedLayers if l.parent.leftKerningGroup] + [ l.parent.rightKerningGroup for l in selectedLayers if l.parent.rightKerningGroup] )
tabString = 'KerningGroups parents:\n%s\n\n' % ("/" + "/".join(keys))


if len(keys):
	thisFont.newTab(tabString)

else:
	Message("No kerning groups set :|", '', OKButton="OK")


