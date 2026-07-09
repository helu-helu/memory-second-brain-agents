* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* Introduction to Animator Controllers

Animator Controller

Create an Animator Controller

# Introduction to Animator Controllers

Use an **Animator Controller** to arrange and maintain a set of **Animation Clips**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) and associated **Animation Transitions**Allows a state machine to switch or blend from one animation state to another. Transitions define how long a blend between states should take, and the conditions that activate them. [More info](StateMachineTransitions.html)  
See in [Glossary](Glossary.html#AnimationTransition) for a character or an animated **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

In most situations, it’s normal to have multiple animations and transition between them when certain game conditions occur. For example, you could transition from a walk animation to a jump whenever the spacebar is pressed. However, even if you just have a single animation clip, you still need to place it into an Animator Controller to use it on a Game Object.

The Animator Controller has references to the Animation clips it uses. The Animator Controller manages the various Animation Clips and the Transitions between them using a ****State Machine**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine)**, which could be thought of as a flow-chart of Animation Clips and Transitions. you can find more information about state machines [here](AnimationStateMachines.html).

![A simple Animator Controller](../uploads/Main/MecanimAnimatorControllerWindow.png)


A simple Animator Controller

Unity automatically creates an Animator Controller when you begin animating a GameObject using the Animation Window, or when you attach an Animation Clip to a GameObject.

To manually create an Animator Controller, right-click within either column of the Project window and select **Create** > **Animator Controller**.

The following topics provide more details on the Animator Controller Asset and state machines:

* [Create an Animator Controller](AnimatorControllerCreation.html)
* [Animator Controller Asset](Animator.html)
* [Animator Window](AnimatorWindow.html)The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html)  
  See in [Glossary](Glossary.html#AnimatorWindow)
* [Animation State Machine](AnimationStateMachines.html)A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](AnimationStateMachines.html)  
  See in [Glossary](Glossary.html#AnimationStateMachine)

## Navigation

Use the scroll wheel to zoom in and zoom out of the Animator Controller view.

To focus on an item in the Animator Controller view, select one or multiple states (click or drag a selection box around the states you wish to select), then press the F key to zoom in on the selection.

![Focus on selected states](../uploads/Main/classAnimatorController-Focus.jpg)


Focus on selected states

Press the A key to fit all of the animation states into the Animator Controller view.

Unity preserves your selection. Press the A and F keys to switch between your selected animation states and the entire Animator Controller.

![Unity automatically fits all states in the Animator Controller view when the A key is pressed](../uploads/Main/classAnimatorController-Autofit.jpg)


Unity automatically fits all states in the Animator Controller view when the A key is pressed

During Play Mode, the Animator pans the view so that the current state being played is always visible. The Animator Controller respects the independent zoom factors of the Base Layer and Sub-State Machine, and the window pans automatically to ensure visibility of the active state or states.

To modify the zoom during Play Mode, follow these steps:

1. Enable **Auto Live Link** in the Animator Controller window.
2. Click the Play button to enter Play Mode.
3. Click Pause.
4. In the Animator Controller view, select the state or states you want to zoom into.
5. Press the F key to zoom into the selection.
6. Click the Play button again to resume Play Mode.

Note that the Animator Controller view pans to each state when it is active.

![The Animator pans to the active state](../uploads/Main/classAnimatorController-Pans.png)


The Animator pans to the active state

Animator Controller

Create an Animator Controller

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)