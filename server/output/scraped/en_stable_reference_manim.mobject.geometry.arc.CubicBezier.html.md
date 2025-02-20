# CubicBezier[¶](https://docs.manim.community/en/stable/reference/<#cubicbezier> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.CubicBezier`
_class_ CubicBezier(_start_anchor_ , _start_handle_ , _end_handle_ , _end_anchor_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#CubicBezier>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.CubicBezier> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A cubic Bézier curve.
Example
Example: BezierSplineExample [¶](https://docs.manim.community/en/stable/reference/<#beziersplineexample>)
![../_images/BezierSplineExample-1.png](https://docs.manim.community/en/stable/_images/BezierSplineExample-1.png)
```
frommanimimport *
classBezierSplineExample(Scene):
  defconstruct(self):
    p1 = np.array([-3, 1, 0])
    p1b = p1 + [1, 0, 0]
    d1 = Dot(point=p1).set_color(BLUE)
    l1 = Line(p1, p1b)
    p2 = np.array([3, -1, 0])
    p2b = p2 - [1, 0, 0]
    d2 = Dot(point=p2).set_color(RED)
    l2 = Line(p2, p2b)
    bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
    self.add(l1, d1, l2, d2, bezier)

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
Parameters:
    
  * **start_anchor** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **start_handle** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **end_handle** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **end_anchor** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **kwargs** (_Any_)


_original__init__(_start_anchor_ , _start_handle_ , _end_handle_ , _end_anchor_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.CubicBezier._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **start_anchor** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **start_handle** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **end_handle** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **end_anchor** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **kwargs** (_Any_)


Return type:
    
None
[ Next CurvedArrow ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.CurvedArrow.html>) [ Previous Circle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Circle.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [CubicBezier](https://docs.manim.community/en/stable/reference/<#>)
    * `[CubicBezier`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.CubicBezier>)
      * `[CubicBezier._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.CubicBezier._original__init__>)


