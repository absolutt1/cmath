# Sphere[¶](https://docs.manim.community/en/stable/reference/<#sphere> "Link to this heading")
Qualified name: `manim.mobject.three\_d.three\_dimensions.Sphere`
_class_ Sphere(_center =array([0., 0., 0.])_, _radius =1_, _resolution =None_, _u_range =(0, 6.283185307179586)_, _v_range =(0, 3.141592653589793)_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Sphere>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere> "Link to this definition")
    
Bases: `[Surface`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface> "manim.mobject.three_d.three_dimensions.Surface")
A three-dimensional sphere.
Parameters:
    
  * **center** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike")) – Center of the `[Sphere`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere").
  * **radius** (_float_) – The radius of the `[Sphere`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere").
  * **resolution** (_Sequence_ _[__int_ _]__|__None_) – The number of samples taken of the `[Sphere`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere"). A tuple can be used to define different resolutions for `u` and `v` respectively.
  * **u_range** (_Sequence_ _[__float_ _]_) – The range of the `u` variable: `(u_min, u_max)`.
  * **v_range** (_Sequence_ _[__float_ _]_) – The range of the `v` variable: `(v_min, v_max)`.


Examples
Example: ExampleSphere [¶](https://docs.manim.community/en/stable/reference/<#examplesphere>)
![../_images/ExampleSphere-1.png](https://docs.manim.community/en/stable/_images/ExampleSphere-1.png)
```
frommanimimport *
classExampleSphere(ThreeDScene):
  defconstruct(self):
    self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
    sphere1 = Sphere(
      center=(3, 0, 0),
      radius=1,
      resolution=(20, 20),
      u_range=[0.001, PI - 0.001],
      v_range=[0, TAU]
    )
    sphere1.set_color(RED)
    self.add(sphere1)
    sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
    sphere2.set_color(GREEN)
    self.add(sphere2)
    sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
    sphere3.set_color(BLUE)
    self.add(sphere3)

```
Copy to clipboard
Make interactive
Methods
`[func`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere.func> "manim.mobject.three_d.three_dimensions.Sphere.func") | The z values defining the `[Sphere`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere") being plotted.  
---|---  
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
_original__init__(_center =array([0., 0., 0.])_, _radius =1_, _resolution =None_, _u_range =(0, 6.283185307179586)_, _v_range =(0, 3.141592653589793)_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **center** ([_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **radius** (_float_)
  * **resolution** (_Sequence_ _[__int_ _]__|__None_)
  * **u_range** (_Sequence_ _[__float_ _]_)
  * **v_range** (_Sequence_ _[__float_ _]_)


Return type:
    
None
func(_u_ , _v_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Sphere.func>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere.func> "Link to this definition")
    
The z values defining the `[Sphere`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere") being plotted.
Returns:
    
The z values defining the `[Sphere`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere").
Return type:
    
`numpy.array`
Parameters:
    
  * **u** (_float_)
  * **v** (_float_)


[ Next Surface ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Surface.html>) [ Previous Prism ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Prism.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Sphere](https://docs.manim.community/en/stable/reference/<#>)
    * `[Sphere`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere>)
      * `[Sphere._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere._original__init__>)
      * `[Sphere.func()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Sphere.func>)


