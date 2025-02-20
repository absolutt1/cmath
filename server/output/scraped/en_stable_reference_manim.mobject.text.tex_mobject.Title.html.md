# Title[¶](https://docs.manim.community/en/stable/reference/<#title> "Link to this heading")
Qualified name: `manim.mobject.text.tex\_mobject.Title`
_class_ Title(_* text_parts_, _include_underline =True_, _match_underline_width_to_text =False_, _underline_buff =0.25_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#Title>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Title> "Link to this definition")
    
Bases: `[Tex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex")
A mobject representing an underlined title.
Examples
Example: TitleExample [¶](https://docs.manim.community/en/stable/reference/<#titleexample>)
![../_images/TitleExample-1.png](https://docs.manim.community/en/stable/_images/TitleExample-1.png)
```
frommanimimport *
importmanim
classTitleExample(Scene):
  defconstruct(self):
    banner = ManimBanner()
    title = Title(f"Manim version {manim.__version__}")
    self.add(banner, title)

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
`font_size` | The font size of the tex mobject.  
`hash_seed` | A unique hash representing the result of the generated mobject points.  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_original__init__(_* text_parts_, _include_underline =True_, _match_underline_width_to_text =False_, _underline_buff =0.25_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Title._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
[ Next text_mobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.html>) [ Previous Tex ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Title](https://docs.manim.community/en/stable/reference/<#>)
    * `[Title`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Title>)
      * `[Title._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Title._original__init__>)


