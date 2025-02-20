# Transform[¶](https://docs.manim.community/en/stable/reference/<#transform> "Link to this heading")
Qualified name: `manim.animation.transform.Transform`
_class_ Transform(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#Transform>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform> "Link to this definition")
    
Bases: `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
A Transform transforms a Mobject into a target Mobject.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__None_) – The `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") to be transformed. It will be mutated to become the `target_mobject`.
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__None_) – The target of the transformation.
  * **path_func** (_Callable_ _|__None_) – A function defining the path that the points of the `mobject` are being moved along until they match the points of the `target_mobject`, see `[utils.paths`](https://docs.manim.community/en/stable/reference/<manim.utils.paths.html#module-manim.utils.paths> "manim.utils.paths").
  * **path_arc** (_float_) – The arc angle (in radians) that the points of `mobject` will follow to reach the points of the target if using a circular path arc, see `path_arc_centers`. See also `[manim.utils.paths.path_along_arc()`](https://docs.manim.community/en/stable/reference/<manim.utils.paths.html#manim.utils.paths.path_along_arc> "manim.utils.paths.path_along_arc").
  * **path_arc_axis** (_np.ndarray_) – The axis to rotate along if using a circular path arc, see `path_arc_centers`.
  * **path_arc_centers** (_np.ndarray_) – 
The center of the circular arcs along which the points of `mobject` are moved by the transformation.
If this is set and `path_func` is not set, then a `path_along_circles` path will be generated using the `path_arc` parameters and stored in `path_func`. If `path_func` is set, this and the other `path_arc` fields are set as attributes, but a `path_func` is not generated from it.
  * **replace_mobject_with_target_in_scene** (_bool_) – 
Controls which mobject is replaced when the transformation is complete.
If set to True, `mobject` will be removed from the scene and `target_mobject` will replace it. Otherwise, `target_mobject` is never added and `mobject` just takes its shape.


Examples
Example: TransformPathArc [¶](https://docs.manim.community/en/stable/reference/<#transformpatharc>)
```
frommanimimport *
classTransformPathArc(Scene):
  defconstruct(self):
    defmake_arc_path(start, end, arc_angle):
      points = []
      p_fn = path_along_arc(arc_angle)
      # alpha animates between 0.0 and 1.0, where 0.0
      # is the beginning of the animation and 1.0 is the end.
      for alpha in range(0, 11):
        points.append(p_fn(start, end, alpha / 10.0))
      path = VMobject(stroke_color=YELLOW)
      path.set_points_smoothly(points)
      return path
    left = Circle(stroke_color=BLUE_E, fill_opacity=1.0, radius=0.5).move_to(LEFT * 2)
    colors = [TEAL_A, TEAL_B, TEAL_C, TEAL_D, TEAL_E, GREEN_A]
    # Positive angles move counter-clockwise, negative angles move clockwise.
    examples = [-90, 0, 30, 90, 180, 270]
    anims = []
    for idx, angle in enumerate(examples):
      left_c = left.copy().shift((3 - idx) * UP)
      left_c.fill_color = colors[idx]
      right_c = left_c.copy().shift(4 * RIGHT)
      path_arc = make_arc_path(left_c.get_center(), right_c.get_center(),
                   arc_angle=angle * DEGREES)
      desc = Text('%d°' % examples[idx]).next_to(left_c, LEFT)
      # Make the circles in front of the text in front of the arcs.
      self.add(
        path_arc.set_z_index(1),
        desc.set_z_index(2),
        left_c.set_z_index(3),
      )
      anims.append(Transform(left_c, right_c, path_arc=angle * DEGREES))
    self.play(*anims, run_time=2)
    self.wait()

```
Copy to clipboard
Make interactive
Methods
`[begin`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.begin> "manim.animation.transform.Transform.begin") | Begin the animation.  
---|---  
`[clean_up_from_scene`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.clean_up_from_scene> "manim.animation.transform.Transform.clean_up_from_scene") | Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.  
`create_target`  
`get_all_families_zipped`  
`[get_all_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.get_all_mobjects> "manim.animation.transform.Transform.get_all_mobjects") | Get all mobjects involved in the animation.  
`interpolate_submobject`  
Attributes
`path_arc`  
---  
`path_func`  
`run_time`  
_original__init__(_mobject_ , _target_mobject =None_, _path_func =None_, _path_arc =0_, _path_arc_axis =array([0., 0., 1.])_, _path_arc_centers =None_, _replace_mobject_with_target_in_scene =False_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__None_)
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__None_)
  * **path_func** (_Callable_ _|__None_)
  * **path_arc** (_float_)
  * **path_arc_axis** (_ndarray_)
  * **path_arc_centers** (_ndarray_)
  * **replace_mobject_with_target_in_scene** (_bool_)


Return type:
    
None
begin()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#Transform.begin>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.begin> "Link to this definition")
    
Begin the animation.
This method is called right as an animation is being played. As much initialization as possible, especially any mobject copying, should live in this method.
Return type:
    
None
clean_up_from_scene(_scene_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#Transform.clean_up_from_scene>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.clean_up_from_scene> "Link to this definition")
    
Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.
This includes to `[remove()`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove> "manim.scene.scene.Scene.remove") the Animation’s `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") if the animation is a remover.
Parameters:
    
**scene** ([_Scene_](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.
Return type:
    
None
get_all_mobjects()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform.html#Transform.get_all_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.get_all_mobjects> "Link to this definition")
    
Get all mobjects involved in the animation.
Ordering must match the ordering of arguments to interpolate_submobject
Returns:
    
The sequence of mobjects.
Return type:
    
Sequence[[Mobject](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")]
[ Next TransformAnimations ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.TransformAnimations.html>) [ Previous Swap ](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Swap.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Transform](https://docs.manim.community/en/stable/reference/<#>)
    * `[Transform`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform>)
      * `[Transform._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform._original__init__>)
      * `[Transform.begin()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.begin>)
      * `[Transform.clean_up_from_scene()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.clean_up_from_scene>)
      * `[Transform.get_all_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform.Transform.get_all_mobjects>)


