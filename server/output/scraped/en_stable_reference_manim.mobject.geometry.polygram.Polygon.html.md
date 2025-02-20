# Polygon[¶](https://docs.manim.community/en/stable/reference/<#polygon> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.Polygon`
_class_ Polygon(_* vertices_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Polygon>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygon> "Link to this definition")
    
Bases: `[Polygram`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram")
A shape consisting of one closed loop of vertices.
Parameters:
    
  * **vertices** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike")) – The vertices of the `[Polygon`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygon> "manim.mobject.geometry.polygram.Polygon").
  * **kwargs** (_Any_) – Forwarded to the parent constructor.


Examples
Example: PolygonExample [¶](https://docs.manim.community/en/stable/reference/<#polygonexample>)
![../_images/PolygonExample-1.png](https://docs.manim.community/en/stable/_images/PolygonExample-1.png)
```
frommanimimport *
classPolygonExample(Scene):
  defconstruct(self):
    isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
    position_list = [
      [4, 1, 0], # middle right
      [4, -2.5, 0], # bottom right
      [0, -2.5, 0], # bottom left
      [0, 3, 0], # top left
      [2, 1, 0], # middle
      [4, 3, 0], # top right
    ]
    square_and_triangles = Polygon(*position_list, color=PURPLE_B)
    self.add(isosceles, square_and_triangles)

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
_original__init__(_* vertices_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygon._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vertices** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Polygram ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygram.html>) [ Previous Cutout ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Cutout.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Polygon](https://docs.manim.community/en/stable/reference/<#>)
    * `[Polygon`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygon>)
      * `[Polygon._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Polygon._original__init__>)


