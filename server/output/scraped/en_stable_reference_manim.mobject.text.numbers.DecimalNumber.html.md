# DecimalNumber[¶](https://docs.manim.community/en/stable/reference/<#decimalnumber> "Link to this heading")
Qualified name: `manim.mobject.text.numbers.DecimalNumber`
_class_ DecimalNumber(_number=0_ , _num_decimal_places=2_ , _mob_class= <class 'manim.mobject.text.tex_mobject.MathTex'>_, _include_sign=False_ , _group_with_commas=True_ , _digit_buff_per_font_unit=0.001_ , _show_ellipsis=False_ , _unit=None_ , _unit_buff_per_font_unit=0_ , _include_background_rectangle=False_ , _edge_to_fix=array([-1._ , _0._ , _0.])_ , _font_size=48_ , _stroke_width=0_ , _fill_opacity=1.0_ , _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/numbers.html#DecimalNumber>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
An mobject representing a decimal number.
Parameters:
    
  * **number** (_float_) – The numeric value to be displayed. It can later be modified using `[set_value()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber.set_value> "manim.mobject.text.numbers.DecimalNumber.set_value").
  * **num_decimal_places** (_int_) – The number of decimal places after the decimal separator. Values are automatically rounded.
  * **mob_class** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The class for rendering digits and units, by default `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex").
  * **include_sign** (_bool_) – Set to `True` to include a sign for positive numbers and zero.
  * **group_with_commas** (_bool_) – When `True` thousands groups are separated by commas for readability.
  * **digit_buff_per_font_unit** (_float_) – Additional spacing between digits. Scales with font size.
  * **show_ellipsis** (_bool_) – When a number has been truncated by rounding, indicate with an ellipsis (`...`).
  * **unit** (_str_ _|__None_) – A unit string which can be placed to the right of the numerical values.
  * **unit_buff_per_font_unit** (_float_) – An additional spacing between the numerical values and the unit. A value of `unit_buff_per_font_unit=0.003` gives a decent spacing. Scales with font size.
  * **include_background_rectangle** (_bool_) – Adds a background rectangle to increase contrast on busy scenes.
  * **edge_to_fix** (_Sequence_ _[__float_ _]_) – Assuring right- or left-alignment of the full object.
  * **font_size** (_float_) – Size of the font.
  * **stroke_width** (_float_)
  * **fill_opacity** (_float_)


Examples
Example: MovingSquareWithUpdaters [¶](https://docs.manim.community/en/stable/reference/<#movingsquarewithupdaters>)
```
frommanimimport *
classMovingSquareWithUpdaters(Scene):
  defconstruct(self):
    decimal = DecimalNumber(
      0,
      show_ellipsis=True,
      num_decimal_places=3,
      include_sign=True,
      unit=r"\text{M-Units}",
      unit_buff_per_font_unit=0.003
    )
    square = Square().to_edge(UP)
    decimal.add_updater(lambda d: d.next_to(square, RIGHT))
    decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
    self.add(square, decimal)
    self.play(
      square.animate.to_edge(DOWN),
      rate_func=there_and_back,
      run_time=5,
    )
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`get_value`  
---  
`increment_value`  
`[set_value`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber.set_value> "manim.mobject.text.numbers.DecimalNumber.set_value") | Set the value of the `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") to a new number.  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`[font_size`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber.font_size> "manim.mobject.text.numbers.DecimalNumber.font_size") | The font size of the tex mobject.  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_get_formatter(_** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/numbers.html#DecimalNumber._get_formatter>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber._get_formatter> "Link to this definition")
    
Configuration is based first off instance attributes, but overwritten by any kew word argument. Relevant key words: - include_sign - group_with_commas - num_decimal_places - field_name (e.g. 0 or 0.real)
_original__init__(_number=0_ , _num_decimal_places=2_ , _mob_class= <class 'manim.mobject.text.tex_mobject.MathTex'>_, _include_sign=False_ , _group_with_commas=True_ , _digit_buff_per_font_unit=0.001_ , _show_ellipsis=False_ , _unit=None_ , _unit_buff_per_font_unit=0_ , _include_background_rectangle=False_ , _edge_to_fix=array([-1._ , _0._ , _0.])_ , _font_size=48_ , _stroke_width=0_ , _fill_opacity=1.0_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **number** (_float_)
  * **num_decimal_places** (_int_)
  * **mob_class** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **include_sign** (_bool_)
  * **group_with_commas** (_bool_)
  * **digit_buff_per_font_unit** (_float_)
  * **show_ellipsis** (_bool_)
  * **unit** (_str_ _|__None_)
  * **unit_buff_per_font_unit** (_float_)
  * **include_background_rectangle** (_bool_)
  * **edge_to_fix** (_Sequence_ _[__float_ _]_)
  * **font_size** (_float_)
  * **stroke_width** (_float_)
  * **fill_opacity** (_float_)


_property_ font_size[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber.font_size> "Link to this definition")
    
The font size of the tex mobject.
set_value(_number_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/numbers.html#DecimalNumber.set_value>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber.set_value> "Link to this definition")
    
Set the value of the `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") to a new number.
Parameters:
    
**number** (_float_) – The value that will overwrite the current number of the `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber").
[ Next Integer ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.Integer.html>) [ Previous numbers ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DecimalNumber](https://docs.manim.community/en/stable/reference/<#>)
    * `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber>)
      * `[DecimalNumber._get_formatter()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber._get_formatter>)
      * `[DecimalNumber._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber._original__init__>)
      * `[DecimalNumber.font_size`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber.font_size>)
      * `[DecimalNumber.set_value()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.DecimalNumber.set_value>)


