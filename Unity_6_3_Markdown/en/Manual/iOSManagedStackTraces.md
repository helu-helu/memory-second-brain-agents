* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* [Test and debug an iOS application](ios-testing-and-debugging.html)
* Managed stack traces on iOS

Collecting performance data on an iOS device

Troubleshooting on iOS devices

# Managed stack traces on iOS

When an exception occurs in managed code, the stack trace for the exception can help you understand the cause of the exception. However, the managed stack trace might not appear as expected for some cases on iOS. The stack trace also varies depending on the Xcode build configuration.

## Debug builds

When you use the debug build configuration with iOS, **IL2CPP**A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) will report a reliable managed stack trace, and include each managed method in the call stack. The stack trace doesn’t include line numbers from the original C# source code.

## Release builds

When you use a release build configuration, IL2CPP might produce a call stack that’s missing one or more managed methods. This is because the C++ compiler has inlined the missing methods. Method inlining is usually good for performance at runtime, but it can make call stacks more difficult to understand. IL2CPP always provides at least one managed method on the call stack. This is the method where the exception occurred. It also includes other methods if they’re not inlined.

If you can reproduce an exception locally, use Xcode to find inlined methods. Run the application in Xcode, using the release configuration, and set an exception breakpoint. The native call stack view in Xcode will indicate which methods actually exist, and which have been inlined.

## Source code line numbers

IL2CPP call stacks don’t include source code line number information by default in debug or release configurations. You can enable source code line numbers using the following steps:

1. Navigate to **Edit** > **Project Settings** > **Player** > **iOS settings** > **Other Settings**.
2. In the Configuration section, set **IL2CPP Stacktrace Information** to **Method Name, File Name, and Line Number**.

**Note**: Using this option can increase both the build time and final size of the built program.

Collecting performance data on an iOS device

Troubleshooting on iOS devices

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)