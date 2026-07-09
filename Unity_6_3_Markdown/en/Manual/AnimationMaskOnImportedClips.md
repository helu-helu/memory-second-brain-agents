* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animation clips](animation-clips-landing.html)
* Mask animation clips

Add events to animation clips

Humanoid Avatar

# Mask animation clips

Masking allows you to discard some of the animation data within a clip, allowing the clip to animate only parts of the object or character rather than the entire thing. For example, if you had a character with a throwing animation. If you wanted to be able to use the throwing animation in conjunction with various other body movements such as running, crouching and jumping, you could create a mask for the throwing animation limiting it to just the right arm, upper body and head. This portion of the animation can then be played in a layer over the top of the base running or jumping animations.

Masking can be applied to your build, making filesize and memory smaller. It also makes for faster processing speed because there is less animation data to blend at run-time. In some cases, import masking may not be suitable for your purposes. In that case you can use the layer settings of the **Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) to apply a mask at run-time. This page relates to masking in the import settings.

To apply a mask to an imported **animation clip**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip), expand the Mask heading to reveal the Mask options. When you open the menu, you’ll see three options: Definition, Humanoid and Transform.

![The Mask Definition, Humanoid and Transform options](../uploads/Main/AnimationInspectorMaskOptions.png)


The Mask Definition, Humanoid and Transform options

## Definition

Allows you to specify whether you want to create a one-off mask in the **inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) specially for this clip, or whether you want to use an existing mask asset from your project.

If you want to create a one-off mask just for this clip, choose / Create From This Model /.

If you are going to set up multiple clips with the same mask, you should select / Copy From Other Mask / and use a mask asset. This allows you to re-use a single mask definition for many clips.

When Copy From Other Mask is selected, the Humanoid and Transform options are unavailable, since these relate to creating a one-off mask within the inspector for this clip.

![Here, the Copy From Other option is selected, and a Mask asset has been assigned](../uploads/Main/AnimationInspectorMaskCopyFromOther.png)


Here, the Copy From Other option is selected, and a Mask asset has been assigned

## Humanoid

The Humanoid option gives you a quick way of defining a mask by selecting or deselecting the body parts of a human diagram. These can be used if the animation has been marked as humanoid and has a valid **avatar**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar).

![The Humanoid mask selection option](../uploads/Main/AnimationInspectorMaskHumanoidSelection.png)


The Humanoid mask selection option

## Transform

This option allows you to specify a mask based on the individual bones or moving parts of the animation. This gives you finer control over the exact mask definition, and also allows you to apply masks to non-humanoid animation clips.

![The Transform mask selection option](../uploads/Main/AnimationInspectorMaskTransformSelection.png)


The Transform mask selection option

Add events to animation clips

Humanoid Avatar

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)