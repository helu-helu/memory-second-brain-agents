* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Humanoid Avatar](AvatarCreationandSetup.html)
* Avatar Mask window reference

Avatar Muscle & Settings tab reference

Human Template window

# Avatar Mask window reference

[Switch to Scripting](../ScriptReference/AvatarMask.html "Go to AvatarMask page in the Scripting Reference")

There are two ways to define which parts of your animation should be masked:

* By selecting from a [Humanoid body map](#Humanoid)
* By choosing which bones to include or exclude from a [Transform hierarchy](#Transform)

## Humanoid body selection

If your animation uses a Humanoid **Avatar**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar), you can select or deselect portions of the simplified humanoid body diagram to indicate where to mask the animation:

![Defining an Avatar Mask using the Humanoid body](../uploads/Main/AvatarMaskInspectorHumanoid.png)


Defining an Avatar Mask using the Humanoid body

The body diagram groups body parts into these portions:

* Head
* Left Arm
* Right Arm
* Left Hand
* Right Hand
* Left Leg
* Right Leg
* Root (denoted by the “shadow” under the feet)

To include animation from one of these body portions, click the Avatar diagram for that portion until it appears as green.
To exclude animation, click the body portion until it appears red.
To include or exclude all, double-click the empty space surrounding the Avatar.

You can also toggle **Inverse** Kinematics\_\_ (IK)\_\_ for hands and feet, which determines whether or not to include IK curves in animation blending.

## Transform selection

If your animation does not use a Humanoid Avatar and you want more detailed control over which bones are masked, you can select or deselect portions of the Model’s hierarchy:

1. Assign a reference to the Avatar whose transform you would like to mask.
2. Click the **Import Skeleton** button. The hierarchy of the avatar appears in the **inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector).
3. You can check each bone in the hierarchy to use as your mask.

![Defining an avatar mask using the Transform method](../uploads/Main/AvatarMaskInspectorTransform.png)


Defining an avatar mask using the Transform method

Mask assets can be used in [Animator Controllers](class-AnimatorController.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), when specifying [Animation Layers](AnimationLayers.html)An Animation Layer contains an Animation State Machine that controls animations of a model or part of it. An example of this is if you have a full-body layer for walking or jumping and a higher layer for upper-body motions such as throwing an object or shooting. The higher layers take precedence for the body parts they control. [More info](AnimationLayers.html)  
See in [Glossary](Glossary.html#AnimationLayer) to apply masking at runtime, or in the import settings of your animation files to apply masking while importing animation.

A benefit of using Masks is that they tend to reduce memory overheads since body parts that are not active do not need their associated **animation curves**Allows you to add data to an imported clip so you can animate the timings of other items based on the state of an animator. For example, for a game set in icy conditions, you could use an extra animation curve to control the emission rate of a particle system to show the player’s condensing breath in the cold air. [More info](AnimationCurvesOnImportedClips.html)  
See in [Glossary](Glossary.html#AnimationCurves). Also, the unused curves need not be calculated during playback which will tend to reduce the CPU overhead of the animation.

AvatarMask

Avatar Muscle & Settings tab reference

Human Template window

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)