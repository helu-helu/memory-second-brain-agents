* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* Animation state machine

Animator window

State machine basics

# Animation state machine

It’s common for a character or a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to have several animations for the different actions it performs in a game. For example, a character might breath and sway slightly when idle, walk when commanded, and raise their arms when they fall from a platform. A sliding door might open, close, or jam.

Mecanim uses a **state machine**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) to arrange these actions. A state machine is a graph of nodes and connecting lines that resembles a flowchart. A state machine plays the animation linked to the current action and determines the next action. You can create a state machine for each character and GameObject in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

| **Topic** | **Description** |
| --- | --- |
| **[State machine basics](StateMachineBasics.html)** | Learn core state machine concepts and build animation flow in the **Animator window**The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html) See in [Glossary](Glossary.html#AnimatorWindow). |
| **[Animation states](class-State.html)** | Configure states, motions, and defaults to control what each state plays. |
| **[Animation parameters](AnimationParameters.html)Used to communicate between scripting and the Animator Controller. Some parameters can be set in scripting and used by the controller, while other parameters are based on Custom Curves in Animation Clips and can be sampled using the scripting API. [More info](AnimationParameters.html) See in [Glossary](Glossary.html#AnimationParameters)** | Control state logic with scriptable parameters. |
| **[State machine transitions](StateMachineTransitions.html)** | Simplify complex controllers with Entry and Exit transitions between state machines. |
| **[Animation transitions](class-Transition.html)Allows a state machine to switch or blend from one animation state to another. Transitions define how long a blend between states should take, and the conditions that activate them. [More info](StateMachineTransitions.html) See in [Glossary](Glossary.html#AnimationTransition)** | Blend between states and define when transitions are triggered. |
| **[Animation blend trees](animation-blend-trees.html)Used for continuous blending between similar Animation Clips based on float Animation Parameters. [More info](class-BlendTree.html) See in [Glossary](Glossary.html#AnimationBlendTree)** | Blend similar motions smoothly using parameters and normalized time. |
| **[State machine behaviors](StateMachineBehaviours.html)** | Attach behavior **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html) See in [Glossary](Glossary.html#Scripts) to states to run code on enter, update, and exit. |
| **[Sub-state machines](NestedStateMachines.html)** | Group related states into nested machines to keep large graphs manageable. |
| **[Animation layers](AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](AnimationLayers.html) See in [Glossary](Glossary.html#AnimationLayer)** | Separate animation with layered controllers, masks, and blending modes. |
| **[State machine solo and mute](AnimationSoloMute.html)** | Preview transitions faster by soloing key paths and muting irrelevant ones. |
| **[Target matching](TargetMatching.html)A scripting function that allows you to move characters in such a way that a hand or foot lands in a certain place at a certain time. For example, the character may need to jump across stepping stones or jump and grab an overhead beam. [More info](TargetMatching.html) See in [Glossary](Glossary.html#targetmatching)** | Match character parts to precise world targets during specific animation windows. |

## Additional resources

* [Humanoid Avatar](AvatarCreationandSetup.html)
* [Create an Animator Controller](AnimatorControllerCreation.html)

Animator window

State machine basics

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)