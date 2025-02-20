# NumberPlane[¶](https://docs.manim.community/en/stable/reference/<#numberplane> "Link to this heading")
Qualified name: `manim.mobject.graphing.coordinate\_systems.NumberPlane`
_class_ NumberPlane(_x_range =(-7.111111111111111, 7.111111111111111, 1)_, _y_range =(-4.0, 4.0, 1)_, _x_length =None_, _y_length =None_, _background_line_style =None_, _faded_line_style =None_, _faded_line_ratio =1_, _make_smooth_after_applying_functions =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane> "Link to this definition")
    
Bases: `[Axes`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes> "manim.mobject.graphing.coordinate_systems.Axes")
Creates a cartesian plane with background lines.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_) – The `[x_min, x_max, x_step]` values of the plane in the horizontal direction.
  * **y_range** (_Sequence_ _[__float_ _]__|__None_) – The `[y_min, y_max, y_step]` values of the plane in the vertical direction.
  * **x_length** (_float_ _|__None_) – The width of the plane.
  * **y_length** (_float_ _|__None_) – The height of the plane.
  * **background_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Arguments that influence the construction of the background lines of the plane.
  * **faded_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Similar to `background_line_style`, affects the construction of the scene’s background lines.
  * **faded_line_ratio** (_int_) – Determines the number of boxes within the background lines: `2` = 4 boxes, `3` = 9 boxes.
  * **make_smooth_after_applying_functions** (_bool_) – Currently non-functional.
  * **kwargs** (_dict_ _[__str_ _,__Any_ _]_) – Additional arguments to be passed to `[Axes`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes> "manim.mobject.graphing.coordinate_systems.Axes").


Note
If `x_length` or `y_length` are not defined, they are automatically calculated such that one unit on each axis is one Manim unit long.
Examples
Example: NumberPlaneExample [¶](https://docs.manim.community/en/stable/reference/<#numberplaneexample>)
![../_images/NumberPlaneExample-1.png](https://docs.manim.community/en/stable/_images/NumberPlaneExample-1.png)
```
frommanimimport *
classNumberPlaneExample(Scene):
  defconstruct(self):
    number_plane = NumberPlane(
      background_line_style={
        "stroke_color": TEAL,
        "stroke_width": 4,
        "stroke_opacity": 0.6
      }
    )
    self.add(number_plane)

```
Copy to clipboard
Make interactive
Example: NumberPlaneScaled [¶](https://docs.manim.community/en/stable/reference/<#numberplanescaled>)
![../_images/NumberPlaneScaled-1.png](https://docs.manim.community/en/stable/_images/NumberPlaneScaled-1.png)
```
frommanimimport *
classNumberPlaneScaled(Scene):
  defconstruct(self):
    number_plane = NumberPlane(
      x_range=(-4, 11, 1),
      y_range=(-3, 3, 1),
      x_length=5,
      y_length=2,
    ).move_to(LEFT*3)
    number_plane_scaled_y = NumberPlane(
      x_range=(-4, 11, 1),
      x_length=5,
      y_length=4,
    ).move_to(RIGHT*3)
    self.add(number_plane)
    self.add(number_plane_scaled_y)

```
Copy to clipboard
Make interactive
Methods
`get_vector`  
---  
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
_get_lines()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._get_lines>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines> "Link to this definition")
    
Generate all the lines, faded and not faded.
    
Two sets of lines are generated: one parallel to the X-axis, and parallel to the Y-axis.
Returns:
    
The first (i.e the non faded lines) and second (i.e the faded lines) sets of lines, respectively.
Return type:
    
Tuple[`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup"), `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")]
_get_lines_parallel_to_axis(_axis_parallel_to_ , _axis_perpendicular_to_ , _freq_ , _ratio_faded_lines_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._get_lines_parallel_to_axis>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines_parallel_to_axis> "Link to this definition")
    
Generate a set of lines parallel to an axis.
Parameters:
    
  * **axis_parallel_to** ([_NumberLine_](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine")) – The axis with which the lines will be parallel.
  * **axis_perpendicular_to** ([_NumberLine_](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine")) – The axis with which the lines will be perpendicular.
  * **ratio_faded_lines** (_int_) – The ratio between the space between faded lines and the space between non-faded lines.
  * **freq** (_float_) – Frequency of non-faded lines (number of non-faded lines per graph unit).


Returns:
    
The first (i.e the non-faded lines parallel to axis_parallel_to) and second
    
(i.e the faded lines parallel to axis_parallel_to) sets of lines, respectively.
Return type:
    
Tuple[`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup"), `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")]
_init_background_lines()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#NumberPlane._init_background_lines>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._init_background_lines> "Link to this definition")
    
Will init all the lines of NumberPlanes (faded or not)
Return type:
    
None
_original__init__(_x_range =(-7.111111111111111, 7.111111111111111, 1)_, _y_range =(-4.0, 4.0, 1)_, _x_length =None_, _y_length =None_, _background_line_style =None_, _faded_line_style =None_, _faded_line_ratio =1_, _make_smooth_after_applying_functions =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_)
  * **y_range** (_Sequence_ _[__float_ _]__|__None_)
  * **x_length** (_float_ _|__None_)
  * **y_length** (_float_ _|__None_)
  * **background_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **faded_line_style** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **faded_line_ratio** (_int_)
  * **make_smooth_after_applying_functions** (_bool_)
  * **kwargs** (_dict_ _[__str_ _,__Any_ _]_)


[ Next PolarPlane ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.PolarPlane.html>) [ Previous CoordinateSystem ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [NumberPlane](https://docs.manim.community/en/stable/reference/<#>)
    * `[NumberPlane`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane>)
      * `[NumberPlane._get_lines()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines>)
      * `[NumberPlane._get_lines_parallel_to_axis()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._get_lines_parallel_to_axis>)
      * `[NumberPlane._init_background_lines()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._init_background_lines>)
      * `[NumberPlane._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.NumberPlane._original__init__>)


