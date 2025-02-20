# TransformMatchingTex[¶](https://docs.manim.community/en/stable/reference/<#transformmatchingtex> "Link to this heading")
Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingTex`
_class_ TransformMatchingTex(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform_matching_parts.html#TransformMatchingTex>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingTex> "Link to this definition")
    
Bases: `[TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase> "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")
A transformation trying to transform rendered LaTeX strings.
Two submobjects match if their `tex_string` matches.
See also
`[TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase> "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")
Examples
Example: MatchingEquationParts [¶](https://docs.manim.community/en/stable/reference/<#matchingequationparts>)
```
frommanimimport *
classMatchingEquationParts(Scene):
  defconstruct(self):
    variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)
    eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
    eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
    eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")
    self.add(eq1)
    self.wait(0.5)
    self.play(TransformMatchingTex(Group(eq1, variables), eq2))
    self.wait(0.5)
    self.play(TransformMatchingTex(eq2, eq3))
    self.wait(0.5)

```
Copy to clipboard
Make interactive
Methods
`get_mobject_key`  
---  
`get_mobject_parts`  
Attributes
`run_time`  
---  
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **transform_mismatches** (_bool_)
  * **fade_transform_mismatches** (_bool_)
  * **key_map** (_dict_ _|__None_)


_original__init__(_mobject_ , _target_mobject_ , _transform_mismatches =False_, _fade_transform_mismatches =False_, _key_map =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingTex._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **transform_mismatches** (_bool_)
  * **fade_transform_mismatches** (_bool_)
  * **key_map** (_dict_ _|__None_)


[ Next updaters ](https://docs.manim.community/en/stable/reference/<manim.animation.updaters.html>) [ Previous TransformMatchingShapes ](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingShapes.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TransformMatchingTex](https://docs.manim.community/en/stable/reference/<#>)
    * `[TransformMatchingTex`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingTex>)
      * `[TransformMatchingTex._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingTex._original__init__>)


