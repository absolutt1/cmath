# MathTex[¶](https://docs.manim.community/en/stable/reference/<#mathtex> "Link to this heading")
Qualified name: `manim.mobject.text.tex\_mobject.MathTex`
_class_ MathTex(_* tex_strings_, _arg_separator =' '_, _substrings_to_isolate =None_, _tex_to_color_map =None_, _tex_environment ='align*'_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#MathTex>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex> "Link to this definition")
    
Bases: `[SingleStringMathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.SingleStringMathTex.html#manim.mobject.text.tex_mobject.SingleStringMathTex> "manim.mobject.text.tex_mobject.SingleStringMathTex")
A string compiled with LaTeX in math mode.
Examples
Example: Formula [¶](https://docs.manim.community/en/stable/reference/<#formula>)
![../_images/Formula-1.png](https://docs.manim.community/en/stable/_images/Formula-1.png)
```
frommanimimport *
classFormula(Scene):
  defconstruct(self):
    t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
    self.add(t)

```
Copy to clipboard
Make interactive
Tests
Check that creating a `[MathTex`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") works:
```
>>> MathTex('a^2 + b^2 = c^2') 
MathTex('a^2 + b^2 = c^2')

```
Copy to clipboard
Check that double brace group splitting works correctly:
```
>>> t1 = MathTex('{{ a }} + {{ b }} = {{ c }}') 
>>> len(t1.submobjects) 
5
>>> t2 = MathTex(r"\frac{1}{a+b\sqrt{2}}") 
>>> len(t2.submobjects) 
1

```
Copy to clipboard
Methods
`get_part_by_tex`  
---  
`get_parts_by_tex`  
`index_of_part`  
`index_of_part_by_tex`  
`set_color_by_tex`  
`set_color_by_tex_to_color_map`  
`[set_opacity_by_tex`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex> "manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex") | Sets the opacity of the tex specified.  
`sort_alphabetically`  
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
Parameters:
    
  * **arg_separator** (_str_)
  * **substrings_to_isolate** (_Iterable_ _[__str_ _]__|__None_)
  * **tex_to_color_map** (_dict_ _[__str_ _,_[_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor") _]_)
  * **tex_environment** (_str_)


_break_up_by_substrings()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#MathTex._break_up_by_substrings>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex._break_up_by_substrings> "Link to this definition")
    
Reorganize existing submobjects one layer deeper based on the structure of tex_strings (as a list of tex_strings)
_original__init__(_* tex_strings_, _arg_separator =' '_, _substrings_to_isolate =None_, _tex_to_color_map =None_, _tex_environment ='align*'_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **arg_separator** (_str_)
  * **substrings_to_isolate** (_Iterable_ _[__str_ _]__|__None_)
  * **tex_to_color_map** (_dict_ _[__str_ _,_[_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor") _]_)
  * **tex_environment** (_str_)


set_opacity_by_tex(_tex_ , _opacity =0.5_, _remaining_opacity =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#MathTex.set_opacity_by_tex>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex> "Link to this definition")
    
Sets the opacity of the tex specified. If ‘remaining_opacity’ is specified, then the remaining tex will be set to that opacity.
Parameters:
    
  * **tex** (_str_) – The tex to set the opacity of.
  * **opacity** (_float_) – Default 0.5. The opacity to set the tex to
  * **remaining_opacity** (_float_) – Default None. The opacity to set the remaining tex to. If None, then the remaining tex will not be changed


[ Next SingleStringMathTex ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.SingleStringMathTex.html>) [ Previous BulletedList ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.BulletedList.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MathTex](https://docs.manim.community/en/stable/reference/<#>)
    * `[MathTex`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex>)
      * `[MathTex._break_up_by_substrings()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex._break_up_by_substrings>)
      * `[MathTex._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex._original__init__>)
      * `[MathTex.set_opacity_by_tex()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.MathTex.set_opacity_by_tex>)


