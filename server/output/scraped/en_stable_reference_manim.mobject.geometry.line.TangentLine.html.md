# TangentLine[¶](https://docs.manim.community/en/stable/reference/<#tangentline> "Link to this heading")
Qualified name: `manim.mobject.geometry.line.TangentLine`
_class_ TangentLine(_vmob_ , _alpha_ , _length =1_, _d_alpha =1e-06_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#TangentLine>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.TangentLine> "Link to this definition")
    
Bases: `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")
Constructs a line tangent to a `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") at a specific point.
Parameters:
    
  * **vmob** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The VMobject on which the tangent line is drawn.
  * **alpha** (_float_) – How far along the shape that the line will be constructed. range: 0-1.
  * **length** (_float_) – Length of the tangent line.
  * **d_alpha** (_float_) – The `dx` value
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")


See also
`[point_from_proportion()`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion> "manim.mobject.types.vectorized_mobject.VMobject.point_from_proportion")
Examples
Example: TangentLineExample [¶](https://docs.manim.community/en/stable/reference/<#tangentlineexample>)
![../_images/TangentLineExample-1.png](https://docs.manim.community/en/stable/_images/TangentLineExample-1.png)
```
frommanimimport *
classTangentLineExample(Scene):
  defconstruct(self):
    circle = Circle(radius=2)
    line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
    line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
    self.add(circle, line_1, line_2)

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
_original__init__(_vmob_ , _alpha_ , _length =1_, _d_alpha =1e-06_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.TangentLine._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vmob** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **alpha** (_float_)
  * **length** (_float_)
  * **d_alpha** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Vector ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Vector.html>) [ Previous RightAngle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.RightAngle.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TangentLine](https://docs.manim.community/en/stable/reference/<#>)
    * `[TangentLine`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.TangentLine>)
      * `[TangentLine._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.TangentLine._original__init__>)


