# Flash[¶](https://docs.manim.community/en/stable/reference/<#flash> "Link to this heading")
Qualified name: `manim.animation.indication.Flash`
_class_ Flash(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#Flash>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Flash> "Link to this definition")
    
Bases: `[AnimationGroup`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup> "manim.animation.composition.AnimationGroup")
Send out lines in all directions.
Parameters:
    
  * **point** (_np.ndarray_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The center of the flash lines. If it is a `Mobject` its center will be used.
  * **line_length** (_float_) – The length of the flash lines.
  * **num_lines** (_int_) – The number of flash lines.
  * **flash_radius** (_float_) – The distance from point at which the flash lines start.
  * **line_stroke_width** (_int_) – The stroke width of the flash lines.
  * **color** (_str_) – The color of the flash lines.
  * **time_width** (_float_) – The time width used for the flash lines. See `ShowPassingFlash` for more details.
  * **run_time** (_float_) – The duration of the animation.
  * **kwargs** – Additional arguments to be passed to the `[Succession`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.Succession.html#manim.animation.composition.Succession> "manim.animation.composition.Succession") constructor


Examples
Example: UsingFlash [¶](https://docs.manim.community/en/stable/reference/<#usingflash>)
```
frommanimimport *
classUsingFlash(Scene):
  defconstruct(self):
    dot = Dot(color=YELLOW).shift(DOWN)
    self.add(Tex("Flash the dot below:"), dot)
    self.play(Flash(dot))
    self.wait()

```
Copy to clipboard
Make interactive
Example: FlashOnCircle [¶](https://docs.manim.community/en/stable/reference/<#flashoncircle>)
```
frommanimimport *
classFlashOnCircle(Scene):
  defconstruct(self):
    radius = 2
    circle = Circle(radius)
    self.add(circle)
    self.play(Flash(
      circle, line_length=1,
      num_lines=30, color=RED,
      flash_radius=radius+SMALL_BUFF,
      time_width=0.3, run_time=2,
      rate_func = rush_from
    ))

```
Copy to clipboard
Make interactive
Methods
`create_line_anims`  
---  
`create_lines`  
Attributes
`run_time`  
---  
_original__init__(_point_ , _line_length =0.2_, _num_lines =12_, _flash_radius =0.1_, _line_stroke_width =3_, _color =ManimColor('#FFFF00')_, _time_width =1_, _run_time =1.0_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Flash._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **point** (_ndarray_ _|_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **line_length** (_float_)
  * **num_lines** (_int_)
  * **flash_radius** (_float_)
  * **line_stroke_width** (_int_)
  * **color** (_str_)
  * **time_width** (_float_)
  * **run_time** (_float_)


Return type:
    
None
[ Next FocusOn ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.FocusOn.html>) [ Previous Circumscribe ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Circumscribe.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Flash](https://docs.manim.community/en/stable/reference/<#>)
    * `[Flash`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Flash>)
      * `[Flash._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Flash._original__init__>)


