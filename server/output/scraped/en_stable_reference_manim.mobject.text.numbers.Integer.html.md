# Integer[¶](https://docs.manim.community/en/stable/reference/<#integer> "Link to this heading")
Qualified name: `manim.mobject.text.numbers.Integer`
_class_ Integer(_number =0_, _num_decimal_places =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/numbers.html#Integer>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.Integer> "Link to this definition")
    
Bases: `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber")
A class for displaying Integers.
Examples
Example: IntegerExample [¶](https://docs.manim.community/en/stable/reference/<#integerexample>)
![../_images/IntegerExample-1.png](https://docs.manim.community/en/stable/_images/IntegerExample-1.png)
```
frommanimimport *
classIntegerExample(Scene):
  defconstruct(self):
    self.add(Integer(number=2.5).set_color(ORANGE).scale(2.5).set_x(-0.5).set_y(0.8))
    self.add(Integer(number=3.14159, show_ellipsis=True).set_x(3).set_y(3.3).scale(3.14159))
    self.add(Integer(number=42).set_x(2.5).set_y(-2.3).set_color_by_gradient(BLUE, TEAL).scale(1.7))
    self.add(Integer(number=6.28).set_x(-1.5).set_y(-2).set_color(YELLOW).scale(1.4))

```
Copy to clipboard
Make interactive
Methods
`get_value`  
---  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`font_size` | The font size of the tex mobject.  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
Parameters:
    
  * **number** (_float_)
  * **num_decimal_places** (_int_)
  * **kwargs** (_Any_)


_original__init__(_number =0_, _num_decimal_places =0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.Integer._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **number** (_float_)
  * **num_decimal_places** (_int_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Variable ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.Variable.html>) [ Previous DecimalNumber ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Integer](https://docs.manim.community/en/stable/reference/<#>)
    * `[Integer`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.Integer>)
      * `[Integer._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.numbers.Integer._original__init__>)


