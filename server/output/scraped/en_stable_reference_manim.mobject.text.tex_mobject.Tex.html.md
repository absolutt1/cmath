# Tex[¶](https://docs.manim.community/en/stable/reference/<#tex> "Link to this heading")
Qualified name: `manim.mobject.text.tex\_mobject.Tex`
_class_ Tex(_* tex_strings_, _arg_separator =''_, _tex_environment ='center'_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#Tex>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Tex> "Link to this definition")
    
Bases: `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex")
A string compiled with LaTeX in normal mode.
The color can be set using the `color` argument. Any parts of the `tex_string` that are colored by the TeX commands `\color` or `\textcolor` will retain their original color.
Tests
Check whether writing a LaTeX string works:
```
>>> Tex('The horse does not eat cucumber salad.') 
Tex('The horse does not eat cucumber salad.')

```
Copy to clipboard
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
_original__init__(_* tex_strings_, _arg_separator =''_, _tex_environment ='center'_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Tex._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
[ Next Title ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Title.html>) [ Previous SingleStringMathTex ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.SingleStringMathTex.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Tex](https://docs.manim.community/en/stable/reference/<#>)
    * `[Tex`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Tex>)
      * `[Tex._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.Tex._original__init__>)


