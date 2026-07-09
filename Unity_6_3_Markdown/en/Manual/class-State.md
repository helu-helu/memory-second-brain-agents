* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* [Animation state machine](AnimationStateMachines.html)
* Animation States

State machine basics

Animation Parameters

# Animation States

**Animation States** are the basic building blocks of an **Animation **State Machine**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine)**. Each state contains an animation sequence (or [blend tree](class-BlendTree.html)) that plays when the character is in that state. Select the state in the ****Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController)**, to view the properties for the state in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

![Animation State properties in the Inspector window.](../uploads/Main/anim-insp-state-properties.png)


Animation State properties in the Inspector window.

| ***Property:*** | ***Description:*** |
| --- | --- |
| **Motion** | The **animation clip**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html) See in [Glossary](Glossary.html#AnimationClip) or blend tree assigned to this state. |
| **Speed** | The default speed of the motion for this state. Enable Parameter to modify the speed with a custom value from a script. For example, you can multiply the speed with a custom value to decelerate or accelerate the play speed. |
| **Motion Time** | The time used to play the motion for this state. Enable Parameter to control the motion time with a custom value from a script. |
| **Mirror** | This property only applies to states with **humanoid animation**An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](ConfiguringtheAvatar.html) See in [Glossary](Glossary.html#Humanoidanimation). Enable to mirror the animation for this state. Enable Parameter to enable or disable mirroring from a script. |
| **Cycle Offset** | The offset added to the state time of the motion. This offset doesn’t affect the Motion Time. Enable Parameter to specify the Cycle Offset from a script. |
| **Foot IK** | This property only applies to states with humanoid animation. Enable to respect Foot IK for this state. |
| **Write Defaults** | Whether the AnimatorStates writes the default values for properties that aren’t animated by its motion. |
| **Transitions** | The list of transitions originating from this state. |

The default state, displayed in brown, is the state where the state machine starts when it’s first activated. To change the default state, right-click on another state and select **Set As Default** from the context menu. Use the **Solo** and **Mute** checkboxes on each transition to control the behaviour of **animation previews**. For more information, refer to [this page](AnimationSoloMute.html).

To add a new empty state, right-click in the Animator Controller view and select **Create State** > **Empty** from the context menu. To create a new state with an animation clip, drag the animation clip into the Animator Controller view.

## Any State

Use **Any State** to add a transition from any state to a specific state. **Any State** is a special state that represents all states. Adding a transition from **Any State** is an efficient way of adding the same transition from all states.

For example, your game has a timer and you want to transition to a time expired animation when the timer reaches zero. You can add a transition from **Any State** to the timer expired state. When the timer reaches zero, regardless of the current state, your state machine transitions to the time expired state.

![The Any State in the Animator Controller view.](../uploads/Main/AnyState.png)


The Any State in the Animator Controller view.

Because of its special purpose, you can’t place **Any State** at the end of a transition. You can’t have an animation or transition end with **Any State**. You also can’t set **Any State** as the default state.

State machine basics

Animation Parameters

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)