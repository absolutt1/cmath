# UntypeWithCursor[¶](https://docs.manim.community/en/stable/reference/<#untypewithcursor> "Link to this heading")
Qualified name: `manim.animation.creation.UntypeWithCursor`
_class_ UntypeWithCursor(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/creation.html#UntypeWithCursor>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.UntypeWithCursor> "Link to this definition")
    
Bases: `[TypeWithCursor`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.TypeWithCursor.html#manim.animation.creation.TypeWithCursor> "manim.animation.creation.TypeWithCursor")
Similar to `[RemoveTextLetterByLetter`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.RemoveTextLetterByLetter.html#manim.animation.creation.RemoveTextLetterByLetter> "manim.animation.creation.RemoveTextLetterByLetter") , but with an additional cursor mobject at the end.
Parameters:
    
  * **time_per_char** (_float_) – Frequency of appearance of the letters.
  * **cursor** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__None_) – `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") shown after the last added letter.
  * **buff** – Controls how far away the cursor is to the right of the last added letter.
  * **keep_cursor_y** – If `True`, the cursor’s y-coordinate is set to the center of the `Text` and remains the same throughout the animation. Otherwise, it is set to the center of the last added letter.
  * **leave_cursor_on** – Whether to show the cursor after the animation.
  * **tip::** (_.._) – This is currently only possible for class:~.Text and not for class:~.MathTex.
  * **text** ([_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text"))


Examples
Example: DeletingTextExample [¶](https://docs.manim.community/en/stable/reference/<#deletingtextexample>)
```
frommanimimport *
classDeletingTextExample(Scene):
  defconstruct(self):
    text = Text("Deleting", color=PURPLE).scale(1.5).to_edge(LEFT)
    cursor = Rectangle(
      color = GREY_A,
      fill_color = GREY_A,
      fill_opacity = 1.0,
      height = 1.1,
      width = 0.5,
    ).move_to(text[0]) # Position the cursor
    self.play(UntypeWithCursor(text, cursor))
    self.play(Blink(cursor, blinks=2))

```
Copy to clipboard
Make interactive
References: `[Blink`](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Blink.html#manim.animation.indication.Blink> "manim.animation.indication.Blink")
Methods
Attributes
`run_time`  
---  
_original__init__(_text_ , _cursor =None_, _time_per_char =0.1_, _reverse_rate_function =True_, _introducer =False_, _remover =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.UntypeWithCursor._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **text** ([_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text"))
  * **cursor** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject") _|__None_)
  * **time_per_char** (_float_)


Return type:
    
None
[ Next Unwrite ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Unwrite.html>) [ Previous Uncreate ](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Uncreate.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [UntypeWithCursor](https://docs.manim.community/en/stable/reference/<#>)
    * `[UntypeWithCursor`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.UntypeWithCursor>)
      * `[UntypeWithCursor._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.creation.UntypeWithCursor._original__init__>)


