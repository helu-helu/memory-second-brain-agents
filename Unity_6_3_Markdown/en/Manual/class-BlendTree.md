* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* [Animation state machine](AnimationStateMachines.html)
* [Animation blend trees](animation-blend-trees.html)
* Animation Blend Trees

Animation blend trees

1D Blending

# Animation Blend Trees

A common task in game animation is to blend between two or more similar motions. Perhaps the best known example is the blending of walking and running animations according to the character’s speed. Another example is a character leaning to the left or right as it turns during a run.

It is important to distinguish between Transitions and Blend Trees. While both are used for creating smooth animation, they are used for different kinds of situations.

* Use **Transitions**The blend from one state to another in a state machine, such as transitioning a character from a walk to a jog animation. Transitions define how long the blend between states should take, and the conditions that activate the blend. [More info](class-Transition.html)  
  See in [Glossary](Glossary.html#transition) to smoothly transition from one Animation State to another over a given amount of time. Transitions are specified as part of an [Animation State Machine](AnimationStateMachines.html)A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](AnimationStateMachines.html)  
  See in [Glossary](Glossary.html#AnimationStateMachine). A transition from one motion to a completely different motion is usually fine if the transition is quick.
* Use **Blend Trees** to smoothly blend multiple animations by incorporating parts of each animation, at varying degrees. The amount that each of the motions contributes to the final effect is controlled using a blending parameter, which is just one of the numeric [animation parameters](AnimationParameters.html)Used to communicate between scripting and the Animator Controller. Some parameters can be set in scripting and used by the controller, while other parameters are based on Custom Curves in Animation Clips and can be sampled using the scripting API. [More info](AnimationParameters.html)  
  See in [Glossary](Glossary.html#AnimationParameters) associated with the **Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
  See in [Glossary](Glossary.html#AnimatorController). In order for the blended motion to make sense, the motions that are blended must be of similar nature and timing. Blend Trees are a special type of state in an Animation **State Machine**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html)  
  See in [Glossary](Glossary.html#StateMachine).

Examples of similar motions could be various walk and run animations. In order for the blend to work well, the movements in the clips must take place at the same points in normalized time. For example, walking and running animations can be aligned so that the moments of contact of foot to the floor take place at the same points in normalized time (e.g. the left foot hits at 0.0 and the right foot at 0.5). Since normalized time is used, it doesn’t matter if the clips are of different length.

## Using Blend Trees

To start working with a new Blend Tree, do the following:

1. Right-click on an empty space in the Animator Controller view.
2. Select **Create State** > **From New Blend Tree** from the context menu.
3. Double-click the Blend Tree to enter the Blend Tree Graph.

The **Animator window**The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow) displays a graph of the entire Blend Tree while the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) shows the currently selected node and its immediate children, if applicable.

![For example, the Blend Tree on the left displays only the root Blend Node because it does not have child nodes. The Blend Tree on the right has a root with three Animation Clips as child nodes.](../uploads/Main/MecanimBlendTreeStateDiagramCombined.png)


For example, the Blend Tree on the left displays only the root Blend Node because it does not have child nodes. The Blend Tree on the right has a root with three Animation Clips as child nodes.

To add **animation clips**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) to the blend tree you can select the blend tree, then click the plus icon in the motion field in the inspector.

![A Blend Node in the inspector before motions are added. Use the plus icon to add animation clips or child blend trees.](../uploads/Main/MecanimBlendTreeInitial.png)


A Blend Node in the inspector before motions are added. Use the plus icon to add animation clips or child blend trees.

You can also right-click and use the context menu to add animation clips or child **blend nodes**:

![The context menu when you right-click on a blend tree node.](../uploads/Main/AnimatorBlendTreeContextMenu.png)


The context menu when you right-click on a blend tree node.

When the blend tree has Animation clips and input parameters, the Inspector window displays a graphical representation of how the animations are combined. Use the slider

This visualization changes as the parameter value changes (as you drag the slider, the arrows from the tree root change their shading to show the dominant animation clip).

![A 2D Blend Tree with five animation clips](../uploads/Main/AnimatorBlendTreeInspectorPreview.jpg)


A 2D Blend Tree with five animation clips

Select any of the nodes in the Blend Tree graph to display it in the Inspector window. If the selected node is an Animation Clip, the Inspector for that Animation Clip will be shown. The settings will be read-only if the animation is imported from a model. If the node is a Blend Node, the Inspector for Blend Nodes will be shown.

Select either 1D or 2D blending from the **Blend Type** menu. The following topics provide more details on these blend types and the settings available in the Inspector window:

* [1D Blending](BlendTree-1DBlending.html)
* [2D Blending](BlendTree-2DBlending.html)
* [Direct Blending](BlendTree-DirectBlending.html)
* [Common Blend Tree Options](BlendTree-AdditionalOptions.html)

Animation blend trees

1D Blending

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)