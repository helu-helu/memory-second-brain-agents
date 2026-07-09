* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Collect rendering performance data](profile-rendering.html)
* [Frame Debugger](FrameDebugger-landing.html)
* Attach the Frame Debugger to a built project

Check or find a rendering event

Share information about a rendering event

# Attach the Frame Debugger to a built project

You can change the Frame Debugger’s target process to attach the Frame Debugger to a built Unity Player. To be compatible with the Frame Debugger, the Unity Player must:

* Use the ****Development Build**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
  See in [Glossary](Glossary.html#developmentbuild)** [Build Setting](BuildSettings.html).
* Support multithreaded rendering. Every Unity platform except Web supports this.
* For desktop platforms, use the **Run In Background** [Player Setting](class-PlayerSettings.html). Otherwise, when you focus the Frame Debugger window in the Unity Editor, the Unity Player loses focus and doesn’t reflect any rendering changes.

If the Unity Player fulfills the above requirements, when you next [debug a frame](FrameDebugger-debug.html), you can attach the Frame Debugger to the Unity Player.

Check or find a rendering event

Share information about a rendering event

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)