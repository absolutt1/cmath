# Arrow3D[¶](https://docs.manim.community/en/stable/reference/<#arrow3d> "Link to this heading")
Qualified name: `manim.mobject.three\_d.three\_dimensions.Arrow3D`
_class_ Arrow3D(_start =array([-1., 0., 0.])_, _end =array([1., 0., 0.])_, _thickness =0.02_, _height =0.3_, _base_radius =0.08_, _color =ManimColor('#FFFFFF')_, _resolution =24_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Arrow3D>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Arrow3D> "Link to this definition")
    
Bases: `[Line3D`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D> "manim.mobject.three_d.three_dimensions.Line3D")
An arrow made out of a cylindrical line and a conical tip.
Parameters:
    
  * **start** (_np.ndarray_) – The start position of the arrow.
  * **end** (_np.ndarray_) – The end position of the arrow.
  * **thickness** (_float_) – The thickness of the arrow.
  * **height** (_float_) – The height of the conical tip.
  * **base_radius** (_float_) – The base radius of the conical tip.
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the arrow.
  * **resolution** (_int_ _|__Sequence_ _[__int_ _]_) – The resolution of the arrow line.


Examples
Example: ExampleArrow3D [¶](https://docs.manim.community/en/stable/reference/<#examplearrow3d>)
![../_images/ExampleArrow3D-1.png](https://docs.manim.community/en/stable/_images/ExampleArrow3D-1.png)
```
frommanimimport *
classExampleArrow3D(ThreeDScene):
  defconstruct(self):
    axes = ThreeDAxes()
    arrow = Arrow3D(
      start=np.array([0, 0, 0]),
      end=np.array([2, 2, 2]),
      resolution=8
    )
    self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
    self.add(axes, arrow)

```
Copy to clipboard
Make interactive
Methods
`[get_end`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Arrow3D.get_end> "manim.mobject.three_d.three_dimensions.Arrow3D.get_end") | Returns the ending point of the `[Line3D`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D> "manim.mobject.three_d.three_dimensions.Line3D").  
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
_original__init__(_start =array([-1., 0., 0.])_, _end =array([1., 0., 0.])_, _thickness =0.02_, _height =0.3_, _base_radius =0.08_, _color =ManimColor('#FFFFFF')_, _resolution =24_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Arrow3D._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **start** (_ndarray_)
  * **end** (_ndarray_)
  * **thickness** (_float_)
  * **height** (_float_)
  * **base_radius** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **resolution** (_int_ _|__Sequence_ _[__int_ _]_)


Return type:
    
None
get_end()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Arrow3D.get_end>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Arrow3D.get_end> "Link to this definition")
    
Returns the ending point of the `[Line3D`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D> "manim.mobject.three_d.three_dimensions.Line3D").
Returns:
    
**end** – Ending point of the `[Line3D`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Line3D.html#manim.mobject.three_d.three_dimensions.Line3D> "manim.mobject.three_d.three_dimensions.Line3D").
Return type:
    
`numpy.array`
[ Next Cone ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Cone.html>) [ Previous three_dimensions ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Arrow3D](https://docs.manim.community/en/stable/reference/<#>)
    * `[Arrow3D`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Arrow3D>)
      * `[Arrow3D._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Arrow3D._original__init__>)
      * `[Arrow3D.get_end()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Arrow3D.get_end>)


