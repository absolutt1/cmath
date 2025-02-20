# animation[¶](https://docs.manim.community/en/stable/reference/<#module-manim.animation.animation> "Link to this heading")
Animate mobjects.
Classes
`[Add`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Add.html#manim.animation.animation.Add> "manim.animation.animation.Add") | Add Mobjects to a scene, without animating them in any other way.  
---|---  
`[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") | An animation.  
`[Wait`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Wait.html#manim.animation.animation.Wait> "manim.animation.animation.Wait") | A "no operation" animation.  
Functions
override_animation(_animation_class_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#override_animation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.override_animation> "Link to this definition")
    
Decorator used to mark methods as overrides for specific `[Animation`](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") types.
Should only be used to decorate methods of classes derived from `[Mobject`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject> "manim.mobject.mobject.Mobject"). `Animation` overrides get inherited to subclasses of the `Mobject` who defined them. They don’t override subclasses of the `Animation` they override.
See also
`[add_animation_override()`](https://docs.manim.community/en/stable/reference/<manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_animation_override> "manim.mobject.mobject.Mobject.add_animation_override")
Parameters:
    
**animation_class** (_type_ _[_[_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") _]_) – The animation to be overridden.
Returns:
    
The actual decorator. This marks the method as overriding an animation.
Return type:
    
Callable[[Callable], Callable]
Examples
Example: OverrideAnimationExample [¶](https://docs.manim.community/en/stable/reference/<#overrideanimationexample>)
```
frommanimimport *
classMySquare(Square):
  @override_animation(FadeIn)
  def_fade_in_override(self, **kwargs):
    return Create(self, **kwargs)
classOverrideAnimationExample(Scene):
  defconstruct(self):
    self.play(FadeIn(MySquare()))

```
Copy to clipboard
Make interactive
prepare_animation(_anim_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/animation/animation.html#prepare_animation>)[¶](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.prepare_animation> "Link to this definition")
    
Returns either an unchanged animation, or the animation built from a passed animation factory.
Examples
```
>>> frommanimimport Square, FadeIn
>>> s = Square()
>>> prepare_animation(FadeIn(s))
FadeIn(Square)

```
Copy to clipboard
```
>>> prepare_animation(s.animate.scale(2).rotate(42))
_MethodAnimation(Square)

```
Copy to clipboard
```
>>> prepare_animation(42)
Traceback (most recent call last):
...
TypeError: Object 42 cannot be converted to an animation

```
Copy to clipboard
Parameters:
    
**anim** ([_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation") _|___AnimationBuilder_)
Return type:
    
[_Animation_](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Animation.html#manim.animation.animation.Animation> "manim.animation.animation.Animation")
[ Next Add ](https://docs.manim.community/en/stable/reference/<manim.animation.animation.Add.html>) [ Previous Animations ](https://docs.manim.community/en/stable/reference/<../reference_index/animations.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [animation](https://docs.manim.community/en/stable/reference/<#>)
    * `[override_animation()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.override_animation>)
    * `[prepare_animation()`](https://docs.manim.community/en/stable/reference/<#manim.animation.animation.prepare_animation>)


