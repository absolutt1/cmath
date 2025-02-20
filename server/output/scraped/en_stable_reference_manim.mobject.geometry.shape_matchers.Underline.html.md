# Underline[¶](https://docs.manim.community/en/stable/reference/<#underline> "Link to this heading")
Qualified name: `manim.mobject.geometry.shape\_matchers.Underline`
_class_ Underline(_mobject_ , _buff =0.1_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/shape_matchers.html#Underline>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Underline> "Link to this definition")
    
Bases: `[Line`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.line.Line.html#manim.mobject.geometry.line.Line> "manim.mobject.geometry.line.Line")
Creates an underline.
Examples
Example: UnderLine [¶](https://docs.manim.community/en/stable/reference/<#underline>)
![../_images/UnderLine-1.png](https://docs.manim.community/en/stable/_images/UnderLine-1.png)
```
frommanimimport *
classUnderLine(Scene):
  defconstruct(self):
    man = Tex("Manim") # Full Word
    ul = Underline(man) # Underlining the word
    self.add(man, ul)

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
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **buff** (_float_)
  * **kwargs** (_Any_)


_original__init__(_mobject_ , _buff =0.1_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Underline._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **buff** (_float_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next tips ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.html>) [ Previous SurroundingRectangle ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.shape_matchers.SurroundingRectangle.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Underline](https://docs.manim.community/en/stable/reference/<#>)
    * `[Underline`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Underline>)
      * `[Underline._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.shape_matchers.Underline._original__init__>)


