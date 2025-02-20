# TransformMatchingAbstractBase[¶](https://docs.manim.community/en/stable/reference/<#transformmatchingabstractbase> "Link to this heading")
Qualified name: `manim.animation.transform\_matching\_parts.TransformMatchingAbstractBase`
_class_ TransformMatchingAbstractBase(_mobject =None_, _* args_, _use_override =True_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform_matching_parts.html#TransformMatchingAbstractBase>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingAbstractBase> "Link to this definition")
    
Bases: `[AnimationGroup`](https://docs.manim.community/en/stable/reference/<manim.animation.composition.AnimationGroup.html#manim.animation.composition.AnimationGroup> "manim.animation.composition.AnimationGroup")
Abstract base class for transformations that keep track of matching parts.
Subclasses have to implement the two static methods `get_mobject_parts()` and `get_mobject_key()`.
Basically, this transformation first maps all submobjects returned by the `get_mobject_parts` method to certain keys by applying the `get_mobject_key` method. Then, submobjects with matching keys are transformed into each other.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The starting `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The target `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").
  * **transform_mismatches** (_bool_) – Controls whether submobjects without a matching key are transformed into each other by using `[Transform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.Transform.html#manim.animation.transform.Transform> "manim.animation.transform.Transform"). Default: `False`.
  * **fade_transform_mismatches** (_bool_) – Controls whether submobjects without a matching key are transformed into each other by using `[FadeTransform`](https://docs.manim.community/en/stable/reference/<manim.animation.transform.FadeTransform.html#manim.animation.transform.FadeTransform> "manim.animation.transform.FadeTransform"). Default: `False`.
  * **key_map** (_dict_ _|__None_) – Optional. A dictionary mapping keys belonging to some of the starting mobject’s submobjects (i.e., the return values of the `get_mobject_key` method) to some keys belonging to the target mobject’s submobjects that should be transformed although the keys don’t match.
  * **kwargs** – All further keyword arguments are passed to the submobject transformations.


Note
If neither `transform_mismatches` nor `fade_transform_mismatches` are set to `True`, submobjects without matching keys in the starting mobject are faded out in the direction of the unmatched submobjects in the target mobject, and unmatched submobjects in the target mobject are faded in from the direction of the unmatched submobjects in the start mobject.
Methods
`[clean_up_from_scene`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene> "manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene") | Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.  
---|---  
`get_mobject_key`  
`get_mobject_parts`  
`get_shape_map`  
Attributes
`run_time`  
---  
_original__init__(_mobject_ , _target_mobject_ , _transform_mismatches =False_, _fade_transform_mismatches =False_, _key_map =None_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingAbstractBase._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **target_mobject** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"))
  * **transform_mismatches** (_bool_)
  * **fade_transform_mismatches** (_bool_)
  * **key_map** (_dict_ _|__None_)


clean_up_from_scene(_scene_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/transform_matching_parts.html#TransformMatchingAbstractBase.clean_up_from_scene>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene> "Link to this definition")
    
Clean up the `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") after finishing the animation.
This includes to `[remove()`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene.remove> "manim.scene.scene.Scene.remove") the Animation’s `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") if the animation is a remover.
Parameters:
    
**scene** ([_Scene_](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene")) – The scene the animation should be cleaned up from.
Return type:
    
None
[ Next TransformMatchingShapes ](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.TransformMatchingShapes.html>) [ Previous transform_matching_parts ](https://docs.manim.community/en/stable/reference/<manim.animation.transform_matching_parts.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TransformMatchingAbstractBase](https://docs.manim.community/en/stable/reference/<#>)
    * `[TransformMatchingAbstractBase`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingAbstractBase>)
      * `[TransformMatchingAbstractBase._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingAbstractBase._original__init__>)
      * `[TransformMatchingAbstractBase.clean_up_from_scene()`](https://docs.manim.community/en/stable/reference/<#manim.animation.transform_matching_parts.TransformMatchingAbstractBase.clean_up_from_scene>)


