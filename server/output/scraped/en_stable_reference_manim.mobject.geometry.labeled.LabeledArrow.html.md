# LabeledArrow[¶](https://docs.manim.community/en/stable/reference/<#labeledarrow> "Link to this heading")
Qualified name: `manim.mobject.geometry.labeled.LabeledArrow`
_class_ LabeledArrow(_* args_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/labeled.html#LabeledArrow>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledArrow> "Link to this definition")
    
Bases: `[LabeledLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine> "manim.mobject.geometry.labeled.LabeledLine"), `[Arrow`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow")
Constructs an arrow containing a label box somewhere along its length. This class inherits its label properties from LabeledLine, so the main parameters controlling it are the same.
Parameters:
    
  * **label** – Label that will be displayed on the Arrow.
  * **label_position** – A ratio in the range [0-1] to indicate the position of the label with respect to the length of the line. Default value is 0.5.
  * **label_config** – A dictionary containing the configuration for the label. This is only applied if `label` is of type `str`.
  * **box_config** – A dictionary containing the configuration for the background box.
  * **frame_config** – 
A dictionary containing the configuration for the frame.
See also
`[LabeledLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.LabeledLine.html#manim.mobject.geometry.labeled.LabeledLine> "manim.mobject.geometry.labeled.LabeledLine")
  * **args** (_Any_)
  * **kwargs** (_Any_)


Examples
Example: LabeledArrowExample [¶](https://docs.manim.community/en/stable/reference/<#labeledarrowexample>)
![../_images/LabeledArrowExample-1.png](https://docs.manim.community/en/stable/_images/LabeledArrowExample-1.png)
```
frommanimimport *
classLabeledArrowExample(Scene):
  defconstruct(self):
    l_arrow = LabeledArrow("0.5", start=LEFT*3, end=RIGHT*3 + UP*2, label_position=0.5)
    self.add(l_arrow)

```
Copy to clipboard
Make interactive
Methods
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_original__init__(_* args_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledArrow._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **args** (_Any_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next LabeledLine ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.LabeledLine.html>) [ Previous Label ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.Label.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [LabeledArrow](https://docs.manim.community/en/stable/reference/<#>)
    * `[LabeledArrow`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledArrow>)
      * `[LabeledArrow._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.LabeledArrow._original__init__>)


