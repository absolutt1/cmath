# Text[¶](https://docs.manim.community/en/stable/reference/<#text> "Link to this heading")
Qualified name: `manim.mobject.text.text\_mobject.Text`
_class_ Text(_text_ , _fill_opacity =1.0_, _stroke_width =0_, _*_ , _color =ManimColor('#FFFFFF')_, _font_size =48_, _line_spacing =-1_, _font =''_, _slant ='NORMAL'_, _weight ='NORMAL'_, _t2c =None_, _t2f =None_, _t2g =None_, _t2s =None_, _t2w =None_, _gradient =None_, _tab_width =4_, _warn_missing_font =True_, _height =None_, _width =None_, _should_center =True_, _disable_ligatures =False_, _use_svg_cache =False_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text> "Link to this definition")
    
Bases: `[SVGMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject> "manim.mobject.svg.svg_mobject.SVGMobject")
Display (non-LaTeX) text rendered using [Pango](https://docs.manim.community/en/stable/reference/<https:/pango.gnome.org/>).
Text objects behave like a `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")-like iterable of all characters in the given text. In particular, slicing is possible.
Parameters:
    
  * **text** (_str_) – The text that needs to be created as a mobject.
  * **font** (_str_) – The font family to be used to render the text. This is either a system font or one loaded with register_font(). Note that font family names may be different across operating systems.
  * **warn_missing_font** (_bool_) – If True (default), Manim will issue a warning if the font does not exist in the (case-sensitive) list of fonts returned from manimpango.list_fonts().
  * **fill_opacity** (_float_)
  * **stroke_width** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
  * **font_size** (_float_)
  * **line_spacing** (_float_)
  * **slant** (_str_)
  * **weight** (_str_)
  * **t2c** (_dict_ _[__str_ _,__str_ _]_)
  * **t2f** (_dict_ _[__str_ _,__str_ _]_)
  * **t2g** (_dict_ _[__str_ _,__tuple_ _]_)
  * **t2s** (_dict_ _[__str_ _,__str_ _]_)
  * **t2w** (_dict_ _[__str_ _,__str_ _]_)
  * **gradient** (_tuple_)
  * **tab_width** (_int_)
  * **height** (_float_)
  * **width** (_float_)
  * **should_center** (_bool_)
  * **disable_ligatures** (_bool_)
  * **use_svg_cache** (_bool_)


Returns:
    
