# IntegerMatrix[¶](https://docs.manim.community/en/stable/reference/<#integermatrix> "Link to this heading")
Qualified name: `manim.mobject.matrix.IntegerMatrix`
_class_ IntegerMatrix(_matrix_ , _element_to_mobject= <class 'manim.mobject.text.numbers.Integer'>_, _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/matrix.html#IntegerMatrix>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.IntegerMatrix> "Link to this definition")
    
Bases: `[Matrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix> "manim.mobject.matrix.Matrix")
A mobject that displays a matrix with integer entries on the screen.
Examples
Example: IntegerMatrixExample [¶](https://docs.manim.community/en/stable/reference/<#integermatrixexample>)
![../_images/IntegerMatrixExample-1.png](https://docs.manim.community/en/stable/_images/IntegerMatrixExample-1.png)
```
frommanimimport *
classIntegerMatrixExample(Scene):
  defconstruct(self):
    m0 = IntegerMatrix(
      [[3.7, 2], [42.2, 12]],
      left_bracket="(",
      right_bracket=")")
    self.add(m0)

```
Copy to clipboard
Make interactive
Will round if there are decimal entries in the matrix.
Parameters:
    
  * **matrix** (_Iterable_) – A numpy 2d array or list of lists
  * **element_to_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – Mobject to use, by default Integer


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
_original__init__(_matrix_ , _element_to_mobject= <class 'manim.mobject.text.numbers.Integer'>_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.IntegerMatrix._original__init__> "Link to this definition")
    
Will round if there are decimal entries in the matrix.
Parameters:
    
  * **matrix** (_Iterable_) – A numpy 2d array or list of lists
  * **element_to_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – Mobject to use, by default Integer


[ Next Matrix ](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.Matrix.html>) [ Previous DecimalMatrix ](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.DecimalMatrix.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [IntegerMatrix](https://docs.manim.community/en/stable/reference/<#>)
    * `[IntegerMatrix`](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.IntegerMatrix>)
      * `[IntegerMatrix._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.IntegerMatrix._original__init__>)


