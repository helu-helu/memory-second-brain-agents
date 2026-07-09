* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animation clips](animation-clips-landing.html)
* Animation from external sources

Introduction to animation clips

Animation window

# Animation from external sources

Animation from external sources are imported into Unity in the same way as regular 3D files. These files, whether they’re generic FBX files or recognized 3D software formats such as Autodesk® Maya®, Cinema 4D, Autodesk® 3ds Max®, or Blender™, can contain animation data in the form of a linear recording of the movements of objects within the file.

![An imported FBX 3D Asset containing an animation titled Run](../uploads/Main/AnimationSelectingImportedClip.png)


An imported FBX 3D Asset containing an animation titled `Run`

Sometimes, the object you want to animate (for example, a character) and its animations are in the same file. In other cases, the animations might exist in a separate file from the object you want to animate.

It may be that animations are specific to a particular model, and cannot be re-used on other models. For example, a giant octopus end-boss in your game might have a unique arrangement of limbs and bones, and its own set of animations.

In other situations, it may be that you have a library of animations which are to be used on various different models in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). For example, a number of different humanoid characters might all use the same walk and run animations. In these situations, it’s common to have a simple placeholder model in your animation files for the purposes of previewing them. Alternatively, it is possible to use animation files even if they have no geometry at all, just the animation data.

When importing multiple animations, the animations can each exist as separate files within your project folder, or you can extract multiple **animation clips**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) from a single FBX file if exported as takes from MotionBuilder or with a **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) or script for Autodesk® Maya®, Autodesk® 3ds Max® or other 3D packages. You might want to do this if your file contains multiple separate animations arranged on a single timeline. For example, a long motion captured timeline might contain the animation for a few different jump motions, and you may want to cut out certain sections of this to use as individual clips and discard the rest. Unity provides animation cutting tools to achieve this when you import all animations in one timeline by allowing you to select the frame range for each clip.

## Import animation files

Before you can use any animation in Unity, you must first import it into your project. Unity can import Autodesk® Maya® (.mb or .ma), Autodesk® 3ds Max® (.max), and Blender™ (.blend), and also generic FBX files which [you can export from most animation software](3D-formats.html). Note that importing from .blend files requires a local installation of Blender™.

For more information, consult [Importing](ImportingAssets.html).

## View and copy data from imported animation files

You can view the **keyframes**A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) and curves of imported animation clips in the Animation window. If these imported clips have many bones with many keyframes, the amount of animation data can be overwhelming. For example, the following image shows bones and keyframes for a run animation:

![Imported animation clips contain many keyframes and curves.](../uploads/Main/AnimationViewingImportedCurves.jpg)


Imported animation clips contain many keyframes and curves.

To limit the animation data being displayed, select only the bones you are interested in examining. The Animation window displays only the keyframes or curves for the selected bones.

![Limit the view to only the selected bones or properties.](../uploads/Main/AnimationViewingImportedCurvesSelected.png)


Limit the view to only the selected bones or properties.

When viewing imported Animation keyframes, the Animation window provides a read-only view of the animation data. You cannot edit this data, but you can edit a copy of the Animation data by copying and pasting keyframes into a new Animation clip. To create a copy of Animation data from a read only FBX file, follow these steps:

1. In the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
   See in [Glossary](Glossary.html#Projectwindow), select the FBX file with the animation data that you want to copy.
2. In the Animation window, select the properties to limit the amount of animation data being displayed.
3. Select the keyframes that you want to copy.
4. Press **Ctrl+C** (macOS: **Cmd+C**) to copy the selected keyframes.
5. Create a new empty Animation Clip for the **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject) where you want to paste the copied keyframes. Consult [Creating a new Animation Clip](animeditor-CreatingANewAnimationClip.html).
6. Press **Ctrl-V** (macOS: **Cmd+V**) to paste the copied keyframes.

For best results, the GameObject where you are pasting should have the same hierarchy and properties as the animation data you are copying. For example, if you are copying properties for chest and head movement from an FBX file, the GameObject should have chest and head properties.

![Selected keyframes from an imported clip.](../uploads/Main/AnimationSelectingKeysOnImportedClip.png)


Selected keyframes from an imported clip.

If the GameObject does not have the same properties, the animation data is copied, but the properties are drawn in yellow. Hovering over the name of the property displays the message `The GameObject or Component are missing`.

Introduction to animation clips

Animation window

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)