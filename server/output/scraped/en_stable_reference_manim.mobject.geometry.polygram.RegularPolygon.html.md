# RegularPolygon[¶](https://docs.manim.community/en/stable/reference/<#regularpolygon> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.RegularPolygon`
_class_ RegularPolygon(_n =6_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#RegularPolygon>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RegularPolygon> "Link to this definition")
    
Bases: `[RegularPolygram`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygram.html#manim.mobject.geometry.polygram.RegularPolygram> "manim.mobject.geometry.polygram.RegularPolygram")
An n-sided regular `[Polygon`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html#manim.mobject.geometry.polygram.Polygon> "manim.mobject.geometry.polygram.Polygon").
Parameters:
    
  * **n** (_int_) – The number of sides of the `[RegularPolygon`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RegularPolygon> "manim.mobject.geometry.polygram.RegularPolygon").
  * **kwargs** (_Any_) – Forwarded to the parent constructor.


Examples
Example: RegularPolygonExample [¶](https://docs.manim.community/en/stable/reference/<#regularpolygonexample>)
![../_images/RegularPolygonExample-1.png](https://docs.manim.community/en/stable/_images/RegularPolygonExample-1.png)
```
frommanimimport *
classRegularPolygonExample(Scene):
  defconstruct(self):
    poly_1 = RegularPolygon(n=6)
    poly_2 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN)
    poly_3 = RegularPolygon(n=10, color=RED)
    poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
    self.add(poly_group)

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
_original__init__(_n =6_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RegularPolygon._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **n** (_int_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next RegularPolygram ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygram.html>) [ Previous Rectangle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [RegularPolygon](https://docs.manim.community/en/stable/reference/<#>)
    * `[RegularPolygon`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RegularPolygon>)
      * `[RegularPolygon._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.RegularPolygon._original__init__>)


