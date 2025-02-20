# Dot3D[¶](https://docs.manim.community/en/stable/reference/<#dot3d> "Link to this heading")
Qualified name: `manim.mobject.three\_d.three\_dimensions.Dot3D`
_class_ Dot3D(_point =array([0., 0., 0.])_, _radius =0.08_, _color =ManimColor('#FFFFFF')_, _resolution =(8, 8)_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Dot3D>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Dot3D> "Link to this definition")
    
Bases: `[Sphere`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere")
A spherical dot.
Parameters:
    
  * **point** (_list_ _|__np.ndarray_) – The location of the dot.
  * **radius** (_float_) – The radius of the dot.
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the `[Dot3D`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Dot3D> "manim.mobject.three_d.three_dimensions.Dot3D").
  * **resolution** (_tuple_ _[__int_ _,__int_ _]_) – The number of samples taken of the `[Dot3D`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Dot3D> "manim.mobject.three_d.three_dimensions.Dot3D"). A tuple can be used to define different resolutions for `u` and `v` respectively.


Examples
Example: Dot3DExample [¶](https://docs.manim.community/en/stable/reference/<#dot3dexample>)
![../_images/Dot3DExample-1.png](https://docs.manim.community/en/stable/_images/Dot3DExample-1.png)
```
frommanimimport *
classDot3DExample(ThreeDScene):
  defconstruct(self):
    self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
    axes = ThreeDAxes()
    dot_1 = Dot3D(point=axes.coords_to_point(0, 0, 1), color=RED)
    dot_2 = Dot3D(point=axes.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
    dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
    self.add(axes, dot_1, dot_2,dot_3)

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
_original__init__(_point =array([0., 0., 0.])_, _radius =0.08_, _color =ManimColor('#FFFFFF')_, _resolution =(8, 8)_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Dot3D._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **point** (_list_ _|__ndarray_)
  * **radius** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **resolution** (_tuple_ _[__int_ _,__int_ _]_)


Return type:
    
None
[ Next Line3D ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Line3D.html>) [ Previous Cylinder ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Cylinder.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Dot3D](https://docs.manim.community/en/stable/reference/<#>)
    * `[Dot3D`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Dot3D>)
      * `[Dot3D._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Dot3D._original__init__>)


