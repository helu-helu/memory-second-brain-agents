* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* [Animation state machine](AnimationStateMachines.html)
* [Animation blend trees](animation-blend-trees.html)
* Direct blending

2D Blending

Common Blend Tree Options

# Direct blending

Use a **Direct Blend Tree** to map animator parameters to the weight of a BlendTree child. This is useful when you want exact control over blending animations rather than the indirectly control provided by 1D blending or 2D blending.

![A Direct Blend Tree with five animation clips assigned.](../uploads/Main/AnimatorDirectBlendTree.png)


A Direct Blend Tree with five animation clips assigned.

In direct blending, you use the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to add motions and to also assign an [Animator Parameter](AnimationParameters.html) to each blend weight. This Direct mode bypasses 2D blending algorithms, such as Freeform Directional and Freeform Cartesian, and allows you to implement a scripting solution to control the mix of blended animations.

For example, you can use Direct mode to to mix blend shape animations for facial expressions or to blend additive animations.

![Example of using Direct Blending for facial expressions](../uploads/Main/AnimatorDirectBlendTreeFacialExpressions.jpg)


Example of using Direct Blending for facial expressions

2D Blending

Common Blend Tree Options

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)