# Triangle[¶](https://docs.manim.community/en/stable/reference/<#triangle> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.Triangle`
_class_ Triangle(_** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Triangle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Triangle> "Link to this definition")
    
Bases: `[RegularPolygon`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygon.html#manim.mobject.geometry.polygram.RegularPolygon> "manim.mobject.geometry.polygram.RegularPolygon")
An equilateral triangle.
Parameters:
    
**kwargs** (_Any_) – Additional arguments to be passed to `[RegularPolygon`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RegularPolygon.html#manim.mobject.geometry.polygram.RegularPolygon> "manim.mobject.geometry.polygram.RegularPolygon")
Examples
Example: TriangleExample [¶](https://docs.manim.community/en/stable/reference/<#triangleexample>)
![../_images/TriangleExample-1.png](https://docs.manim.community/en/stable/_images/TriangleExample-1.png)
```
frommanimimport *
classTriangleExample(Scene):
  defconstruct(self):
    triangle_1 = Triangle()
    triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
    tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
    self.add(tri_group)

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
_original__init__(_** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Triangle._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
**kwargs** (_Any_)
Return type:
    
None
[ Next shape_matchers ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.html>) [ Previous Star ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Star.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Triangle](https://docs.manim.community/en/stable/reference/<#>)
    * `[Triangle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Triangle>)
      * `[Triangle._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Triangle._original__init__>)


