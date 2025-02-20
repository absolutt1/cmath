# Arc[¶](https://docs.manim.community/en/stable/reference/<#arc> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.Arc`
_class_ Arc(_radius =1.0_, _start_angle =0_, _angle =1.5707963267948966_, _num_components =9_, _arc_center =array([0., 0., 0.])_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Arc>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc> "Link to this definition")
    
Bases: `[TipableVMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.TipableVMobject.html#manim.mobject.geometry.arc.TipableVMobject> "manim.mobject.geometry.arc.TipableVMobject")
A circular arc.
Examples
A simple arc of angle Pi.
Example: ArcExample [¶](https://docs.manim.community/en/stable/reference/<#arcexample>)
![../_images/ArcExample-1.png](https://docs.manim.community/en/stable/_images/ArcExample-1.png)
```
frommanimimport *
classArcExample(Scene):
  defconstruct(self):
    self.add(Arc(angle=PI))

```
Copy to clipboard
Make interactive
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc.generate_points> "manim.mobject.geometry.arc.Arc.generate_points") | Initializes `points` and therefore the shape.  
---|---  
`[get_arc_center`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc.get_arc_center> "manim.mobject.geometry.arc.Arc.get_arc_center") | Looks at the normals to the first two anchors, and finds their intersection points  
`init_points`  
`move_arc_center_to`  
`stop_angle`  
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
    
  * **radius** (_float_ _|__None_)
  * **start_angle** (_float_)
  * **angle** (_float_)
  * **num_components** (_int_)
  * **arc_center** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **kwargs** (_Any_)


_original__init__(_radius =1.0_, _start_angle =0_, _angle =1.5707963267948966_, _num_components =9_, _arc_center =array([0., 0., 0.])_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **radius** (_float_ _|__None_)
  * **start_angle** (_float_)
  * **angle** (_float_)
  * **num_components** (_int_)
  * **arc_center** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **kwargs** (_Any_)


generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Arc.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc.generate_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
None
get_arc_center(_warning =True_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#Arc.get_arc_center>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc.get_arc_center> "Link to this definition")
    
Looks at the normals to the first two anchors, and finds their intersection points
Parameters:
    
**warning** (_bool_)
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
[ Next ArcBetweenPoints ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.ArcBetweenPoints.html>) [ Previous Annulus ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Annulus.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Arc](https://docs.manim.community/en/stable/reference/<#>)
    * `[Arc`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc>)
      * `[Arc._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc._original__init__>)
      * `[Arc.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc.generate_points>)
      * `[Arc.get_arc_center()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.Arc.get_arc_center>)


