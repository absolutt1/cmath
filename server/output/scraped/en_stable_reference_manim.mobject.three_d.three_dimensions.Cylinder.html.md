# Cylinder[¶](https://docs.manim.community/en/stable/reference/<#cylinder> "Link to this heading")
Qualified name: `manim.mobject.three\_d.three\_dimensions.Cylinder`
_class_ Cylinder(_radius =1_, _height =2_, _direction =array([0., 0., 1.])_, _v_range =[0, 6.283185307179586]_, _show_ends =True_, _resolution =(24, 24)_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "Link to this definition")
    
Bases: `[Surface`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface> "manim.mobject.three_d.three_dimensions.Surface")
A cylinder, defined by its height, radius and direction,
Parameters:
    
  * **radius** (_float_) – The radius of the cylinder.
  * **height** (_float_) – The height of the cylinder.
  * **direction** (_np.ndarray_) – The direction of the central axis of the cylinder.
  * **v_range** (_Sequence_ _[__float_ _]_) – The height along the height axis (given by direction) to start and end on.
  * **show_ends** (_bool_) – Whether to show the end caps or not.
  * **resolution** (_Sequence_ _[__int_ _]_) – The number of samples taken of the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder"). A tuple can be used to define different resolutions for `u` and `v` respectively.


Examples
Example: ExampleCylinder [¶](https://docs.manim.community/en/stable/reference/<#examplecylinder>)
![../_images/ExampleCylinder-1.png](https://docs.manim.community/en/stable/_images/ExampleCylinder-1.png)
```
frommanimimport *
classExampleCylinder(ThreeDScene):
  defconstruct(self):
    axes = ThreeDAxes()
    cylinder = Cylinder(radius=2, height=3)
    self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
    self.add(axes, cylinder)

```
Copy to clipboard
Make interactive
Methods
`[add_bases`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.add_bases> "manim.mobject.three_d.three_dimensions.Cylinder.add_bases") | Adds the end caps of the cylinder.  
---|---  
`[func`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.func> "manim.mobject.three_d.three_dimensions.Cylinder.func") | Converts from cylindrical coordinates to cartesian.  
`[get_direction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.get_direction> "manim.mobject.three_d.three_dimensions.Cylinder.get_direction") | Returns the direction of the central axis of the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder").  
`[set_direction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.set_direction> "manim.mobject.three_d.three_dimensions.Cylinder.set_direction") | Sets the direction of the central axis of the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder").  
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
_original__init__(_radius =1_, _height =2_, _direction =array([0., 0., 1.])_, _v_range =[0, 6.283185307179586]_, _show_ends =True_, _resolution =(24, 24)_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **radius** (_float_)
  * **height** (_float_)
  * **direction** (_ndarray_)
  * **v_range** (_Sequence_ _[__float_ _]_)
  * **show_ends** (_bool_)
  * **resolution** (_Sequence_ _[__int_ _]_)


Return type:
    
None
add_bases()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.add_bases>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.add_bases> "Link to this definition")
    
Adds the end caps of the cylinder.
Return type:
    
None
func(_u_ , _v_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.func>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.func> "Link to this definition")
    
Converts from cylindrical coordinates to cartesian.
Parameters:
    
  * **u** (_float_) – The height.
  * **v** (_float_) – The azimuthal angle.


Returns:
    
Points defining the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder").
Return type:
    
`numpy.ndarray`
get_direction()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.get_direction>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.get_direction> "Link to this definition")
    
Returns the direction of the central axis of the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder").
Returns:
    
**direction** – The direction of the central axis of the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder").
Return type:
    
`numpy.array`
set_direction(_direction_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Cylinder.set_direction>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.set_direction> "Link to this definition")
    
Sets the direction of the central axis of the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder").
Parameters:
    
**direction** (`numpy.array`) – The direction of the central axis of the `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder> "manim.mobject.three_d.three_dimensions.Cylinder").
Return type:
    
None
[ Next Dot3D ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Dot3D.html>) [ Previous Cube ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Cube.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Cylinder](https://docs.manim.community/en/stable/reference/<#>)
    * `[Cylinder`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder>)
      * `[Cylinder._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder._original__init__>)
      * `[Cylinder.add_bases()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.add_bases>)
      * `[Cylinder.func()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.func>)
      * `[Cylinder.get_direction()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.get_direction>)
      * `[Cylinder.set_direction()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cylinder.set_direction>)


