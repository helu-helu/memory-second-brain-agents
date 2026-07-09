* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Collect rendering performance data](profile-rendering.html)
* [Collect frame timing data](frame-timing-manager-landing.html)
* Frame timing API counter reference

Read frame timing data with ProfilerRecorder

Rendering Profiler module reference

# Frame timing API counter reference

The following table describes the purpose of the counters that [the `FrameTiming` API](../ScriptReference/FrameTiming.html) provides.

| **FrameTiming API field** | ****Profiler counter**Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html) See in [Glossary](Glossary.html#profilercounter)** | **Description** |
| --- | --- | --- |
| [`cpuFrameTime`](../ScriptReference/FrameTiming-cpuFrameTime.html) | **CPU Total Frame Time** | The total CPU frame time, in nanoseconds. Unity calculates this as the time between the ends of two frames, including any overheads or time spent waiting between frames. This value doesn’t include the time that the application is paused with `Application.Pause`. |
| [`cpuMainThreadFrameTime`](../ScriptReference/FrameTiming-cpuMainThreadFrameTime.html) | **CPU Main Thread Frame Time** | Active main thread work time in nanoseconds. This is the **PlayerLoop** time without the time the main thread was waiting for the VSync or render thread to finish its work, calculated as follows:   `cpuMainThreadFrameTime = PlayerLoop - GfxDevice.WaitForRenderThread - Gfx.WaitForPresentOnGfxThread - WaitForTargetFPS` |
| [`cpuMainThreadPresentWaitTime`](../ScriptReference/FrameTiming-cpuMainThreadPresentWaitTime.html) | N/A | The CPU time in nanoseconds spent waiting for the frame presentation or VSync during the frame, calculated as follows:   `cpuMainThreadPresentWaitTime = Gfx.WaitForPresentOnGfxThread + WaitForTargetFPS`. |
| [`cpuRenderThreadFrameTime`](../ScriptReference/FrameTiming-cpuRenderThreadFrameTime.html) | **CPU Render Thread Frame Time** | Active Render Thread work time in nanoseconds without Unity calling the `Present()` function, calculated as follows:   `cpuRenderThreadFrameTime = RenderLoop - Gfx.PresentFrame`. |
| [`gpuFrameTime`](../ScriptReference/FrameTiming-gpuFrameTime.html) | **GPU Frame Time** | The time difference in nanoseconds between the beginning and the end of the GPU rendering a single frame. |

The following diagram visualizes the relationships between **FrameTiming** and [the Profiler](Profiler.html) frame data.

![Diagram showing relation of FrameTiming API to Profiler data](../uploads/Main/frame-timing-manager-times.drawio.svg)


Diagram showing relation of FrameTiming API to Profiler data

## Additional resources

* [Get frame timing data](frame-timing-manager-get-timing-data.html)
* [Record frame timing data](frame-timing-manager-record-timing-data.html)

Read frame timing data with ProfilerRecorder

Rendering Profiler module reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)