* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* Animator Controller

Animator component

Introduction to Animator Controllers

# Animator Controller

Use an **Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) to arrange and maintain a set of **Animation Clips**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) and associated **Animation Transitions**Allows a state machine to switch or blend from one animation state to another. Transitions define how long a blend between states should take, and the conditions that activate them. [More info](StateMachineTransitions.html)  
See in [Glossary](Glossary.html#AnimationTransition) for a character or an animated **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

| **Topic** | **Description** |
| --- | --- |
| **[Introduction to Animator Controllers](class-AnimatorController.html)** | Learn how the Animator Controller uses **state machines**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html) See in [Glossary](Glossary.html#StateMachine) to manage clips and transitions. |
| **[Create an Animator Controller](AnimatorControllerCreation.html)** | Build an Animator Controller asset from the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html) See in [Glossary](Glossary.html#Projectwindow) or Assets menu. |
| **[Animator Controller Asset](Animator.html)** | Reference for the Animator Controller asset that maintains your character’s animations. |
| **[Animator window](AnimatorWindow.html)The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html) See in [Glossary](Glossary.html#AnimatorWindow)** | Create, view, and modify Animator Controller assets in the Animator Window. |
| **[Animation state machine](AnimationStateMachines.html)A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](AnimationStateMachines.html) See in [Glossary](Glossary.html#AnimationStateMachine)** | Arrange animations into graphs to control action flow. |

## Additional resources

* [Animation Layers](AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](AnimationLayers.html)  
  See in [Glossary](Glossary.html#AnimationLayer)
* [Humanoid Avatar](AvatarCreationandSetup.html)

Animator component

Introduction to Animator Controllers

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)