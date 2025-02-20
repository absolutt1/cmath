# ThreeDAxes[¶](https://docs.manim.community/en/stable/reference/<#threedaxes> "Link to this heading")
Qualified name: `manim.mobject.graphing.coordinate\_systems.ThreeDAxes`
_class_ ThreeDAxes(_x_range =(-6, 6, 1)_, _y_range =(-5, 5, 1)_, _z_range =(-4, 4, 1)_, _x_length =10.5_, _y_length =10.5_, _z_length =6.5_, _z_axis_config =None_, _z_normal =array([0., -1., 0.])_, _num_axis_pieces =20_, _light_source =array([-7., -9., 10.])_, _depth =None_, _gloss =0.5_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes> "Link to this definition")
    
Bases: `[Axes`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes> "manim.mobject.graphing.coordinate_systems.Axes")
A 3-dimensional set of axes.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_) – The `[x_min, x_max, x_step]` values of the x-axis.
  * **y_range** (_Sequence_ _[__float_ _]__|__None_) – The `[y_min, y_max, y_step]` values of the y-axis.
  * **z_range** (_Sequence_ _[__float_ _]__|__None_) – The `[z_min, z_max, z_step]` values of the z-axis.
  * **x_length** (_float_ _|__None_) – The length of the x-axis.
  * **y_length** (_float_ _|__None_) – The length of the y-axis.
  * **z_length** (_float_ _|__None_) – The length of the z-axis.
  * **z_axis_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Arguments to be passed to `[NumberLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine") that influence the z-axis.
  * **z_normal** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D")) – The direction of the normal.
  * **num_axis_pieces** (_int_) – The number of pieces used to construct the axes.
  * **light_source** (_Sequence_ _[__float_ _]_) – The direction of the light source.
  * **depth** – Currently non-functional.
  * **gloss** – Currently non-functional.
  * **kwargs** (_dict_ _[__str_ _,__Any_ _]_) – Additional arguments to be passed to `[Axes`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes> "manim.mobject.graphing.coordinate_systems.Axes").


Methods
`[get_axis_labels`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_axis_labels> "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_axis_labels") | Defines labels for the x_axis and y_axis of the graph.  
---|---  
`[get_y_axis_label`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label> "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label") | Generate a y-axis label.  
`[get_z_axis_label`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label> "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label") | Generate a z-axis label.  
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
_original__init__(_x_range =(-6, 6, 1)_, _y_range =(-5, 5, 1)_, _z_range =(-4, 4, 1)_, _x_length =10.5_, _y_length =10.5_, _z_length =6.5_, _z_axis_config =None_, _z_normal =array([0., -1., 0.])_, _num_axis_pieces =20_, _light_source =array([-7., -9., 10.])_, _depth =None_, _gloss =0.5_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_)
  * **y_range** (_Sequence_ _[__float_ _]__|__None_)
  * **z_range** (_Sequence_ _[__float_ _]__|__None_)
  * **x_length** (_float_ _|__None_)
  * **y_length** (_float_ _|__None_)
  * **z_length** (_float_ _|__None_)
  * **z_axis_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **z_normal** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D"))
  * **num_axis_pieces** (_int_)
  * **light_source** (_Sequence_ _[__float_ _]_)
  * **kwargs** (_dict_ _[__str_ _,__Any_ _]_)


Return type:
    
None
get_axis_labels(_x_label ='x'_, _y_label ='y'_, _z_label ='z'_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes.get_axis_labels>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_axis_labels> "Link to this definition")
    
Defines labels for the x_axis and y_axis of the graph.
For increased control over the position of the labels, use `[get_x_axis_label()`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label> "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label"), `[get_y_axis_label()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label> "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label"), and `[get_z_axis_label()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label> "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label").
Parameters:
    
  * **x_label** (_float_ _|__str_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The label for the x_axis. Defaults to `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
  * **y_label** (_float_ _|__str_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The label for the y_axis. Defaults to `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
  * **z_label** (_float_ _|__str_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The label for the z_axis. Defaults to `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.


Returns:
    
A `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup") of the labels for the x_axis, y_axis, and z_axis.
Return type:
    
`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
See also
`[get_x_axis_label()`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label> "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label") `[get_y_axis_label()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label> "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label") `[get_z_axis_label()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label> "manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label")
Examples
Example: GetAxisLabelsExample [¶](https://docs.manim.community/en/stable/reference/<#getaxislabelsexample>)
![../_images/GetAxisLabelsExample-2.png](https://docs.manim.community/en/stable/_images/GetAxisLabelsExample-2.png)
```
frommanimimport *
classGetAxisLabelsExample(ThreeDScene):
  defconstruct(self):
    self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
    axes = ThreeDAxes()
    labels = axes.get_axis_labels(
      Text("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
    )
    self.add(axes, labels)

```
Copy to clipboard
Make interactive
get_y_axis_label(_label_ , _edge =array([1., 1., 0.])_, _direction =array([1., 1., 0.])_, _buff =0.1_, _rotation =1.5707963267948966_, _rotation_axis =array([0., 0., 1.])_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes.get_y_axis_label>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label> "Link to this definition")
    
Generate a y-axis label.
Parameters:
    
  * **label** (_float_ _|__str_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The label. Defaults to `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
  * **edge** (_Sequence_ _[__float_ _]_) – The edge of the y-axis to which the label will be added, by default `UR`.
  * **direction** (_Sequence_ _[__float_ _]_) – Allows for further positioning of the label from an edge, by default `UR`.
  * **buff** (_float_) – The distance of the label from the line, by default `SMALL_BUFF`.
  * **rotation** (_float_) – The angle at which to rotate the label, by default `PI/2`.
  * **rotation_axis** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D")) – The axis about which to rotate the label, by default `OUT`.


Returns:
    
The positioned label.
Return type:
    
`[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
Examples
Example: GetYAxisLabelExample [¶](https://docs.manim.community/en/stable/reference/<#getyaxislabelexample>)
![../_images/GetYAxisLabelExample-2.png](https://docs.manim.community/en/stable/_images/GetYAxisLabelExample-2.png)
```
frommanimimport *
classGetYAxisLabelExample(ThreeDScene):
  defconstruct(self):
    ax = ThreeDAxes()
    lab = ax.get_y_axis_label(Tex("$y$-label"))
    self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
    self.add(ax, lab)

```
Copy to clipboard
Make interactive
get_z_axis_label(_label_ , _edge =array([0., 0., 1.])_, _direction =array([1., 0., 0.])_, _buff =0.1_, _rotation =1.5707963267948966_, _rotation_axis =array([1., 0., 0.])_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#ThreeDAxes.get_z_axis_label>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label> "Link to this definition")
    
Generate a z-axis label.
Parameters:
    
  * **label** (_float_ _|__str_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The label. Defaults to `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
  * **edge** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D")) – The edge of the z-axis to which the label will be added, by default `OUT`.
  * **direction** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D")) – Allows for further positioning of the label from an edge, by default `RIGHT`.
  * **buff** (_float_) – The distance of the label from the line, by default `SMALL_BUFF`.
  * **rotation** (_float_) – The angle at which to rotate the label, by default `PI/2`.
  * **rotation_axis** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D")) – The axis about which to rotate the label, by default `RIGHT`.
  * **kwargs** (_Any_)


Returns:
    
The positioned label.
Return type:
    
`[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
Examples
Example: GetZAxisLabelExample [¶](https://docs.manim.community/en/stable/reference/<#getzaxislabelexample>)
![../_images/GetZAxisLabelExample-1.png](https://docs.manim.community/en/stable/_images/GetZAxisLabelExample-1.png)
```
frommanimimport *
classGetZAxisLabelExample(ThreeDScene):
  defconstruct(self):
    ax = ThreeDAxes()
    lab = ax.get_z_axis_label(Tex("$z$-label"))
    self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
    self.add(ax, lab)

```
Copy to clipboard
Make interactive
[ Next functions ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.functions.html>) [ Previous PolarPlane ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.PolarPlane.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ThreeDAxes](https://docs.manim.community/en/stable/reference/<#>)
    * `[ThreeDAxes`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes>)
      * `[ThreeDAxes._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes._original__init__>)
      * `[ThreeDAxes.get_axis_labels()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_axis_labels>)
      * `[ThreeDAxes.get_y_axis_label()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_y_axis_label>)
      * `[ThreeDAxes.get_z_axis_label()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.ThreeDAxes.get_z_axis_label>)


