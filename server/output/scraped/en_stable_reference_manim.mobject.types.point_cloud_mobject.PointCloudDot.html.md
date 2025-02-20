# PointCloudDot[¶](https://docs.manim.community/en/stable/reference/<#pointclouddot> "Link to this heading")
Qualified name: `manim.mobject.types.point\_cloud\_mobject.PointCloudDot`
_class_ PointCloudDot(_center =array([0., 0., 0.])_, _radius =2.0_, _stroke_width =2_, _density =10_, _color =ManimColor('#FFFF00')_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/point_cloud_mobject.html#PointCloudDot>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PointCloudDot> "Link to this definition")
    
Bases: `[Mobject1D`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.point_cloud_mobject.Mobject1D.html#manim.mobject.types.point_cloud_mobject.Mobject1D> "manim.mobject.types.point_cloud_mobject.Mobject1D")
A disc made of a cloud of dots.
Examples
Example: PointCloudDotExample [¶](https://docs.manim.community/en/stable/reference/<#pointclouddotexample>)
![../_images/PointCloudDotExample-1.png](https://docs.manim.community/en/stable/_images/PointCloudDotExample-1.png)
```
frommanimimport *
classPointCloudDotExample(Scene):
  defconstruct(self):
    cloud_1 = PointCloudDot(color=RED)
    cloud_2 = PointCloudDot(stroke_width=4, radius=1)
    cloud_3 = PointCloudDot(density=15)
    group = Group(cloud_1, cloud_2, cloud_3).arrange()
    self.add(group)

```
Copy to clipboard
Make interactive
Example: PointCloudDotExample2 [¶](https://docs.manim.community/en/stable/reference/<#pointclouddotexample2>)
```
frommanimimport *
classPointCloudDotExample2(Scene):
  defconstruct(self):
    plane = ComplexPlane()
    cloud = PointCloudDot(color=RED)
    self.add(
      plane, cloud
    )
    self.wait()
    self.play(
      cloud.animate.apply_complex_function(lambda z: np.exp(z))
    )

```
Copy to clipboard
Make interactive
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points> "manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points") | Initializes `points` and therefore the shape.  
---|---  
`init_points`  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`depth` | The depth of the mobject.  
`height` | The height of the mobject.  
`width` | The width of the mobject.  
Parameters:
    
  * **center** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D"))
  * **radius** (_float_)
  * **stroke_width** (_int_)
  * **density** (_int_)
  * **color** ([_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor"))
  * **kwargs** (_Any_)


_original__init__(_center =array([0., 0., 0.])_, _radius =2.0_, _stroke_width =2_, _density =10_, _color =ManimColor('#FFFF00')_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PointCloudDot._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **center** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D"))
  * **radius** (_float_)
  * **stroke_width** (_int_)
  * **density** (_int_)
  * **color** ([_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor"))
  * **kwargs** (_Any_)


Return type:
    
None
generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/point_cloud_mobject.html#PointCloudDot.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points> "Link to this definition")
    
Initializes `points` and therefore the shape.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
Return type:
    
None
[ Next vectorized_mobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.html>) [ Previous Point ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.point_cloud_mobject.Point.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [PointCloudDot](https://docs.manim.community/en/stable/reference/<#>)
    * `[PointCloudDot`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PointCloudDot>)
      * `[PointCloudDot._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PointCloudDot._original__init__>)
      * `[PointCloudDot.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.point_cloud_mobject.PointCloudDot.generate_points>)


