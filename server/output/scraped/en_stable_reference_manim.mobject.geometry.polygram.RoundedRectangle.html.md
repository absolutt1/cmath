# RoundedRectangle[¶](https://docs.manim.community/en/stable/reference/<#roundedrectangle> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.RoundedRectangle`
_class_ RoundedRectangle(_corner_radius =0.5_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#RoundedRectangle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RoundedRectangle> "Link to this definition")
    
Bases: `[Rectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle> "manim.mobject.geometry.polygram.Rectangle")
A rectangle with rounded corners.
Parameters:
    
  * **corner_radius** (_float_ _|__list_ _[__float_ _]_) – The curvature of the corners of the rectangle.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Rectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle> "manim.mobject.geometry.polygram.Rectangle")


Examples
Example: RoundedRectangleExample [¶](https://docs.manim.community/en/stable/reference/<#roundedrectangleexample>)
![../_images/RoundedRectangleExample-1.png](https://docs.manim.community/en/stable/_images/RoundedRectangleExample-1.png)
```
frommanimimport *
classRoundedRectangleExample(Scene):
  defconstruct(self):
    rect_1 = RoundedRectangle(corner_radius=0.5)
    rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)
    rect_group = Group(rect_1, rect_2).arrange(buff=1)
    self.add(rect_group)

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
_original__init__(_corner_radius =0.5_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RoundedRectangle._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **corner_radius** (_float_ _|__list_ _[__float_ _]_)
  * **kwargs** (_Any_)


[ Next Square ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Square.html>) [ Previous RegularPolygram ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygram.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [RoundedRectangle](https://docs.manim.community/en/stable/reference/<#>)
    * `[RoundedRectangle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RoundedRectangle>)
      * `[RoundedRectangle._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RoundedRectangle._original__init__>)


