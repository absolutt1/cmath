# BraceLabel[¶](https://docs.manim.community/en/stable/reference/<#bracelabel> "Link to this heading")
Qualified name: `manim.mobject.svg.brace.BraceLabel`
_class_ BraceLabel(_obj_ , _text_ , _brace_direction=array([ 0._, _-1._ , _0.])_ , _label_constructor= <class 'manim.mobject.text.tex_mobject.MathTex'>_, _font_size=48_ , _buff=0.2_ , _brace_config=None_ , _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/svg/brace.html#BraceLabel>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceLabel> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
Create a brace with a label attached.
Parameters:
    
  * **obj** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The mobject adjacent to which the brace is placed.
  * **text** (_str_) – The label text.
  * **brace_direction** (_np.ndarray_) – The direction of the brace. By default `DOWN`.
  * **label_constructor** (_type_) – A class or function used to construct a mobject representing the label. By default `[MathTex`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.tex_mobject.MathTex.html#manim.mobject.text.tex_mobject.MathTex> "manim.mobject.text.tex_mobject.MathTex").
  * **font_size** (_float_) – The font size of the label, passed to the `label_constructor`.
  * **buff** (_float_) – The buffer between the mobject and the brace.
  * **brace_config** (_dict_ _|__None_) – Arguments to be passed to `[Brace`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.Brace.html#manim.mobject.svg.brace.Brace> "manim.mobject.svg.brace.Brace").
  * **kwargs** – Additional arguments to be passed to `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject").


Methods
`change_brace_label`  
---  
`change_label`  
`creation_anim`  
`shift_brace`  
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
_original__init__(_obj_ , _text_ , _brace_direction=array([ 0._, _-1._ , _0.])_ , _label_constructor= <class 'manim.mobject.text.tex_mobject.MathTex'>_, _font_size=48_ , _buff=0.2_ , _brace_config=None_ , _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceLabel._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **obj** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **text** (_str_)
  * **brace_direction** (_ndarray_)
  * **label_constructor** (_type_)
  * **font_size** (_float_)
  * **buff** (_float_)
  * **brace_config** (_dict_ _|__None_)


[ Next BraceText ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.BraceText.html>) [ Previous BraceBetweenPoints ](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.brace.BraceBetweenPoints.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [BraceLabel](https://docs.manim.community/en/stable/reference/<#>)
    * `[BraceLabel`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceLabel>)
      * `[BraceLabel._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.svg.brace.BraceLabel._original__init__>)


