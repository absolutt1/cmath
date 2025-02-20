# LogBase[¶](https://docs.manim.community/en/stable/reference/<#logbase> "Link to this heading")
Qualified name: `manim.mobject.graphing.scale.LogBase`
_class_ LogBase(_base =10_, _custom_labels =True_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/scale.html#LogBase>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase> "Link to this definition")
    
Bases: `_ScaleBase`
Scale for logarithmic graphs/functions.
Parameters:
    
  * **base** (_float_) – The base of the log, by default 10.
  * **custom_labels** (_bool_) – For use with `[Axes`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.Axes.html#manim.mobject.graphing.coordinate_systems.Axes> "manim.mobject.graphing.coordinate_systems.Axes"): Whether or not to include `LaTeX` axis labels, by default True.


Examples
```
func = ParametricFunction(lambda x: x, scaling=LogBase(base=2))

```
Copy to clipboard
Methods
`[function`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.function> "manim.mobject.graphing.scale.LogBase.function") | Scales the value to fit it to a logarithmic scale.``self.function(5)==10**5``  
---|---  
`[get_custom_labels`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.get_custom_labels> "manim.mobject.graphing.scale.LogBase.get_custom_labels") | Produces custom `[Integer`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer> "manim.mobject.text.numbers.Integer") labels in the form of `10^2`.  
`[inverse_function`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.inverse_function> "manim.mobject.graphing.scale.LogBase.inverse_function") | Inverse of `function`.  
function(_value_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/scale.html#LogBase.function>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.function> "Link to this definition")
    
Scales the value to fit it to a logarithmic scale.``self.function(5)==10**5``
Parameters:
    
**value** (_float_)
Return type:
    
float
get_custom_labels(_val_range_ , _unit_decimal_places =0_, _** base_config_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/scale.html#LogBase.get_custom_labels>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.get_custom_labels> "Link to this definition")
    
Produces custom `[Integer`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer> "manim.mobject.text.numbers.Integer") labels in the form of `10^2`.
Parameters:
    
  * **val_range** (_Iterable_ _[__float_ _]_) – The iterable of values used to create the labels. Determines the exponent.
  * **unit_decimal_places** (_int_) – The number of decimal places to include in the exponent
  * **base_config** (_dict_ _[__str_ _,__Any_ _]_) – Additional arguments to be passed to `[Integer`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.Integer.html#manim.mobject.text.numbers.Integer> "manim.mobject.text.numbers.Integer").


Return type:
    
list[[Mobject](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")]
inverse_function(_value_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/scale.html#LogBase.inverse_function>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.inverse_function> "Link to this definition")
    
Inverse of `function`. The value must be greater than 0
Parameters:
    
**value** (_float_)
Return type:
    
float
[ Next logo ](https://docs.manim.community/en/stable/reference/<manim.mobject.logo.html>) [ Previous LinearBase ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.scale.LinearBase.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [LogBase](https://docs.manim.community/en/stable/reference/<#>)
    * `[LogBase`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase>)
      * `[LogBase.function()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.function>)
      * `[LogBase.get_custom_labels()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.get_custom_labels>)
      * `[LogBase.inverse_function()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.scale.LogBase.inverse_function>)


