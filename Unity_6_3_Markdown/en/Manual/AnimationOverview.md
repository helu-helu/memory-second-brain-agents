* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* Introduction to Mecanim Animation system

Mecanim Animation system

Animation clips

# Introduction to Mecanim Animation system

The Mecanim Animation system is based on [animation clips](AnimationClips.html)Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). An animation clip contains information about how a character or **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) changes its position, rotation, or other properties over time. Think of each animation clip as a recording. An animation clip from an external source is created by an artist or animator with third-party software, such as Autodesk® 3ds Max® or Autodesk® Maya®.

You can organize many animation clips into a structured flowchart-like system called an [Animator Controller](class-AnimatorController.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController). The Animator Controller acts as a [state machine](AnimationStateMachines.html)The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) which keeps track of the animation clip being played and the criteria for when the next animation clip should be played.

For example, a simple Animator Controller might contain a single animation clip for a collectable item that spins and bounces. An Animator Controller for a door might contain two animation clips: one for the door opening and a second for the door closing.

A more advanced Animator Controller might contain a dozen **humanoid animations**An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Humanoidanimation) for each of a character’s actions such as idle, turning, walking, and jogging. This Animator Controller might use [blend trees](class-BlendTree.html) to blend between multiple animation clips and provide fluid motion as the player moves around the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

The Mecanim Animation system also provides special features for handling humanoid characters including the ability to [retarget](Retargeting.html) animation from one source to another and adjust [muscle definitions](MuscleDefinitions.html)This allows you to have more intuitive control over the character’s skeleton. When an Avatar is in place, the Animation system works in muscle space, which is more intuitive than bone space. [More info](MuscleDefinitions.html)  
See in [Glossary](Glossary.html#muscledefinition) to ensure that a character deforms correctly. For example, you can retarget animation from a third-party animation library to your own character then adjust the its range of motion. These special features are available through Unity’s [Avatar](AvatarCreationandSetup.html)An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) system which maps humanoid characters to a common internal format.

The Animation Clips, the Animator Controller, and the Avatar, are connected together through a GameObject with the [Animator Component](class-Animator.html)A component on a model that animates that model using the Animation system. The component has a reference to an Animator Controller asset that controls the animation. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent). This component references an Animator Controller and, if required, the Avatar for the model. The Animator Controller also references its animation clips.

![How the parts of the Mecanim Animation system connect together](../uploads/Main/MecanimHowItFitsTogether.jpg)


How the parts of the Mecanim Animation system connect together

The previous diagram demonstrates the following workflow:

1. Animation clips are [imported from an external source](class-AnimationClip.html) or created within Unity. In this example, they are [imported humanoid animations](ConfiguringtheAvatar.html).
2. Animation clips are placed and arranged in an Animator Controller. This demonstrates an Animator Controller in the **Animator window**The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html)  
   See in [Glossary](Glossary.html#AnimatorWindow). The States, which may represent animations or nested sub-state machines, display as nodes connected by lines. This Animator Controller exists as an asset in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
   See in [Glossary](Glossary.html#Projectwindow).
3. The rigged character model, an astronaut named `Astrella`, has a specific configuration of bones mapped to Unity’s [Avatar](class-Avatar.html) format. The mapping is stored as an Avatar asset, under the imported character model in the Project window.
4. When animating the character model, it has an Animator component attached. In the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector) window, the [Animator Component](class-Animator.html) has the [Animator Controller](class-AnimatorController.html) and the [Avatar](class-Avatar.html) assigned. The animator uses these together to animate the model. The Avatar reference is only necessary when animating a humanoid character. For [other types of animation](GenericAnimations.html), only an Animator Controller is required.

The following topics provide more details on the Mecanim Animation system:

* [Animation Clips](AnimationClips.html)
* [Humanoid Avatars](AvatarCreationandSetup.html)
* [Animator component](class-Animator.html)
* [Animator Controller](class-AnimatorController.html)
* [Animator Override Controller](AnimatorOverrideController.html)Allows you to create multiple variants of an Animator Controller, with each variant using a different set of animations, while retaining the original Controller’s structure, parameters and logic. [More info](AnimatorOverrideController.html)  
  See in [Glossary](Glossary.html#AnimatorOverrideController)
* [Playables API](Playables.html)
* [Performance and Optimization](MecanimPeformanceandOptimization.html)
* [Mecanim FAQ](MecanimFAQ.html)

Mecanim Animation system

Animation clips

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)