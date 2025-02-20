# DecimalMatrix[¶](https://docs.manim.community/en/stable/reference/<#decimalmatrix> "Link to this heading")
Qualified name: `manim.mobject.matrix.DecimalMatrix`
_class_ DecimalMatrix(_matrix_ , _element_to_mobject= <class 'manim.mobject.text.numbers.DecimalNumber'>_, _element_to_mobject_config={'num_decimal_places': 1}_, _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/matrix.html#DecimalMatrix>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.DecimalMatrix> "Link to this definition")
    
Bases: `[Matrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix> "manim.mobject.matrix.Matrix")
A mobject that displays a matrix with decimal entries on the screen.
Examples
Example: DecimalMatrixExample [¶](https://docs.manim.community/en/stable/reference/<#decimalmatrixexample>)
![../_images/DecimalMatrixExample-1.png](https://docs.manim.community/en/stable/_images/DecimalMatrixExample-1.png)
```
frommanimimport *
classDecimalMatrixExample(Scene):
  defconstruct(self):
    m0 = DecimalMatrix(
      [[3.456, 2.122], [33.2244, 12]],
      element_to_mobject_config={"num_decimal_places": 2},
      left_bracket="\\{",
      right_bracket="\\}")
    self.add(m0)

```
Copy to clipboard
Make interactive
Will round/truncate the decimal places as per the provided config.
Parameters:
    
  * **matrix** (_Iterable_) – A numpy 2d array or list of lists
  * **element_to_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – Mobject to use, by default DecimalNumber
  * **element_to_mobject_config** (_dict_ _[__str_ _,_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_) – Config for the desired mobject, by default {“num_decimal_places”: 1}


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
_original__init__(_matrix_ , _element_to_mobject= <class 'manim.mobject.text.numbers.DecimalNumber'>_, _element_to_mobject_config={'num_decimal_places': 1}_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.DecimalMatrix._original__init__> "Link to this definition")
    
Will round/truncate the decimal places as per the provided config.
Parameters:
    
  * **matrix** (_Iterable_) – A numpy 2d array or list of lists
  * **element_to_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – Mobject to use, by default DecimalNumber
  * **element_to_mobject_config** (_dict_ _[__str_ _,_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_) – Config for the desired mobject, by default {“num_decimal_places”: 1}


[ Next IntegerMatrix ](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.IntegerMatrix.html>) [ Previous matrix ](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DecimalMatrix](https://docs.manim.community/en/stable/reference/<#>)
    * `[DecimalMatrix`](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.DecimalMatrix>)
      * `[DecimalMatrix._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.DecimalMatrix._original__init__>)


