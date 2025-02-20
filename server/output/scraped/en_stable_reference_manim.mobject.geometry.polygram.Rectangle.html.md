# Rectangle[¶](https://docs.manim.community/en/stable/reference/<#rectangle> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.Rectangle`
_class_ Rectangle(_color =ManimColor('#FFFFFF')_, _height =2.0_, _width =4.0_, _grid_xstep =None_, _grid_ystep =None_, _mark_paths_closed =True_, _close_new_points =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Rectangle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Rectangle> "Link to this definition")
    
Bases: `[Polygon`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon> "manim.mobject.geometry.polygram.Polygon")
A quadrilateral with two sets of parallel sides.
Parameters:
    
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the rectangle.
  * **height** (_float_) – The vertical height of the rectangle.
  * **width** (_float_) – The horizontal width of the rectangle.
  * **grid_xstep** (_float_ _|__None_) – Space between vertical grid lines.
  * **grid_ystep** (_float_ _|__None_) – Space between horizontal grid lines.
  * **mark_paths_closed** (_bool_) – No purpose.
  * **close_new_points** (_bool_) – No purpose.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Polygon`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon> "manim.mobject.geometry.polygram.Polygon")


Examples
Example: RectangleExample [¶](https://docs.manim.community/en/stable/reference/<#rectangleexample>)
![../_images/RectangleExample-1.png](https://docs.manim.community/en/stable/_images/RectangleExample-1.png)
```
frommanimimport *
classRectangleExample(Scene):
  defconstruct(self):
    rect1 = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
    rect2 = Rectangle(width=1.0, height=4.0)
    rect3 = Rectangle(width=2.0, height=2.0, grid_xstep=1.0, grid_ystep=1.0)
    rect3.grid_lines.set_stroke(width=1)
    rects = Group(rect1, rect2, rect3).arrange(buff=1)
    self.add(rects)

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
_original__init__(_color =ManimColor('#FFFFFF')_, _height =2.0_, _width =4.0_, _grid_xstep =None_, _grid_ystep =None_, _mark_paths_closed =True_, _close_new_points =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Rectangle._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **height** (_float_)
  * **width** (_float_)
  * **grid_xstep** (_float_ _|__None_)
  * **grid_ystep** (_float_ _|__None_)
  * **mark_paths_closed** (_bool_)
  * **close_new_points** (_bool_)
  * **kwargs** (_Any_)


[ Next RegularPolygon ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygon.html>) [ Previous Polygram ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygram.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Rectangle](https://docs.manim.community/en/stable/reference/<#>)
    * `[Rectangle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Rectangle>)
      * `[Rectangle._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Rectangle._original__init__>)


