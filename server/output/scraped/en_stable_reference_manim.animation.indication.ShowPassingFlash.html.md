# ShowPassingFlash[¶](https://docs.manim.community/en/stable/reference/<#showpassingflash> "Link to this heading")
Qualified name: `manim.animation.indication.ShowPassingFlash`
_class_ ShowPassingFlash(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#ShowPassingFlash>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ShowPassingFlash> "Link to this definition")
    
Bases: `[ShowPartial`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.ShowPartial.html#manim.animation.creation.ShowPartial> "manim.animation.creation.ShowPartial")
Show only a sliver of the VMobject each frame.
Parameters:
    
  * **mobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")) – The mobject whose stroke is animated.
  * **time_width** (_float_) – The length of the sliver relative to the length of the stroke.


Examples
Example: TimeWidthValues [¶](https://docs.manim.community/en/stable/reference/<#timewidthvalues>)
```
frommanimimport *
classTimeWidthValues(Scene):
  defconstruct(self):
    p = RegularPolygon(5, color=DARK_GRAY, stroke_width=6).scale(3)
    lbl = VMobject()
    self.add(p, lbl)
    p = p.copy().set_color(BLUE)
    for time_width in [0.2, 0.5, 1, 2]:
      lbl.become(Tex(r"\texttt{time\_width={{%.1f}}}"%time_width))
      self.play(ShowPassingFlash(
        p.copy().set_color(BLUE),
        run_time=2,
        time_width=time_width
      ))

```
Copy to clipboard
Make interactive
See also
`[Create`](https://docs.manim.community/en/stable/reference/<manim.animation.creation.Create.html#manim.animation.creation.Create> "manim.animation.creation.Create")
Methods
`[clean_up_from_scene`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ShowPassingFlash.clean_up_from_scene> "manim.animation.indication.ShowPassingFlash.clean_up_from_scene") | Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.  
---|---  
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _time_width =0.1_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ShowPassingFlash._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject"))
  * **time_width** (_float_)


Return type:
    
None
clean_up_from_scene(_scene_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/indication.html#ShowPassingFlash.clean_up_from_scene>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ShowPassingFlash.clean_up_from_scene> "Link to this definition")
    
Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.
This includes to `[remove()`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove> "manim.scene.scene.Scene.remove") the Animation’s `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") if the animation is a remover.
Parameters:
    
**scene** ([_Scene_](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.
Return type:
    
None
[ Next ShowPassingFlashWithThinningStrokeWidth ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.ShowPassingFlashWithThinningStrokeWidth.html>) [ Previous Indicate ](https://docs.manim.community/en/stable/reference/<manim.animation.indication.Indicate.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ShowPassingFlash](https://docs.manim.community/en/stable/reference/<#>)
    * `[ShowPassingFlash`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ShowPassingFlash>)
      * `[ShowPassingFlash._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ShowPassingFlash._original__init__>)
      * `[ShowPassingFlash.clean_up_from_scene()`](https://docs.manim.community/en/stable/reference/<#manim.animation.indication.ShowPassingFlash.clean_up_from_scene>)


