# BulletedList[¶](https://docs.manim.community/en/stable/reference/<#bulletedlist> "Link to this heading")
Qualified name: `manim.mobject.text.tex\_mobject.BulletedList`
_class_ BulletedList(_* items_, _buff =0.5_, _dot_scale_factor =2_, _tex_environment =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#BulletedList>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.BulletedList> "Link to this definition")
    
Bases: `[Tex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html#manim.mobject.text.tex_mobject.Tex> "manim.mobject.text.tex_mobject.Tex")
A bulleted list.
Examples
Example: BulletedListExample [¶](https://docs.manim.community/en/stable/reference/<#bulletedlistexample>)
![../_images/BulletedListExample-1.png](https://docs.manim.community/en/stable/_images/BulletedListExample-1.png)
```
frommanimimport *
classBulletedListExample(Scene):
  defconstruct(self):
    blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
    blist.set_color_by_tex("Item 1", RED)
    blist.set_color_by_tex("Item 2", GREEN)
    blist.set_color_by_tex("Item 3", BLUE)
    self.add(blist)

```
Copy to clipboard
Make interactive
Methods
`fade_all_but`  
---  
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
_original__init__(_* items_, _buff =0.5_, _dot_scale_factor =2_, _tex_environment =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.BulletedList._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
[ Next MathTex ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html>) [ Previous tex_mobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [BulletedList](https://docs.manim.community/en/stable/reference/<#>)
    * `[BulletedList`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.BulletedList>)
      * `[BulletedList._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.BulletedList._original__init__>)


