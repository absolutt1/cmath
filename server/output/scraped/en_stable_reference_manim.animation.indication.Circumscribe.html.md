# Circumscribe[¶](https://docs.manim.community/en/stable/reference/<#circumscribe> "Link to this heading")
Qualified name: `manim.animation.indication.Circumscribe`
_class_ Circumscribe(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#Circumscribe>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Circumscribe> "Link to this definition")
    
Bases: `[Succession`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.Succession.html#manim.animation.composition.Succession> "manim.animation.composition.Succession")
Draw a temporary line surrounding the mobject.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to be circumscribed.
  * **shape** (_type_) – The shape with which to surround the given mobject. Should be either `[Rectangle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.polygram.Rectangle.html#manim.mobject.geometry.polygram.Rectangle> "manim.mobject.geometry.polygram.Rectangle") or `[Circle`](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Circle.html#manim.mobject.geometry.arc.Circle> "manim.mobject.geometry.arc.Circle")
  * **fade_in** – Whether to make the surrounding shape to fade in. It will be drawn otherwise.
  * **fade_out** – Whether to make the surrounding shape to fade out. It will be undrawn otherwise.
  * **time_width** – The time_width of the drawing and undrawing. Gets ignored if either fade_in or fade_out is True.
  * **buff** (_float_) – The distance between the surrounding shape and the given mobject.
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor")) – The color of the surrounding shape.
  * **run_time** – The duration of the entire animation.
  * **kwargs** – Additional arguments to be passed to the `[Succession`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.Succession.html#manim.animation.composition.Succession> "manim.animation.composition.Succession") constructor


Examples
Example: UsingCircumscribe [¶](https://docs.manim.community/en/stable/reference/<#usingcircumscribe>)
```
frommanimimport *
classUsingCircumscribe(Scene):
  defconstruct(self):
    lbl = Tex(r"Circum-\\scribe").scale(2)
    self.add(lbl)
    self.play(Circumscribe(lbl))
    self.play(Circumscribe(lbl, Circle))
    self.play(Circumscribe(lbl, fade_out=True))
    self.play(Circumscribe(lbl, time_width=2))
    self.play(Circumscribe(lbl, Circle, True))

```
Copy to clipboard
Make interactive
Methods
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _shape= <class 'manim.mobject.geometry.polygram.Rectangle'>_, _fade_in=False_ , _fade_out=False_ , _time_width=0.3_ , _buff=0.1_ , _color=ManimColor('#FFFF00')_ , _run_time=1_ , _stroke_width=4_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Circumscribe._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **shape** (_type_)
  * **buff** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))


[ Next Flash ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Flash.html>) [ Previous Blink ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Blink.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Circumscribe](https://docs.manim.community/en/stable/reference/<#>)
    * `[Circumscribe`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Circumscribe>)
      * `[Circumscribe._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Circumscribe._original__init__>)


