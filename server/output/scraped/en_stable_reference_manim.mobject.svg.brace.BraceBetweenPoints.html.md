# BraceBetweenPoints[¶](https://docs.manim.community/en/stable/reference/<#bracebetweenpoints> "Link to this heading")
Qualified name: `manim.mobject.svg.brace.BraceBetweenPoints`
_class_ BraceBetweenPoints(_point_1_ , _point_2_ , _direction =array([0., 0., 0.])_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#BraceBetweenPoints>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceBetweenPoints> "Link to this definition")
    
Bases: `[Brace`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace> "manim.mobject.svg.brace.Brace")
Similar to Brace, but instead of taking a mobject it uses 2 points to place the brace.
A fitting direction for the brace is computed, but it still can be manually overridden. If the points go from left to right, the brace is drawn from below. Swapping the points places the brace on the opposite side.
Parameters:
    
  * **point_1** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|__None_) – The first point.
  * **point_2** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|__None_) – The second point.
  * **direction** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D") _|__None_) – The direction from which the brace faces towards the points.


Examples
Example: BraceBPExample [¶](https://docs.manim.community/en/stable/reference/<#bracebpexample>)
```
frommanimimport *
classBraceBPExample(Scene):
  defconstruct(self):
    p1 = [0,0,0]
    p2 = [1,2,0]
    brace = BraceBetweenPoints(p1,p2)
    self.play(Create(NumberPlane()))
    self.play(Create(brace))
    self.wait(2)

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
_original__init__(_point_1_ , _point_2_ , _direction =array([0., 0., 0.])_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceBetweenPoints._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **point_1** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|__None_)
  * **point_2** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike") _|__None_)
  * **direction** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D") _|__None_)


[ Next BraceLabel ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.BraceLabel.html>) [ Previous Brace ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [BraceBetweenPoints](https://docs.manim.community/en/stable/reference/<#>)
    * `[BraceBetweenPoints`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceBetweenPoints>)
      * `[BraceBetweenPoints._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceBetweenPoints._original__init__>)


