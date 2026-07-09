* [Visual effects](visual-effects.html)
* [Particle effects](ParticleSystems.html)
* Access the Particle System from the Animation system

Optimize the Particle System with the C# Job System

Particle System component reference

# Access the Particle System from the Animation system

All **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) properties are accessible by the Animation system, meaning you can **keyframe**A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) them in and control them from your animations.

To access the **Particle System**A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem)’s properties, follow these steps:

1. Attach an **Animator component**A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](class-AnimatorController.html)  
   See in [Glossary](Glossary.html#AnimatorComponent) to the Particle System’s **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject). An Animation Controller and an Animation are also required.
2. To animate a Particle System property, open the **Animation Window** with the GameObject containing the Animator and Particle System selected. Click **Add Property** to add properties.
3. Scroll to the right to reveal the **add controls**.

Note that for curves, you can only keyframe the overall **curve multiplier**, which can be found next to the curve editor in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

Optimize the Particle System with the C# Job System

Particle System component reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)