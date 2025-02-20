# LaggedStart[¶](https://docs.manim.community/en/stable/reference/<#laggedstart> "Link to this heading")
Qualified name: `manim.animation.composition.LaggedStart`
_class_ LaggedStart(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/composition.html#LaggedStart>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStart> "Link to this definition")
    
Bases: `[AnimationGroup`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup> "manim.animation.composition.AnimationGroup")
Adjusts the timing of a series of `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") according to `lag_ratio`.
Parameters:
    
  * **animations** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")) – Sequence of `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") objects to be played.
  * **lag_ratio** (_float_) – 
Defines the delay after which the animation is applied to submobjects. A lag_ratio of `n.nn` means the next animation will play when `nnn%` of the current animation has played. Defaults to 0.05, meaning that the next animation will begin when 5% of the current animation has played.
This does not influence the total runtime of the animation. Instead the runtime of individual animations is adjusted so that the complete animation has the defined run time.


Examples
Example: LaggedStartExample [¶](https://docs.manim.community/en/stable/reference/<#laggedstartexample>)
```
frommanimimport *
classLaggedStartExample(Scene):
  defconstruct(self):
    title = Text("lag_ratio = 0.25").to_edge(UP)
    dot1 = Dot(point=LEFT * 2 + UP, radius=0.16)
    dot2 = Dot(point=LEFT * 2, radius=0.16)
    dot3 = Dot(point=LEFT * 2 + DOWN, radius=0.16)
    line_25 = DashedLine(
      start=LEFT + UP * 2,
      end=LEFT + DOWN * 2,
      color=RED
    )
    label = Text("25%", font_size=24).next_to(line_25, UP)
    self.add(title, dot1, dot2, dot3, line_25, label)
    self.play(LaggedStart(
      dot1.animate.shift(RIGHT * 4),
      dot2.animate.shift(RIGHT * 4),
      dot3.animate.shift(RIGHT * 4),
      lag_ratio=0.25,
      run_time=4
    ))

```
Copy to clipboard
Make interactive
Methods
Attributes
`run_time`  
---  
_original__init__(_* animations_, _lag_ratio =0.05_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStart._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **animations** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation"))
  * **lag_ratio** (_float_)


[ Next LaggedStartMap ](https://docs.manim.community/en/stable/reference/<manim.animation.composition.LaggedStartMap.html>) [ Previous AnimationGroup ](https://docs.manim.community/en/stable/reference/<manim.animation.composition.AnimationGroup.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [LaggedStart](https://docs.manim.community/en/stable/reference/<#>)
    * `[LaggedStart`](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStart>)
      * `[LaggedStart._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.composition.LaggedStart._original__init__>)


