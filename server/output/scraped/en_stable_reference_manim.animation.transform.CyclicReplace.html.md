# CyclicReplace[¶](https://docs.manim.community/en/stable/reference/<#cyclicreplace> "Link to this heading")
Qualified name: `manim.animation.transform.CyclicReplace`
_class_ CyclicReplace(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#CyclicReplace>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.CyclicReplace> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
An animation moving mobjects cyclically.
In particular, this means: the first mobject takes the place of the second mobject, the second one takes the place of the third mobject, and so on. The last mobject takes the place of the first one.
Parameters:
    
  * **mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – List of mobjects to be transformed.
  * **path_arc** (_float_) – The angle of the arc (in radians) that the mobjects will follow to reach their target.
  * **kwargs** – Further keyword arguments that are passed to `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform").


Examples
Example: CyclicReplaceExample [¶](https://docs.manim.community/en/stable/reference/<#cyclicreplaceexample>)
```
frommanimimport *
classCyclicReplaceExample(Scene):
  defconstruct(self):
    group = VGroup(Square(), Circle(), Triangle(), Star())
    group.arrange(RIGHT)
    self.add(group)
    for _ in range(4):
      self.play(CyclicReplace(*group))

```
Copy to clipboard
Make interactive
Methods
`create_target`  
---  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_* mobjects_, _path_arc =1.5707963267948966_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.CyclicReplace._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **path_arc** (_float_)


Return type:
    
None
[ Next FadeToColor ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.FadeToColor.html>) [ Previous CounterclockwiseTransform ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.CounterclockwiseTransform.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [CyclicReplace](https://docs.manim.community/en/stable/reference/<#>)
    * `[CyclicReplace`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.CyclicReplace>)
      * `[CyclicReplace._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.CyclicReplace._original__init__>)


