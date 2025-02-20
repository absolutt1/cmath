# Axes[¶](https://docs.manim.community/en/stable/reference/<#axes> "Link to this heading")
Qualified name: `manim.mobject.graphing.coordinate\_systems.Axes`
_class_ Axes(_x_range =None_, _y_range =None_, _x_length =12_, _y_length =6_, _axis_config =None_, _x_axis_config =None_, _y_axis_config =None_, _tips =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes> "Link to this definition")
    
Bases: `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup"), `[CoordinateSystem`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem> "manim.mobject.graphing.coordinate_systems.CoordinateSystem")
Creates a set of axes.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_) – The `(x_min, x_max, x_step)` values of the x-axis.
  * **y_range** (_Sequence_ _[__float_ _]__|__None_) – The `(y_min, y_max, y_step)` values of the y-axis.
  * **x_length** (_float_ _|__None_) – The length of the x-axis.
  * **y_length** (_float_ _|__None_) – The length of the y-axis.
  * **axis_config** (_dict_ _|__None_) – Arguments to be passed to `[NumberLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine") that influences both axes.
  * **x_axis_config** (_dict_ _|__None_) – Arguments to be passed to `[NumberLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine") that influence the x-axis.
  * **y_axis_config** (_dict_ _|__None_) – Arguments to be passed to `[NumberLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine") that influence the y-axis.
  * **tips** (_bool_) – Whether or not to include the tips on both axes.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[CoordinateSystem`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem> "manim.mobject.graphing.coordinate_systems.CoordinateSystem") and `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup").


Examples
Example: LogScalingExample [¶](https://docs.manim.community/en/stable/reference/<#logscalingexample>)
![../_images/LogScalingExample-1.png](https://docs.manim.community/en/stable/_images/LogScalingExample-1.png)
```
frommanimimport *
classLogScalingExample(Scene):
  defconstruct(self):
    ax = Axes(
      x_range=[0, 10, 1],
      y_range=[-2, 6, 1],
      tips=False,
      axis_config={"include_numbers": True},
      y_axis_config={"scaling": LogBase(custom_labels=True)},
    )
    # x_min must be > 0 because log is undefined at 0.
    graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
    self.add(ax, graph)

```
Copy to clipboard
Make interactive
Styling arguments can be passed to the underlying `[NumberLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine") mobjects that represent the axes:
Example: AxesWithDifferentTips [¶](https://docs.manim.community/en/stable/reference/<#axeswithdifferenttips>)
![../_images/AxesWithDifferentTips-1.png](https://docs.manim.community/en/stable/_images/AxesWithDifferentTips-1.png)
```
frommanimimport *
classAxesWithDifferentTips(Scene):
  defconstruct(self):
    ax = Axes(axis_config={'tip_shape': StealthTip})
    self.add(ax)

```
Copy to clipboard
Make interactive
Methods
`[coords_to_point`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.coords_to_point> "manim.mobject.graphing.coordinate_systems.Axes.coords_to_point") | Accepts coordinates from the axes and returns a point with respect to the scene.  
---|---  
`[get_axes`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.get_axes> "manim.mobject.graphing.coordinate_systems.Axes.get_axes") | Gets the axes.  
`[get_axis_labels`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.get_axis_labels> "manim.mobject.graphing.coordinate_systems.Axes.get_axis_labels") | Defines labels for the x-axis and y-axis of the graph.  
`[plot_line_graph`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.plot_line_graph> "manim.mobject.graphing.coordinate_systems.Axes.plot_line_graph") | Draws a line graph.  
`[point_to_coords`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.point_to_coords> "manim.mobject.graphing.coordinate_systems.Axes.point_to_coords") | Accepts a point from the scene and returns its coordinates with respect to the axes.  
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
_create_axis(_range_terms_ , _axis_config_ , _length_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes._create_axis>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._create_axis> "Link to this definition")
    
Creates an axis and dynamically adjusts its position depending on where 0 is located on the line.
Parameters:
    
  * **range_terms** (_Sequence_ _[__float_ _]_) – The range of the the axis : `(x_min, x_max, x_step)`.
  * **axis_config** (_dict_ _[__str_ _,__Any_ _]_) – Additional parameters that are passed to `[NumberLine`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.NumberLine.html#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine").
  * **length** (_float_) – The length of the axis.


Returns:
    
Returns a number line based on `range_terms`.
Return type:
    
`NumberLine`
_static_ _origin_shift(_axis_range_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes._origin_shift>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._origin_shift> "Link to this definition")
    
Determines how to shift graph mobjects to compensate when 0 is not on the axis.
Parameters:
    
**axis_range** (_Sequence_ _[__float_ _]_) – The range of the axis : `(x_min, x_max, x_step)`.
Return type:
    
float
_original__init__(_x_range =None_, _y_range =None_, _x_length =12_, _y_length =6_, _axis_config =None_, _x_axis_config =None_, _y_axis_config =None_, _tips =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_)
  * **y_range** (_Sequence_ _[__float_ _]__|__None_)
  * **x_length** (_float_ _|__None_)
  * **y_length** (_float_ _|__None_)
  * **axis_config** (_dict_ _|__None_)
  * **x_axis_config** (_dict_ _|__None_)
  * **y_axis_config** (_dict_ _|__None_)
  * **tips** (_bool_)
  * **kwargs** (_Any_)


Return type:
    
None
_static_ _update_default_configs(_default_configs_ , _passed_configs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes._update_default_configs>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._update_default_configs> "Link to this definition")
    
Takes in two tuples of dicts and return modifies the first such that values from `passed_configs` overwrite values in `default_configs`. If a key does not exist in default_configs, it is added to the dict.
This method is useful for having defaults in a class and being able to overwrite them with user-defined input.
Parameters:
    
  * **default_configs** (_tuple_ _[__dict_ _[__Any_ _,__Any_ _]__]_) – The dict that will be updated.
  * **passed_configs** (_tuple_ _[__dict_ _[__Any_ _,__Any_ _]__]_) – The dict that will be used to update.


Return type:
    
None
Examples
To create a tuple with one dictionary, add a comma after the element:
```
self._update_default_configs(
  (dict_1,)(
    dict_2,
  )
)

```
Copy to clipboard
coords_to_point(_* coords_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes.coords_to_point>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.coords_to_point> "Link to this definition")
    
Accepts coordinates from the axes and returns a point with respect to the scene. Equivalent to ax @ (coord1)
Parameters:
    
**coords** (_float_ _|__Sequence_ _[__float_ _]__|__Sequence_ _[__Sequence_ _[__float_ _]__]__|__ndarray_) – 
The coordinates. Each coord is passed as a separate argument: `ax.coords_to_point(1, 2, 3)`.
Also accepts a list of coordinates
`ax.coords_to_point( [x_0, x_1, ...], [y_0, y_1, ...], ... )`
`ax.coords_to_point( [[x_0, y_0, z_0], [x_1, y_1, z_1]] )`
Returns:
    
A point with respect to the scene’s coordinate system. The shape of the array will be similar to the shape of the input.
Return type:
    
np.ndarray
Examples
```
>>> frommanimimport Axes
>>> importnumpyasnp
>>> ax = Axes()
>>> np.around(ax.coords_to_point(1, 0, 0), 2)
array([0.86, 0. , 0. ])
>>> np.around(ax @ (1, 0, 0), 2)
array([0.86, 0. , 0. ])
>>> np.around(ax.coords_to_point([[0, 1], [1, 1], [1, 0]]), 2)
array([[0. , 0.75, 0. ],
    [0.86, 0.75, 0. ],
    [0.86, 0. , 0. ]])
>>> np.around(
...   ax.coords_to_point([0, 1, 1], [1, 1, 0]), 2
... ) # Transposed version of the above
array([[0. , 0.86, 0.86],
    [0.75, 0.75, 0. ],
    [0. , 0. , 0. ]])

```
Copy to clipboard
Example: CoordsToPointExample [¶](https://docs.manim.community/en/stable/reference/<#coordstopointexample>)
![../_images/CoordsToPointExample-1.png](https://docs.manim.community/en/stable/_images/CoordsToPointExample-1.png)
```
frommanimimport *
classCoordsToPointExample(Scene):
  defconstruct(self):
    ax = Axes().add_coordinates()
    # a dot with respect to the axes
    dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
    lines = ax.get_lines_to_point(ax.c2p(2,2))
    # a dot with respect to the scene
    # the default plane corresponds to the coordinates of the scene.
    plane = NumberPlane()
    dot_scene = Dot((2,2,0), color=RED)
    self.add(plane, dot_scene, ax, dot_axes, lines)

```
Copy to clipboard
Make interactive
get_axes()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes.get_axes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.get_axes> "Link to this definition")
    
Gets the axes.
Returns:
    
A pair of axes.
Return type:
    
`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
get_axis_labels(_x_label ='x'_, _y_label ='y'_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes.get_axis_labels>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.get_axis_labels> "Link to this definition")
    
Defines labels for the x-axis and y-axis of the graph.
For increased control over the position of the labels, use `[get_x_axis_label()`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label> "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label") and `[get_y_axis_label()`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_y_axis_label> "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_y_axis_label").
Parameters:
    
  * **x_label** (_float_ _|__str_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The label for the x_axis. Defaults to `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.
  * **y_label** (_float_ _|__str_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The label for the y_axis. Defaults to `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") for `str` and `float` inputs.


Returns:
    
A `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup") of the labels for the x_axis and y_axis.
Return type:
    
`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
See also
`[get_x_axis_label()`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label> "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_x_axis_label") `[get_y_axis_label()`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_y_axis_label> "manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_y_axis_label")
Examples
Example: GetAxisLabelsExample [¶](https://docs.manim.community/en/stable/reference/<#getaxislabelsexample>)
![../_images/GetAxisLabelsExample-1.png](https://docs.manim.community/en/stable/_images/GetAxisLabelsExample-1.png)
```
frommanimimport *
classGetAxisLabelsExample(Scene):
  defconstruct(self):
    ax = Axes()
    labels = ax.get_axis_labels(
      Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45)
    )
    self.add(ax, labels)

```
Copy to clipboard
Make interactive
plot_line_graph(_x_values_ , _y_values_ , _z_values =None_, _line_color =ManimColor('#FFFF00')_, _add_vertex_dots =True_, _vertex_dot_radius =0.08_, _vertex_dot_style =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes.plot_line_graph>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.plot_line_graph> "Link to this definition")
    
Draws a line graph.
The graph connects the vertices formed from zipping `x_values`, `y_values` and `z_values`. Also adds `[Dots`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot> "manim.mobject.geometry.arc.Dot") at the vertices if `add_vertex_dots` is set to `True`.
Parameters:
    
  * **x_values** (_Iterable_ _[__float_ _]_) – Iterable of values along the x-axis.
  * **y_values** (_Iterable_ _[__float_ _]_) – Iterable of values along the y-axis.
  * **z_values** (_Iterable_ _[__float_ _]__|__None_) – Iterable of values (zeros if z_values is None) along the z-axis.
  * **line_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – Color for the line graph.
  * **add_vertex_dots** (_bool_) – Whether or not to add `[Dot`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot> "manim.mobject.geometry.arc.Dot") at each vertex.
  * **vertex_dot_radius** (_float_) – Radius for the `[Dot`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot> "manim.mobject.geometry.arc.Dot") at each vertex.
  * **vertex_dot_style** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Style arguments to be passed into `[Dot`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Dot.html#manim.mobject.geometry.arc.Dot> "manim.mobject.geometry.arc.Dot") at each vertex.
  * **kwargs** (_Any_) – Additional arguments to be passed into `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").


Returns:
    
A VDict containing both the line and dots (if specified). The line can be accessed with: `line_graph["line_graph"]`. The dots can be accessed with: `line_graph["vertex_dots"]`.
Return type:
    
`[VDict`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict> "manim.mobject.types.vectorized_mobject.VDict")
Examples
Example: LineGraphExample [¶](https://docs.manim.community/en/stable/reference/<#linegraphexample>)
![../_images/LineGraphExample-1.png](https://docs.manim.community/en/stable/_images/LineGraphExample-1.png)
```
frommanimimport *
classLineGraphExample(Scene):
  defconstruct(self):
    plane = NumberPlane(
      x_range = (0, 7),
      y_range = (0, 5),
      x_length = 7,
      axis_config={"include_numbers": True},
    )
    plane.center()
    line_graph = plane.plot_line_graph(
      x_values = [0, 1.5, 2, 2.8, 4, 6.25],
      y_values = [1, 3, 2.25, 4, 2.5, 1.75],
      line_color=GOLD_E,
      vertex_dot_style=dict(stroke_width=3, fill_color=PURPLE),
      stroke_width = 4,
    )
    self.add(plane, line_graph)

```
Copy to clipboard
Make interactive
point_to_coords(_point_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/coordinate_systems.html#Axes.point_to_coords>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.point_to_coords> "Link to this definition")
    
Accepts a point from the scene and returns its coordinates with respect to the axes.
Parameters:
    
**point** (_Sequence_ _[__float_ _]_) – The point, i.e. `RIGHT` or `[0, 1, 0]`. Also accepts a list of points as `[RIGHT, [0, 1, 0]]`.
Returns:
    
The coordinates on the axes, i.e. `[4.0, 7.0]`. Or a list of coordinates if point is a list of points.
Return type:
    
np.ndarray[float]
Examples
```
>>> frommanimimport Axes, RIGHT
>>> importnumpyasnp
>>> ax = Axes(x_range=[0, 10, 2])
>>> np.around(ax.point_to_coords(RIGHT), 2)
array([5.83, 0. ])
>>> np.around(ax.point_to_coords([[0, 0, 1], [1, 0, 0]]), 2)
array([[5. , 0. ],
    [5.83, 0. ]])

```
Copy to clipboard
Example: PointToCoordsExample [¶](https://docs.manim.community/en/stable/reference/<#pointtocoordsexample>)
![../_images/PointToCoordsExample-1.png](https://docs.manim.community/en/stable/_images/PointToCoordsExample-1.png)
```
frommanimimport *
classPointToCoordsExample(Scene):
  defconstruct(self):
    ax = Axes(x_range=[0, 10, 2]).add_coordinates()
    circ = Circle(radius=0.5).shift(UR * 2)
    # get the coordinates of the circle with respect to the axes
    coords = np.around(ax.point_to_coords(circ.get_right()), decimals=2)
    label = (
      Matrix([[coords[0]], [coords[1]]]).scale(0.75).next_to(circ, RIGHT)
    )
    self.add(ax, circ, label, Dot(circ.get_right()))

```
Copy to clipboard
Make interactive
[ Next ComplexPlane ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.ComplexPlane.html>) [ Previous coordinate_systems ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Axes](https://docs.manim.community/en/stable/reference/<#>)
    * `[Axes`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes>)
      * `[Axes._create_axis()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._create_axis>)
      * `[Axes._origin_shift()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._origin_shift>)
      * `[Axes._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._original__init__>)
      * `[Axes._update_default_configs()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes._update_default_configs>)
      * `[Axes.coords_to_point()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.coords_to_point>)
      * `[Axes.get_axes()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.get_axes>)
      * `[Axes.get_axis_labels()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.get_axis_labels>)
      * `[Axes.plot_line_graph()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.plot_line_graph>)
      * `[Axes.point_to_coords()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.coordinate_systems.Axes.point_to_coords>)


