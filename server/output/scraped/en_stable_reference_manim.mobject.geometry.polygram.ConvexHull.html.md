# ConvexHull[¶](https://docs.manim.community/en/stable/reference/<#convexhull> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.ConvexHull`
_class_ ConvexHull(_* points_, _tolerance =1e-05_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#ConvexHull>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.ConvexHull> "Link to this definition")
    
Bases: `[Polygram`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygram.html#manim.mobject.geometry.polygram.Polygram> "manim.mobject.geometry.polygram.Polygram")
Constructs a convex hull for a set of points in no particular order.
Parameters:
    
  * **points** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike")) – The points to consider.
  * **tolerance** (_float_) – The tolerance used by quickhull.
  * **kwargs** (_Any_) – Forwarded to the parent constructor.


Examples
Example: ConvexHullExample [¶](https://docs.manim.community/en/stable/reference/<#convexhullexample>)
![../_images/ConvexHullExample-1.png](https://docs.manim.community/en/stable/_images/ConvexHullExample-1.png)
```
frommanimimport *
classConvexHullExample(Scene):
  defconstruct(self):
    points = [
      [-2.35, -2.25, 0],
      [1.65, -2.25, 0],
      [2.65, -0.25, 0],
      [1.65, 1.75, 0],
      [-0.35, 2.75, 0],
      [-2.35, 0.75, 0],
      [-0.35, -1.25, 0],
      [0.65, -0.25, 0],
      [-1.35, 0.25, 0],
      [0.15, 0.75, 0]
    ]
    hull = ConvexHull(*points, color=BLUE)
    dots = VGroup(*[Dot(point) for point in points])
    self.add(hull)
    self.add(dots)

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
_original__init__(_* points_, _tolerance =1e-05_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.ConvexHull._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **points** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **tolerance** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Cutout ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Cutout.html>) [ Previous polygram ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ConvexHull](https://docs.manim.community/en/stable/reference/<#>)
    * `[ConvexHull`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.ConvexHull>)
      * `[ConvexHull._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.ConvexHull._original__init__>)


