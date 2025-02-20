
# ThreeDScene[¶](https://docs.manim.community/en/stable/reference/<#threedscene> "Link to this heading")
Qualified name: `manim.scene.three\_d\_scene.ThreeDScene`
_class_ ThreeDScene(_camera_class= <class 'manim.camera.three_d_camera.ThreeDCamera'>_, _ambient_camera_rotation=None_ , _default_angled_camera_orientation_kwargs=None_ , _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene> "Link to this definition")
    
Bases: `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene")
This is a Scene, with special configurations and properties that make it suitable for Three Dimensional Scenes.
Methods
`[add_fixed_in_frame_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects> "manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects") | This method is used to prevent the rotation and movement of mobjects as the camera moves around.  
---|---  
`[add_fixed_orientation_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects> "manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects") | This method is used to prevent the rotation and tilting of mobjects as the camera moves around.  
`[begin_3dillusion_camera_rotation`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation> "manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation") | This method creates a 3D camera rotation illusion around the current camera orientation.  
`[begin_ambient_camera_rotation`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation> "manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation") | This method begins an ambient rotation of the camera about the Z_AXIS, in the anticlockwise direction  
`[get_moving_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects> "manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects") | This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed.  
`[move_camera`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.move_camera> "manim.scene.three_d_scene.ThreeDScene.move_camera") | This method animates the movement of the camera to the given spherical coordinates.  
`[remove_fixed_in_frame_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects> "manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects") | This method undoes what add_fixed_in_frame_mobjects does.  
`[remove_fixed_orientation_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects> "manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects") | This method "unfixes" the orientation of the mobjects passed, meaning they will no longer be at the same angle relative to the camera.  
`[set_camera_orientation`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation> "manim.scene.three_d_scene.ThreeDScene.set_camera_orientation") | This method sets the orientation of the camera in the scene.  
`[set_to_default_angled_camera_orientation`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation> "manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation") | This method sets the default_angled_camera_orientation to the keyword arguments passed, and sets the camera to that orientation.  
`[stop_3dillusion_camera_rotation`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation> "manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation") | This method stops all illusion camera rotations.  
`[stop_ambient_camera_rotation`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation> "manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation") | This method stops all ambient camera rotation.  
Attributes
`camera`  
---  
`time` | The time since the start of the scene.  
add_fixed_in_frame_mobjects(_* mobjects_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.add_fixed_in_frame_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects> "Link to this definition")
    
This method is used to prevent the rotation and movement of mobjects as the camera moves around. The mobject is essentially overlaid, and is not impacted by the camera’s movement in any way.
Parameters:
    
***mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The Mobjects whose orientation must be fixed.
add_fixed_orientation_mobjects(_* mobjects_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.add_fixed_orientation_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects> "Link to this definition")
    
This method is used to prevent the rotation and tilting of mobjects as the camera moves around. The mobject can still move in the x,y,z directions, but will always be at the angle (relative to the camera) that it was at when it was passed through this method.)
Parameters:
    
  * ***mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The Mobject(s) whose orientation must be fixed.
  * ****kwargs** – 
Some valid kwargs are
    
use_static_center_func : bool center_func : function


begin_3dillusion_camera_rotation(_rate =1_, _origin_phi =None_, _origin_theta =None_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.begin_3dillusion_camera_rotation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation> "Link to this definition")
    
This method creates a 3D camera rotation illusion around the current camera orientation.
Parameters:
    
  * **rate** (_float_) – The rate at which the camera rotation illusion should operate.
  * **origin_phi** (_float_ _|__None_) – The polar angle the camera should move around. Defaults to the current phi angle.
  * **origin_theta** (_float_ _|__None_) – The azimutal angle the camera should move around. Defaults to the current theta angle.


begin_ambient_camera_rotation(_rate =0.02_, _about ='theta'_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.begin_ambient_camera_rotation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation> "Link to this definition")
    
This method begins an ambient rotation of the camera about the Z_AXIS, in the anticlockwise direction
Parameters:
    
  * **rate** (_float_) – The rate at which the camera should rotate about the Z_AXIS. Negative rate means clockwise rotation.
  * **about** (_str_) – one of 3 options: [“theta”, “phi”, “gamma”]. defaults to theta.


get_moving_mobjects(_* animations_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.get_moving_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects> "Link to this definition")
    
This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed.
Parameters:
    
***animations** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")) – The animations whose mobjects will be checked.
move_camera(_phi =None_, _theta =None_, _gamma =None_, _zoom =None_, _focal_distance =None_, _frame_center =None_, _added_anims =[]_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.move_camera>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.move_camera> "Link to this definition")
    
