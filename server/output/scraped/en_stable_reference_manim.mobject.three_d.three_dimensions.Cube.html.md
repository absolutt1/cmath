# Cube[¶](https://docs.manim.community/en/stable/reference/<#cube> "Link to this heading")
Qualified name: `manim.mobject.three\_d.three\_dimensions.Cube`
_class_ Cube(_side_length =2_, _fill_opacity =0.75_, _fill_color =ManimColor('#58C4DD')_, _stroke_width =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Cube>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "Link to this definition")
    
Bases: `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
A three-dimensional cube.
Parameters:
    
  * **side_length** (_float_) – Length of each side of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube").
  * **fill_opacity** (_float_) – The opacity of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube"), from 0 being fully transparent to 1 being fully opaque. Defaults to 0.75.
  * **fill_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube").
  * **stroke_width** (_float_) – The width of the stroke surrounding each face of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube").


Examples
Example: CubeExample [¶](https://docs.manim.community/en/stable/reference/<#cubeexample>)
![../_images/CubeExample-1.png](https://docs.manim.community/en/stable/_images/CubeExample-1.png)
```
frommanimimport *
classCubeExample(ThreeDScene):
  defconstruct(self):
    self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
    axes = ThreeDAxes()
    cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
    self.add(cube)

```
Copy to clipboard
Make interactive
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube.generate_points> "manim.mobject.three_d.three_dimensions.Cube.generate_points") | Creates the sides of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube").  
---|---  
`[init_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube.init_points> "manim.mobject.three_d.three_dimensions.Cube.init_points") | Creates the sides of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube").  
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
_original__init__(_side_length =2_, _fill_opacity =0.75_, _fill_color =ManimColor('#58C4DD')_, _stroke_width =0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **side_length** (_float_)
  * **fill_opacity** (_float_)
  * **fill_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **stroke_width** (_float_)


Return type:
    
None
generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Cube.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube.generate_points> "Link to this definition")
    
Creates the sides of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube").
Return type:
    
None
init_points()[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube.init_points> "Link to this definition")
    
Creates the sides of the `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube").
Return type:
    
None
[ Next Cylinder ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Cylinder.html>) [ Previous Cone ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Cone.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Cube](https://docs.manim.community/en/stable/reference/<#>)
    * `[Cube`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube>)
      * `[Cube._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube._original__init__>)
      * `[Cube.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube.generate_points>)
      * `[Cube.init_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Cube.init_points>)


