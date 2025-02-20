# mobject[¶](https://docs.manim.community/en/stable/reference/<#module-manim.mobject.mobject> "Link to this heading")
Base classes for objects that can be displayed.
Type Aliases
_class_ TimeBasedUpdater[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.TimeBasedUpdater> "Link to this definition")
    
```
Callable[['Mobject', float], object]

```
Copy to clipboard
_class_ NonTimeBasedUpdater[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.NonTimeBasedUpdater> "Link to this definition")
    
```
Callable[['Mobject'], object]

```
Copy to clipboard
_class_ Updater[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.Updater> "Link to this definition")
```
NonTimeBasedUpdater` | TimeBasedUpdater`
```

Classes
`[Group`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Group.html#manim.mobject.mobject.Group> "manim.mobject.mobject.Group") | Groups together multiple `[Mobjects`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject").  
---|---  
`[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject") | Mathematical Object: base class for objects that can be displayed on screen.  
Functions
override_animate(_method_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/mobject/mobject.html#override_animate>)[¶](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.override_animate> "Link to this definition")
    
Decorator for overriding method animations.
This allows to specify a method (returning an `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")) which is called when the decorated method is used with the `.animate` syntax for animating the application of a method.
See also
`[Mobject.animate`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate> "manim.mobject.mobject.Mobject.animate")
Note
Overridden methods cannot be combined with normal or other overridden methods using method chaining with the `.animate` syntax.
Examples
Example: AnimationOverrideExample [¶](https://docs.manim.community/en/stable/reference/<#animationoverrideexample>)
```
frommanimimport *
classCircleWithContent(VGroup):
  def__init__(self, content):
    super().__init__()
    self.circle = Circle()
    self.content = content
    self.add(self.circle, content)
    content.move_to(self.circle.get_center())
  defclear_content(self):
    self.remove(self.content)
    self.content = None
  @override_animate(clear_content)
  def_clear_content_animation(self, anim_args=None):
    if anim_args is None:
      anim_args = {}
    anim = Uncreate(self.content, **anim_args)
    self.clear_content()
    return anim
classAnimationOverrideExample(Scene):
  defconstruct(self):
    t = Text("hello!")
    my_mobject = CircleWithContent(t)
    self.play(Create(my_mobject))
    self.play(my_mobject.animate.clear_content())
    self.wait()

```
Copy to clipboard
Make interactive
Return type:
    
_LambdaType_
[ Next Group ](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Group.html>) [ Previous MobjectMatrix ](https://docs.manim.community/en/stable/reference/<manim.mobject.matrix.MobjectMatrix.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [mobject](https://docs.manim.community/en/stable/reference/<#>)
    * `[TimeBasedUpdater`](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.TimeBasedUpdater>)
    * `[NonTimeBasedUpdater`](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.NonTimeBasedUpdater>)
    * `[Updater`](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.Updater>)
    * `[override_animate()`](https://docs.manim.community/en/stable/reference/<#manim.mobject.mobject.override_animate>)


