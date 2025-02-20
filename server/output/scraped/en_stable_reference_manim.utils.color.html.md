
# color[¶](https://docs.manim.community/en/stable/reference/<#module-manim.utils.color> "Link to this heading")
Utilities for working with colors and predefined color constants.
## Color data structure[¶](https://docs.manim.community/en/stable/reference/<#color-data-structure> "Link to this heading")
`[core`](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#module-manim.utils.color.core> "manim.utils.color.core") | Manim's (internal) color data structure and some utilities for color conversion.  
---|---  
## Predefined colors[¶](https://docs.manim.community/en/stable/reference/<#predefined-colors> "Link to this heading")
There are several predefined colors available in Manim:
  * The colors listed in `[color.manim_colors`](https://docs.manim.community/en/stable/reference/<manim.utils.color.manim_colors.html#module-manim.utils.color.manim_colors> "manim.utils.color.manim_colors") are loaded into Manim’s global name space.
  * The colors in `[color.AS2700`](https://docs.manim.community/en/stable/reference/<manim.utils.color.AS2700.html#module-manim.utils.color.AS2700> "manim.utils.color.AS2700"), `[color.BS381`](https://docs.manim.community/en/stable/reference/<manim.utils.color.BS381.html#module-manim.utils.color.BS381> "manim.utils.color.BS381"), `[color.DVIPSNAMES`](https://docs.manim.community/en/stable/reference/<manim.utils.color.DVIPSNAMES.html#module-manim.utils.color.DVIPSNAMES> "manim.utils.color.DVIPSNAMES"), `[color.SVGNAMES`](https://docs.manim.community/en/stable/reference/<manim.utils.color.SVGNAMES.html#module-manim.utils.color.SVGNAMES> "manim.utils.color.SVGNAMES"), `[color.X11`](https://docs.manim.community/en/stable/reference/<manim.utils.color.X11.html#module-manim.utils.color.X11> "manim.utils.color.X11") and `[color.XKCD`](https://docs.manim.community/en/stable/reference/<manim.utils.color.XKCD.html#module-manim.utils.color.XKCD> "manim.utils.color.XKCD") need to be accessed via their module (which are available in Manim’s global name space), or imported separately. For example:
```
>>> frommanimimport XKCD
>>> XKCD.AVOCADO
ManimColor('#90B134')

```
Copy to clipboard
Or, alternatively:
```
>>> frommanim.utils.color.XKCDimport AVOCADO
>>> AVOCADO
ManimColor('#90B134')

```
Copy to clipboard


The following modules contain the predefined color constants:
`[manim_colors`](https://docs.manim.community/en/stable/reference/<manim.utils.color.manim_colors.html#module-manim.utils.color.manim_colors> "manim.utils.color.manim_colors") | Colors included in the global name space.  
---|---  
`[AS2700`](https://docs.manim.community/en/stable/reference/<manim.utils.color.AS2700.html#module-manim.utils.color.AS2700> "manim.utils.color.AS2700") | Australian Color Standard  
`[BS381`](https://docs.manim.community/en/stable/reference/<manim.utils.color.BS381.html#module-manim.utils.color.BS381> "manim.utils.color.BS381") | British Color Standard  
`[DVIPSNAMES`](https://docs.manim.community/en/stable/reference/<manim.utils.color.DVIPSNAMES.html#module-manim.utils.color.DVIPSNAMES> "manim.utils.color.DVIPSNAMES") | dvips Colors  
`[SVGNAMES`](https://docs.manim.community/en/stable/reference/<manim.utils.color.SVGNAMES.html#module-manim.utils.color.SVGNAMES> "manim.utils.color.SVGNAMES") | SVG 1.1 Colors  
`[XKCD`](https://docs.manim.community/en/stable/reference/<manim.utils.color.XKCD.html#module-manim.utils.color.XKCD> "manim.utils.color.XKCD") | Colors from the XKCD Color Name Survey  
`[X11`](https://docs.manim.community/en/stable/reference/<manim.utils.color.X11.html#module-manim.utils.color.X11> "manim.utils.color.X11") | X11 Colors  
[ Next core ](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html>) [ Previous render ](https://docs.manim.community/en/stable/reference/<manim.cli.render.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [color](https://docs.manim.community/en/stable/reference/<#>)
    * [Color data structure](https://docs.manim.community/en/stable/reference/<#color-data-structure>)
    * [Predefined colors](https://docs.manim.community/en/stable/reference/<#predefined-colors>)


