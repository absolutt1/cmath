# DrawBorderThenFill[¶](https://docs.manim.community/en/stable/reference/<#drawborderthenfill> "Link to this heading")
Qualified name: `manim.animation.creation.DrawBorderThenFill`
_class_ DrawBorderThenFill(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#DrawBorderThenFill>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Draw the border first and then show the fill.
Examples
Example: ShowDrawBorderThenFill [¶](https://docs.manim.community/en/stable/reference/<#showdrawborderthenfill>)
```
frommanimimport *
classShowDrawBorderThenFill(Scene):
  defconstruct(self):
    self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))

```
Copy to clipboard
Make interactive
Methods
`[begin`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill.begin> "manim.animation.creation.DrawBorderThenFill.begin") | Begin the animation.  
---|---  
`[get_all_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill.get_all_mobjects> "manim.animation.creation.DrawBorderThenFill.get_all_mobjects") | Get all mobjects involved in the animation.  
`get_outline`  
`get_stroke_color`  
`interpolate_submobject`  
Attributes
`run_time`  
---  
Parameters:
    
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_)
  * **run_time** (_float_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **stroke_width** (_float_)
  * **stroke_color** (_str_)
  * **draw_border_animation_config** (_dict_)
  * **fill_animation_config** (_dict_)
  * **introducer** (_bool_)


_original__init__(_vmobject_ , _run_time=2_ , _rate_func= <function double_smooth>_, _stroke_width=2_ , _stroke_color=None_ , _draw_border_animation_config={}_ , _fill_animation_config={}_ , _introducer=True_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_)
  * **run_time** (_float_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **stroke_width** (_float_)
  * **stroke_color** (_str_)
  * **draw_border_animation_config** (_dict_)
  * **fill_animation_config** (_dict_)
  * **introducer** (_bool_)


Return type:
    
None
begin()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#DrawBorderThenFill.begin>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill.begin> "Link to this definition")
    
Begin the animation.
This method is called right as an animation is being played. As much initialization as possible, especially any mobject copying, should live in this method.
Return type:
    
None
get_all_mobjects()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#DrawBorderThenFill.get_all_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill.get_all_mobjects> "Link to this definition")
    
Get all mobjects involved in the animation.
Ordering must match the ordering of arguments to interpolate_submobject
Returns:
    
The sequence of mobjects.
Return type:
    
Sequence[[Mobject](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")]
[ Next RemoveTextLetterByLetter ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.RemoveTextLetterByLetter.html>) [ Previous Create ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Create.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DrawBorderThenFill](https://docs.manim.community/en/stable/reference/<#>)
    * `[DrawBorderThenFill`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill>)
      * `[DrawBorderThenFill._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill._original__init__>)
      * `[DrawBorderThenFill.begin()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill.begin>)
      * `[DrawBorderThenFill.get_all_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.DrawBorderThenFill.get_all_mobjects>)


