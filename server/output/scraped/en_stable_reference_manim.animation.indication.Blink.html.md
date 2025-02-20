# Blink[¶](https://docs.manim.community/en/stable/reference/<#blink> "Link to this heading")
Qualified name: `manim.animation.indication.Blink`
_class_ Blink(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#Blink>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Blink> "Link to this definition")
    
Bases: `[Succession`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.Succession.html#manim.animation.composition.Succession> "manim.animation.composition.Succession")
Blink the mobject.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject to be blinked.
  * **time_on** (_float_) – The duration that the mobject is shown for one blink.
  * **time_off** (_float_) – The duration that the mobject is hidden for one blink.
  * **blinks** (_int_) – The number of blinks
  * **hide_at_end** (_bool_) – Whether to hide the mobject at the end of the animation.
  * **kwargs** – Additional arguments to be passed to the `[Succession`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.Succession.html#manim.animation.composition.Succession> "manim.animation.composition.Succession") constructor.


Examples
Example: BlinkingExample [¶](https://docs.manim.community/en/stable/reference/<#blinkingexample>)
```
frommanimimport *
classBlinkingExample(Scene):
  defconstruct(self):
    text = Text("Blinking").scale(1.5)
    self.add(text)
    self.play(Blink(text, blinks=3))

```
Copy to clipboard
Make interactive
Methods
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _time_on =0.5_, _time_off =0.5_, _blinks =1_, _hide_at_end =False_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Blink._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **time_on** (_float_)
  * **time_off** (_float_)
  * **blinks** (_int_)
  * **hide_at_end** (_bool_)


[ Next Circumscribe ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Circumscribe.html>) [ Previous ApplyWave ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.ApplyWave.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Blink](https://docs.manim.community/en/stable/reference/<#>)
    * `[Blink`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Blink>)
      * `[Blink._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.Blink._original__init__>)


