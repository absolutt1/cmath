
# TexTemplateLibrary[¶](https://docs.manim.community/en/stable/reference/<#textemplatelibrary> "Link to this heading")
Qualified name: `manim.utils.tex\_templates.TexTemplateLibrary`
_class_ TexTemplateLibrary[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/utils/tex_templates.html#TexTemplateLibrary>)[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary> "Link to this definition")
    
Bases: `object`
A collection of basic TeX template objects
Examples
Normal usage as a value for the keyword argument tex_template of Tex() and MathTex() mobjects:
```
``Tex("My TeX code", tex_template=TexTemplateLibrary.ctex)``

```
Copy to clipboard
Methods
Attributes
`[ctex`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.ctex> "manim.utils.tex_templates.TexTemplateLibrary.ctex") | An instance of the TeX template used by 3b1b when using the use_ctex flag  
---|---  
`[default`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.default> "manim.utils.tex_templates.TexTemplateLibrary.default") | An instance of the default TeX template in manim  
`[simple`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.simple> "manim.utils.tex_templates.TexTemplateLibrary.simple") | An instance of a simple TeX template with only basic AMS packages loaded  
`[threeb1b`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.threeb1b> "manim.utils.tex_templates.TexTemplateLibrary.threeb1b") | An instance of the default TeX template used by 3b1b  
ctex _= TexTemplate(_body='', tex_compiler='xelatex', description='', output_format='.xdv', documentclass='\\\documentclass[preview]{standalone}', preamble='\n\\\usepackage[english]{babel}\n\\\usepackage[utf8]{inputenc}\n\\\usepackage[T1]{fontenc}\n\\\usepackage{lmodern}\n\\\usepackage{amsmath}\n\\\usepackage{amssymb}\n\\\usepackage{dsfont}\n\\\usepackage{setspace}\n\\\usepackage{tipa}\n\\\usepackage{relsize}\n\\\usepackage{textcomp}\n\\\usepackage{mathrsfs}\n\\\usepackage{calligra}\n\\\usepackage{wasysym}\n\\\usepackage{ragged2e}\n\\\usepackage{physics}\n\\\usepackage{xcolor}\n\\\usepackage{microtype}\n\\\usepackage[UTF8]{ctex}\n\\\linespread{1}\n', placeholder_text='YourTextHere', post_doc_commands='')_[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.ctex> "Link to this definition")
    
An instance of the TeX template used by 3b1b when using the use_ctex flag
default _= TexTemplate(_body='', tex_compiler='latex', description='', output_format='.dvi', documentclass='\\\documentclass[preview]{standalone}', preamble='\n\\\usepackage[english]{babel}\n\\\usepackage[utf8]{inputenc}\n\\\usepackage[T1]{fontenc}\n\\\usepackage{lmodern}\n\\\usepackage{amsmath}\n\\\usepackage{amssymb}\n\\\usepackage{dsfont}\n\\\usepackage{setspace}\n\\\usepackage{tipa}\n\\\usepackage{relsize}\n\\\usepackage{textcomp}\n\\\usepackage{mathrsfs}\n\\\usepackage{calligra}\n\\\usepackage{wasysym}\n\\\usepackage{ragged2e}\n\\\usepackage{physics}\n\\\usepackage{xcolor}\n\\\usepackage{microtype}\n\\\DisableLigatures{encoding = *, family = * }\n\\\linespread{1}\n', placeholder_text='YourTextHere', post_doc_commands='')_[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.default> "Link to this definition")
    
An instance of the default TeX template in manim
simple _= TexTemplate(_body='', tex_compiler='latex', description='', output_format='.dvi', documentclass='\\\documentclass[preview]{standalone}', preamble='\n\\\usepackage[english]{babel}\n\\\usepackage{amsmath}\n\\\usepackage{amssymb}\n', placeholder_text='YourTextHere', post_doc_commands='')_[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.simple> "Link to this definition")
    
An instance of a simple TeX template with only basic AMS packages loaded
threeb1b _= TexTemplate(_body='', tex_compiler='latex', description='', output_format='.dvi', documentclass='\\\documentclass[preview]{standalone}', preamble='\n\\\usepackage[english]{babel}\n\\\usepackage[utf8]{inputenc}\n\\\usepackage[T1]{fontenc}\n\\\usepackage{lmodern}\n\\\usepackage{amsmath}\n\\\usepackage{amssymb}\n\\\usepackage{dsfont}\n\\\usepackage{setspace}\n\\\usepackage{tipa}\n\\\usepackage{relsize}\n\\\usepackage{textcomp}\n\\\usepackage{mathrsfs}\n\\\usepackage{calligra}\n\\\usepackage{wasysym}\n\\\usepackage{ragged2e}\n\\\usepackage{physics}\n\\\usepackage{xcolor}\n\\\usepackage{microtype}\n\\\DisableLigatures{encoding = *, family = * }\n\\\linespread{1}\n', placeholder_text='YourTextHere', post_doc_commands='')_[¶](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.threeb1b> "Link to this definition")
    
An instance of the default TeX template used by 3b1b
[ Next typing ](https://docs.manim.community/en/stable/reference/<manim.typing.html>) [ Previous TexFontTemplates ](https://docs.manim.community/en/stable/reference/<manim.utils.tex_templates.TexFontTemplates.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TexTemplateLibrary](https://docs.manim.community/en/stable/reference/<#>)
    * `[TexTemplateLibrary`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary>)
      * `[TexTemplateLibrary.ctex`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.ctex>)
      * `[TexTemplateLibrary.default`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.default>)
      * `[TexTemplateLibrary.simple`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.simple>)
      * `[TexTemplateLibrary.threeb1b`](https://docs.manim.community/en/stable/reference/<#manim.utils.tex_templates.TexTemplateLibrary.threeb1b>)


