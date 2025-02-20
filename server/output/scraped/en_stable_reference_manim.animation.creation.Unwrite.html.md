# Unwrite[¶](https://docs.manim.community/en/stable/reference/<#unwrite> "Link to this heading")
Qualified name: `manim.animation.creation.Unwrite`
_class_ Unwrite(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#Unwrite>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Unwrite> "Link to this definition")
    
Bases: `[Write`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Write.html#manim.animation.creation.Write> "manim.animation.creation.Write")
Simulate erasing by hand a `[Text`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text") or a `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").
Parameters:
    
  * **reverse** (_bool_) – Set True to have the animation start erasing from the last submobject first.
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)


Examples
Example: UnwriteReverseTrue [¶](https://docs.manim.community/en/stable/reference/<#unwritereversetrue>)
```
frommanimimport *
classUnwriteReverseTrue(Scene):
  defconstruct(self):
    text = Tex("Alice and Bob").scale(3)
    self.add(text)
    self.play(Unwrite(text))

```
Copy to clipboard
Make interactive
Example: UnwriteReverseFalse [¶](https://docs.manim.community/en/stable/reference/<#unwritereversefalse>)
```
frommanimimport *
classUnwriteReverseFalse(Scene):
  defconstruct(self):
    text = Tex("Alice and Bob").scale(3)
    self.add(text)
    self.play(Unwrite(text, reverse=False))

```
Copy to clipboard
Make interactive
Methods
Attributes
`run_time`  
---  
_original__init__(_vmobject_ , _rate_func= <function linear>_, _reverse=True_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Unwrite._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **vmobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **reverse** (_bool_)


Return type:
    
None
[ Next Write ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Write.html>) [ Previous UntypeWithCursor ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.UntypeWithCursor.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Unwrite](https://docs.manim.community/en/stable/reference/<#>)
    * `[Unwrite`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Unwrite>)
      * `[Unwrite._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.Unwrite._original__init__>)


