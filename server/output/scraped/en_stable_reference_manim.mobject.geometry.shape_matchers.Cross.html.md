# Cross[¶](https://docs.manim.community/en/stable/reference/<#cross> "Link to this heading")
Qualified name: `manim.mobject.geometry.shape\_matchers.Cross`
_class_ Cross(_mobject =None_, _stroke_color =ManimColor('#FC6255')_, _stroke_width =6.0_, _scale_factor =1.0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/shape_matchers.html#Cross>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Cross> "Link to this definition")
    
Bases: `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
Creates a cross.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__None_) – The mobject linked to this instance. It fits the mobject when specified. Defaults to None.
  * **stroke_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – Specifies the color of the cross lines. Defaults to RED.
  * **stroke_width** (_float_) – Specifies the width of the cross lines. Defaults to 6.
  * **scale_factor** (_float_) – Scales the cross to the provided units. Defaults to 1.
  * **kwargs** (_Any_)


Examples
Example: ExampleCross [¶](https://docs.manim.community/en/stable/reference/<#examplecross>)
![../_images/ExampleCross-1.png](https://docs.manim.community/en/stable/_images/ExampleCross-1.png)
```
frommanimimport *
classExampleCross(Scene):
  defconstruct(self):
    cross = Cross()
    self.add(cross)

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
_original__init__(_mobject =None_, _stroke_color =ManimColor('#FC6255')_, _stroke_width =6.0_, _scale_factor =1.0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Cross._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__None_)
  * **stroke_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **stroke_width** (_float_)
  * **scale_factor** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next SurroundingRectangle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.SurroundingRectangle.html>) [ Previous BackgroundRectangle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.BackgroundRectangle.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Cross](https://docs.manim.community/en/stable/reference/<#>)
    * `[Cross`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Cross>)
      * `[Cross._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Cross._original__init__>)


