* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animation clips](animation-clips-landing.html)
* Use curves to control the timing of animation clips

Loop optimization on animation clips

Add events to animation clips

# Use curves to control the timing of animation clips

You can attach **animation curves** to imported **animation clips**Animation data that can be used for animated characters or simple animations. It is a simple “unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) in the [Animation tab](class-AnimationClip.html).

You can use these curves to add additional animated data to an imported clip. You can use that data to animate the timings of other items based on the state of an animator. For example, in a game set in icy conditions, an extra animation curve could be used to control the emission rate of a **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) system to show the player’s condensing breath in the cold air.

To add a curve to an imported animation, expand the **Curves** section at the bottom of the [Animation tab](class-AnimationClip.html), and click the plus icon to add a new curve to the current animation clip:

![The expanded Curves section on the Animation tab](../uploads/Main/classAnimationClip-Curves.png)


The expanded Curves section on the Animation tab

If your imported animation file is split into multiple animation clips, each clip can have its own custom curves.

![The curves on an imported animation clip](../uploads/Main/MecanimCurves.png)


The curves on an imported animation clip

The curve’s X-axis represents *normalized time* and always ranges between 0.0 and 1.0 (corresponding to the beginning and the end of the animation clip respectively, regardless of its duration).

![Unity Curve Editor](../uploads/Main/CurveEditorPopupDescr.png)


Unity Curve Editor

**(A)** Wrapping mode

**(B)** Curve Presets

Double-clicking an animation curve brings up the [standard Unity curve editor](EditingCurves.html) which you can use to add **keys** to the curve. Keys are points along the curve’s timeline where it has a value explicitly set by the animator rather than just using an interpolated value. Keys are very useful for marking important points along the timeline of the animation. For example, with a walking animation, you might use keys to mark the points where the left foot is on the ground, then both feet on the ground, right foot on the ground, and so on. Once the keys are set up, you can move conveniently between key frames by pressing the **Previous Key Frame** and **Next Key Frame** buttons. This moves the vertical red line and shows the *normalized time* at the **keyframe**A frame that marks the start or end point of a transition in an animation. Frames in between the keyframes are called inbetweens.  
See in [Glossary](Glossary.html#keyframe). The value you enter in the text box drives the value of the curve at that time.

## Animation curves and animator controller parameters

If you have a curve with the same name as one of the [parameters](AnimationParameters.html) in the [Animator Controller](Animator.html)Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), then that parameter takes its value from the value of the curve at each point in the timeline. For example, if you make a call to [GetFloat](../ScriptReference/Animator.GetFloat.html) from a script, the returned value is equal to the value of the curve at the time the call is made. Note that at any given point in time, there might be multiple animation clips attempting to set the same parameter from the same controller. In that case, Unity blends the curve values from the multiple animation clips. If an animation has no curve for a particular parameter, then Unity blends with the default value for that parameter.

Loop optimization on animation clips

Add events to animation clips

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)