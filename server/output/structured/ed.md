# SingleStringMathTex
Qualified name: `manim.mobject.text.tex\_mobject.SingleStringMathTex`
_class_ SingleStringMathTex(_tex_string_ , _stroke_width =0_, _should_center =True_, _height =None_, _organize_left_to_right =False_, _tex_environment ='align*'_, _tex_template =None_, _font_size =48_, _color =None_, _** kwargs_)[[source]](

Bases: `
Elementary building block for rendering text with LaTeX.
Tests
Check that creating a ` object works:
```
>>> SingleStringMathTex('Test') 
SingleStringMathTex('Test')

```
Copy to clipboard
Methods
`get_tex_string`  
---  
` | Initializes the colors.  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
` | The font size of the tex mobject.  
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
  * **tex_template** ( _|__None_)
  * **font_size** (_float_)
  * **color** ( _|__None_)

_original__init__(_tex_string_ , _stroke_width =0_, _should_center =True_, _height =None_, _organize_left_to_right =False_, _tex_environment ='align*'_, _tex_template =None_, _font_size =48_, _color =None_, _** kwargs_)

Initialize self. See help(type(self)) for accurate signature.
Parameters:

  * **tex_string** (_str_)
  * **stroke_width** (_float_)
  * **should_center** (_bool_)
  * **height** (_float_ _|__None_)
  * **organize_left_to_right** (_bool_)
  * **tex_environment** (_str_)
  * **tex_template** ( _|__None_)
  * **font_size** (_float_)
  * **color** ( _|__None_)

_remove_stray_braces(_tex_)[[source]](

Makes ` resilient to unmatched braces.
This is important when the braces in the TeX code are spread over multiple arguments as in, e.g., `MathTex(r"e^{i", r"\tau} = 1")`.
_property_ font_size

The font size of the tex mobject.
init_colors(_propagate_colors =True_)[[source]](

Initializes the colors.
Gets called upon creation. This is an empty method that can be implemented by subclasses.

Copyright © 2020-2025, The Manim Community Dev Team 
Made with  and 's 
On this page 
  * 
    * `
      * `
      * `
      * `
      * `