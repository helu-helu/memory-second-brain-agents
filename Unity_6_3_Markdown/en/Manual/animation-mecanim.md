* [Animation](AnimationSection.html)
* Mecanim Animation system

Animation

Introduction to Mecanim Animation system

# Mecanim Animation system

The Mecanim Animation system is based on [animation clips](AnimationClips.html)Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). An animation clip contains information about how a character or **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) changes its position, rotation, or other properties over time. This section contains information on how to work with the Mecanim Animation system in Unity.

| **Topic** | **Description** |
| --- | --- |
| **[Introduction to Mecanim Animation system](AnimationOverview.html)** | Learn how clips, controllers, **avatars**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html) See in [Glossary](Glossary.html#Avatar), and the Animator component work together. |
| **[Animation clips](animation-clips-landing.html)** | Explore clip workflows, from import and editing to events, masks, and looping. |
| **[Humanoid Avatar](AvatarCreationandSetup.html)** | Set up humanoid avatars so Unity can map and retarget character animation. |
| **[Animator component](class-Animator.html)A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](class-AnimatorController.html) See in [Glossary](Glossary.html#AnimatorComponent)** | Assign controllers and avatars, then configure **root motion**Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](RootMotion.html) See in [Glossary](Glossary.html#RootMotion), updates, and culling. |
| **[Animator Controller](animation-animator-controller.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html) See in [Glossary](Glossary.html#AnimatorController)** | Build **state machines**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html) See in [Glossary](Glossary.html#StateMachine) that drive clips, transitions, and character animation flow. |
| **[Animator Override Controller](AnimatorOverrideController.html)Allows you to create multiple variants of an Animator Controller, with each variant using a different set of animations, while retaining the original Controller’s structure, parameters and logic. [More info](AnimatorOverrideController.html) See in [Glossary](Glossary.html#AnimatorOverrideController)** | Reuse one state machine and swap clips for character-specific animation variants. |
| **[Playables API](Playables.html)** | Create and evaluate **playable graphs**An API for controlling Playables. Playable Graphs allow you to create, connect and destroy playables. [More info](Playables-Graph.html) See in [Glossary](Glossary.html#PlayableGraph) to blend and control animation at runtime. |
| **[Performance and optimization](MecanimPeformanceandOptimization.html)** | Improve animation runtime cost with focused controller, layer, and curve optimizations. |
| **[Mecanim FAQ](MecanimFAQ.html)** | Resolve common Mecanim questions about windows, import behavior, and layers. |

## Additional resources

* [Legacy Animation system](Animations.html)
* [Models](models.html)A 3D model representation of an object, such as a character, a building, or a piece of furniture. [More info](3D-formats.html)  
  See in [Glossary](Glossary.html#model)

Animation

Introduction to Mecanim Animation system

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)