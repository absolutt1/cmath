# SpiralIn[¶](https://docs.manim.community/en/stable/reference/<#spiralin> "Link to this heading")
Qualified name: `manim.animation.creation.SpiralIn`
_class_ SpiralIn(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#SpiralIn>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.SpiralIn> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
Create the Mobject with sub-Mobjects flying in on spiral trajectories.
Parameters:
    
  * **shapes** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The Mobject on which to be operated.
  * **scale_factor** (_float_) – The factor used for scaling the effect.
  * **fade_in_fraction** – Fractional duration of initial fade-in of sub-Mobjects as they fly inward.


Examples
Example: SpiralInExample [¶](https://docs.manim.community/en/stable/reference/<#spiralinexample>)
```
frommanimimport *
classSpiralInExample(Scene):
  defconstruct(self):
    pi = MathTex(r"\pi").scale(7)
    pi.shift(2.25 * LEFT + 1.5 * UP)
    circle = Circle(color=GREEN_C, fill_opacity=1).shift(LEFT)
    square = Square(color=BLUE_D, fill_opacity=1).shift(UP)
    shapes = VGroup(pi, circle, square)
    self.play(SpiralIn(shapes))

```
Copy to clipboard
Make interactive
Methods
`[interpolate_mobject`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.SpiralIn.interpolate_mobject> "manim.animation.creation.SpiralIn.interpolate_mobject") | Interpolates the mobject of the `Animation` based on alpha value.  
---|---  
Attributes
`run_time`  
---  
_original__init__(_shapes_ , _scale_factor =8_, _fade_in_fraction =0.3_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.SpiralIn._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **shapes** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **scale_factor** (_float_)


Return type:
    
None
interpolate_mobject(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#SpiralIn.interpolate_mobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.SpiralIn.interpolate_mobject> "Link to this definition")
    
Interpolates the mobject of the `Animation` based on alpha value.
Parameters:
    
**alpha** (_float_) – A float between 0 and 1 expressing the ratio to which the animation is completed. For example, alpha-values of 0, 0.5, and 1 correspond to the animation being completed 0%, 50%, and 100%, respectively.
Return type:
    
None
[ Next TypeWithCursor ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.TypeWithCursor.html>) [ Previous ShowSubmobjectsOneByOne ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.ShowSubmobjectsOneByOne.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [SpiralIn](https://docs.manim.community/en/stable/reference/<#>)
    * `[SpiralIn`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.SpiralIn>)
      * `[SpiralIn._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.SpiralIn._original__init__>)
      * `[SpiralIn.interpolate_mobject()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.SpiralIn.interpolate_mobject>)


