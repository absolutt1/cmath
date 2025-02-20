# Vector[¶](https://docs.manim.community/en/stable/reference/<#vector> "Link to this heading")
Qualified name: `manim.mobject.geometry.line.Vector`
_class_ Vector(_direction =array([1., 0., 0.])_, _buff =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Vector>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Vector> "Link to this definition")
    
Bases: `[Arrow`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow")
A vector specialized for use in graphs.
Caution
Do not confuse with the `[Vector2D`](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector2D> "manim.typing.Vector2D"), `[Vector3D`](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D") or `[VectorND`](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.VectorND> "manim.typing.VectorND") type aliases, which are not Mobjects!
Parameters:
    
  * **direction** ([_Point2DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point2DLike> "manim.typing.Point2DLike") _|_[_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike")) – The direction of the arrow.
  * **buff** (_float_) – The distance of the vector from its endpoints.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Arrow`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Arrow.html#manim.mobject.geometry.line.Arrow> "manim.mobject.geometry.line.Arrow")


Examples
Example: VectorExample [¶](https://docs.manim.community/en/stable/reference/<#vectorexample>)
![../_images/VectorExample-1.png](https://docs.manim.community/en/stable/_images/VectorExample-1.png)
```
frommanimimport *
classVectorExample(Scene):
  defconstruct(self):
    plane = NumberPlane()
    vector_1 = Vector([1,2])
    vector_2 = Vector([-5,-2])
    self.add(plane, vector_1, vector_2)

```
Copy to clipboard
Make interactive
Methods
`[coordinate_label`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Vector.coordinate_label> "manim.mobject.geometry.line.Vector.coordinate_label") | Creates a label based on the coordinates of the vector.  
---|---  
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
_original__init__(_direction =array([1., 0., 0.])_, _buff =0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Vector._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **direction** ([_Point2DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point2DLike> "manim.typing.Point2DLike") _|_[_Point3DLike_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3DLike> "manim.typing.Point3DLike"))
  * **buff** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
coordinate_label(_integer_labels =True_, _n_dim =2_, _color =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/line.html#Vector.coordinate_label>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Vector.coordinate_label> "Link to this definition")
    
Creates a label based on the coordinates of the vector.
Parameters:
    
  * **integer_labels** (_bool_) – Whether or not to round the coordinates to integers.
  * **n_dim** (_int_) – The number of dimensions of the vector.
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_) – Sets the color of label, optional.
  * **kwargs** (_Any_) – Additional arguments to be passed to `[Matrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix> "manim.mobject.matrix.Matrix").


Returns:
    
The label.
Return type:
    
`[Matrix`](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.Matrix.html#manim.mobject.matrix.Matrix> "manim.mobject.matrix.Matrix")
Examples
Example: VectorCoordinateLabel [¶](https://docs.manim.community/en/stable/reference/<#vectorcoordinatelabel>)
![../_images/VectorCoordinateLabel-1.png](https://docs.manim.community/en/stable/_images/VectorCoordinateLabel-1.png)
```
frommanimimport *
classVectorCoordinateLabel(Scene):
  defconstruct(self):
    plane = NumberPlane()
    vec_1 = Vector([1, 2])
    vec_2 = Vector([-3, -2])
    label_1 = vec_1.coordinate_label()
    label_2 = vec_2.coordinate_label(color=YELLOW)
    self.add(plane, vec_1, vec_2, label_1, label_2)

```
Copy to clipboard
Make interactive
[ Next polygram ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.html>) [ Previous TangentLine ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.TangentLine.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Vector](https://docs.manim.community/en/stable/reference/<#>)
    * `[Vector`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Vector>)
      * `[Vector._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Vector._original__init__>)
      * `[Vector.coordinate_label()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.line.Vector.coordinate_label>)


