# matrix[¶](https://docs.manim.community/en/stable/reference/<#module-manim.mobject.matrix> "Link to this heading")
Mobjects representing matrices.
Examples
Example: MatrixExamples [¶](https://docs.manim.community/en/stable/reference/<#matrixexamples>)
![../_images/MatrixExamples-1.png](https://docs.manim.community/en/stable/_images/MatrixExamples-1.png)
```
frommanimimport *
classMatrixExamples(Scene):
  defconstruct(self):
    m0 = Matrix([["\\pi", 0], [-1, 1]])
    m1 = IntegerMatrix([[1.5, 0.], [12, -1.3]],
      left_bracket="(",
      right_bracket=")")
    m2 = DecimalMatrix(
      [[3.456, 2.122], [33.2244, 12.33]],
      element_to_mobject_config={"num_decimal_places": 2},
      left_bracket=r"\{",
      right_bracket=r"\}")
    m3 = MobjectMatrix(
      [[Circle().scale(0.3), Square().scale(0.3)],
      [MathTex("\\pi").scale(2), Star().scale(0.3)]],
      left_bracket="\\langle",
      right_bracket="\\rangle")
    g = Group(m0, m1, m2, m3).arrange_in_grid(buff=2)
    self.add(g)

```
Copy to clipboard
Make interactive
Classes
`[DecimalMatrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.DecimalMatrix.html#manim.mobject.matrix.DecimalMatrix> "manim.mobject.matrix.DecimalMatrix") | A mobject that displays a matrix with decimal entries on the screen.  
---|---  
`[IntegerMatrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.IntegerMatrix.html#manim.mobject.matrix.IntegerMatrix> "manim.mobject.matrix.IntegerMatrix") | A mobject that displays a matrix with integer entries on the screen.  
`[Matrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix> "manim.mobject.matrix.Matrix") | A mobject that displays a matrix on the screen.  
`[MobjectMatrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.MobjectMatrix.html#manim.mobject.matrix.MobjectMatrix> "manim.mobject.matrix.MobjectMatrix") | A mobject that displays a matrix of mobject entries on the screen.  
Functions
get_det_text(_matrix_ , _determinant =None_, _background_rect =False_, _initial_scale_factor =2_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/matrix.html#get_det_text>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.get_det_text> "Link to this definition")
    
Helper function to create determinant.
Parameters:
    
  * **matrix** ([_Matrix_](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix> "manim.mobject.matrix.Matrix")) – The matrix whose determinant is to be created
  * **determinant** (_int_ _|__str_ _|__None_) – The value of the determinant of the matrix
  * **background_rect** (_bool_) – The background rectangle
  * **initial_scale_factor** (_float_) – The scale of the text det w.r.t the matrix


Returns:
    
A VGroup containing the determinant
Return type:
    
`[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
Examples
Example: DeterminantOfAMatrix [¶](https://docs.manim.community/en/stable/reference/<#determinantofamatrix>)
![../_images/DeterminantOfAMatrix-1.png](https://docs.manim.community/en/stable/_images/DeterminantOfAMatrix-1.png)
```
frommanimimport *
classDeterminantOfAMatrix(Scene):
  defconstruct(self):
    matrix = Matrix([
      [2, 0],
      [-1, 1]
    ])
    # scaling down the `det` string
    det = get_det_text(matrix,
          determinant=3,
          initial_scale_factor=1)
    # must add the matrix
    self.add(matrix)
    self.add(det)

```
Copy to clipboard
Make interactive
matrix_to_mobject(_matrix_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/matrix.html#matrix_to_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.matrix_to_mobject> "Link to this definition")
matrix_to_tex_string(_matrix_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/matrix.html#matrix_to_tex_string>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.matrix_to_tex_string> "Link to this definition")
[ Next DecimalMatrix ](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.DecimalMatrix.html>) [ Previous ManimBanner ](https://docs.manim.community/en/stable/reference/<manim.mobject.logo.ManimBanner.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [matrix](https://docs.manim.community/en/stable/reference/<#>)
    * `[get_det_text()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.get_det_text>)
    * `[matrix_to_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.matrix_to_mobject>)
    * `[matrix_to_tex_string()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.matrix.matrix_to_tex_string>)


