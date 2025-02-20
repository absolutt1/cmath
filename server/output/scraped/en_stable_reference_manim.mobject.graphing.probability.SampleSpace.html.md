# SampleSpace[¶](https://docs.manim.community/en/stable/reference/<#samplespace> "Link to this heading")
Qualified name: `manim.mobject.graphing.probability.SampleSpace`
_class_ SampleSpace(_height =3_, _width =3_, _fill_color =ManimColor('#444444')_, _fill_opacity =1_, _stroke_width =0.5_, _stroke_color =ManimColor('#BBBBBB')_, _default_label_scale_val =1_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/graphing/probability.html#SampleSpace>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.probability.SampleSpace> "Link to this definition")
    
Bases: `[Rectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle> "manim.mobject.geometry.polygram.Rectangle")
A mobject representing a twodimensional rectangular sampling space.
Examples
Example: ExampleSampleSpace [¶](https://docs.manim.community/en/stable/reference/<#examplesamplespace>)
![../_images/ExampleSampleSpace-1.png](https://docs.manim.community/en/stable/_images/ExampleSampleSpace-1.png)
```
frommanimimport *
classExampleSampleSpace(Scene):
  defconstruct(self):
    poly1 = SampleSpace(stroke_width=15, fill_opacity=1)
    poly2 = SampleSpace(width=5, height=3, stroke_width=5, fill_opacity=0.5)
    poly3 = SampleSpace(width=2, height=2, stroke_width=5, fill_opacity=0.1)
    poly3.divide_vertically(p_list=np.array([0.37, 0.13, 0.5]), colors=[BLACK, WHITE, GRAY], vect=RIGHT)
    poly_group = VGroup(poly1, poly2, poly3).arrange()
    self.add(poly_group)

```
Copy to clipboard
Make interactive
Methods
`add_braces_and_labels`  
---  
`add_label`  
`add_title`  
`complete_p_list`  
`divide_horizontally`  
`divide_vertically`  
`get_bottom_braces_and_labels`  
`get_division_along_dimension`  
`get_horizontal_division`  
`get_side_braces_and_labels`  
`get_subdivision_braces_and_labels`  
`get_top_braces_and_labels`  
`get_vertical_division`  
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
_original__init__(_height =3_, _width =3_, _fill_color =ManimColor('#444444')_, _fill_opacity =1_, _stroke_width =0.5_, _stroke_color =ManimColor('#BBBBBB')_, _default_label_scale_val =1_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.probability.SampleSpace._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
[ Next scale ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.scale.html>) [ Previous BarChart ](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.probability.BarChart.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [SampleSpace](https://docs.manim.community/en/stable/reference/<#>)
    * `[SampleSpace`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.probability.SampleSpace>)
      * `[SampleSpace._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.graphing.probability.SampleSpace._original__init__>)


