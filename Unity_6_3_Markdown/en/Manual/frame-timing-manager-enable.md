* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Collect rendering performance data](profile-rendering.html)
* [Collect frame timing data](frame-timing-manager-landing.html)
* Enable frame timing statistics for release builds

Get frame timing data

Read frame timing data with ProfilerRecorder

# Enable frame timing statistics for release builds

[`FrameTimingManager`](../ScriptReference/FrameTimingManager.html) is disabled by default for [release builds](building-introduction.html) due to the GPU measurement overhead on some platforms and graphics APIs such as OpenGL ES.

`FrameTimingManager` is always active in **development builds**A development build includes debug symbols and enables the Profiler. [More info](building-introduction.html)  
See in [Glossary](Glossary.html#developmentbuild) and the Unity Editor.

To enable frame timing statistics for release builds:

1. Go to **Edit** > **Project Settings** > **Player**.
2. Go to **Other Settings** > **Rendering**.
3. Enable the **Frame Timing Stats** property.

**Tip:** If you [use `ProfilerRecorder`](frame-timing-manager-record-timing-data.html) to collect data, then you don’t need to enable the **Frame Timing Stats** property.

If you use the OpenGL platform, you also need to enable the **OpenGL: Profiler GPU Recorders** property to measure GPU usage. To do this:

1. Go to **Edit** > **Project** > **Settings** > **Player**.
2. Go to **Other Settings** > **Rendering**.
3. Enable the **OpenGL: Profiler GPU** property.

## Additional resources

* [Get frame timing data](frame-timing-manager-get-timing-data.html)
* [Read frame timing data with ProfilerRecorder](frame-timing-manager-record-timing-data.html)

Get frame timing data

Read frame timing data with ProfilerRecorder

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)