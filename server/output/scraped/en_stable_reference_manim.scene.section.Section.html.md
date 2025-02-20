# Section[¶](https://docs.manim.community/en/stable/reference/<#section> "Link to this heading")
Qualified name: `manim.scene.section.Section`
_class_ Section(_type__ , _video_ , _name_ , _skip_animations_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/section.html#Section>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section> "Link to this definition")
    
Bases: `object`
A `[Scene`](https://docs.manim.community/en/stable/reference/<manim.scene.scene.Scene.html#manim.scene.scene.Scene> "manim.scene.scene.Scene") can be segmented into multiple Sections. Refer to [the documentation](https://docs.manim.community/en/stable/reference/<../tutorials/output_and_config.html>) for more info. It consists of multiple animations.
Parameters:
    
  * **type_** (_str_)
  * **video** (_str_ _|__None_)
  * **name** (_str_)
  * **skip_animations** (_bool_)


type\\_
    
Can be used by a third party applications to classify different types of sections.
video[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.video> "Link to this definition")
    
Path to video file with animations belonging to section relative to sections directory. If `None`, then the section will not be saved.
name[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.name> "Link to this definition")
    
Human readable, non-unique name for this section.
skip_animations[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.skip_animations> "Link to this definition")
    
Skip rendering the animations in this section when `True`.
partial_movie_files[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.partial_movie_files> "Link to this definition")
    
Animations belonging to this section.
See also
`[DefaultSectionType`](https://docs.manim.community/en/stable/reference/<manim.scene.section.DefaultSectionType.html#manim.scene.section.DefaultSectionType> "manim.scene.section.DefaultSectionType"), `CairoRenderer.update_skipping_status()`, `OpenGLRenderer.update_skipping_status()`
Methods
`[get_clean_partial_movie_files`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.get_clean_partial_movie_files> "manim.scene.section.Section.get_clean_partial_movie_files") | Return all partial movie files that are not `None`.  
---|---  
`[get_dict`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.get_dict> "manim.scene.section.Section.get_dict") | Get dictionary representation with metadata of output video.  
`[is_empty`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.is_empty> "manim.scene.section.Section.is_empty") | Check whether this section is empty.  
get_clean_partial_movie_files()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/section.html#Section.get_clean_partial_movie_files>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.get_clean_partial_movie_files> "Link to this definition")
    
Return all partial movie files that are not `None`.
Return type:
    
list[str]
get_dict(_sections_dir_)[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/section.html#Section.get_dict>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.get_dict> "Link to this definition")
    
Get dictionary representation with metadata of output video.
The output from this function is used from every section to build the sections index file. The output video must have been created in the `sections_dir` before executing this method. This is the main part of the Segmented Video API.
Parameters:
    
**sections_dir** (_Path_)
Return type:
    
dict[str, _Any_]
is_empty()[[source]](https://docs.manim.community/en/stable/reference/<../_modules/manim/scene/section.html#Section.is_empty>)[¶](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.is_empty> "Link to this definition")
    
Check whether this section is empty.
Note that animations represented by `None` are also counted.
Return type:
    
bool
[ Next scene ](https://docs.manim.community/en/stable/reference/<manim.scene.scene.html>) [ Previous DefaultSectionType ](https://docs.manim.community/en/stable/reference/<manim.scene.section.DefaultSectionType.html>)
Copyright © 2020-2025, The Manim Community Dev Team 
Made with [Sphinx](https://docs.manim.community/en/stable/reference/<https:/www.sphinx-doc.org/>) and [@pradyunsg](https://docs.manim.community/en/stable/reference/<https:/pradyunsg.me>)'s [Furo](https://docs.manim.community/en/stable/reference/<https:/github.com/pradyunsg/furo>)
On this page 
  * [Section](https://docs.manim.community/en/stable/reference/<#>)
    * `[Section`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section>)
      * `[Section.video`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.video>)
      * `[Section.name`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.name>)
      * `[Section.skip_animations`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.skip_animations>)
      * `[Section.partial_movie_files`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.partial_movie_files>)
      * `[Section.get_clean_partial_movie_files()`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.get_clean_partial_movie_files>)
      * `[Section.get_dict()`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.get_dict>)
      * `[Section.is_empty()`](https://docs.manim.community/en/stable/reference/<#manim.scene.section.Section.is_empty>)


