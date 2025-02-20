# SurroundingRectangle[¶](https://docs.manim.community/en/stable/reference/<#surroundingrectangle> "Link to this heading")
Qualified name: `manim.mobject.geometry.shape\_matchers.SurroundingRectangle`
_class_ SurroundingRectangle(_* mobjects_, _color =ManimColor('#FFFF00')_, _buff =0.1_, _corner_radius =0.0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/shape_matchers.html#SurroundingRectangle>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.SurroundingRectangle> "Link to this definition")
    
Bases: `[RoundedRectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.RoundedRectangle.html#manim.mobject.geometry.polygram.RoundedRectangle> "manim.mobject.geometry.polygram.RoundedRectangle")
A rectangle surrounding a `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")
Examples
Example: SurroundingRectExample [¶](https://docs.manim.community/en/stable/reference/<#surroundingrectexample>)
![../_images/SurroundingRectExample-1.png](https://docs.manim.community/en/stable/_images/SurroundingRectExample-1.png)
```
frommanimimport *
classSurroundingRectExample(Scene):
  defconstruct(self):
    title = Title("A Quote from Newton")
    quote = Text(
      "If I have seen further than others, \n"
      "it is by standing upon the shoulders of giants.",
      color=BLUE,
    ).scale(0.75)
    box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)
    t2 = Tex(r"Hello World").scale(1.5)
    box2 = SurroundingRectangle(t2, corner_radius=0.2)
    mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
    self.add(title, mobjects)

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
Parameters:
    
  * **mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **buff** (_float_)
  * **corner_radius** (_float_)
  * **kwargs** (_Any_)


_original__init__(_* mobjects_, _color =ManimColor('#FFFF00')_, _buff =0.1_, _corner_radius =0.0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.SurroundingRectangle._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
  * **buff** (_float_)
  * **corner_radius** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next Underline ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.Underline.html>) [ Previous Cross ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.Cross.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [SurroundingRectangle](https://docs.manim.community/en/stable/reference/<#>)
    * `[SurroundingRectangle`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.SurroundingRectangle>)
      * `[SurroundingRectangle._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.SurroundingRectangle._original__init__>)


