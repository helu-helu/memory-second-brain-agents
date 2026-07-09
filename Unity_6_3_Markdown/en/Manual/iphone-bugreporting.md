* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* [Test and debug an iOS application](ios-testing-and-debugging.html)
* Report crash bugs for iOS

Troubleshooting on iOS devices

Optimize performance for iOS

# Report crash bugs for iOS

You can report crash bugs for iOS with Unity [Bug Reporting](https://unity.com/releases/editor/qa/bug-reporting). If your application crashes in the Xcode debugger, it’s recommended to add the Xcode console output to your bug report. Use the following steps to access the console output if your application crashes:

**Note**: Before submitting a [bug report](https://unity.com/releases/editor/qa/bug-reporting), refer to [Troubleshooting on iOS devices](TroubleShootingIPhone.html) where you will find solutions to common crashes and other problems.

1. From the **Debug** menu , select **Continue** twice.
2. Open the debugger console from **View** > **Debug Area** > **Activate Console**.
3. In the console, type `thread backtrace all` and press **Enter**.
4. Copy the console output and attach it to your bug report.

When reporting any application freezes, you can click **Pause** and repeat the previous steps.

If your application crashes on the iOS device, it’s recommended to retrieve the crash report. To achieve this, refer to [Acquiring Crash and Low Memory Reports](https://developer.apple.com/library/archive/technotes/tn2151/_index.html#//apple_ref/doc/uid/DTS40008184-CH1-ACQUIRING_CRASH_AND_LOW_MEMORY_REPORTS) (Apple Developer). Attach the crash report, your built application, and the console log to your bug report.

## Additional resources

* [Troubleshooting on iOS devices](TroubleShootingIPhone.html)
* [Bug reporting](https://unity.com/releases/editor/qa/bug-reporting)

Troubleshooting on iOS devices

Optimize performance for iOS

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)