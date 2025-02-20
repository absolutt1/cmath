# NumberLine[¶](https://docs.manim.community/en/stable/reference/<#numberline> "Link to this heading")
Qualified name: `manim.mobject.graphing.number\_line.NumberLine`
_class_ NumberLine(_x_range=None_ , _length=None_ , _unit_size=1_ , _include_ticks=True_ , _tick_size=0.1_ , _numbers_with_elongated_ticks=None_ , _longer_tick_multiple=2_ , _exclude_origin_tick=False_ , _rotation=0_ , _stroke_width=2.0_ , _include_tip=False_ , _tip_width=0.35_ , _tip_height=0.35_ , _tip_shape=None_ , _include_numbers=False_ , _font_size=36_ , _label_direction=array([ 0._, _-1._ , _0.])_ , _label_constructor= <class 'manim.mobject.text.tex_mobject.MathTex'>_, _scaling= <manim.mobject.graphing.scale.LinearBase object>_, _line_to_number_buff=0.25_ , _decimal_number_config=None_ , _numbers_to_exclude=None_ , _numbers_to_include=None_ , _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine> "Link to this definition")
    
Bases: `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")
Creates a number line with tick marks.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_) – The `[x_min, x_max, x_step]` values to create the line.
  * **length** (_float_ _|__None_) – The length of the number line.
  * **unit_size** (_float_) – The distance between each tick of the line. Overwritten by `length`, if specified.
  * **include_ticks** (_bool_) – Whether to include ticks on the number line.
  * **tick_size** (_float_) – The length of each tick mark.
  * **numbers_with_elongated_ticks** (_Iterable_ _[__float_ _]__|__None_) – An iterable of specific values with elongated ticks.
  * **longer_tick_multiple** (_int_) – Influences how many times larger elongated ticks are than regular ticks (2 = 2x).
  * **rotation** (_float_) – The angle (in radians) at which the line is rotated.
  * **stroke_width** (_float_) – The thickness of the line.
  * **include_tip** (_bool_) – Whether to add a tip to the end of the line.
  * **tip_width** (_float_) – The width of the tip.
  * **tip_height** (_float_) – The height of the tip.
  * **tip_shape** (_type_ _[_[_ArrowTip_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip") _]__|__None_) – The mobject class used to construct the tip, or `None` (the default) for the default arrow tip. Passed classes have to inherit from `[ArrowTip`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip").
  * **include_numbers** (_bool_) – Whether to add numbers to the tick marks. The number of decimal places is determined by the step size, this default can be overridden by `decimal_number_config`.
  * **scaling** (__ScaleBase_) – The way the `x_range` is value is scaled, i.e. `[LogBase`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.scale.LogBase.html#manim.mobject.graphing.scale.LogBase> "manim.mobject.graphing.scale.LogBase") for a logarithmic numberline. Defaults to `[LinearBase`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.scale.LinearBase.html#manim.mobject.graphing.scale.LinearBase> "manim.mobject.graphing.scale.LinearBase").
  * **font_size** (_float_) – The size of the label mobjects. Defaults to 36.
  * **label_direction** (_Sequence_ _[__float_ _]_) – The specific position to which label mobjects are added on the line.
  * **label_constructor** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – Determines the mobject class that will be used to construct the labels of the number line.
  * **line_to_number_buff** (_float_) – The distance between the line and the label mobject.
  * **decimal_number_config** (_dict_ _|__None_) – Arguments that can be passed to `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") to influence number mobjects.
  * **numbers_to_exclude** (_Iterable_ _[__float_ _]__|__None_) – An explicit iterable of numbers to not be added to the number line.
  * **numbers_to_include** (_Iterable_ _[__float_ _]__|__None_) – An explicit iterable of numbers to add to the number line
  * **kwargs** – Additional arguments to be passed to `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line").
  * **exclude_origin_tick** (_bool_)


Note
Number ranges that include both negative and positive values will be generated from the 0 point, and may not include a tick at the min / max values as the tick locations are dependent on the step size.
Examples
Example: NumberLineExample [¶](https://docs.manim.community/en/stable/reference/<#numberlineexample>)
![../_images/NumberLineExample-1.png](https://docs.manim.community/en/stable/_images/NumberLineExample-1.png)
```
frommanimimport *
classNumberLineExample(Scene):
  defconstruct(self):
    l0 = NumberLine(
      x_range=[-10, 10, 2],
      length=10,
      color=BLUE,
      include_numbers=True,
      label_direction=UP,
    )
    l1 = NumberLine(
      x_range=[-10, 10, 2],
      unit_size=0.5,
      numbers_with_elongated_ticks=[-2, 4],
      include_numbers=True,
      font_size=24,
    )
    num6 = l1.numbers[8]
    num6.set_color(RED)
    l2 = NumberLine(
      x_range=[-2.5, 2.5 + 0.5, 0.5],
      length=12,
      decimal_number_config={"num_decimal_places": 2},
      include_numbers=True,
    )
    l3 = NumberLine(
      x_range=[-5, 5 + 1, 1],
      length=6,
      include_tip=True,
      include_numbers=True,
      rotation=10 * DEGREES,
    )
    line_group = VGroup(l0, l1, l2, l3).arrange(DOWN, buff=1)
    self.add(line_group)

```
Copy to clipboard
Make interactive
Methods
`[add_labels`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_labels> "manim.mobject.graphing.number_line.NumberLine.add_labels") | Adds specifically positioned labels to the `[NumberLine`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine") using a `dict`.  
---|---  
`[add_numbers`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_numbers> "manim.mobject.graphing.number_line.NumberLine.add_numbers") | Adds `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") mobjects representing their position at each tick of the number line.  
`[add_ticks`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_ticks> "manim.mobject.graphing.number_line.NumberLine.add_ticks") | Adds ticks to the number line.  
`get_labels`  
`[get_number_mobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_number_mobject> "manim.mobject.graphing.number_line.NumberLine.get_number_mobject") | Generates a positioned `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") mobject generated according to `label_constructor`.  
`get_number_mobjects`  
`[get_tick`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_tick> "manim.mobject.graphing.number_line.NumberLine.get_tick") | Generates a tick and positions it along the number line.  
`get_tick_marks`  
`[get_tick_range`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_tick_range> "manim.mobject.graphing.number_line.NumberLine.get_tick_range") | Generates the range of values on which labels are plotted based on the `x_range` attribute of the number line.  
`get_unit_size`  
`get_unit_vector`  
`[n2p`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.n2p> "manim.mobject.graphing.number_line.NumberLine.n2p") | Abbreviation for `[number_to_point()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.number_to_point> "manim.mobject.graphing.number_line.NumberLine.number_to_point").  
`[number_to_point`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.number_to_point> "manim.mobject.graphing.number_line.NumberLine.number_to_point") | Accepts a value along the number line and returns a point with respect to the scene.  
`[p2n`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.p2n> "manim.mobject.graphing.number_line.NumberLine.p2n") | Abbreviation for `[point_to_number()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.point_to_number> "manim.mobject.graphing.number_line.NumberLine.point_to_number").  
`[point_to_number`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.point_to_number> "manim.mobject.graphing.number_line.NumberLine.point_to_number") | Accepts a point with respect to the scene and returns a float along the number line.  
`rotate_about_number`  
`rotate_about_zero`  
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
_create_label_tex(_label_tex_ , _label_constructor =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine._create_label_tex>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine._create_label_tex> "Link to this definition")
    
Checks if the label is a `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"), otherwise, creates a label by passing `label_tex` to `label_constructor`.
Parameters:
    
  * **label_tex** (_str_ _|__float_ _|_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The label for which a mobject should be created. If the label already is a mobject, no new mobject is created.
  * **label_constructor** (_Callable_ _|__None_) – Optional. A class or function returning a mobject when passing `label_tex` as an argument. If `None` is passed (the default), the label constructor from the `label_constructor` attribute is used.


Returns:
    
The label.
Return type:
    
`[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
_original__init__(_x_range=None_ , _length=None_ , _unit_size=1_ , _include_ticks=True_ , _tick_size=0.1_ , _numbers_with_elongated_ticks=None_ , _longer_tick_multiple=2_ , _exclude_origin_tick=False_ , _rotation=0_ , _stroke_width=2.0_ , _include_tip=False_ , _tip_width=0.35_ , _tip_height=0.35_ , _tip_shape=None_ , _include_numbers=False_ , _font_size=36_ , _label_direction=array([ 0._, _-1._ , _0.])_ , _label_constructor= <class 'manim.mobject.text.tex_mobject.MathTex'>_, _scaling= <manim.mobject.graphing.scale.LinearBase object>_, _line_to_number_buff=0.25_ , _decimal_number_config=None_ , _numbers_to_exclude=None_ , _numbers_to_include=None_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **x_range** (_Sequence_ _[__float_ _]__|__None_)
  * **length** (_float_ _|__None_)
  * **unit_size** (_float_)
  * **include_ticks** (_bool_)
  * **tick_size** (_float_)
  * **numbers_with_elongated_ticks** (_Iterable_ _[__float_ _]__|__None_)
  * **longer_tick_multiple** (_int_)
  * **exclude_origin_tick** (_bool_)
  * **rotation** (_float_)
  * **stroke_width** (_float_)
  * **include_tip** (_bool_)
  * **tip_width** (_float_)
  * **tip_height** (_float_)
  * **tip_shape** (_type_ _[_[_ArrowTip_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip") _]__|__None_)
  * **include_numbers** (_bool_)
  * **font_size** (_float_)
  * **label_direction** (_Sequence_ _[__float_ _]_)
  * **label_constructor** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **scaling** (__ScaleBase_)
  * **line_to_number_buff** (_float_)
  * **decimal_number_config** (_dict_ _|__None_)
  * **numbers_to_exclude** (_Iterable_ _[__float_ _]__|__None_)
  * **numbers_to_include** (_Iterable_ _[__float_ _]__|__None_)


add_labels(_dict_values_ , _direction =None_, _buff =None_, _font_size =None_, _label_constructor =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.add_labels>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_labels> "Link to this definition")
    
Adds specifically positioned labels to the `[NumberLine`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine> "manim.mobject.graphing.number_line.NumberLine") using a `dict`. The labels can be accessed after creation via `self.labels`.
Parameters:
    
  * **dict_values** (_dict_ _[__float_ _,__str_ _|__float_ _|_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]_) – A dictionary consisting of the position along the number line and the mobject to be added: `{1: Tex("Monday"), 3: Tex("Tuesday")}`. `label_constructor` will be used to construct the labels if the value is not a mobject (`str` or `float`).
  * **direction** (_Sequence_ _[__float_ _]_) – Determines the direction at which the label is positioned next to the line.
  * **buff** (_float_ _|__None_) – The distance of the label from the line.
  * **font_size** (_float_ _|__None_) – The font size of the mobject to be positioned.
  * **label_constructor** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__None_) – The `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") class that will be used to construct the label. Defaults to the `label_constructor` attribute of the number line if not specified.


Raises:
    
**AttributeError** – If the label does not have a `font_size` attribute, an `AttributeError` is raised.
add_numbers(_x_values =None_, _excluding =None_, _font_size =None_, _label_constructor =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.add_numbers>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_numbers> "Link to this definition")
    
Adds `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") mobjects representing their position at each tick of the number line. The numbers can be accessed after creation via `self.numbers`.
Parameters:
    
  * **x_values** (_Iterable_ _[__float_ _]__|__None_) – An iterable of the values used to position and create the labels. Defaults to the output produced by `[get_tick_range()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_tick_range> "manim.mobject.graphing.number_line.NumberLine.get_tick_range")
  * **excluding** (_Iterable_ _[__float_ _]__|__None_) – A list of values to exclude from `x_values`.
  * **font_size** (_float_ _|__None_) – The font size of the labels. Defaults to the `font_size` attribute of the number line.
  * **label_constructor** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__None_) – The `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") class that will be used to construct the label. Defaults to the `label_constructor` attribute of the number line if not specified.


add_ticks()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.add_ticks>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_ticks> "Link to this definition")
    
Adds ticks to the number line. Ticks can be accessed after creation via `self.ticks`.
get_number_mobject(_x_ , _direction =None_, _buff =None_, _font_size =None_, _label_constructor =None_, _** number_config_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.get_number_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_number_mobject> "Link to this definition")
    
Generates a positioned `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") mobject generated according to `label_constructor`.
Parameters:
    
  * **x** (_float_) – The x-value at which the mobject should be positioned.
  * **direction** (_Sequence_ _[__float_ _]__|__None_) – Determines the direction at which the label is positioned next to the line.
  * **buff** (_float_ _|__None_) – The distance of the label from the line.
  * **font_size** (_float_ _|__None_) – The font size of the label mobject.
  * **label_constructor** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__None_) – The `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") class that will be used to construct the label. Defaults to the `label_constructor` attribute of the number line if not specified.


Returns:
    
The positioned mobject.
Return type:
    
`[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber")
get_tick(_x_ , _size =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.get_tick>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_tick> "Link to this definition")
    
Generates a tick and positions it along the number line.
Parameters:
    
  * **x** (_float_) – The position of the tick.
  * **size** (_float_ _|__None_) – The factor by which the tick is scaled.


Returns:
    
A positioned tick.
Return type:
    
`[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")
get_tick_range()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.get_tick_range>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_tick_range> "Link to this definition")
    
Generates the range of values on which labels are plotted based on the `x_range` attribute of the number line.
Returns:
    
A numpy array of floats represnting values along the number line.
Return type:
    
np.ndarray
n2p(_number_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.n2p>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.n2p> "Link to this definition")
    
Abbreviation for `[number_to_point()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.number_to_point> "manim.mobject.graphing.number_line.NumberLine.number_to_point").
Parameters:
    
**number** (_float_ _|__ndarray_)
Return type:
    
_ndarray_
number_to_point(_number_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.number_to_point>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.number_to_point> "Link to this definition")
    
Accepts a value along the number line and returns a point with respect to the scene. Equivalent to NumberLine @ number
Parameters:
    
**number** (_float_ _|__ndarray_) – The value to be transformed into a coordinate. Or a list of values.
Returns:
    
A point with respect to the scene’s coordinate system. Or a list of points.
Return type:
    
np.ndarray
Examples
```
>>> frommanimimport NumberLine
>>> number_line = NumberLine()
>>> number_line.number_to_point(0)
array([0., 0., 0.])
>>> number_line.number_to_point(1)
array([1., 0., 0.])
>>> number_line @ 1
array([1., 0., 0.])
>>> number_line.number_to_point([1, 2, 3])
array([[1., 0., 0.],
    [2., 0., 0.],
    [3., 0., 0.]])

```
Copy to clipboard
p2n(_point_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.p2n>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.p2n> "Link to this definition")
    
Abbreviation for `[point_to_number()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.point_to_number> "manim.mobject.graphing.number_line.NumberLine.point_to_number").
Parameters:
    
**point** (_Sequence_ _[__float_ _]_)
Return type:
    
float
point_to_number(_point_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/number_line.html#NumberLine.point_to_number>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.point_to_number> "Link to this definition")
    
Accepts a point with respect to the scene and returns a float along the number line.
Parameters:
    
**point** (_Sequence_ _[__float_ _]_) – A sequence of values consisting of `(x_coord, y_coord, z_coord)`.
Returns:
    
A float representing a value along the number line.
Return type:
    
float
Examples
```
>>> frommanimimport NumberLine
>>> number_line = NumberLine()
>>> number_line.point_to_number((0, 0, 0))
np.float64(0.0)
>>> number_line.point_to_number((1, 0, 0))
np.float64(1.0)
>>> number_line.point_to_number([[0.5, 0, 0], [1, 0, 0], [1.5, 0, 0]])
array([0.5, 1. , 1.5])

```
Copy to clipboard
[ Next UnitInterval ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.UnitInterval.html>) [ Previous number_line ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.number_line.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [NumberLine](https://docs.manim.community/en/stable/reference/<#>)
    * `[NumberLine`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine>)
      * `[NumberLine._create_label_tex()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine._create_label_tex>)
      * `[NumberLine._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine._original__init__>)
      * `[NumberLine.add_labels()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_labels>)
      * `[NumberLine.add_numbers()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_numbers>)
      * `[NumberLine.add_ticks()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.add_ticks>)
      * `[NumberLine.get_number_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_number_mobject>)
      * `[NumberLine.get_tick()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_tick>)
      * `[NumberLine.get_tick_range()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.get_tick_range>)
      * `[NumberLine.n2p()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.n2p>)
      * `[NumberLine.number_to_point()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.number_to_point>)
      * `[NumberLine.p2n()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.p2n>)
      * `[NumberLine.point_to_number()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.number_line.NumberLine.point_to_number>)


