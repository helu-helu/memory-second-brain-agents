* [Animation](AnimationSection.html)
* [Legacy Animation system](animation-legacy.html)
* Legacy Animation component

Introduction to Legacy Animation system

Audio

# Legacy Animation component

[Switch to Scripting](../ScriptReference/Animation.html "Go to Animation page in the Scripting Reference")

This is the Legacy Animation component, which was used on **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) for animation purposes prior to the introduction of the Mecanim Animation system.
This component is retained in Unity for backwards compatibility. For new projects, use the [Animator component](class-Animator.html)A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent).

![The Animation Inspector](../uploads/Main/AnimationInspector35.png)


The Animation Inspector

## Properties

| **Property** | **Function** |
| --- | --- |
| **Animation** | The default animation to play when **Play Automatically** is enabled. |
| **Animations** | A list of animations that you can access from **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts). |
| **Play Automatically** | Enable this option to play animation automatically when the game starts. |
| **Animate Physics** | Enable this option to have the animation interact with Physics. |
| **Culling Type** | Determine when not to play the animation.  * **Always Animate**: Always animate. * **Based on Renderers**: Cull based on the default animation pose. |

Consult the [Animation Window Guide](AnimationEditorGuide.html) for more information on how to create animations inside Unity.
Consult [Model import workflows](ImportingModelFiles.html) page on how to import animated characters.

Introduction to Legacy Animation system

Audio

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)