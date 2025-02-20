# MovingCameraScene[¶](https://docs.manim.community/en/stable/reference/<#movingcamerascene> "Link to this heading")
Qualified name: `manim.scene.moving\_camera\_scene.MovingCameraScene`
_class_ MovingCameraScene(_camera_class= <class 'manim.camera.moving_camera.MovingCamera'>_, _**kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/moving_camera_scene.html#MovingCameraScene>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.moving_camera_scene.MovingCameraScene> "Link to this definition")
    
Bases: `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene")
This is a Scene, with special configurations and properties that make it suitable for cases where the camera must be moved around.
Note: Examples are included in the moving_camera_scene module documentation, see below in the ‘see also’ section.
See also
`[moving_camera_scene`](https://docs.manim.community/en/stable/reference/<manim.scene.moving_camera_scene.html#module-manim.scene.moving_camera_scene> "manim.scene.moving_camera_scene") `[MovingCamera`](https://docs.manim.community/en/stable/reference/<manim.camera.moving_camera.MovingCamera.html#manim.camera.moving_camera.MovingCamera> "manim.camera.moving_camera.MovingCamera")
Methods
`[get_moving_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.scene.moving_camera_scene.MovingCameraScene.get_moving_mobjects> "manim.scene.moving_camera_scene.MovingCameraScene.get_moving_mobjects") | This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed.  
---|---  
Attributes
`camera`  
---  
`time` | The time since the start of the scene.  
get_moving_mobjects(_* animations_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/moving_camera_scene.html#MovingCameraScene.get_moving_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.moving_camera_scene.MovingCameraScene.get_moving_mobjects> "Link to this definition")
    
This method returns a list of all of the Mobjects in the Scene that are moving, that are also in the animations passed.
Parameters:
    
***animations** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")) – The Animations whose mobjects will be checked.
[ Next section ](https://docs.manim.community/en/stable/reference/<manim.scene.section.html>) [ Previous moving_camera_scene ](https://docs.manim.community/en/stable/reference/<manim.scene.moving_camera_scene.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MovingCameraScene](https://docs.manim.community/en/stable/reference/<#>)
    * `[MovingCameraScene`](https://docs.manim.community/en/stable/reference/<#manim.scene.moving_camera_scene.MovingCameraScene>)
      * `[MovingCameraScene.get_moving_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.scene.moving_camera_scene.MovingCameraScene.get_moving_mobjects>)


