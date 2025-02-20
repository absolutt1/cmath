# TipableVMobject[¶](https://docs.manim.community/en/stable/reference/<#tipablevmobject> "Link to this heading")
Qualified name: `manim.mobject.geometry.arc.TipableVMobject`
_class_ TipableVMobject(_tip_length =0.35_, _normal_vector =array([0., 0., 1.])_, _tip_style ={}_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject> "Link to this definition")
    
Bases: `[VMobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
Meant for shared functionality between Arc and Line. Functionality can be classified broadly into these groups:
>   * Adding, Creating, Modifying tips
>     
>     * add_tip calls create_tip, before pushing the new tip
>     
> into the TipableVMobject’s list of submobjects
>     * stylistic and positional configuration
>   * Checking for tips
>     
>     * Boolean checks for whether the TipableVMobject has a tip
>     
> and a starting tip
>   * Getters
>     
>     * Straightforward accessors, returning information pertaining
>     
> to the TipableVMobject instance’s tip(s), its length etc
> 

Methods
`[add_tip`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.add_tip> "manim.mobject.geometry.arc.TipableVMobject.add_tip") | Adds a tip to the TipableVMobject instance, recognising that the endpoints might need to be switched if it's a 'starting tip' or not.  
---|---  
`asign_tip_attr`  
`[create_tip`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.create_tip> "manim.mobject.geometry.arc.TipableVMobject.create_tip") | Stylises the tip, positions it spatially, and returns the newly instantiated tip to the caller.  
`get_default_tip_length`  
`[get_end`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_end> "manim.mobject.geometry.arc.TipableVMobject.get_end") | Returns the point, where the stroke that surrounds the `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") ends.  
`get_first_handle`  
`get_last_handle`  
`get_length`  
`[get_start`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_start> "manim.mobject.geometry.arc.TipableVMobject.get_start") | Returns the point, where the stroke that surrounds the `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") starts.  
`[get_tip`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_tip> "manim.mobject.geometry.arc.TipableVMobject.get_tip") | Returns the TipableVMobject instance's (first) tip, otherwise throws an exception.  
`[get_tips`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_tips> "manim.mobject.geometry.arc.TipableVMobject.get_tips") | Returns a VGroup (collection of VMobjects) containing the TipableVMObject instance's tips.  
`[get_unpositioned_tip`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip> "manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip") | Returns a tip that has been stylistically configured, but has not yet been given a position in space.  
`has_start_tip`  
`has_tip`  
`pop_tips`  
`position_tip`  
`reset_endpoints_based_on_tip`  
Attributes
`animate` | Used to animate the application of any method of `self`.  
---|---  
`animation_overrides`  
`color`  
`depth` | The depth of the mobject.  
`fill_color` | If there are multiple colors (for gradient) this returns the first one  
`height` | The height of the mobject.  
`n_points_per_curve`  
`sheen_factor`  
`stroke_color`  
`width` | The width of the mobject.  
Parameters:
    
  * **tip_length** (_float_)
  * **normal_vector** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D"))
  * **tip_style** (_dict_)
  * **kwargs** (_Any_)


_original__init__(_tip_length =0.35_, _normal_vector =array([0., 0., 1.])_, _tip_style ={}_, _** kwargs_)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject._original__init__> "Link to this definition")
    
Initialize self. See help(type(self)) for accurate signature.
Parameters:
    
  * **tip_length** (_float_)
  * **normal_vector** ([_Vector3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Vector3D> "manim.typing.Vector3D"))
  * **tip_style** (_dict_)
  * **kwargs** (_Any_)


Return type:
    
None
add_tip(_tip =None_, _tip_shape =None_, _tip_length =None_, _tip_width =None_, _at_start =False_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject.add_tip>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.add_tip> "Link to this definition")
    
Adds a tip to the TipableVMobject instance, recognising that the endpoints might need to be switched if it’s a ‘starting tip’ or not.
Parameters:
    
  * **tip** ([_tips.ArrowTip_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip") _|__None_)
  * **tip_shape** (_type_ _[_[_tips.ArrowTip_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip") _]__|__None_)
  * **tip_length** (_float_ _|__None_)
  * **tip_width** (_float_ _|__None_)
  * **at_start** (_bool_)


Return type:
    
Self
create_tip(_tip_shape =None_, _tip_length =None_, _tip_width =None_, _at_start =False_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject.create_tip>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.create_tip> "Link to this definition")
    
Stylises the tip, positions it spatially, and returns the newly instantiated tip to the caller.
Parameters:
    
  * **tip_shape** (_type_ _[_[_tips.ArrowTip_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip") _]__|__None_)
  * **tip_length** (_float_ _|__None_)
  * **tip_width** (_float_ _|__None_)
  * **at_start** (_bool_)


Return type:
    
[tips.ArrowTip](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip")
get_end()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_end>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_end> "Link to this definition")
    
Returns the point, where the stroke that surrounds the `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") ends.
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
get_start()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_start>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_start> "Link to this definition")
    
Returns the point, where the stroke that surrounds the `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") starts.
Return type:
    
[_Point3D_](https://docs.manim.community/en/stable/reference/<manim.typing.html#manim.typing.Point3D> "manim.typing.Point3D")
get_tip()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_tip>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_tip> "Link to this definition")
    
Returns the TipableVMobject instance’s (first) tip, otherwise throws an exception.
Return type:
    
[_VMobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject> "manim.mobject.types.vectorized_mobject.VMobject")
get_tips()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_tips>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_tips> "Link to this definition")
    
Returns a VGroup (collection of VMobjects) containing the TipableVMObject instance’s tips.
Return type:
    
[_VGroup_](https://docs.manim.community/en/stable/reference/<manim.mobject.types.vectorized_mobject.VGroup.html#manim.mobject.types.vectorized_mobject.VGroup> "manim.mobject.types.vectorized_mobject.VGroup")
get_unpositioned_tip(_tip_shape =None_, _tip_length =None_, _tip_width =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/geometry/arc.html#TipableVMobject.get_unpositioned_tip>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip> "Link to this definition")
    
Returns a tip that has been stylistically configured, but has not yet been given a position in space.
Parameters:
    
  * **tip_shape** (_type_ _[_[_tips.ArrowTip_](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip") _]__|__None_)
  * **tip_length** (_float_ _|__None_)
  * **tip_width** (_float_ _|__None_)


Return type:
    
[tips.ArrowTip](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTip.html#manim.mobject.geometry.tips.ArrowTip> "manim.mobject.geometry.tips.ArrowTip") | [tips.ArrowTriangleFilledTip](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.tips.ArrowTriangleFilledTip.html#manim.mobject.geometry.tips.ArrowTriangleFilledTip> "manim.mobject.geometry.tips.ArrowTriangleFilledTip")
[ Next boolean_ops ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.boolean_ops.html>) [ Previous Sector ](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.arc.Sector.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [TipableVMobject](https://docs.manim.community/en/stable/reference/<#>)
    * `[TipableVMobject`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject>)
      * `[TipableVMobject._original__init__()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject._original__init__>)
      * `[TipableVMobject.add_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.add_tip>)
      * `[TipableVMobject.create_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.create_tip>)
      * `[TipableVMobject.get_end()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_end>)
      * `[TipableVMobject.get_start()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_start>)
      * `[TipableVMobject.get_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_tip>)
      * `[TipableVMobject.get_tips()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_tips>)
      * `[TipableVMobject.get_unpositioned_tip()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.geometry.arc.TipableVMobject.get_unpositioned_tip>)