This method animates the movement of the camera to the given spherical coordinates.
Parameters:
    
  * **phi** (_float_ _|__None_) – The polar angle i.e the angle between Z_AXIS and Camera through ORIGIN in radians.
  * **theta** (_float_ _|__None_) – The azimuthal angle i.e the angle that spins the camera around the Z_AXIS.
  * **focal_distance** (_float_ _|__None_) – The radial focal_distance between ORIGIN and Camera.
  * **gamma** (_float_ _|__None_) – The rotation of the camera about the vector from the ORIGIN to the Camera.
  * **zoom** (_float_ _|__None_) – The zoom factor of the camera.
  * **frame_center** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__Sequence_ _[__float_ _]__|__None_) – The new center of the camera frame in cartesian coordinates.
  * **added_anims** (_Iterable_ _[_[_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") _]_) – Any other animations to be played at the same time.


remove_fixed_in_frame_mobjects(_* mobjects_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.remove_fixed_in_frame_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects> "Link to this definition")
    
> This method undoes what add_fixed_in_frame_mobjects does. It allows the mobject to be affected by the movement of the camera.
Parameters:
    
***mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The Mobjects whose position and orientation must be unfixed.
remove_fixed_orientation_mobjects(_* mobjects_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.remove_fixed_orientation_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects> "Link to this definition")
    
This method “unfixes” the orientation of the mobjects passed, meaning they will no longer be at the same angle relative to the camera. This only makes sense if the mobject was passed through add_fixed_orientation_mobjects first.
Parameters:
    
***mobjects** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject")) – The Mobjects whose orientation must be unfixed.
set_camera_orientation(_phi =None_, _theta =None_, _gamma =None_, _zoom =None_, _focal_distance =None_, _frame_center =None_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.set_camera_orientation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation> "Link to this definition")
    
This method sets the orientation of the camera in the scene.
Parameters:
    
  * **phi** (_float_ _|__None_) – The polar angle i.e the angle between Z_AXIS and Camera through ORIGIN in radians.
  * **theta** (_float_ _|__None_) – The azimuthal angle i.e the angle that spins the camera around the Z_AXIS.
  * **focal_distance** (_float_ _|__None_) – The focal_distance of the Camera.
  * **gamma** (_float_ _|__None_) – The rotation of the camera about the vector from the ORIGIN to the Camera.
  * **zoom** (_float_ _|__None_) – The zoom factor of the scene.
  * **frame_center** ([_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _|__Sequence_ _[__float_ _]__|__None_) – The new center of the camera frame in cartesian coordinates.


set_to_default_angled_camera_orientation(_** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.set_to_default_angled_camera_orientation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation> "Link to this definition")
    
This method sets the default_angled_camera_orientation to the keyword arguments passed, and sets the camera to that orientation.
Parameters:
    
****kwargs** – Some recognised kwargs are phi, theta, focal_distance, gamma, which have the same meaning as the parameters in set_camera_orientation.
stop_3dillusion_camera_rotation()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.stop_3dillusion_camera_rotation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation> "Link to this definition")
    
This method stops all illusion camera rotations.
stop_ambient_camera_rotation(_about ='theta'_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/three_d_scene.html#ThreeDScene.stop_ambient_camera_rotation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation> "Link to this definition")
    
This method stops all ambient camera rotation.
[ Next vector_space_scene ](https://docs.manim.community/en/stable/reference/<manim.scene.vector_space_scene.html>) [ Previous SpecialThreeDScene ](https://docs.manim.community/en/stable/reference/<manim.scene.three_d_scene.SpecialThreeDScene.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [ThreeDScene](https://docs.manim.community/en/stable/reference/<#>)
    * `[ThreeDScene`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene>)
      * `[ThreeDScene.add_fixed_in_frame_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.add_fixed_in_frame_mobjects>)
      * `[ThreeDScene.add_fixed_orientation_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.add_fixed_orientation_mobjects>)
      * `[ThreeDScene.begin_3dillusion_camera_rotation()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.begin_3dillusion_camera_rotation>)
      * `[ThreeDScene.begin_ambient_camera_rotation()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.begin_ambient_camera_rotation>)
      * `[ThreeDScene.get_moving_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.get_moving_mobjects>)
      * `[ThreeDScene.move_camera()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.move_camera>)
      * `[ThreeDScene.remove_fixed_in_frame_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.remove_fixed_in_frame_mobjects>)
      * `[ThreeDScene.remove_fixed_orientation_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.remove_fixed_orientation_mobjects>)
      * `[ThreeDScene.set_camera_orientation()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.set_camera_orientation>)
      * `[ThreeDScene.set_to_default_angled_camera_orientation()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.set_to_default_angled_camera_orientation>)
      * `[ThreeDScene.stop_3dillusion_camera_rotation()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.stop_3dillusion_camera_rotation>)
      * `[ThreeDScene.stop_ambient_camera_rotation()`](https://docs.manim.community/en/stable/reference/<#manim.scene.three_d_scene.ThreeDScene.stop_ambient_camera_rotation>)


