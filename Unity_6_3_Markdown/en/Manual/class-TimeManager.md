* [Unity Editor interface](unity-editor.html)
* [Unity Editor settings reference](editor-settings-reference.html)
* [Project Settings reference](comp-ManagerGroup.html)
* Time

Tags and Layers

UI Toolkit project settings

# Time

Use **Time** settings to set properties that control timing within your game. To access **Time** settings, go to **Edit > Project Settings > Time**.

![The Time Project Settings](../uploads/Main/TimeSet.png)


The Time Project Settings

## Properties

| **Property** | **Description** |
| --- | --- |
| **Fixed Timestep** | A frame rate independent interval that dictates when physics calculations and `FixedUpdate`events are performed. |
| **Maximum Allowed Timestep** | A frame rate independent interval that caps the worst case scenario when frame rate is low. Physics calculations and `FixedUpdate` events will not be performed for longer time than specified. |
| **Time Scale** | The speed at which time progresses. Change this value to simulate slow motion effects. A value of 1 means real-time. A value of 0.5 means half speed; a value of 2 is double speed. |
| **Maximum** Particle\_\_ Timestep\_\_ | A frame rate independent interval that controls the accuracy of the particle simulation. When the frame time exceeds this value, multiple iterations of the particle update are performed in one frame, so that the duration of each step does not exceed this value. For example, a game running at 30fps (0.03 seconds per frame) could run the particle update at 60fps (in steps of 0.0167 seconds) to achieve a more accurate simulation, at the expense of performance. |

## Details

The **Time Manager** lets you set properties globally, but it is often useful to set them from a script during gameplay (for example, setting **Time Scale** to zero is a useful way to pause the game). Refer to the page on [Time and frame rate management](managing-time-and-frame-rate.html) for full details of how time can be managed in Unity.

## Additional resources

* [Fixed updates](fixed-updates.html)
* [Optimize physics performance](physics-optimization.html)

Tags and Layers

UI Toolkit project settings

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)