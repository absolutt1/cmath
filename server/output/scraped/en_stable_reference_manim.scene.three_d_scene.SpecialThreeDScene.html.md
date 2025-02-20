
# SpecialThreeDScene[¶](https://docs.manim.community/en/stable/reference/<#specialthreedscene> "Link to this heading")
Qualified name: `manim.scene.three\_d\_scene.SpecialThreeDScene`
_class_ SpecialThreeDScene(_cut_axes_at_radius =True_, _camera_config ={'exponential_projection': True, 'should_apply_shading': True}_, _three_d_axes_config ={'axis_config': {'numbers_with_elongated_ticks': [0, 1, 2], 'stroke_width': 2, 'tick_frequency': 1, 'unit_size': 2}, 'num_axis_pieces': 1}_, _sphere_config ={'radius': 2, 'resolution': (24, 48)}_, _default_angled_camera_position ={'phi': 1.2217304763960306, 'theta': -1.9198621771937625}_, _low_quality_config ={'camera_config': {'should_apply_shading': False}, 'sphere_config': {'resolution': (12, 24)}, 'three_d_axes_config': {'num_axis_pieces': 1}}_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene> "Link to this definition")
    
Bases: `[ThreeDScene`](https://docs.manim.community/en/stable/reference/<manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene> "manim.scene.three_d_scene.ThreeDScene")
An extension of `[ThreeDScene`](https://docs.manim.community/en/stable/reference/<manim.scene.three_d_scene.ThreeDScene.html#manim.scene.three_d_scene.ThreeDScene> "manim.scene.three_d_scene.ThreeDScene") with more settings.
It has some extra configuration for axes, spheres, and an override for low quality rendering. Further key differences are:
  * The camera shades applicable 3DMobjects by default, except if rendering in low quality.
  * Some default params for Spheres and Axes have been added.


Methods
`[get_axes`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_axes> "manim.scene.three_d_scene.SpecialThreeDScene.get_axes") | Return a set of 3D axes.  
---|---  
`[get_default_camera_position`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position> "manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position") | Returns the default_angled_camera position.  
`[get_sphere`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_sphere> "manim.scene.three_d_scene.SpecialThreeDScene.get_sphere") | Returns a sphere with the passed keyword arguments as properties.  
`[set_camera_to_default_position`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position> "manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position") | Sets the camera to its default position.  
Attributes
`camera`  
---  
`time` | The time since the start of the scene.  
get_axes()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.get_axes>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_axes> "Link to this definition")
    
Return a set of 3D axes.
Returns:
    
A set of 3D axes.
Return type:
    
`[ThreeDAxes`](https://docs.manim.community/en/stable/reference/<manim.mobject.graphing.coordinate_systems.ThreeDAxes.html#manim.mobject.graphing.coordinate_systems.ThreeDAxes> "manim.mobject.graphing.coordinate_systems.ThreeDAxes")
get_default_camera_position()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.get_default_camera_position>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position> "Link to this definition")
    
Returns the default_angled_camera position.
Returns:
    
Dictionary of phi, theta, focal_distance, and gamma.
Return type:
    
dict
get_sphere(_** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.get_sphere>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_sphere> "Link to this definition")
    
Returns a sphere with the passed keyword arguments as properties.
Parameters:
    
****kwargs** – Any valid parameter of `[Sphere`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere") or `[Surface`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Surface.html#manim.mobject.three_d.three_dimensions.Surface> "manim.mobject.three_d.three_dimensions.Surface").
Returns:
    
The sphere object.
Return type:
    
`[Sphere`](https://docs.manim.community/en/stable/reference/<manim.mobject.three_d.three_dimensions.Sphere.html#manim.mobject.three_d.three_dimensions.Sphere> "manim.mobject.three_d.three_dimensions.Sphere")
set_camera_to_default_position()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#SpecialThreeDScene.set_camera_to_default_position>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position> "Link to this definition")
    
Sets the camera to its default position.
[ Next ThreeDScene ](https://docs.manim.community/en/stable/reference/<manim.scene.three_d_scene.ThreeDScene.html>) [ Previous three_d_scene ](https://docs.manim.community/en/stable/reference/<manim.scene.three_d_scene.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [SpecialThreeDScene](https://docs.manim.community/en/stable/reference/<#>)
    * `[SpecialThreeDScene`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene>)
      * `[SpecialThreeDScene.get_axes()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_axes>)
      * `[SpecialThreeDScene.get_default_camera_position()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_default_camera_position>)
      * `[SpecialThreeDScene.get_sphere()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.get_sphere>)
      * `[SpecialThreeDScene.set_camera_to_default_position()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.SpecialThreeDScene.set_camera_to_default_position>)


