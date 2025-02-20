# Brace[¶](https://docs.manim.community/en/stable/reference/<#brace> "Link to this heading")
Qualified name: `manim.mobject.svg.brace.Brace`
_class_ Brace(_mobject_ , _direction =array([0., -1., 0.])_, _buff =0.2_, _sharpness =2_, _stroke_width =0_, _fill_opacity =1.0_, _background_stroke_width =0_, _background_stroke_color =ManimColor('#000000')_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#Brace>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace> "Link to this definition")
    
Bases: `[VMobjectFromSVGPath`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.VMobjectFromSVGPath.html#manim.mobject.svg.svg_mobject.VMobjectFromSVGPath> "manim.mobject.svg.svg_mobject.VMobjectFromSVGPath")
Takes a mobject and draws a brace adjacent to it.
Passing a direction vector determines the direction from which the brace is drawn. By default it is drawn from below.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject adjacent to which the brace is placed.
  * **direction** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D") _|__None_) – The direction from which the brace faces the mobject.
  * **buff** (_float_)
  * **sharpness** (_float_)
  * **stroke_width** (_float_)
  * **fill_opacity** (_float_)
  * **background_stroke_width** (_float_)
  * **background_stroke_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))


See also
`[BraceBetweenPoints`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.BraceBetweenPoints.html#manim.mobject.svg.brace.BraceBetweenPoints> "manim.mobject.svg.brace.BraceBetweenPoints")
Examples
Example: BraceExample [¶](https://docs.manim.community/en/stable/reference/<#braceexample>)
![../_images/BraceExample-1.png](https://docs.manim.community/en/stable/_images/BraceExample-1.png)
```
frommanimimport *
classBraceExample(Scene):
  defconstruct(self):
    s = Square()
    self.add(s)
    for i in np.linspace(0.1,1.0,4):
      br = Brace(s, sharpness=i)
      t = Text(f"sharpness= {i}").next_to(br, RIGHT)
      self.add(t)
      self.add(br)
    VGroup(*self.mobjects).arrange(DOWN, buff=0.2)

```
Copy to clipboard
Make interactive
Methods
`[get_direction`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_direction> "manim.mobject.svg.brace.Brace.get_direction") | Returns the direction from the center to the brace tip.  
---|---  
`[get_tex`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_tex> "manim.mobject.svg.brace.Brace.get_tex") | Places the tex at the brace tip.  
`[get_text`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_text> "manim.mobject.svg.brace.Brace.get_text") | Places the text at the brace tip.  
`[get_tip`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_tip> "manim.mobject.svg.brace.Brace.get_tip") | Returns the point at the brace tip.  
`[put_at_tip`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.put_at_tip> "manim.mobject.svg.brace.Brace.put_at_tip") | Puts the given mobject at the brace tip.  
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
_original__init__(_mobject_ , _direction =array([0., -1., 0.])_, _buff =0.2_, _sharpness =2_, _stroke_width =0_, _fill_opacity =1.0_, _background_stroke_width =0_, _background_stroke_color =ManimColor('#000000')_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **direction** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D") _|__None_)
  * **buff** (_float_)
  * **sharpness** (_float_)
  * **stroke_width** (_float_)
  * **fill_opacity** (_float_)
  * **background_stroke_width** (_float_)
  * **background_stroke_color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))


get_direction()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#Brace.get_direction>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_direction> "Link to this definition")
    
Returns the direction from the center to the brace tip.
get_tex(_* tex_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#Brace.get_tex>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_tex> "Link to this definition")
    
Places the tex at the brace tip.
Parameters:
    
  * **tex** – The tex to be placed at the brace tip.
  * **kwargs** – Any further keyword arguments are passed to `[put_at_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.put_at_tip> "manim.mobject.svg.brace.Brace.put_at_tip") which is used to position the tex at the brace tip.


Return type:
    
`[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex")
get_text(_* text_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#Brace.get_text>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_text> "Link to this definition")
    
Places the text at the brace tip.
Parameters:
    
  * **text** – The text to be placed at the brace tip.
  * **kwargs** – Any additional keyword arguments are passed to `[put_at_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.put_at_tip> "manim.mobject.svg.brace.Brace.put_at_tip") which is used to position the text at the brace tip.


Return type:
    
`[Tex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex")
get_tip()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#Brace.get_tip>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_tip> "Link to this definition")
    
Returns the point at the brace tip.
put_at_tip(_mob_ , _use_next_to =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#Brace.put_at_tip>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.put_at_tip> "Link to this definition")
    
Puts the given mobject at the brace tip.
Parameters:
    
  * **mob** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to be placed at the tip.
  * **use_next_to** (_bool_) – If true, then `next_to()` is used to place the mobject at the tip.
  * **kwargs** – Any additional keyword arguments are passed to `next_to()` which is used to put the mobject next to the brace tip.


[ Next BraceBetweenPoints ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.BraceBetweenPoints.html>) [ Previous ArcBrace ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.ArcBrace.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Brace](https://docs.manim.community/en/stable/reference/<#>)
    * `[Brace`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace>)
      * `[Brace._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace._original__init__>)
      * `[Brace.get_direction()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_direction>)
      * `[Brace.get_tex()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_tex>)
      * `[Brace.get_text()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_text>)
      * `[Brace.get_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.get_tip>)
      * `[Brace.put_at_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.Brace.put_at_tip>)


