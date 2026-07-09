* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Collect rendering performance data](profile-rendering.html)
* [Collect frame timing data](frame-timing-manager-landing.html)
* Get frame timing data

Frame timing manager introduction

Enable frame timing statistics for release builds

# Get frame timing data

You can get frame timing data from the `FrameTiming` API in the following ways:

* [Use a custom Profiler module](#use-a-custom-profiler-module)
* [Use the `FrameTiming` API](#use-the-frametiming-api)

To get frame timing data from release builds, you must first enable the [Frame Timing Stats property](frame-timing-manager-enable.html).

## Use a custom Profiler module

To view frame timing data in a [custom Profiler module](profiler-create-modules.html) perform the following steps:

1. Create a custom profiler module according to the instructions on [Creating a custom profiler module](profiler-create-modules.html).
2. Open the **Profiler** window (**Window** > **Analysis** > **Profiler**)
3. Open the **Profiler Module Editor** (**Profler Modules** dropdown > gear icon) and select your custom Profiler module.
4. In the **Available Counters** panel, select **Unity**.
5. Select **Render** to open the submenu that contains **Profiler counters**Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html)  
   See in [Glossary](Glossary.html#profilercounter) related to memory usage, which includes those that the `FrameTimingStats` property enables. You can then click on the relevant counters in the submenu to add them to your custom module.

For a list of available counters, refer to [Profiler counters reference](profiler-counters-reference.html).

The [Highlights Profiler module](ProfilerHighlights.html) uses `FrameTiming` to determine whether a frame is CPU or GPU bound.

## Use the FrameTiming API

Use the `FrameTiming` API to access timestamp information. In each variable, `FrameTimingManager` records the time a specific event happens during a frame.

The following table contains the values available through the API, in the order that Unity executes them during a frame:

| **Property** | **Description** |
| --- | --- |
| [`frameStartTimestamp`](../ScriptReference/FrameTiming-frameStartTimestamp.html) | The CPU timestamp time when the frame begins. |
| [`firstSubmitTimestamp`](../ScriptReference/FrameTiming-firstSubmitTimestamp.html) | The CPU timestamp time when Unity submits the first job to the GPU during this frame. |
| [`cpuTimePresentCalled`](../ScriptReference/FrameTiming-cpuTimePresentCalled.html) | The CPU timestamp time when Unity calls the Present() function for the current frame. |
| [`cpuTimeFrameComplete`](../ScriptReference/FrameTiming-cpuTimeFrameComplete.html) | The CPU timestamp time when the GPU finishes rendering the frame and interrupts the CPU. |

Use [`FrameTimingManager.GetCpuTimerFrequency`](../ScriptReference/FrameTimingManager.GetCpuTimerFrequency.html) API to convert the timestamp to seconds.

## Additional resources

* [Enable frame timing statistics for release builds](frame-timing-manager-enable.html)
* [Frame timing API counter reference](frame-timing-manager-counter-reference.html)

Frame timing manager introduction

Enable frame timing statistics for release builds

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)