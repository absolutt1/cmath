# Code[¶](https://docs.manim.community/en/stable/reference/<#code> "Link to this heading")
Qualified name: `manim.mobject.text.code\_mobject.Code`
_class_ Code(_code_file =None_, _code_string =None_, _language =None_, _formatter_style ='vim'_, _tab_width =4_, _add_line_numbers =True_, _line_numbers_from =1_, _background ='rectangle'_, _background_config =None_, _paragraph_config =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/code_mobject.html#Code>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
A highlighted source code listing.
Examples
Normal usage:
```
listing = Code(
  "helloworldcpp.cpp",
  tab_width=4,
  formatter_style="emacs",
  background="window",
  language="cpp",
  background_config={"stroke_color": WHITE},
  paragraph_config={"font": "Noto Sans Mono"},
)

```
Copy to clipboard
We can also render code passed as a string. As the automatic language detection can be a bit flaky, it is recommended to specify the language explicitly:
Example: CodeFromString [¶](https://docs.manim.community/en/stable/reference/<#codefromstring>)
![../_images/CodeFromString-1.png](https://docs.manim.community/en/stable/_images/CodeFromString-1.png)
```
frommanimimport *
classCodeFromString(Scene):
  defconstruct(self):
    code = '''from manim import Scene, Square
class FadeInSquare(Scene):
  def construct(self):
    s = Square()
    self.play(FadeIn(s))
    self.play(s.animate.scale(2))
    self.wait()'''
    rendered_code = Code(
      code_string=code,
      language="python",
      background="window",
      background_config={"stroke_color": "maroon"},
    )
    self.add(rendered_code)

```
Copy to clipboard
Make interactive
Parameters:
    
  * **code_file** ([_StrPath_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.StrPath> "manim.typing.StrPath") _|__None_) – The path to the code file to display.
  * **code_string** (_str_ _|__None_) – Alternatively, the code string to display.
  * **language** (_str_ _|__None_) – The programming language of the code. If not specified, it will be guessed from the file extension or the code itself.
  * **formatter_style** (_str_) – The style to use for the code highlighting. Defaults to `"vim"`. A list of all available styles can be obtained by calling `[Code.get_styles_list()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code.get_styles_list> "manim.mobject.text.code_mobject.Code.get_styles_list").
  * **tab_width** (_int_) – The width of a tab character in spaces. Defaults to 4.
  * **add_line_numbers** (_bool_) – Whether to display line numbers. Defaults to `True`.
  * **line_numbers_from** (_int_) – The first line number to display. Defaults to 1.
  * **background** (_Literal_ _[__'rectangle'__,__'window'__]_) – The type of background to use. Can be either `"rectangle"` (the default) or `"window"`.
  * **background_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Keyword arguments passed to the background constructor. Default settings are stored in the class attribute `default_background_config` (which can also be modified directly).
  * **paragraph_config** (_dict_ _[__str_ _,__Any_ _]__|__None_) – Keyword arguments passed to the constructor of the `[Paragraph`](https://docs.manim.community/en/stable/reference/<manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph> "manim.mobject.text.text_mobject.Paragraph") objects holding the code, and the line numbers. Default settings are stored in the class attribute `default_paragraph_config` (which can also be modified directly).


Methods
`[get_styles_list`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code.get_styles_list> "manim.mobject.text.code_mobject.Code.get_styles_list") | Get the list of all available formatter styles.  
---|---  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`default_background_config`  
`default_paragraph_config`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
_original__init__(_code_file =None_, _code_string =None_, _language =None_, _formatter_style ='vim'_, _tab_width =4_, _add_line_numbers =True_, _line_numbers_from =1_, _background ='rectangle'_, _background_config =None_, _paragraph_config =None_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **code_file** ([_StrPath_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.StrPath> "manim.typing.StrPath") _|__None_)
  * **code_string** (_str_ _|__None_)
  * **language** (_str_ _|__None_)
  * **formatter_style** (_str_)
  * **tab_width** (_int_)
  * **add_line_numbers** (_bool_)
  * **line_numbers_from** (_int_)
  * **background** (_Literal_ _[__'rectangle'__,__'window'__]_)
  * **background_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)
  * **paragraph_config** (_dict_ _[__str_ _,__Any_ _]__|__None_)


_classmethod_ get_styles_list()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/text/code_mobject.html#Code.get_styles_list>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code.get_styles_list> "Link to this definition")
    
Get the list of all available formatter styles.
Return type:
    
list[str]
[ Next numbers ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.numbers.html>) [ Previous code_mobject ](https://docs.manim.community/en/stable/reference/<manim.mobject.text.code_mobject.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Code](https://docs.manim.community/en/stable/reference/<#>)
    * `[Code`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code>)
      * `[Code._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code._original__init__>)
      * `[Code.get_styles_list()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.text.code_mobject.Code.get_styles_list>)


