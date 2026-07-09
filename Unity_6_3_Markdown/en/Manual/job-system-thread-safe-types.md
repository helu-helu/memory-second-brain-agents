* [Programming in Unity](scripting.html)
* [Code optimization](scripting-optimization.html)
* [Write multithreaded code with the job system](job-system.html)
* Thread safe types

Parallel jobs

Introduction to NativeContainer

# Thread safe types

The job system works best when you use it with the [Burst compiler](https://docs.unity3d.com/Packages/com.unity.burst@latest/). Because Burst doesn’t support managed objects, you need to use unmanaged types to access the data in jobs. You can do this with [blittable types](https://learn.microsoft.com/en-us/dotnet/framework/interop/blittable-and-non-blittable-types), or use Unity’s built-in [`NativeContainer`](../ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerAttribute.html) objects.

| **Topic** | **Description** |
| --- | --- |
| [Introduction to NativeContainer](job-system-native-container.html) | Understand Unity’s custom thread-safe type, `NativeContainer`. |
| [Implement a custom NativeContainer](job-system-custom-nativecontainer.html) | Implement custom native containers. |
| [Copying NativeContainer structures](job-system-copy-nativecontainer.html) | Copy and reference multiple native containers. |
| [Custom NativeContainer example](job-system-custom-nativecontainer-example.html) | Use a real world custom NativeContainer example. |

## Additional resources

* [Burst compiler](https://docs.unity3d.com/Packages/com.unity.burst@latest/)
* [Collections](https://docs.unity3d.com/Packages/com.unity.collections@latest)

Parallel jobs

Introduction to NativeContainer

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)