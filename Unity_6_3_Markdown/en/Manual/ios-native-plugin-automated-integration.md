* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* [Native plug-ins for iOS](PluginsForIOS.html)
* [Use your native plug-in for iOS](ios-native-plugin-use.html)
* Automated plug-in integration

Callback from native code

Bonjour browser sample

# Automated plug-in integration

Unity supports automated **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#plug-in) integration and copies files with the following extensions to the generated Xcode project: `.a`, `.m` , `.mm`, `.c`, `.cpp`, `.h`, `.swift`.

To enable automated plug-in integration, enable iOS plug-ins in the Plug-in **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector).

If you place files with these extensions in the `Assets/Plugins/iOS` folder, Unity only enables them for the iOS platform.

**Note:** Files copied to the generated Xcode project are no longer linked to their counterparts in your Unity Project. If you change these files in Xcode, you must copy them back into your Unity Project. Otherwise, Unity will overwrite them the next time you build your Project.

## Additional resources

* [Bonjour browser code sample](ios-native-plugin-bonjour-sample.html)

Callback from native code

Bonjour browser sample

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)