* [Platform development](PlatformSpecific.html)
* [iOS](iphone.html)
* [Developing for iOS](ios-developing.html)
* Deep linking on iOS

Integrating Unity into native iOS applications

iOS authorizations in Unity

# Deep linking on iOS

Deep links are hyperlinks outside of your application that take a user to a specific location within the application rather than a website. When a user clicks a deep link, the application opens from the designated location, such as a specific **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in a Unity application. For more information about deep links and how to use them, refer to [Deep linking](deep-linking.html).

There are two ways to enable deep links for iOS applications: URL schemes and universal links.

For information on how to use deep links and handle them when your application opens, refer to [Using deep links](deep-linking.html#using-deep-links).

## URL schemes

A URL scheme specifies a link structure that your iOS application refers to. The device opens the application when the user clicks a deep link that matches the URL scheme structure. To add a URL scheme, use the following steps:

1. Go to **Edit** > **Project Settings** > **Player** > **iOS** > **Other Settings** > **Configuration**.
2. Expand **Supported URL schemes** and set the following properties:
   * **Size** to `1`. To support multiple URL schemes, set this to the total number of schemes you want to use.
   * **Element 0** to the name of your URL scheme. Enter only the scheme name, without `://`. For example, enter `unitydl` to open your application when the device processes links that start with `unitydl://`.

![Supported URL schemes settings for iOS.](../uploads/Main/ios-supported-url.png)


Supported URL schemes settings for iOS.

After you build and deploy your application, it opens when the device processes links that start with the URL scheme you configured.

## Universal links

Universal links use `https` URLs. They don’t use **Supported URL schemes** in Unity **Player settings**Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings). To set up universal links on iOS, refer to Apple’s documentation on [Allowing Apps and Websites to Link to Your Content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

In Unity, universal links are handled the same way as URL schemes. When iOS opens your application from a universal link, Unity exposes the URL through [Application.absoluteURL](../ScriptReference/Application-absoluteURL.html) and [Application.deepLinkActivated](../ScriptReference/Application-deepLinkActivated.html). For cold start versus running application behavior, refer to [Using deep links](deep-linking.html#using-deep-links).

## Additional resources

* [Deep linking](deep-linking.html)

Integrating Unity into native iOS applications

iOS authorizations in Unity

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)