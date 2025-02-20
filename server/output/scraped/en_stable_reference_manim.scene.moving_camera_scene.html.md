# moving_camera_scene[¶](https://docs.manim.community/en/stable/reference/<#module-manim.scene.moving_camera_scene> "Link to this heading")
A scene whose camera can be moved around.
See also
`[moving_camera`](https://docs.manim.community/en/stable/reference/<manim.camera.moving_camera.html#module-manim.camera.moving_camera> "manim.camera.moving_camera")
Examples
Example: ChangingCameraWidthAndRestore [¶](https://docs.manim.community/en/stable/reference/<#changingcamerawidthandrestore>)
```
frommanimimport *
classChangingCameraWidthAndRestore(MovingCameraScene):
  defconstruct(self):
    text = Text("Hello World").set_color(BLUE)
    self.add(text)
    self.camera.frame.save_state()
    self.play(self.camera.frame.animate.set(width=text.width * 1.2))
    self.wait(0.3)
    self.play(Restore(self.camera.frame))

```
Copy to clipboard
Make interactive
Example: MovingCameraCenter [¶](https://docs.manim.community/en/stable/reference/<#movingcameracenter>)
```
frommanimimport *
classMovingCameraCenter(MovingCameraScene):
  defconstruct(self):
    s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
    t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
    self.wait(0.3)
    self.add(s, t)
    self.play(self.camera.frame.animate.move_to(s))
    self.wait(0.3)
    self.play(self.camera.frame.animate.move_to(t))

```
Copy to clipboard
Make interactive
Example: MovingAndZoomingCamera [¶](https://docs.manim.community/en/stable/reference/<#movingandzoomingcamera>)
```
frommanimimport *
classMovingAndZoomingCamera(MovingCameraScene):
  defconstruct(self):
    s = Square(color=BLUE, fill_opacity=0.5).move_to(2 * LEFT)
    t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 * RIGHT)
    self.add(s, t)
    self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
    self.wait(0.3)
    self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))
    self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))

```
Copy to clipboard
Make interactive
Example: MovingCameraOnGraph [¶](https://docs.manim.community/en/stable/reference/<#movingcameraongraph>)
```
frommanimimport *
classMovingCameraOnGraph(MovingCameraScene):
  defconstruct(self):
    self.camera.frame.save_state()
    ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
    graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])
    dot_1 = Dot(ax.i2gp(graph.t_min, graph))
    dot_2 = Dot(ax.i2gp(graph.t_max, graph))
    self.add(ax, graph, dot_1, dot_2)
    self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
    self.play(self.camera.frame.animate.move_to(dot_2))
    self.play(Restore(self.camera.frame))
    self.wait()

```
Copy to clipboard
Make interactive
Example: SlidingMultipleScenes [¶](https://docs.manim.community/en/stable/reference/<#slidingmultiplescenes>)
```
frommanimimport *
classSlidingMultipleScenes(MovingCameraScene):
  defconstruct(self):
    defcreate_scene(number):
      frame = Rectangle(width=16,height=9)
      circ = Circle().shift(LEFT)
      text = Tex(f"This is Scene {str(number)}").next_to(circ, RIGHT)
      frame.add(circ,text)
      return frame
    group = VGroup(*(create_scene(i) for i in range(4))).arrange_in_grid(buff=4)
    self.add(group)
    self.camera.auto_zoom(group[0], animate=False)
    for scene in group:
      self.play(self.camera.auto_zoom(scene))
      self.wait()
    self.play(self.camera.auto_zoom(group, margin=2))

```
Copy to clipboard
Make interactive
Classes
`[MovingCameraScene`](https://docs.manim.community/en/stable/reference/<manim.scene.moving_camera_scene.MovingCameraScene.html#manim.scene.moving_camera_scene.MovingCameraScene> "manim.scene.moving_camera_scene.MovingCameraScene") | This is a Scene, with special configurations and properties that make it suitable for cases where the camera must be moved around.  
---|---  
[ Next MovingCameraScene ](https://docs.manim.community/en/stable/reference/<manim.scene.moving_camera_scene.MovingCameraScene.html>) [ Previous Scenes ](https://docs.manim.community/en/stable/reference/<../reference_index/scenes.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
