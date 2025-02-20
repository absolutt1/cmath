# DecimalTable[¶](https://docs.manim.community/en/stable/reference/<#decimaltable> "Link to this heading")
Qualified name: `manim.mobject.table.DecimalTable`
_class_ DecimalTable(_table_ , _element_to_mobject= <class 'manim.mobject.text.numbers.DecimalNumber'>_, _element_to_mobject_config={'num_decimal_places': 1}_, _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/table.html#DecimalTable>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.DecimalTable> "Link to this definition")
    
Bases: `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table")
A specialized `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table") mobject for use with `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber") to display decimal entries.
Examples
Example: DecimalTableExample [¶](https://docs.manim.community/en/stable/reference/<#decimaltableexample>)
![../_images/DecimalTableExample-1.png](https://docs.manim.community/en/stable/_images/DecimalTableExample-1.png)
```
frommanimimport *
classDecimalTableExample(Scene):
  defconstruct(self):
    x_vals = [-2,-1,0,1,2]
    y_vals = np.exp(x_vals)
    t0 = DecimalTable(
      [x_vals, y_vals],
      row_labels=[MathTex("x"), MathTex("f(x)=e^{x}")],
      h_buff=1,
      element_to_mobject_config={"num_decimal_places": 2})
    self.add(t0)

```
Copy to clipboard
Make interactive
Special case of `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table") with `element_to_mobject` set to `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber"). By default, `num_decimal_places` is set to 1. Will round/truncate the decimal places based on the provided `element_to_mobject_config`.
Parameters:
    
  * **table** (_Iterable_ _[__Iterable_ _[__float_ _|__str_ _]__]_) – A 2D array, or a list of lists. Content of the table must be valid input for `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber").
  * **element_to_mobject** (_Callable_ _[__[__float_ _|__str_ _]__,_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]_) – The `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") class applied to the table entries. Set as `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber").
  * **element_to_mobject_config** (_dict_) – Element to mobject config, here set as {“num_decimal_places”: 1}.
  * **kwargs** – Additional arguments to be passed to `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table").


Methods
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
_original__init__(_table_ , _element_to_mobject= <class 'manim.mobject.text.numbers.DecimalNumber'>_, _element_to_mobject_config={'num_decimal_places': 1}_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.DecimalTable._original__init__> "Link to this definition")
    
Special case of `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table") with `element_to_mobject` set to `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber"). By default, `num_decimal_places` is set to 1. Will round/truncate the decimal places based on the provided `element_to_mobject_config`.
Parameters:
    
  * **table** (_Iterable_ _[__Iterable_ _[__float_ _|__str_ _]__]_) – A 2D array, or a list of lists. Content of the table must be valid input for `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber").
  * **element_to_mobject** (_Callable_ _[__[__float_ _|__str_ _]__,_[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _]_) – The `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") class applied to the table entries. Set as `[DecimalNumber`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber").
  * **element_to_mobject_config** (_dict_) – Element to mobject config, here set as {“num_decimal_places”: 1}.
  * **kwargs** – Additional arguments to be passed to `[Table`](https://docs.manim.community/en/stable/reference/<manim.mobject.table.Table.html#manim.mobject.table.Table> "manim.mobject.table.Table").


[ Next IntegerTable ](https://docs.manim.community/en/stable/reference/<manim.mobject.table.IntegerTable.html>) [ Previous table ](https://docs.manim.community/en/stable/reference/<manim.mobject.table.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DecimalTable](https://docs.manim.community/en/stable/reference/<#>)
    * `[DecimalTable`](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.DecimalTable>)
      * `[DecimalTable._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.table.DecimalTable._original__init__>)


