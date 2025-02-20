# DefaultSectionType[¶](https://docs.manim.community/en/stable/reference/<#defaultsectiontype> "Link to this heading")
Qualified name: `manim.scene.section.DefaultSectionType`
_class_ DefaultSectionType(_value_ , _names= <not given>_, _*values_ , _module=None_ , _qualname=None_ , _type=None_ , _start=1_ , _boundary=None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/section.html#DefaultSectionType>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.DefaultSectionType> "Link to this definition")
    
Bases: `str`, `Enum`
The type of a section can be used for third party applications. A presentation system could for example use the types to created loops.
Examples
This class can be reimplemented for more types:
```
classPresentationSectionType(str, Enum):
  # start, end, wait for continuation by user
  NORMAL = "presentation.normal"
  # start, end, immediately continue to next section
  SKIP = "presentation.skip"
  # start, end, restart, immediately continue to next section when continued by user
  LOOP = "presentation.loop"
  # start, end, restart, finish animation first when user continues
  COMPLETE_LOOP = "presentation.complete_loop"

```
Copy to clipboard
Methods
Attributes
`NORMAL`  
---  
[ Next Section ](https://docs.manim.community/en/stable/reference/<manim.scene.section.Section.html>) [ Previous section ](https://docs.manim.community/en/stable/reference/<manim.scene.section.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [DefaultSectionType](https://docs.manim.community/en/stable/reference/<#>)
    * `[DefaultSectionType`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.DefaultSectionType>)


