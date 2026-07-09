* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Getting started with Android](android-getting-started.html)
* [Android keystores](android-keystore.html)
* Load a keystore

Add keys to a keystore

Developing for Android

# Load a keystore

This page explains how to load an existing keystore and select a key from it to use as the project key.

This is relevant if you want to publish your application, because you must provide a key from a keystore when you sign the application.

To load an existing keystore:

1. Open [Android Publishing Settings](class-PlayerSettingsAndroid.html#Publishing).
2. Under the **Project Keystore** heading, enable **Custom Keystore**.
3. Click the drop-down below **Custom Keystore**.
4. Select **Browse** to load a keystore from your file system, or select a keystore from below the partition in the UI. The keystores below the partition are those stored in the keystores dedicated location. For more information, see [Choose the keystore location](android-keystore-create.html#choose-the-keystore-location).
5. Enter the password for the keystore in the **Keystore password** property field. If the password is correct, Unity loads the keystore.

After you load a keystore into your project, select a key from the keystore to use as the key alias. To do this:

1. Use the dropdown list in **Key alias** to select the key you want to use.
2. In the **Key password** property field, enter the password for the key.

## Additional resources

* [Keystore Manager window reference](android-keystore-manager.html)
* [Add keys to a keystore](android-keystore-add-keys.html)
* [useCustomKeystore API reference](../ScriptReference/PlayerSettings.Android-useCustomKeystore.html)
* [keystoreName API reference](../ScriptReference/PlayerSettings.Android-keystoreName.html)
* [keystorePass API reference](../ScriptReference/PlayerSettings.Android-keystorePass.html)
* [keyaliasName API reference](../ScriptReference/PlayerSettings.Android-keyaliasName.html)
* [keyaliasPass API reference](../ScriptReference/PlayerSettings.Android-keyaliasPass.html)

Add keys to a keystore

Developing for Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)