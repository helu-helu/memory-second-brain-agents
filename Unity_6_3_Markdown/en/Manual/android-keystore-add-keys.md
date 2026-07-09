* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Getting started with Android](android-getting-started.html)
* [Android keystores](android-keystore.html)
* Add keys to a keystore

Create a new keystore

Load a keystore

# Add keys to a keystore

This page explains how to use the Keystore Manager window to add a new key to an existing keystore. Unity requests the same information as Android Studio does when you generate a key or keystore through that. Unity doesn’t validate this information. If you leave a field blank, Unity uses an empty value. This might affect the final validity of the key. For more information, see [Generate an upload key and keystore](https://developer.android.com/studio/publish/app-signing#generate-key).

This task is relevant if you want to create a new keystore from the Keystore Manager window, or want to store multiple keys in the same keystore.

To add a key to a keystore:

1. Open the [Keystore Manager window](android-keystore-manager.html).
2. Either start to create a new keystore, or load an existing keystore. To do this, see [Create a new keystore](android-keystore-create.html) or [Load a keystore](android-keystore-load.html) respectively.
3. In the **New Key Values** section, add values for all the relevant properties. For information on each property, see [Keystore Manager window reference](android-keystore-manager.html).
4. Select **Add key**. If this button is grayed out, there is an issue with one of your key properties and the text to the left of this button explains what the issue is.
5. In the dialogue window that appears, if you want to use the keystore as your Project keystore and the new key as the active key for the Project, select **Yes**. Otherwise, select **No**.

## Additional resources

* [Create a new keystore](android-keystore-create.html)
* [Load a keystore](android-keystore-load.html)

Create a new keystore

Load a keystore

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)