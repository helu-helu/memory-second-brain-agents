* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Collect rendering performance data](profile-rendering.html)
* [Collect frame timing data](frame-timing-manager-landing.html)
* Read frame timing data with ProfilerRecorder

Enable frame timing statistics for release builds

Frame timing API counter reference

# Read frame timing data with ProfilerRecorder

You can use the [`ProfilerRecorder`](../ScriptReference/Unity.Profiling.ProfilerRecorder.html) API to get custom and built-in **Profiler counter**Placed in code with the ProfilerCounter API to track metrics, such as the number of enemies spawned in your game. [More info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-guide.html)  
See in [Glossary](Glossary.html#profilercounter) values, and to read `FrameTimingManager` values.

The benefit of this is that when you use the `ProfilerRecorder` API, `FrameTimingManager` only records values when you attach a recorder to a specific counter. This behavior enables you to control which counters collect data and reduces the impact that the `FrameTimingManager` has on performance.

The following example tracks only the CPU Main Thread Frame Time variable with the `ProfilerRecorder` API:

```
using Unity.Profiling;
using UnityEngine;

public class ExampleScript : MonoBehaviour
{
    ProfilerRecorder mainThreadTimeRecorder;

    void OnEnable()
    {
        mainThreadTimeRecorder = ProfilerRecorder.StartNew(ProfilerCategory.Internal, "CPU Main Thread Frame Time");
    }

    void OnDisable()
    {
        mainThreadTimeRecorder.Dispose();
    }

    void Update()
    {
        var frameTime = mainThreadTimeRecorder.LastValue;

        // Your code logic here
    }
}
```

## Additional resources

* [Get frame timing data](frame-timing-manager-get-timing-data.html)
* [Adding profiling information to your code](profiler-adding-information-code.html)

Enable frame timing statistics for release builds

Frame timing API counter reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)