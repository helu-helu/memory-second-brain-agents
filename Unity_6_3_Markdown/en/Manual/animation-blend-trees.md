* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* [Animation state machine](AnimationStateMachines.html)
* Animation blend trees

Animation transitions

Animation Blend Trees

# Animation blend trees

Use blend trees to blend between two or more similar motions, such as between walking and running animations. The **Animator window**The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow) contains a visual blend tree which you can use to smoothly blend multiple animations together.

| **Topic** | **Description** |
| --- | --- |
| **[Animation Blend Trees](class-BlendTree.html)Used for continuous blending between similar Animation Clips based on float Animation Parameters. [More info](class-BlendTree.html) See in [Glossary](Glossary.html#AnimationBlendTree)** | Blend multiple animations smoothly by incorporating parts of each motion at varying degrees. |
| **[1D Blending](BlendTree-1DBlending.html)** | Blend child motions according to a single parameter such as direction or speed. |
| **[2D Blending](BlendTree-2DBlending.html)** | Blend child motions according to two parameters using directional or cartesian algorithms. |
| **[Direct blending](BlendTree-DirectBlending.html)** | Map animator parameters directly to the weight of a child motion for exact blending control. |
| **[Common Blend Tree Options](BlendTree-AdditionalOptions.html)** | Configure time scale adjustments and mirroring on blend tree motions. |

## Additional resources

* [Animation state machine](AnimationStateMachines.html)A graph within an Animator Controller that controls the interaction of Animation States. Each state references an Animation Blend Tree or a single Animation Clip. [More info](AnimationStateMachines.html)  
  See in [Glossary](Glossary.html#AnimationStateMachine)
* [Animation parameters](AnimationParameters.html)Used to communicate between scripting and the Animator Controller. Some parameters can be set in scripting and used by the controller, while other parameters are based on Custom Curves in Animation Clips and can be sampled using the scripting API. [More info](AnimationParameters.html)  
  See in [Glossary](Glossary.html#AnimationParameters)

Animation transitions

Animation Blend Trees

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)