# MarkupText[¶](https://docs.manim.community/en/stable/reference/<#markuptext> "Link to this heading")
Qualified name: `manim.mobject.text.text\_mobject.MarkupText`
_class_ MarkupText(_text_ , _fill_opacity =1_, _stroke_width =0_, _color =None_, _font_size =48_, _line_spacing =-1_, _font =''_, _slant ='NORMAL'_, _weight ='NORMAL'_, _justify =False_, _gradient =None_, _tab_width =4_, _height =None_, _width =None_, _should_center =True_, _disable_ligatures =False_, _warn_missing_font =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#MarkupText>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText> "Link to this definition")
    
Bases: `[SVGMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.svg.svg_mobject.SVGMobject.html#manim.mobject.svg.svg_mobject.SVGMobject> "manim.mobject.svg.svg_mobject.SVGMobject")
Display (non-LaTeX) text rendered using [Pango](https://docs.manim.community/en/stable/reference/<https:/pango.gnome.org/>).
Text objects behave like a `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")-like iterable of all characters in the given text. In particular, slicing is possible.
**What is PangoMarkup?**
PangoMarkup is a small markup language like html and it helps you avoid using “range of characters” while coloring or styling a piece a Text. You can use this language with `[MarkupText`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText> "manim.mobject.text.text_mobject.MarkupText").
A simple example of a marked-up string might be:
```
<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"

```
Copy to clipboard
and it can be used with `[MarkupText`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText> "manim.mobject.text.text_mobject.MarkupText") as
Example: MarkupExample [¶](https://docs.manim.community/en/stable/reference/<#markupexample>)
![../_images/MarkupExample-1.png](https://docs.manim.community/en/stable/_images/MarkupExample-1.png)
```
frommanimimport *
classMarkupExample(Scene):
  defconstruct(self):
    text = MarkupText('<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')
    self.add(text)

```
Copy to clipboard
Make interactive
A more elaborate example would be:
Example: MarkupElaborateExample [¶](https://docs.manim.community/en/stable/reference/<#markupelaborateexample>)
![../_images/MarkupElaborateExample-1.png](https://docs.manim.community/en/stable/_images/MarkupElaborateExample-1.png)
```
frommanimimport *
classMarkupElaborateExample(Scene):
  defconstruct(self):
    text = MarkupText(
      '<span foreground="purple">ا</span><span foreground="red">َ</span>'
      'ل<span foreground="blue">ْ</span>ع<span foreground="red">َ</span>ر'
      '<span foreground="red">َ</span>ب<span foreground="red">ِ</span>ي'
      '<span foreground="green">ّ</span><span foreground="red">َ</span>ة'
      '<span foreground="blue">ُ</span>'
    )
    self.add(text)

```
Copy to clipboard
Make interactive
PangoMarkup can also contain XML features such as numeric character entities such as `&#169;` for © can be used too.
The most general markup tag is `<span>`, then there are some convenience tags.
Here is a list of supported tags:
  * `<b>bold</b>`, `<i>italic</i>` and `<b><i>bold+italic</i></b>`
  * `<u>underline</u>` and `<s>strike through</s>`
  * `<tt>typewriter font</tt>`
  * `<big>bigger font</big>` and `<small>smaller font</small>`
  * `<sup>superscript</sup>` and `<sub>subscript</sub>`
  * `<span underline="double" underline_color="green">double underline</span>`
  * `<span underline="error">error underline</span>`
  * `<span overline="single" overline_color="green">overline</span>`
  * `<span strikethrough="true" strikethrough_color="red">strikethrough</span>`
  * `<span font_family="sans">temporary change of font</span>`
  * `<span foreground="red">temporary change of color</span>`
  * `<span fgcolor="red">temporary change of color</span>`
  * `<gradient from="YELLOW" to="RED">temporary gradient</gradient>`


For `<span>` markup, colors can be specified either as hex triples like `#aabbcc` or as named CSS colors like `AliceBlue`. The `<gradient>` tag is handled by Manim rather than Pango, and supports hex triplets or Manim constants like `RED` or `RED_A`. If you want to use Manim constants like `RED_A` together with `<span>`, you will need to use Python’s f-String syntax as follows:
```
MarkupText(f'<span foreground="{RED_A}">here you go</span>')

```
Copy to clipboard
If your text contains ligatures, the `[MarkupText`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText> "manim.mobject.text.text_mobject.MarkupText") class may incorrectly determine the first and last letter when creating the gradient. This is due to the fact that `fl` are two separate characters, but might be set as one single glyph - a ligature. If your language does not depend on ligatures, consider setting `disable_ligatures` to `True`. If you must use ligatures, the `gradient` tag supports an optional attribute `offset` which can be used to compensate for that error.
For example:
  * `<gradient from="RED" to="YELLOW" offset="1">example</gradient>` to _start_ the gradient one letter earlier
  * `<gradient from="RED" to="YELLOW" offset=",1">example</gradient>` to _end_ the gradient one letter earlier
  * `<gradient from="RED" to="YELLOW" offset="2,1">example</gradient>` to _start_ the gradient two letters earlier and _end_ it one letter earlier


Specifying a second offset may be necessary if the text to be colored does itself contain ligatures. The same can happen when using HTML entities for special chars.
When using `underline`, `overline` or `strikethrough` together with `<gradient>` tags, you will also need to use the offset, because underlines are additional paths in the final `SVGMobject`. Check out the following example.
Escaping of special characters: `>` **should** be written as `&gt;` whereas `<` and `&` _must_ be written as `&lt;` and `&amp;`.
You can find more information about Pango markup formatting at the corresponding documentation page: [Pango Markup](https://docs.manim.community/en/stable/reference/<https:/docs.gtk.org/Pango/pango_markup.html>). Please be aware that not all features are supported by this class and that the `<gradient>` tag mentioned above is not supported by Pango.
Parameters:
    
  * **text** (_str_) – The text that needs to be created as mobject.
  * **fill_opacity** (_float_) – The fill opacity, with 1 meaning opaque and 0 meaning transparent.
  * **stroke_width** (_float_) – Stroke width.
  * **font_size** (_float_) – Font size.
  * **line_spacing** (_int_) – Line spacing.
  * **font** (_str_) – Global font setting for the entire text. Local overrides are possible.
  * **slant** (_str_) – Global slant setting, e.g. NORMAL or ITALIC. Local overrides are possible.
  * **weight** (_str_) – Global weight setting, e.g. NORMAL or BOLD. Local overrides are possible.
  * **gradient** (_tuple_) – Global gradient setting. Local overrides are possible.
  * **warn_missing_font** (_bool_) – If True (default), Manim will issue a warning if the font does not exist in the (case-sensitive) list of fonts returned from manimpango.list_fonts().
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
  * **justify** (_bool_)
  * **tab_width** (_int_)
  * **height** (_int_)
  * **width** (_int_)
  * **should_center** (_bool_)
  * **disable_ligatures** (_bool_)


Returns:
    
The text displayed in form of a `[VGroup`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")-like mobject.
Return type:
    
`[MarkupText`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText> "manim.mobject.text.text_mobject.MarkupText")
Examples
Example: BasicMarkupExample [¶](https://docs.manim.community/en/stable/reference/<#basicmarkupexample>)
![../_images/BasicMarkupExample-1.png](https://docs.manim.community/en/stable/_images/BasicMarkupExample-1.png)
```
frommanimimport *
classBasicMarkupExample(Scene):
  defconstruct(self):
    text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
    text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
    text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
    text4 = MarkupText("type <tt>help</tt> for help")
    text5 = MarkupText(
      '<span underline="double">foo</span> <span underline="error">bar</span>'
    )
    group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
    self.add(group)

```
Copy to clipboard
Make interactive
Example: ColorExample [¶](https://docs.manim.community/en/stable/reference/<#colorexample>)
![../_images/ColorExample-1.png](https://docs.manim.community/en/stable/_images/ColorExample-1.png)
```
frommanimimport *
classColorExample(Scene):
  defconstruct(self):
    text1 = MarkupText(
      f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
    )
    text2 = MarkupText("nice gradient", gradient=(BLUE, GREEN))
    text3 = MarkupText(
      'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
      gradient=(BLUE, GREEN),
    )
    text4 = MarkupText(
      'fl ligature <gradient from="RED" to="YELLOW">causing trouble</gradient> here'
    )
    text5 = MarkupText(
      'fl ligature <gradient from="RED" to="YELLOW" offset="1">defeated</gradient> with offset'
    )
    text6 = MarkupText(
      'fl ligature <gradient from="RED" to="YELLOW" offset="1">floating</gradient> inside'
    )
    text7 = MarkupText(
      'fl ligature <gradient from="RED" to="YELLOW" offset="1,1">floating</gradient> inside'
    )
    group = VGroup(text1, text2, text3, text4, text5, text6, text7).arrange(DOWN)
    self.add(group)

```
Copy to clipboard
Make interactive
Example: UnderlineExample [¶](https://docs.manim.community/en/stable/reference/<#underlineexample>)
![../_images/UnderlineExample-1.png](https://docs.manim.community/en/stable/_images/UnderlineExample-1.png)
```
frommanimimport *
classUnderlineExample(Scene):
  defconstruct(self):
    text1 = MarkupText(
      '<span underline="double" underline_color="green">bla</span>'
    )
    text2 = MarkupText(
      '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
    )
    text3 = MarkupText(
      '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-1">aabb</gradient>y'
    )
    text4 = MarkupText(
      '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
    )
    text5 = MarkupText(
      '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-2">aabb</gradient>y'
    )
    group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
    self.add(group)

```
Copy to clipboard
Make interactive
Example: FontExample [¶](https://docs.manim.community/en/stable/reference/<#fontexample>)
![../_images/FontExample-1.png](https://docs.manim.community/en/stable/_images/FontExample-1.png)
```
frommanimimport *
classFontExample(Scene):
  defconstruct(self):
    text1 = MarkupText(
      'all in sans <span font_family="serif">except this</span>', font="sans"
    )
    text2 = MarkupText(
      '<span font_family="serif">mixing</span> <span font_family="sans">fonts</span> <span font_family="monospace">is ugly</span>'
    )
    text3 = MarkupText("special char > or &gt;")
    text4 = MarkupText("special char &lt; and &amp;")
    group = VGroup(text1, text2, text3, text4).arrange(DOWN)
    self.add(group)

```
Copy to clipboard
Make interactive
Example: NewlineExample [¶](https://docs.manim.community/en/stable/reference/<#newlineexample>)
![../_images/NewlineExample-1.png](https://docs.manim.community/en/stable/_images/NewlineExample-1.png)
```
frommanimimport *
classNewlineExample(Scene):
  defconstruct(self):
    text = MarkupText('foooo<span foreground="red">oo\nbaa</span>aar')
    self.add(text)

```
Copy to clipboard
Make interactive
Example: NoLigaturesExample [¶](https://docs.manim.community/en/stable/reference/<#noligaturesexample>)
![../_images/NoLigaturesExample-1.png](https://docs.manim.community/en/stable/_images/NoLigaturesExample-1.png)
```
frommanimimport *
classNoLigaturesExample(Scene):
  defconstruct(self):
    text1 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing')
    text2 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing', disable_ligatures=True)
    group = VGroup(text1, text2).arrange(DOWN)
    self.add(group)

```
Copy to clipboard
Make interactive
As `[MarkupText`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText> "manim.mobject.text.text_mobject.MarkupText") uses Pango to render text, rendering non-English characters is easily possible:
Example: MultiLanguage [¶](https://docs.manim.community/en/stable/reference/<#multilanguage>)
![../_images/MultiLanguage-1.png](https://docs.manim.community/en/stable/_images/MultiLanguage-1.png)
```
frommanimimport *
classMultiLanguage(Scene):
  defconstruct(self):
    morning = MarkupText("வணக்கம்", font="sans-serif")
    japanese = MarkupText(
      '<span fgcolor="blue">日本</span>へようこそ'
    ) # works as in ``Text``.
    mess = MarkupText("Multi-Language", weight=BOLD)
    russ = MarkupText("Здравствуйте मस नम म ", font="sans-serif")
    hin = MarkupText("नमस्ते", font="sans-serif")
    chinese = MarkupText("臂猿「黛比」帶著孩子", font="sans-serif")
    group = VGroup(morning, japanese, mess, russ, hin, chinese).arrange(DOWN)
    self.add(group)

```
Copy to clipboard
Make interactive
You can justify the text by passing `justify` parameter.
Example: JustifyText [¶](https://docs.manim.community/en/stable/reference/<#justifytext>)
```
frommanimimport *
classJustifyText(Scene):
  defconstruct(self):
    ipsum_text = (
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
      "Praesent feugiat metus sit amet iaculis pulvinar. Nulla posuere "
      "quam a ex aliquam, eleifend consectetur tellus viverra. Aliquam "
      "fermentum interdum justo, nec rutrum elit pretium ac. Nam quis "
      "leo pulvinar, dignissim est at, venenatis nisi."
    )
    justified_text = MarkupText(ipsum_text, justify=True).scale(0.4)
    not_justified_text = MarkupText(ipsum_text, justify=False).scale(0.4)
    just_title = Title("Justified")
    njust_title = Title("Not Justified")
    self.add(njust_title, not_justified_text)
    self.play(
      FadeOut(not_justified_text),
      FadeIn(justified_text),
      FadeOut(njust_title),
      FadeIn(just_title),
    )
    self.wait(1)

```
Copy to clipboard
Make interactive
Tests
Check that the creation of `[MarkupText`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText> "manim.mobject.text.text_mobject.MarkupText") works:
```
>>> MarkupText('The horse does not eat cucumber salad.')
MarkupText('The horse does not eat cucumber salad.')

```
Copy to clipboard
Methods
`font_list`  
---  
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
_count_real_chars(_s_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#MarkupText._count_real_chars>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._count_real_chars> "Link to this definition")
    
Counts characters that will be displayed.
This is needed for partial coloring or gradients, because space counts to the text’s len, but has no corresponding character.
_extract_color_tags()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#MarkupText._extract_color_tags>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._extract_color_tags> "Link to this definition")
    
Used to determine which parts (if any) of the string should be formatted with a custom color.
Removes the `<color>` tag, as it is not part of Pango’s markup and would cause an error.
Note: Using the `<color>` tags is deprecated. As soon as the legacy syntax is gone, this function will be removed.
_extract_gradient_tags()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#MarkupText._extract_gradient_tags>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._extract_gradient_tags> "Link to this definition")
    
Used to determine which parts (if any) of the string should be formatted with a gradient.
Removes the `<gradient>` tag, as it is not part of Pango’s markup and would cause an error.
_original__init__(_text_ , _fill_opacity =1_, _stroke_width =0_, _color =None_, _font_size =48_, _line_spacing =-1_, _font =''_, _slant ='NORMAL'_, _weight ='NORMAL'_, _justify =False_, _gradient =None_, _tab_width =4_, _height =None_, _width =None_, _should_center =True_, _disable_ligatures =False_, _warn_missing_font =True_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **text** (_str_)
  * **fill_opacity** (_float_)
  * **stroke_width** (_float_)
  * **color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
  * **font_size** (_float_)
  * **line_spacing** (_int_)
  * **font** (_str_)
  * **slant** (_str_)
  * **weight** (_str_)
  * **justify** (_bool_)
  * **gradient** (_tuple_)
  * **tab_width** (_int_)
  * **height** (_int_)
  * **width** (_int_)
  * **should_center** (_bool_)
  * **disable_ligatures** (_bool_)
  * **warn_missing_font** (_bool_)


Return type:
    
None
_parse_color(_col_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#MarkupText._parse_color>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._parse_color> "Link to this definition")
    
Parse color given in `<color>` or `<gradient>` tags.
_text2hash(_color_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#MarkupText._text2hash>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._text2hash> "Link to this definition")
    
Generates `sha256` hash for file name.
Parameters:
    
**color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor"))
_text2svg(_color_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/text_mobject.html#MarkupText._text2svg>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._text2svg> "Link to this definition")
    
Convert the text to SVG using Pango.
Parameters:
    
**color** ([_ParsableManimColor_](https://docs.manim.community/en/stable/reference/<manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor> "manim.utils.color.core.ParsableManimColor") _|__None_)
[ Next Paragraph ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Paragraph.html>) [ Previous text_mobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MarkupText](https://docs.manim.community/en/stable/reference/<#>)
    * `[MarkupText`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText>)
      * `[MarkupText._count_real_chars()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._count_real_chars>)
      * `[MarkupText._extract_color_tags()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._extract_color_tags>)
      * `[MarkupText._extract_gradient_tags()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._extract_gradient_tags>)
      * `[MarkupText._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._original__init__>)
      * `[MarkupText._parse_color()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._parse_color>)
      * `[MarkupText._text2hash()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._text2hash>)
      * `[MarkupText._text2svg()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.text_mobject.MarkupText._text2svg>)


