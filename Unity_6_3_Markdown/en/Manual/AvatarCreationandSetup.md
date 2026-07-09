* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* Humanoid Avatar

Mask animation clips

Retarget Humanoid animations

# Humanoid Avatar

Unity’s Animation System has special features for working with humanoid characters. Because humanoid characters are so common in games, Unity provides a specialized workflow, and an extended tool set for **humanoid animations**An animation using humanoid skeletons. Humanoid models generally have the same basic structure, representing the major articulate parts of the body, head and limbs. This makes it easy to map animations from one humanoid skeleton to another, allowing retargeting and inverse kinematics. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Humanoidanimation).

[The Avatar system](ConfiguringtheAvatar.html) is how Unity identifies that a particular animated model is a humanoid, and which parts of the model correspond to the legs, arms, head, and body.

Because of the similarity in bone structure between different humanoid characters, it is possible to map animations from one humanoid character to another.

![Unitys Avatar structure](../uploads/Main/AvatarIntro.jpg)


Unity’s Avatar structure

The following topics provide more details on humanoid animation and **root motion**Motion of character’s root node, whether it’s controlled by the animation itself or externally. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootMotion):

| **Topic** | **Description** |
| --- | --- |
| **[Retarget humanoid animation](Retargeting.html)** | Reuse humanoid clips on different models after you configure each **Avatar**An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html) See in [Glossary](Glossary.html#Avatar). |
| **[Inverse Kinematics](InverseKinematics.html)** | Use inverse **kinematics**The geometry that describes the position and orientation of a character’s joints and bodies. Used by inverse kinematics to control character movement. See in [Glossary](Glossary.html#kinematics) to pose **joints**A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html) See in [Glossary](Glossary.html#joint) from a fixed point. |
| **[How Root Motion works](RootMotion.html)** | Learn how body and **root transforms**The Transform at the top of a hierarchy of Transforms. In a Prefab, the Root Transform is the topmost Transform in the Prefab. In an animated humanoid character, the Root Transform is a projection on the Y plane of the Body Transform and is computed at run time. At every frame, a change in the Root Transform is computed, and then this is applied to the GameObject to make it move. [More info](RootMotion.html) See in [Glossary](Glossary.html#RootTransform) drive character motion from clips. |
| **[Scripting Root Motion](ScriptingRootMotion.html)** | Move characters from in-place clips using curves, controllers, and the `OnAnimatorMove` API. |
| **[Avatar Mapping tab reference](class-Avatar.html)** | Reference for mapping bones to the humanoid Avatar. |
| **[Avatar Muscle and Settings tab reference](MuscleDefinitions.html)** | Reference for muscle limits, previews, and range-of-motion settings on an Avatar. |
| **[Avatar Mask window reference](class-AvatarMask.html)** | Reference for masking humanoid body regions or transform paths in animation. |
| **[Human Template window reference](class-HumanTemplate.html)** | Reference for editing saved **Human Template**A pre-defined bone-mapping. Used for matching bones from FBX files to the Avatar. [More info](class-HumanTemplate.html) See in [Glossary](Glossary.html#Humantemplate) bone mappings. |

## Additional resources

* [Importing a model with humanoid animations](ConfiguringtheAvatar.html)
* [Use Animation curves](animeditor-AnimationCurves.html)

Mask animation clips

Retarget Humanoid animations

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)