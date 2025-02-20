# PolarPlane[¶](https://docs.manim.community/en/stable/reference/<#polarplane> "Link to this heading")
Qualified name: `manim.mobject.graphing.coordinate\_systems.PolarPlane`
_class_ PolarPlane(_radius_max =4.0_, _size =None_, _radius_step =1_, _azimuth_step =None_, _azimuth_units ='PI radians'_, _azimuth_compact_fraction =True_, _azimuth_offset =0_, _azimuth_direction ='CCW'_, _azimuth_label_buff =0.1_, _azimuth_label_font_size =24_, _radius_config =None_, _background_line_style =None_, _faded_line_style =None_, _faded_line_ratio =1_, _make_smooth_after_applying_functions =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane> "Link to this definition")
    
Bases: `[Axes`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes> "manim.mobject.graphing.coordinate_systems.Axes")
Creates a polar plane with background lines.
Parameters:
    
  * **azimuth_step** (_float_ _|__None_) – 
The number of divisions in the azimuth (also known as the angular coordinate or polar angle). If `None` is specified then it will use the default specified by `azimuth_units`:
    * `"PI radians"` or `"TAU radians"`: 20
    * `"degrees"`: 36
    * `"gradians"`: 40
    * `None`: 1
A non-integer value will result in a partial division at the end of the circle.
  * **size** (_float_ _|__None_) – The diameter of the plane.
  * **radius_step** (_float_) – The distance between faded radius lines.
  * **radius_max** (_float_) – The maximum value of the radius.
  * **azimuth_units** (_str_ _|__None_) – 
Specifies a default labelling system for the azimuth. Choices are:
    * `"PI radians"`: Fractional labels in the interval [0,2π] with π as a constant.
    * `"TAU radians"`: Fractional labels in the interval [0,τ] (where τ=2π) with τ as a constant.
    * `"degrees"`: Decimal labels in the interval [0,360] with a degree (∘) symbol.
    * `"gradians"`: Decimal labels in the interval [0,400] with a superscript “g” (g).
    * `None`: Decimal labels in the interval [0,1].
  * **azimuth_compact_fraction** (_bool_) – If the `azimuth_units` choice has fractional labels, choose whether to combine the constant in a compact form xuy as opposed to xyu, where u is the constant.
  * **azimuth_offset** (_float_) – The angle offset of the azimuth, expressed in radians.
  * **azimuth_direction** (_str_) – 
The direction of the azimuth.
    * `"CW"`: Clockwise.
    * `"CCW"`: Anti-clockwise.
  * **azimuth_label_buff** (_float_) – The buffer for the azimuth labels.
  * **azimuth_label_font_size** (_float_) – The font size of the azimuth labels.
  * **radius_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – The axis config for the radius.
  * **background_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **faded_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **faded_line_ratio** (_int_)
  * **make_smooth_after_applying_functions** (_bool_)
  * **kwargs** (_Any_)


Examples
Example: PolarPlaneExample [¶](https://docs.manim.community/en/stable/reference/<#polarplaneexample>)
![../_images/PolarPlaneExample-1.png](https://docs.manim.community/en/stable/_images/PolarPlaneExample-1.png)
```
frommanimimport *
classPolarPlaneExample(Scene):
  defconstruct(self):
    polarplane_pi = PolarPlane(
      azimuth_units="PI radians",
      size=6,
      azimuth_label_font_size=33.6,
      radius_config={"font_size": 33.6},
    ).add_coordinates()
    self.add(polarplane_pi)

```
Copy to clipboard
Make interactive
References: `[PolarPlane`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane> "manim.mobject.graphing.coordinate_systems.PolarPlane")
Methods
`[add_coordinates`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates> "manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates") | Adds the coordinates.  
---|---  
`[get_axes`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes> "manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes") | Gets the axes.  
`[get_coordinate_labels`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels> "manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels") | Gets labels for the coordinates  
`get_radian_label`  
`get_vector`  
`prepare_for_nonlinear_transform`  
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
_get_lines()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane._get_lines>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane._get_lines> "Link to this definition")
    
Generate all the lines and circles, faded and not faded.
Returns:
    
The first (i.e the non faded lines and circles) and second (i.e the faded lines and circles) sets of lines and circles, respectively.
Return type:
    
Tuple[`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup"), `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")]
_init_background_lines()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane._init_background_lines>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane._init_background_lines> "Link to this definition")
    
Will init all the lines of NumberPlanes (faded or not)
Return type:
    
None
_original__init__(_radius_max =4.0_, _size =None_, _radius_step =1_, _azimuth_step =None_, _azimuth_units ='PI radians'_, _azimuth_compact_fraction =True_, _azimuth_offset =0_, _azimuth_direction ='CCW'_, _azimuth_label_buff =0.1_, _azimuth_label_font_size =24_, _radius_config =None_, _background_line_style =None_, _faded_line_style =None_, _faded_line_ratio =1_, _make_smooth_after_applying_functions =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **radius_max** (_float_)
  * **size** (_float_ _|__None_)
  * **radius_step** (_float_)
  * **azimuth_step** (_float_ _|__None_)
  * **azimuth_units** (_str_ _|__None_)
  * **azimuth_compact_fraction** (_bool_)
  * **azimuth_offset** (_float_)
  * **azimuth_direction** (_str_)
  * **azimuth_label_buff** (_float_)
  * **azimuth_label_font_size** (_float_)
  * **radius_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **background_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **faded_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **faded_line_ratio** (_int_)
  * **make_smooth_after_applying_functions** (_bool_)
  * **kwargs** (_Any_)


Return type:
    
None
add_coordinates(_r_values =None_, _a_values =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.add_coordinates>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates> "Link to this definition")
    
Adds the coordinates.
Parameters:
    
  * **r_values** (_Iterable_ _[__float_ _]__|__None_) – Iterable of values along the radius, by default None.
  * **a_values** (_Iterable_ _[__float_ _]__|__None_) – Iterable of values along the azimuth, by default None.


Return type:
    
_Self_
get_axes()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.get_axes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes> "Link to this definition")
    
Gets the axes.
Returns:
    
A pair of axes.
Return type:
    
`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
get_coordinate_labels(_r_values =None_, _a_values =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#PolarPlane.get_coordinate_labels>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels> "Link to this definition")
    
Gets labels for the coordinates
Parameters:
    
  * **r_values** (_Iterable_ _[__float_ _]__|__None_) – Iterable of values along the radius, by default None.
  * **a_values** (_Iterable_ _[__float_ _]__|__None_) – Iterable of values along the azimuth, by default None.
  * **kwargs** (_Any_)


Returns:
    
Labels for the radius and azimuth values.
Return type:
    
[VDict](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict> "manim.mobject.types.vectorized_mobject.VDict")
[ Next ThreeDAxes ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.ThreeDAxes.html>) [ Previous NumberPlane ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.NumberPlane.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [PolarPlane](https://docs.manim.community/en/stable/reference/<#>)
    * `[PolarPlane`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane>)
      * `[PolarPlane._get_lines()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane._get_lines>)
      * `[PolarPlane._init_background_lines()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane._init_background_lines>)
      * `[PolarPlane._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane._original__init__>)
      * `[PolarPlane.add_coordinates()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.add_coordinates>)
      * `[PolarPlane.get_axes()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.get_axes>)
      * `[PolarPlane.get_coordinate_labels()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.PolarPlane.get_coordinate_labels>)


