# TransformMatchingShapes[¶](https://docs.manim.community/en/stable/reference/<#transformmatchingshapes> "Link to this heading")
Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingShapes`
_class_ TransformMatchingShapes(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform_matching_parts.html#TransformMatchingShapes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingShapes> "Link to this definition")
    
Bases: `[TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase> "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")
An animation trying to transform groups by matching the shape of their submobjects.
Two submobjects match if the hash of their point coordinates after normalization (i.e., after translation to the origin, fixing the submobject height at 1 unit, and rounding the coordinates to three decimal places) matches.
See also
`[TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html#manim.animation.transform_matching_parts.TransformMatchingAbstractBase> "manim.animation.transform_matching_parts.TransformMatchingAbstractBase")
Examples
Example: Anagram [¶](https://docs.manim.community/en/stable/reference/<#anagram>)
```
frommanimimport *
classAnagram(Scene):
  defconstruct(self):
    src = Text("the morse code")
    tar = Text("here come dots")
    self.play(Write(src))
    self.wait(0.5)
    self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
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


_original__init__(_mobject_ , _target_mobject_ , _transform_mismatches =False_, _fade_transform_mismatches =False_, _key_map =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingShapes._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **transform_mismatches** (_bool_)
  * **fade_transform_mismatches** (_bool_)
  * **key_map** (_dict_ _|__None_)


[ Next TransformMatchingTex ](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingTex.html>) [ Previous TransformMatchingAbstractBase ](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingAbstractBase.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TransformMatchingShapes](https://docs.manim.community/en/stable/reference/<#>)
    * `[TransformMatchingShapes`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingShapes>)
      * `[TransformMatchingShapes._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingShapes._original__init__>)