The mobject-like `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup").
Return type:
    
`[Text`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text")
Examples
Example: Example1Text [¶](https://docs.manim.community/en/stable/reference/<#example1text>)
![../_images/Example1Text-1.png](https://docs.manim.community/en/stable/_images/Example1Text-1.png)
```
frommanimimport *
classExample1Text(Scene):
  defconstruct(self):
    text = Text('Hello world').scale(3)
    self.add(text)

```
Copy to clipboard
Make interactive
Example: TextColorExample [¶](https://docs.manim.community/en/stable/reference/<#textcolorexample>)
![../_images/TextColorExample-1.png](https://docs.manim.community/en/stable/_images/TextColorExample-1.png)
```
frommanimimport *
classTextColorExample(Scene):
  defconstruct(self):
    text1 = Text('Hello world', color=BLUE).scale(3)
    text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
    self.add(text1, text2)

```
Copy to clipboard
Make interactive
Example: TextItalicAndBoldExample [¶](https://docs.manim.community/en/stable/reference/<#textitalicandboldexample>)
![../_images/TextItalicAndBoldExample-1.png](https://docs.manim.community/en/stable/_images/TextItalicAndBoldExample-1.png)
```
frommanimimport *
classTextItalicAndBoldExample(Scene):
  defconstruct(self):
    text1 = Text("Hello world", slant=ITALIC)
    text2 = Text("Hello world", t2s={'world':ITALIC})
    text3 = Text("Hello world", weight=BOLD)
    text4 = Text("Hello world", t2w={'world':BOLD})
    text5 = Text("Hello world", t2c={'o':YELLOW}, disable_ligatures=True)
    text6 = Text(
      "Visit us at docs.manim.community",
      t2c={"docs.manim.community": YELLOW},
      disable_ligatures=True,
    )
    text6.scale(1.3).shift(DOWN)
    self.add(text1, text2, text3, text4, text5 , text6)
    Group(*self.mobjects).arrange(DOWN, buff=.8).set(height=config.frame_height-LARGE_BUFF)

```
Copy to clipboard
Make interactive
Example: TextMoreCustomization [¶](https://docs.manim.community/en/stable/reference/<#textmorecustomization>)
![../_images/TextMoreCustomization-1.png](https://docs.manim.community/en/stable/_images/TextMoreCustomization-1.png)
```
frommanimimport *
classTextMoreCustomization(Scene):
  defconstruct(self):
    text1 = Text(
      'Google',
      t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
         '[2:3]': '#fbb003', '[3:4]': '#3174f0',
         '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
    self.add(text1)

```
Copy to clipboard
Make interactive
As `[Text`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text") uses Pango to render text, rendering non-English characters is easily possible:
Example: MultipleFonts [¶](https://docs.manim.community/en/stable/reference/<#multiplefonts>)
![../_images/MultipleFonts-1.png](https://docs.manim.community/en/stable/_images/MultipleFonts-1.png)
```
frommanimimport *
classMultipleFonts(Scene):
  defconstruct(self):
    morning = Text("வணக்கம்", font="sans-serif")
    japanese = Text(
      "日本へようこそ", t2c={"日本": BLUE}
    ) # works same as ``Text``.
    mess = Text("Multi-Language", weight=BOLD)
    russ = Text("Здравствуйте मस नम म ", font="sans-serif")
    hin = Text("नमस्ते", font="sans-serif")
    arb = Text(
      "صباح الخير \n تشرفت بمقابلتك", font="sans-serif"
    ) # don't mix RTL and LTR languages nothing shows up then ;-)
    chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
    self.add(morning, japanese, mess, russ, hin, arb, chinese)
    for i,mobj in enumerate(self.mobjects):
      mobj.shift(DOWN*(i-3))

```
Copy to clipboard
Make interactive
Example: PangoRender [¶](https://docs.manim.community/en/stable/reference/<#pangorender>)
```
frommanimimport *
classPangoRender(Scene):
  defconstruct(self):
    morning = Text("வணக்கம்", font="sans-serif")
    self.play(Write(morning))
    self.wait(2)

```
Copy to clipboard
Make interactive
Tests
Check that the creation of `[Text`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text> "manim.mobject.text.text_mobject.Text") works:
```
>>> Text('The horse does not eat cucumber salad.')
Text('The horse does not eat cucumber salad.')

```
Copy to clipboard
Methods
`font_list`  
---  
`[init_colors`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text.init_colors> "manim.mobject.text.text_mobject.Text.init_colors") | Initializes the colors.  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`font_size`  
`hash_seed` | A unique hash representing the result of the generated mobject points.  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_find_indexes(_word_ , _text_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text._find_indexes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._find_indexes> "Link to this definition")
    
Finds the indexes of `text` in `word`.
Parameters:
    
  * **word** (_str_)
  * **text** (_str_)


_original__init__(_text_ , _fill_opacity =1.0_, _stroke_width =0_, _color =None_, _font_size =48_, _line_spacing =-1_, _font =''_, _slant ='NORMAL'_, _weight ='NORMAL'_, _t2c =None_, _t2f =None_, _t2g =None_, _t2s =None_, _t2w =None_, _gradient =None_, _tab_width =4_, _warn_missing_font =True_, _height =None_, _width =None_, _should_center =True_, _disable_ligatures =False_, _use_svg_cache =False_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **text** (_str_)
  * **fill_opacity** (_float_)
  * **stroke_width** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
  * **font_size** (_float_)
  * **line_spacing** (_float_)
  * **font** (_str_)
  * **slant** (_str_)
  * **weight** (_str_)
  * **t2c** (_dict_ _[__str_ _,__str_ _]_)
  * **t2f** (_dict_ _[__str_ _,__str_ _]_)
  * **t2g** (_dict_ _[__str_ _,__tuple_ _]_)
  * **t2s** (_dict_ _[__str_ _,__str_ _]_)
  * **t2w** (_dict_ _[__str_ _,__str_ _]_)
  * **gradient** (_tuple_)
  * **tab_width** (_int_)
  * **warn_missing_font** (_bool_)
  * **height** (_float_)
  * **width** (_float_)
  * **should_center** (_bool_)
  * **disable_ligatures** (_bool_)
  * **use_svg_cache** (_bool_)


Return type:
    
None
_set_color_by_t2c(_t2c =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text._set_color_by_t2c>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._set_color_by_t2c> "Link to this definition")
    
Sets color for specified strings.
Attention
Deprecated The method Text._set_color_by_t2c has been deprecated since v0.14.0 and is expected to be removed after v0.15.0. This was internal function, you shouldn’t be using it anyway.
_set_color_by_t2g(_t2g =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text._set_color_by_t2g>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._set_color_by_t2g> "Link to this definition")
    
Sets gradient colors for specified strings. Behaves similarly to `set_color_by_t2c`.
Attention
Deprecated The method Text._set_color_by_t2g has been deprecated since v0.14.0 and is expected to be removed after v0.15.0. This was internal function, you shouldn’t be using it anyway.
_text2hash(_color_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text._text2hash>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._text2hash> "Link to this definition")
    
Generates `sha256` hash for file name.
Parameters:
    
**color** ([_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor"))
_text2settings(_color_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text._text2settings>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._text2settings> "Link to this definition")
    
Converts the texts and styles to a setting for parsing.
Parameters:
    
**color** (_str_)
_text2svg(_color_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text._text2svg>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._text2svg> "Link to this definition")
    
Convert the text to SVG using Pango.
Parameters:
    
**color** ([_ManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor> "manim.utils.color.core.ManimColor"))
init_colors(_propagate_colors =True_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#Text.init_colors>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text.init_colors> "Link to this definition")
    
Initializes the colors.
Gets called upon creation. This is an empty method that can be implemented by subclasses.
[ Next three_d ](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.html>) [ Previous Paragraph ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Paragraph.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Text](https://docs.manim.community/en/stable/reference/<#>)
    * `[Text`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text>)
      * `[Text._find_indexes()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._find_indexes>)
      * `[Text._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._original__init__>)
      * `[Text._set_color_by_t2c()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._set_color_by_t2c>)
      * `[Text._set_color_by_t2g()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._set_color_by_t2g>)
      * `[Text._text2hash()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._text2hash>)
      * `[Text._text2settings()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._text2settings>)
      * `[Text._text2svg()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text._text2svg>)
      * `[Text.init_colors()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.Text.init_colors>)


