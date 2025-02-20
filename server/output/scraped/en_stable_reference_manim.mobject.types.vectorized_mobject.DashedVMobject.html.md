# DashedVMobject[¶](https://docs.manim.community/en/stable/reference/<#dashedvmobject> "Link to this heading")
Qualified name: `manim.mobject.types.vectorized\_mobject.DashedVMobject`
_class_ DashedVMobject(_vmobject_ , _num_dashes =15_, _dashed_ratio =0.5_, _dash_offset =0_, _color =ManimColor('#FFFFFF')_, _equal_lengths =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/types/vectorized_mobject.html#DashedVMobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.vectorized_mobject.DashedVMobject> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") composed of dashes instead of lines.
Parameters:
    
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The object that will get dashed
  * **num_dashes** (_int_) – Number of dashes to add.
  * **dashed_ratio** (_float_) – Ratio of dash to empty space.
  * **dash_offset** (_float_) – Shifts the starting point of dashes along the path. Value 1 shifts by one full dash length.
  * **equal_lengths** (_bool_) – If `True`, dashes will be (approximately) equally long. If `False`, dashes will be split evenly in the curve’s input t variable (legacy behavior).
  * **color** ([_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor"))


Examples
Example: DashedVMobjectExample [¶](https://docs.manim.community/en/stable/reference/<#dashedvmobjectexample>)
![../_images/DashedVMobjectExample-1.png](https://docs.manim.community/en/stable/_images/DashedVMobjectExample-1.png)
```
frommanimimport *
classDashedVMobjectExample(Scene):
  defconstruct(self):
    r = 0.5
    top_row = VGroup() # Increasing num_dashes
    for dashes in range(1, 12):
      circ = DashedVMobject(Circle(radius=r, color=WHITE), num_dashes=dashes)
      top_row.add(circ)
    middle_row = VGroup() # Increasing dashed_ratio
    for ratio in np.arange(1 / 11, 1, 1 / 11):
      circ = DashedVMobject(
        Circle(radius=r, color=WHITE), dashed_ratio=ratio
      )
      middle_row.add(circ)
    func1 = FunctionGraph(lambda t: t**5,[-1,1],color=WHITE)
    func_even = DashedVMobject(func1,num_dashes=6,equal_lengths=True)
    func_stretched = DashedVMobject(func1, num_dashes=6, equal_lengths=False)
    bottom_row = VGroup(func_even,func_stretched)
    top_row.arrange(buff=0.3)
    middle_row.arrange()
    bottom_row.arrange(buff=1)
    everything = VGroup(top_row, middle_row, bottom_row).arrange(DOWN, buff=1)
    self.add(everything)

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
_original__init__(_vmobject_ , _num_dashes =15_, _dashed_ratio =0.5_, _dash_offset =0_, _color =ManimColor('#FFFFFF')_, _equal_lengths =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.vectorized_mobject.DashedVMobject._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **num_dashes** (_int_)
  * **dashed_ratio** (_float_)
  * **dash_offset** (_float_)
  * **color** ([_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor"))
  * **equal_lengths** (_bool_)


Return type:
    
None
[ Next VDict ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VDict.html>) [ Previous CurvesAsSubmobjects ](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.CurvesAsSubmobjects.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DashedVMobject](https://docs.manim.community/en/stable/reference/<#>)
    * `[DashedVMobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.vectorized_mobject.DashedVMobject>)
      * `[DashedVMobject._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.types.vectorized_mobject.DashedVMobject._original__init__>)


