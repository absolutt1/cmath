# ChangingDecimal[¶](https://docs.manim.community/en/stable/reference/<#changingdecimal> "Link to this heading")
Qualified name: `manim.animation.numbers.ChangingDecimal`
_class_ ChangingDecimal(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/numbers.html#ChangingDecimal>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.numbers.ChangingDecimal> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Methods
`check_validity_of_input`  
---  
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.numbers.ChangingDecimal.interpolate_mobject> "manim.animation.numbers.ChangingDecimal.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
Attributes
`run_time`  
---  
Parameters:
    
  * **decimal_mob** ([_DecimalNumber_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber"))
  * **number_update_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **suspend_mobject_updating** (_bool_ _|__None_)


_original__init__(_decimal_mob_ , _number_update_func_ , _suspend_mobject_updating =False_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.numbers.ChangingDecimal._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **decimal_mob** ([_DecimalNumber_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.DecimalNumber.html#manim.mobject.text.numbers.DecimalNumber> "manim.mobject.text.numbers.DecimalNumber"))
  * **number_update_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)
  * **suspend_mobject_updating** (_bool_ _|__None_)


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/numbers.html#ChangingDecimal.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.numbers.ChangingDecimal.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next rotation ](https://docs.manim.community/en/stable/reference/<manim.animation.rotation.html>) [ Previous ChangeDecimalToValue ](https://docs.manim.community/en/stable/reference/<manim.animation.numbers.ChangeDecimalToValue.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ChangingDecimal](https://docs.manim.community/en/stable/reference/<#>)
    * `[ChangingDecimal`](https://docs.manim.community/en/stable/reference/<#manim.animation.numbers.ChangingDecimal>)
      * `[ChangingDecimal._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.numbers.ChangingDecimal._original__init__>)
      * `[ChangingDecimal.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.numbers.ChangingDecimal.interpolate_mobject>)


