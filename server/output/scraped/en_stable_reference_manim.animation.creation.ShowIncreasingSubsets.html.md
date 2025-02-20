# ShowIncreasingSubsets[¶](https://docs.manim.community/en/stable/reference/<#showincreasingsubsets> "Link to this heading")
Qualified name: `manim.animation.creation.ShowIncreasingSubsets`
_class_ ShowIncreasingSubsets(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#ShowIncreasingSubsets>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.ShowIncreasingSubsets> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Show one submobject at a time, leaving all previous ones displayed on screen.
Examples
Example: ShowIncreasingSubsetsScene [¶](https://docs.manim.community/en/stable/reference/<#showincreasingsubsetsscene>)
```
frommanimimport *
classShowIncreasingSubsetsScene(Scene):
  defconstruct(self):
    p = VGroup(Dot(), Square(), Triangle())
    self.add(p)
    self.play(ShowIncreasingSubsets(p))
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject> "manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
---|---  
`update_submobject_list`  
Attributes
`run_time`  
---  
Parameters:
    
  * **group** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **suspend_mobject_updating** (_bool_)
  * **int_func** (_Callable_ _[__[__np.ndarray_ _]__,__np.ndarray_ _]_)


_original__init__(_group_ , _suspend_mobject_updating=False_ , _int_func= <ufunc 'floor'>_, _reverse_rate_function=False_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.ShowIncreasingSubsets._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **group** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **suspend_mobject_updating** (_bool_)
  * **int_func** (_Callable_ _[__[__ndarray_ _]__,__ndarray_ _]_)


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#ShowIncreasingSubsets.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next ShowPartial ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.ShowPartial.html>) [ Previous RemoveTextLetterByLetter ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.RemoveTextLetterByLetter.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ShowIncreasingSubsets](https://docs.manim.community/en/stable/reference/<#>)
    * `[ShowIncreasingSubsets`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.ShowIncreasingSubsets>)
      * `[ShowIncreasingSubsets._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.ShowIncreasingSubsets._original__init__>)
      * `[ShowIncreasingSubsets.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.ShowIncreasingSubsets.interpolate_mobject>)


