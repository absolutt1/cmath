# Prism[¶](https://docs.manim.community/en/stable/reference/<#prism> "Link to this heading")
Qualified name: `manim.mobject.three\_d.three\_dimensions.Prism`
_class_ Prism(_dimensions =[3, 2, 1]_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Prism>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism> "Link to this definition")
    
Bases: `[Cube`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Cube.html#manim.mobject.three_d.three_dimensions.Cube> "manim.mobject.three_d.three_dimensions.Cube")
A right rectangular prism (or rectangular cuboid). Defined by the length of each side in `[x, y, z]` format.
Parameters:
    
**dimensions** (_tuple_ _[__float_ _,__float_ _,__float_ _]__|__np.ndarray_) – Dimensions of the `[Prism`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism> "manim.mobject.three_d.three_dimensions.Prism") in `[x, y, z]` format.
Examples
Example: ExamplePrism [¶](https://docs.manim.community/en/stable/reference/<#exampleprism>)
![../_images/ExamplePrism-1.png](https://docs.manim.community/en/stable/_images/ExamplePrism-1.png)
```
frommanimimport *
classExamplePrism(ThreeDScene):
  defconstruct(self):
    self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
    prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
    prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
    self.add(prismSmall, prismLarge)

```
Copy to clipboard
Make interactive
Methods
`[generate_points`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism.generate_points> "manim.mobject.three_d.three_dimensions.Prism.generate_points") | Creates the sides of the `[Prism`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism> "manim.mobject.three_d.three_dimensions.Prism").  
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
_original__init__(_dimensions =[3, 2, 1]_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
**dimensions** (_tuple_ _[__float_ _,__float_ _,__float_ _]__|__ndarray_)
Return type:
    
None
generate_points()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/three_d/three_dimensions.html#Prism.generate_points>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism.generate_points> "Link to this definition")
    
Creates the sides of the `[Prism`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism> "manim.mobject.three_d.three_dimensions.Prism").
Return type:
    
None
[ Next Sphere ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Sphere.html>) [ Previous Line3D ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Line3D.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Prism](https://docs.manim.community/en/stable/reference/<#>)
    * `[Prism`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism>)
      * `[Prism._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism._original__init__>)
      * `[Prism.generate_points()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.three_d.three_dimensions.Prism.generate_points>)


