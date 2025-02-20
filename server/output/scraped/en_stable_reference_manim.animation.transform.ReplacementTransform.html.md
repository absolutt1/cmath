# ReplacementTransform[¶](https://docs.manim.community/en/stable/reference/<#replacementtransform> "Link to this heading")
Qualified name: `manim.animation.transform.ReplacementTransform`
_class_ ReplacementTransform(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#ReplacementTransform>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ReplacementTransform> "Link to this definition")
    
Bases: `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform")
Replaces and morphs a mobject into a target mobject.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The starting `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The target `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **kwargs** – Further keyword arguments that are passed to `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform").


Examples
Example: ReplacementTransformOrTransform [¶](https://docs.manim.community/en/stable/reference/<#replacementtransformortransform>)
```
frommanimimport *
classReplacementTransformOrTransform(Scene):
  defconstruct(self):
    # set up the numbers
    r_transform = VGroup(*[Integer(i) for i in range(1,4)])
    text_1 = Text("ReplacementTransform", color=RED)
    r_transform.add(text_1)
    transform = VGroup(*[Integer(i) for i in range(4,7)])
    text_2 = Text("Transform", color=BLUE)
    transform.add(text_2)
    ints = VGroup(r_transform, transform)
    texts = VGroup(text_1, text_2).scale(0.75)
    r_transform.arrange(direction=UP, buff=1)
    transform.arrange(direction=UP, buff=1)
    ints.arrange(buff=2)
    self.add(ints, texts)
    # The mobs replace each other and none are left behind
    self.play(ReplacementTransform(r_transform[0], r_transform[1]))
    self.play(ReplacementTransform(r_transform[1], r_transform[2]))
    # The mobs linger after the Transform()
    self.play(Transform(transform[0], transform[1]))
    self.play(Transform(transform[1], transform[2]))
    self.wait()

```
Copy to clipboard
Make interactive
Methods
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_mobject_ , _target_mobject_ , _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ReplacementTransform._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))


Return type:
    
None
[ Next Restore ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Restore.html>) [ Previous MoveToTarget ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.MoveToTarget.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ReplacementTransform](https://docs.manim.community/en/stable/reference/<#>)
    * `[ReplacementTransform`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ReplacementTransform>)
      * `[ReplacementTransform._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.ReplacementTransform._original__init__>)


