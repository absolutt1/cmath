# Cutout[¶](https://docs.manim.community/en/stable/reference/<#cutout> "Link to this heading")
Qualified name: `manim.mobject.geometry.polygram.Cutout`
_class_ Cutout(_main_shape_ , _* mobjects_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/polygram.html#Cutout>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Cutout> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A shape with smaller cutouts.
Parameters:
    
  * **main_shape** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The primary shape from which cutouts are made.
  * **mobjects** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The smaller shapes which are to be cut out of the `main_shape`.
  * **kwargs** (_Any_) – Further keyword arguments that are passed to the constructor of `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").


Warning
Technically, this class behaves similar to a symmetric difference: if parts of the `mobjects` are not located within the `main_shape`, these parts will be added to the resulting `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").
Examples
Example: CutoutExample [¶](https://docs.manim.community/en/stable/reference/<#cutoutexample>)
```
frommanimimport *
classCutoutExample(Scene):
  defconstruct(self):
    s1 = Square().scale(2.5)
    s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
    s3 = Square().shift(UP + RIGHT).scale(0.5)
    s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
    s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
    c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
    self.play(Write(c), run_time=4)
    self.wait()

```
Copy to clipboard
Make interactive
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
_original__init__(_main_shape_ , _* mobjects_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Cutout._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **main_shape** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **mobjects** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Polygon ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Polygon.html>) [ Previous ConvexHull ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.ConvexHull.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Cutout](https://docs.manim.community/en/stable/reference/<#>)
    * `[Cutout`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Cutout>)
      * `[Cutout._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.polygram.Cutout._original__init__>)


