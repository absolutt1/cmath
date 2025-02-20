# Write[¶](https://docs.manim.community/en/stable/reference/<#write> "Link to this heading")
Qualified name: `manim.animation.creation.Write`
_class_ Write(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#Write>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write> "Link to this definition")
    
Bases: `[DrawBorderThenFill`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.DrawBorderThenFill.html#manim.animation.creation.DrawBorderThenFill> "manim.animation.creation.DrawBorderThenFill")
Simulate hand-writing a `[Text`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text") or hand-drawing a `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").
Examples
Example: ShowWrite [¶](https://docs.manim.community/en/stable/reference/<#showwrite>)
```
frommanimimport *
classShowWrite(Scene):
  defconstruct(self):
    self.play(Write(Text("Hello", font_size=144)))

```
Copy to clipboard
Make interactive
Example: ShowWriteReversed [¶](https://docs.manim.community/en/stable/reference/<#showwritereversed>)
```
frommanimimport *
classShowWriteReversed(Scene):
  defconstruct(self):
    self.play(Write(Text("Hello", font_size=144), reverse=True, remover=False))

```
Copy to clipboard
Make interactive
Tests
Check that creating empty `[Write`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write> "manim.animation.creation.Write") animations works:
```
>>> frommanimimport Write, Text
>>> Write(Text(''))
Write(Text(''))

```
Copy to clipboard
Methods
`[begin`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write.begin> "manim.animation.creation.Write.begin") | Begin the animation.  
---|---  
`[finish`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write.finish> "manim.animation.creation.Write.finish") | Finish the animation.  
`reverse_submobjects`  
Attributes
`run_time`  
---  
Parameters:
    
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **reverse** (_bool_)


_original__init__(_vmobject_ , _rate_func= <function linear>_, _reverse=False_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__OpenGLVMobject_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **reverse** (_bool_)


Return type:
    
None
begin()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#Write.begin>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write.begin> "Link to this definition")
    
Begin the animation.
This method is called right as an animation is being played. As much initialization as possible, especially any mobject copying, should live in this method.
Return type:
    
None
finish()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#Write.finish>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write.finish> "Link to this definition")
    
Finish the animation.
This method gets called when the animation is over.
Return type:
    
None
[ Next fading ](https://docs.manim.community/en/stable/reference/<manim.animation.fading.html>) [ Previous Unwrite ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Unwrite.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Write](https://docs.manim.community/en/stable/reference/<#>)
    * `[Write`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write>)
      * `[Write._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write._original__init__>)
      * `[Write.begin()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write.begin>)
      * `[Write.finish()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Write.finish>)


