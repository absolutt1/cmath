# Label[¶](https://docs.manim.community/en/stable/reference/<#label> "Link to this heading")
Qualified name: `manim.mobject.geometry.labeled.Label`
_class_ Label(_label_ , _label_config =None_, _box_config =None_, _frame_config =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/labeled.html#Label>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.Label> "Link to this definition")
    
Bases: `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
A Label consisting of text surrounded by a frame.
Parameters:
    
  * **label** (_str_ _|_[_Tex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex") _|_[_MathTex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") _|_[_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text")) – Label that will be displayed.
  * **label_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – A dictionary containing the configuration for the label. This is only applied if `label` is of type `str`.
  * **box_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – A dictionary containing the configuration for the background box.
  * **frame_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – A dictionary containing the configuration for the frame.
  * **kwargs** (_Any_)


Examples
Example: LabelExample [¶](https://docs.manim.community/en/stable/reference/<#labelexample>)
![../_images/LabelExample-1.png](https://docs.manim.community/en/stable/_images/LabelExample-1.png)
```
frommanimimport *
classLabelExample(Scene):
  defconstruct(self):
    label = Label(
      label=Text('Label Text', font='sans-serif'),
      box_config = {
        "color" : BLUE,
        "fill_opacity" : 0.75
      }
    )
    label.scale(3)
    self.add(label)

```
Copy to clipboard
Make interactive
Methods
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_original__init__(_label_ , _label_config =None_, _box_config =None_, _frame_config =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.Label._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **label** (_str_ _|_[_Tex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex") _|_[_MathTex_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") _|_[_Text_](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text"))
  * **label_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **box_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **frame_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **kwargs** (_Any_)


Return type:
    
None
[ Next LabeledArrow ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.LabeledArrow.html>) [ Previous labeled ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.labeled.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Label](https://docs.manim.community/en/stable/reference/<#>)
    * `[Label`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.Label>)
      * `[Label._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.labeled.Label._original__init__>)


