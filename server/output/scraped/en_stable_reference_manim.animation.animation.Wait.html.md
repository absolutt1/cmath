# Wait[¶](https://docs.manim.community/en/stable/reference/<#wait> "Link to this heading")
Qualified name: `manim.animation.animation.Wait`
_class_ Wait(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#Wait>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
A “no operation” animation.
Parameters:
    
  * **run_time** (_float_) – The amount of time that should pass.
  * **stop_condition** (_Callable_ _[__[__]__,__bool_ _]__|__None_) – A function without positional arguments that evaluates to a boolean. The function is evaluated after every new frame has been rendered. Playing the animation stops after the return value is truthy, or after the specified `run_time` has passed.
  * **frozen_frame** (_bool_ _|__None_) – Controls whether or not the wait animation is static, i.e., corresponds to a frozen frame. If `False` is passed, the render loop still progresses through the animation as usual and (among other things) continues to call updater functions. If `None` (the default value), the `[Scene.play()`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene.play> "manim.scene.scene.Scene.play") call tries to determine whether the Wait call can be static or not itself via `Scene.should_mobjects_update()`.
  * **kwargs** – Keyword arguments to be passed to the parent class, `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation").
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)


Methods
`[begin`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.begin> "manim.animation.animation.Wait.begin") | Begin the animation.  
---|---  
`[clean_up_from_scene`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.clean_up_from_scene> "manim.animation.animation.Wait.clean_up_from_scene") | Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.  
`[finish`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.finish> "manim.animation.animation.Wait.finish") | Finish the animation.  
`[interpolate`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.interpolate> "manim.animation.animation.Wait.interpolate") | Set the animation progress.  
`[update_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.update_mobjects> "manim.animation.animation.Wait.update_mobjects") | Updates things like starting_mobject, and (for Transforms) target_mobject.  
Attributes
`run_time`  
---  
_original__init__(_run_time=1_ , _stop_condition=None_ , _frozen_frame=None_ , _rate_func= <function linear>_, _**kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **run_time** (_float_)
  * **stop_condition** (_Callable_ _[__[__]__,__bool_ _]__|__None_)
  * **frozen_frame** (_bool_ _|__None_)
  * **rate_func** (_Callable_ _[__[__float_ _]__,__float_ _]_)


begin()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#Wait.begin>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.begin> "Link to this definition")
    
Begin the animation.
This method is called right as an animation is being played. As much initialization as possible, especially any mobject copying, should live in this method.
Return type:
    
None
clean_up_from_scene(_scene_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#Wait.clean_up_from_scene>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.clean_up_from_scene> "Link to this definition")
    
Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.
This includes to `[remove()`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove> "manim.scene.scene.Scene.remove") the Animation’s `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") if the animation is a remover.
Parameters:
    
**scene** ([_Scene_](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.
Return type:
    
None
finish()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#Wait.finish>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.finish> "Link to this definition")
    
Finish the animation.
This method gets called when the animation is over.
Return type:
    
None
interpolate(_alpha_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#Wait.interpolate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.interpolate> "Link to this definition")
    
Set the animation progress.
This method gets called for every frame during an animation.
Parameters:
    
**alpha** (_float_) – The relative time to set the animation to, 0 meaning the start, 1 meaning the end.
Return type:
    
None
update_mobjects(_dt_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#Wait.update_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.update_mobjects> "Link to this definition")
    
Updates things like starting_mobject, and (for Transforms) target_mobject. Note, since typically (always?) self.mobject will have its updating suspended during the animation, this will do nothing to self.mobject.
Parameters:
    
**dt** (_float_)
Return type:
    
None
[ Next changing ](https://docs.manim.community/en/stable/reference/<manim.animation.changing.html>) [ Previous Animation ](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Wait](https://docs.manim.community/en/stable/reference/<#>)
    * `[Wait`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait>)
      * `[Wait._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait._original__init__>)
      * `[Wait.begin()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.begin>)
      * `[Wait.clean_up_from_scene()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.clean_up_from_scene>)
      * `[Wait.finish()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.finish>)
      * `[Wait.interpolate()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.interpolate>)
      * `[Wait.update_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.Wait.update_mobjects>)


