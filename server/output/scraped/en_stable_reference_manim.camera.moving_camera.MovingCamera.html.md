# MovingCamera[¶](https://docs.manim.community/en/stable/reference/<#movingcamera> "Link to this heading")
Qualified name: `manim.camera.moving\_camera.MovingCamera`
_class_ MovingCamera(_frame =None_, _fixed_dimension =0_, _default_frame_stroke_color =ManimColor('#FFFFFF')_, _default_frame_stroke_width =0_, _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/moving_camera.html#MovingCamera>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera> "Link to this definition")
    
Bases: `[Camera`](https://docs.manim.community/en/stable/reference/<manim.camera.camera.Camera.html#manim.camera.camera.Camera> "manim.camera.camera.Camera")
Stays in line with the height, width and position of it’s ‘frame’, which is a Rectangle
See also
`[MovingCameraScene`](https://docs.manim.community/en/stable/reference/<manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene> "manim.scene.moving_camera_scene.MovingCameraScene")
Frame is a Mobject, (should almost certainly be a rectangle) determining which region of space the camera displays
Methods
`[auto_zoom`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.auto_zoom> "manim.camera.moving_camera.MovingCamera.auto_zoom") | Zooms on to a given array of mobjects (or a singular mobject) and automatically resizes to frame all the mobjects.  
---|---  
`[cache_cairo_context`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.cache_cairo_context> "manim.camera.moving_camera.MovingCamera.cache_cairo_context") | Since the frame can be moving around, the cairo context used for updating should be regenerated at each frame.  
`[capture_mobjects`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.capture_mobjects> "manim.camera.moving_camera.MovingCamera.capture_mobjects") | Capture mobjects by printing them on `pixel_array`.  
`[get_cached_cairo_context`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.get_cached_cairo_context> "manim.camera.moving_camera.MovingCamera.get_cached_cairo_context") | Since the frame can be moving around, the cairo context used for updating should be regenerated at each frame.  
`[get_mobjects_indicating_movement`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.get_mobjects_indicating_movement> "manim.camera.moving_camera.MovingCamera.get_mobjects_indicating_movement") | Returns all mobjects whose movement implies that the camera should think of all other mobjects on the screen as moving  
Attributes
`background_color`  
---  
`background_opacity`  
`[frame_center`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_center> "manim.camera.moving_camera.MovingCamera.frame_center") | Returns the centerpoint of the frame in cartesian coordinates.  
`[frame_height`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_height> "manim.camera.moving_camera.MovingCamera.frame_height") | Returns the height of the frame.  
`[frame_width`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_width> "manim.camera.moving_camera.MovingCamera.frame_width") | Returns the width of the frame  
auto_zoom(_mobjects_ , _margin =0_, _only_mobjects_in_frame =False_, _animate =True_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/moving_camera.html#MovingCamera.auto_zoom>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.auto_zoom> "Link to this definition")
    
Zooms on to a given array of mobjects (or a singular mobject) and automatically resizes to frame all the mobjects.
Note
This method only works when 2D-objects in the XY-plane are considered, it will not work correctly when the camera has been rotated.
Parameters:
    
  * **mobjects** (_list_ _[_[_Mobject_](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") _]_) – The mobject or array of mobjects that the camera will focus on.
  * **margin** (_float_) – The width of the margin that is added to the frame (optional, 0 by default).
  * **only_mobjects_in_frame** (_bool_) – If set to `True`, only allows focusing on mobjects that are already in frame.
  * **animate** (_bool_) – If set to `False`, applies the changes instead of returning the corresponding animation


Returns:
    
_AnimationBuilder that zooms the camera view to a given list of mobjects or ScreenRectangle with position and size updated to zoomed position.
Return type:
    
[Union](https://docs.manim.community/en/stable/reference/<manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union> "manim.mobject.geometry.boolean_ops.Union")[_AnimationBuilder, [ScreenRectangle](https://docs.manim.community/en/stable/reference/<manim.mobject.frame.ScreenRectangle.html#manim.mobject.frame.ScreenRectangle> "manim.mobject.frame.ScreenRectangle")]
cache_cairo_context(_pixel_array_ , _ctx_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/moving_camera.html#MovingCamera.cache_cairo_context>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.cache_cairo_context> "Link to this definition")
    
Since the frame can be moving around, the cairo context used for updating should be regenerated at each frame. So no caching.
capture_mobjects(_mobjects_ , _** kwargs_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/moving_camera.html#MovingCamera.capture_mobjects>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.capture_mobjects> "Link to this definition")
    
Capture mobjects by printing them on `pixel_array`.
This is the essential function that converts the contents of a Scene into an array, which is then converted to an image or video.
Parameters:
    
  * **mobjects** – Mobjects to capture.
  * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.


Notes
For a list of classes that can currently be rendered, see `display_funcs()`.
_property_ frame_center[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_center> "Link to this definition")
    
Returns the centerpoint of the frame in cartesian coordinates.
Returns:
    
The cartesian coordinates of the center of the frame.
Return type:
    
np.array
_property_ frame_height[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_height> "Link to this definition")
    
Returns the height of the frame.
Returns:
    
The height of the frame.
Return type:
    
float
_property_ frame_width[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_width> "Link to this definition")
    
Returns the width of the frame
Returns:
    
The width of the frame.
Return type:
    
float
get_cached_cairo_context(_pixel_array_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/moving_camera.html#MovingCamera.get_cached_cairo_context>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.get_cached_cairo_context> "Link to this definition")
    
Since the frame can be moving around, the cairo context used for updating should be regenerated at each frame. So no caching.
get_mobjects_indicating_movement()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/camera/moving_camera.html#MovingCamera.get_mobjects_indicating_movement>)[¶](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.get_mobjects_indicating_movement> "Link to this definition")
    
Returns all mobjects whose movement implies that the camera should think of all other mobjects on the screen as moving
Return type:
    
list
[ Next multi_camera ](https://docs.manim.community/en/stable/reference/<manim.camera.multi_camera.html>) [ Previous moving_camera ](https://docs.manim.community/en/stable/reference/<manim.camera.moving_camera.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [MovingCamera](https://docs.manim.community/en/stable/reference/<#>)
    * `[MovingCamera`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera>)
      * `[MovingCamera.auto_zoom()`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.auto_zoom>)
      * `[MovingCamera.cache_cairo_context()`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.cache_cairo_context>)
      * `[MovingCamera.capture_mobjects()`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.capture_mobjects>)
      * `[MovingCamera.frame_center`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_center>)
      * `[MovingCamera.frame_height`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_height>)
      * `[MovingCamera.frame_width`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.frame_width>)
      * `[MovingCamera.get_cached_cairo_context()`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.get_cached_cairo_context>)
      * `[MovingCamera.get_mobjects_indicating_movement()`](https://docs.manim.community/en/stable/reference/<#manim.camera.moving_camera.MovingCamera.get_mobjects_indicating_movement>)


