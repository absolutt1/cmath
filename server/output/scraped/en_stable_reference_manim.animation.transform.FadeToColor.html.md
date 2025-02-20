# FadeToColor[¶](https://docs.manim.community/en/stable/reference/<#fadetocolor> "Link to this heading")
Qualified name: `manim.animation.transform.FadeToColor`
_class_ FadeToColor(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#FadeToColor>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.FadeToColor> "Link to this definition")
    
Bases: `[ApplyMethod`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.ApplyMethod.html#manim.animation.transform.ApplyMethod> "manim.animation.transform.ApplyMethod")
Animation that changes color of a mobject.
Examples
Example: FadeToColorExample [¶](https://docs.manim.community/en/stable/reference/<#fadetocolorexample>)
```
frommanimimport *
classFadeToColorExample(Scene):
  defconstruct(self):
    self.play(FadeToColor(Text("Hello World!"), color=RED))

```
Copy to clipboard
Make interactive
Methods
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **color** (_str_)


_original__init__(_mobject_ , _color_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.FadeToColor._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **color** (_str_)


Return type:
    
None
[ Next FadeTransform ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.FadeTransform.html>) [ Previous CyclicReplace ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.CyclicReplace.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [FadeToColor](https://docs.manim.community/en/stable/reference/<#>)
    * `[FadeToColor`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.FadeToColor>)
      * `[FadeToColor._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.FadeToColor._original__init__>)


