* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Building and delivering for iOS](ios-building-and-delivering.html)
* Encryption export regulations

Apple’s privacy manifest policy requirements

Linux

# Encryption export regulations

When publishing to the App Store, you must declare if your application uses encryption in order to comply with U.S. export regulations.

To make a declaration, you must add the [ITSAppUsesNonExemptEncryption](https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption) key in your applications [Information Property List](https://developer.apple.com/documentation/bundleresources/information_property_list) file. If your application doesn’t use encryption, or uses encryption that’s exempt from U.S. export compliance, set [ITSAppUsesNonExemptEncryption](https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption) to false.

The Unity Editor with Apple Platform support, in its base configuration without any additional packages, **plug-ins**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in), or extensions, doesn’t use non-exempt encryption. It’s your responsibility to verify that any third-party components and plug-ins included in your Unity project comply with encryption export regulations.

To streamline the submission process, add the `ITSAppUsesNonExemptEncryption` key to your `Info.plist` file. Without this key, App Store Connect prompts you to complete an export compliance questionnaire every time you upload a new version of your application.

For more information, refer to [Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations).

**Note**: [`UnityWebRequest`](../ScriptReference/Networking.UnityWebRequest.html) uses [NSURLSession](https://developer.apple.com/documentation/foundation/nsurlsession) which is exempt from export compliance.

## Packages

The [Unity Mobile Notifications](https://docs.unity3d.com/Packages/com.unity.mobile.notifications@latest) package is built on top of Apple’s notification API. Any networking for notifications is handled by the operating system, not the application, and is therefore exempt.

## Additional resources

* [Information Property List](https://developer.apple.com/documentation/bundleresources/information_property_list)
* [ITSAppUsesNonExemptEncryption](https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption)

Apple’s privacy manifest policy requirements

Linux

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)