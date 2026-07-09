* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* [Native plug-ins for iOS](PluginsForIOS.html)
* [Use your native plug-in for iOS](ios-native-plugin-use.html)
* Bonjour browser sample

Automated plug-in integration

Integrating Unity into native iOS applications

# Bonjour browser sample

For a simple example of how to use a native **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in), download the [Bonjour Browser Sample](../uploads/Examples/iPhoneNativeCodeSample.zip).

This example demonstrates how you can invoke Objective-C code from a Unity iOS application. This application implements a simple Bonjour client and consists of:

* A Unity iOS Project where `Plugins\Bonjour.cs` is the C# interface to the native code, and `BonjourTest.cs` is the script that implements the application logic.
* Native code (located in `Assets/Plugins/iOS`) that will be added to the built Xcode project as described in [Automated plug-in integration](ios-native-plugin-automated-integration.html).

Automated plug-in integration

Integrating Unity into native iOS applications

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)