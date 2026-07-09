* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* Animator window

Animator Controller Asset

Animation state machine

# Animator window

Use the **Animator window** to create, view, and modify Animator Controller assets.

![The Animator window](../uploads/Main/MecanimAnimatorControllerWindow.png)


The Animator window

The Animator window displays the **state machine**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) from the most recently selected `.controller` asset, regardless of which **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) is loaded.

The Animator window contains:

* [Animation Layers](AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](AnimationLayers.html)  
  See in [Glossary](Glossary.html#AnimationLayer)
* [Animation Parameters](AnimationParameters.html)Used to communicate between scripting and the Animator Controller. Some parameters can be set in scripting and used by the controller, while other parameters are based on Custom Curves in Animation Clips and can be sampled using the scripting API. [More info](AnimationParameters.html)  
  See in [Glossary](Glossary.html#AnimationParameters)
* The Animator Controller view where you create, arrange, and connect states for the [Animator Controller](Animator.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
  See in [Glossary](Glossary.html#AnimatorController).

You can right-click (macOS: **Ctrl\_\_+click) on the grid to create a new state node. Use the middle mouse button or press** Alt\_\_ (macOS: **Option**) and drag to pan the Animator Controller view. Click to select and edit a state node. Click and drag a state node to rearrange your state machine.

![The Parameters view with two parameters](../uploads/Main/AnimatorWindowParametersPane.png)


The Parameters view with two parameters

Use the Parameters view to create, view, and edit [Animator Controller Parameters](AnimationParameters.html). These are variables you define that act as inputs for the state machine. To add a parameter, select the Plus icon, then select the parameter type from the context menu. To delete a parameter, select the parameter in the list and press **Delete** (macOS: **Ctrl\_\_+click and select** Delete\_\_).

![The Layers view](../uploads/Main/AnimatorWindowLayersPane.png)


The Layers view

Use the Layers view to create, view, and edit [layers](AnimationLayers.html)Layers in Unity can be used to selectively opt groups of GameObjects in or out of certain processes or calculations. This includes camera rendering, lighting, physics collisions, or custom calculations in your own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#layer) for your Animator Controller. You can control each layer with a different state machine. For example, you can create a base layer that controls the full body animation of your character and a second layer that controls the upper-body animation.

![The Eye icon](../uploads/Main/AnimatorWindowEyeIcon.png)


The Eye icon

Enable or disable the Eye icon to display or hide the side pane. Hide the side pane to have more room to edit your state machine.

![The breadcrumb list](../uploads/Main/AnimatorWindowBreadcrumbLocation.png)


The breadcrumb list

States can contain [sub-states](NestedStateMachines.html) and [blend trees](class-BlendTree.html). You can nest these structures repeatedly. When you view a sub-state or blend tree within another state, the breadcrumb list displays the nested hierarchy. Select an item in the breadcrumb list to display the state, sub-state, or blend tree.

![The lock icon](../uploads/Main/AnimatorWindowLockIcon.png)


The lock icon

Select the Lock icon to focus the Animator window on the selected Animator Controller asset. The Animator window doesn’t change focus when you select a different Animator Controller asset. If you disable the Lock icon, the Animator window changes focus when you select a different Animator Controller asset.

Animator Controller Asset

Animation state machine

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)