* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animation clips](animation-clips-landing.html)
* [Animation window](AnimationEditorGuide.html)
* Rotation in animations

Edit Animation curves

Key manipulation in Dopesheet mode

# Rotation in animations

You can use Unity to animate your **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)’s rotations. There are different methods of applying these rotations to suit your project best.

Consult [Rotation and orientation in Unity](QuaternionAndEulerRotationsInUnity.html) for more information on rotational representations.

## Rotation interpolation

You can use the [Animation window](AnimationEditorGuide.html) to choose how Unity applies rotation to your GameObject. Unity uses interpolation to calculate how a GameObject visually moves from one orientation to another in your animation.

Different interpolation methods look different in motion, but have the same result. Unity offers three types of interpolation for your animations:

![The Animation window, with the interpolation menu expanded to show the rotation interpolation options.](../uploads/Main/QuaternionInterpolation.png)


The Animation window, with the interpolation menu expanded to show the rotation interpolation options.

### Euler angle interpolation

**Euler Angles** interpolation applies the full range of motion to the GameObject specified by the angles you enter; if the rotation is greater than 360 degrees, the GameObject rotates fully before it stops at the correct orientation.

**Euler Angles (Quaternion)** interpolation uses the above interpolation method but bakes the information into a **quaternion**Unity’s standard way of representing rotations as data. When writing code that deals with rotations, you should usually use the Quaternion class and its methods. [More info](QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](Glossary.html#Quaternion) curve. This method uses more memory but results in a slightly faster runtime.

### Quaternion interpolation

**Quaternion** interpolation rotates the GameObject across the shortest distance to a particular orientation. For example, regardless of whether the rotation value is 5 degrees or 365 degrees, the GameObject rotates 5 degrees.

## External animation sources

[Animation from external sources](AnimationsImport.html) often contains rotational **keyframe**A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe) animation in Euler format. Unity resamples these animations and generates new keyframes for each frame in the animation to avoid rotations that exceed the valid range of rotational quaternions.

For example, if you have two keyframes that are six frames apart with the x value going from 0 to 270 degrees, the GameObject rotates 90 degrees in the opposite direction because it’s the shortest way to get to the same result. Instead, Unity resamples and adds a keyframe on every frame, so the rotation is only 45 degrees between keyframes and the rotation is correct.

### Resolve rotation problems with external animation sources

If the quaternion resampling of the imported animation doesn’t match the original closely enough for your needs, you can turn off animation resampling and use the original Euler animation keyframes at runtime. For more information, consult [Euler curve resampling](AnimationEulerCurveImport.html).

## Additional resources

* [Rotation and orientation in Unity](QuaternionAndEulerRotationsInUnity.html)
* [Using Animation Curves](animeditor-AnimationCurves.html)
* [Euler curve resampling](AnimationEulerCurveImport.html)

Edit Animation curves

Key manipulation in Dopesheet mode

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)