
# CapStyleType[¶](https://docs.manim.community/en/stable/reference/<#capstyletype> "Link to this heading")
Qualified name: `manim.constants.CapStyleType`
_class_ CapStyleType(_value_ , _names= <not given>_, _*values_ , _module=None_ , _qualname=None_ , _type=None_ , _start=1_ , _boundary=None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/constants.html#CapStyleType>)[¶](https://docs.manim.community/en/stable/reference/<#manim.constants.CapStyleType> "Link to this definition")
    
Bases: `Enum`
Collection of available cap styles.
See the example below for a visual illustration of the different cap styles.
Examples
Example: CapStyleVariants [¶](https://docs.manim.community/en/stable/reference/<#capstylevariants>)
![../_images/CapStyleVariants-1.png](https://docs.manim.community/en/stable/_images/CapStyleVariants-1.png)
```
frommanimimport *
classCapStyleVariants(Scene):
  defconstruct(self):
    arcs = VGroup(*[
      Arc(
        radius=1,
        start_angle=0,
        angle=TAU / 4,
        stroke_width=20,
        color=GREEN,
        cap_style=cap_style,
      )
      for cap_style in CapStyleType
    ])
    arcs.arrange(RIGHT, buff=1)
    self.add(arcs)
    for arc in arcs:
      label = Text(arc.cap_style.name, font_size=24).next_to(arc, DOWN)
      self.add(label)

```
Copy to clipboard
Make interactive
Attributes
`AUTO`  
---  
`ROUND`  
`BUTT`  
`SQUARE`  
[ Next LineJointType ](https://docs.manim.community/en/stable/reference/<manim.constants.LineJointType.html>) [ Previous constants ](https://docs.manim.community/en/stable/reference/<manim.constants.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [CapStyleType](https://docs.manim.community/en/stable/reference/<#>)
    * `[CapStyleType`](https://docs.manim.community/en/stable/reference/<#manim.constants.CapStyleType>)


