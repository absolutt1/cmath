# Ellipse[¶](https://docs.manim.community/en/stable/reference/<#ellipse> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.Ellipse`
_class_ Ellipse(_width =2_, _height =1_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Ellipse>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Ellipse> "Link to this definition")
    
Bases: `[Circle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle> "manim.mobject.geometry.arc.Circle")
A circular shape; oval, circle.
Parameters:
    
  * **width** (_float_) – The horizontal width of the ellipse.
  * **height** (_float_) – The vertical height of the ellipse.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Circle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle> "manim.mobject.geometry.arc.Circle").


Examples
Example: EllipseExample [¶](https://docs.manim.community/en/stable/reference/<#ellipseexample>)
![../_images/EllipseExample-1.png](https://docs.manim.community/en/stable/_images/EllipseExample-1.png)
```
frommanimimport *
classEllipseExample(Scene):
  defconstruct(self):
    ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
    ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
    ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
    self.add(ellipse_group)

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
_original__init__(_width =2_, _height =1_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Ellipse._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **width** (_float_)
  * **height** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next LabeledDot ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.LabeledDot.html>) [ Previous Dot ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Dot.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Ellipse](https://docs.manim.community/en/stable/reference/<#>)
    * `[Ellipse`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Ellipse>)
      * `[Ellipse._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Ellipse._original__init__>)


