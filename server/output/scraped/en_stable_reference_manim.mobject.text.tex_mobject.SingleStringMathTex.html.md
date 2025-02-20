# SingleStringMathTex[¶](https://docs.manim.community/en/stable/reference/<#singlestringmathtex> "Link to this heading")
Qualified name: `manim.mobject.text.tex\_mobject.SingleStringMathTex`
_class_ SingleStringMathTex(_tex_string_ , _stroke_width =0_, _should_center =True_, _height =None_, _organize_left_to_right =False_, _tex_environment ='align*'_, _tex_template =None_, _font_size =48_, _color =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex> "Link to this definition")
    
Bases: `[SVGMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject> "manim.mobject.svg.svg_mobject.SVGMobject")
Elementary building block for rendering text with LaTeX.
Tests
Check that creating a `[SingleStringMathTex`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex> "manim.mobject.text.tex_mobject.SingleStringMathTex") object works:
```
>>> SingleStringMathTex('Test') 
SingleStringMathTex('Test')

```
Copy to clipboard
Methods
`get_tex_string`  
---  
`[init_colors`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors> "manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors") | Initializes the colors.  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`[font_size`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size> "manim.mobject.text.tex_mobject.SingleStringMathTex.font_size") | The font size of the tex mobject.  
`hash_seed` | A unique hash representing the result of the generated mobject points.  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
Parameters:
    
  * **tex_string** (_str_)
  * **stroke_width** (_float_)
  * **should_center** (_bool_)
  * **height** (_float_ _|__None_)
  * **organize_left_to_right** (_bool_)
  * **tex_environment** (_str_)
  * **tex_template** ([_TexTemplate_](https://docs.manim.community/en/stable/reference/<manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate> "manim.utils.tex.TexTemplate") _|__None_)
  * **font_size** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)


_original__init__(_tex_string_ , _stroke_width =0_, _should_center =True_, _height =None_, _organize_left_to_right =False_, _tex_environment ='align*'_, _tex_template =None_, _font_size =48_, _color =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **tex_string** (_str_)
  * **stroke_width** (_float_)
  * **should_center** (_bool_)
  * **height** (_float_ _|__None_)
  * **organize_left_to_right** (_bool_)
  * **tex_environment** (_str_)
  * **tex_template** ([_TexTemplate_](https://docs.manim.community/en/stable/reference/<manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate> "manim.utils.tex.TexTemplate") _|__None_)
  * **font_size** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)


_remove_stray_braces(_tex_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex._remove_stray_braces>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex._remove_stray_braces> "Link to this definition")
    
Makes `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex") resilient to unmatched braces.
This is important when the braces in the TeX code are spread over multiple arguments as in, e.g., `MathTex(r"e^{i", r"\tau} = 1")`.
_property_ font_size[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size> "Link to this definition")
    
The font size of the tex mobject.
init_colors(_propagate_colors =True_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/tex_mobject.html#SingleStringMathTex.init_colors>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors> "Link to this definition")
    
Initializes the colors.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
[ Next Tex ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.Tex.html>) [ Previous MathTex ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [SingleStringMathTex](https://docs.manim.community/en/stable/reference/<#>)
    * `[SingleStringMathTex`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex>)
      * `[SingleStringMathTex._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex._original__init__>)
      * `[SingleStringMathTex._remove_stray_braces()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex._remove_stray_braces>)
      * `[SingleStringMathTex.font_size`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex.font_size>)
      * `[SingleStringMathTex.init_colors()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.tex_mobject.SingleStringMathTex.init_colors>)


