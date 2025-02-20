# AddTextLetterByLetter[¶](https://docs.manim.community/en/stable/reference/<#addtextletterbyletter> "Link to this heading")
Qualified name: `manim.animation.creation.AddTextLetterByLetter`
_class_ AddTextLetterByLetter(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#AddTextLetterByLetter>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.AddTextLetterByLetter> "Link to this definition")
    
Bases: `[ShowIncreasingSubsets`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.ShowIncreasingSubsets.html#manim.animation.creation.ShowIncreasingSubsets> "manim.animation.creation.ShowIncreasingSubsets")
Show a `[Text`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text") letter by letter on the scene.
Parameters:
    
  * **time_per_char** (_float_) – Frequency of appearance of the letters.
  * **tip::** (_.._) – This is currently only possible for class:~.Text and not for class:~.MathTex
  * **text** ([_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text"))
  * **suspend_mobject_updating** (_bool_)
  * **int_func** (_Callable_ _[__[__np.ndarray_ _]__,__np.ndarray_ _]_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **run_time** (_float_ _|__None_)


Methods
Attributes
`run_time`  
---  
_original__init__(_text_ , _suspend_mobject_updating=False_ , _int_func= <ufunc 'ceil'>_, _rate_func= <function linear>_, _time_per_char=0.1_ , _run_time=None_ , _reverse_rate_function=False_ , _introducer=True_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.AddTextLetterByLetter._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **text** ([_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text"))
  * **suspend_mobject_updating** (_bool_)
  * **int_func** (_Callable_ _[__[__np.ndarray_ _]__,__np.ndarray_ _]_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **time_per_char** (_float_)
  * **run_time** (_float_ _|__None_)


Return type:
    
None
[ Next AddTextWordByWord ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.AddTextWordByWord.html>) [ Previous creation ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [AddTextLetterByLetter](https://docs.manim.community/en/stable/reference/<#>)
    * `[AddTextLetterByLetter`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.AddTextLetterByLetter>)
      * `[AddTextLetterByLetter._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.AddTextLetterByLetter._original__init__>)


