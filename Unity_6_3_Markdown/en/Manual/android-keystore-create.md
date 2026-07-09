* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Getting started with Android](android-getting-started.html)
* [Android keystores](android-keystore.html)
* Create a new keystore

Keystore Manager window reference

Add keys to a keystore

# Create a new keystore

Use the Keystore Manager window to create a new keystore to sign your application before publishing.

To create a new keystore:

1. Open the [Keystore Manager](android-keystore-manager.html) window (menu: **Edit** > **Project Settings** > **Player** > **Android** > **Publishing Settings**).
2. In the top-left of the window, select **Keystore** > **Create New**.
3. Choose from the following options to save your keystore file to a default location. You can navigate to a different folder to save the file at any other location.

   * Select **Anywhere** to save the keystore file in your Project folder.
   * Select **In Dedicated Location** to save the keystore file to a path set in **Keystores Dedicated Location**.

   For more information, refer to [Choose the keystore location](#choose-the-keystore-location).
4. In the **Password** field, enter a password for the keystore, then re-enter it in the **Confirm password** field.
5. Add a key to finish creating the keystore. For instructions, refer to [Add keys to a keystore](android-keystore-add-keys.html).

   **Note**: A keystore must contain at least one key.

## Choose the keystore location

You can create a new keystore anywhere on your computer through the following options under **Keystore** > **Create New**. These options open a specific folder on your machine by default, which you can change.

| **Option** | **Description** |
| --- | --- |
| **Anywhere** | Opens the file explorer at the root of your Project folder. |
| **In Dedicated Location** | Opens the file explorer at the location set in **Keystores Dedicated Location**. By default, this path points to the home directory on your machine, `$HOME/` on macOS and `%USER_HOME%\` on Windows.   To change this default path, go to **Edit** > **Preferences** (macOS: **Unity > Settings**) and then navigate to **External Tools** > **Android** > **Keystores Dedicated Location**. Select **Browse** to choose a location or enter a path in the text box. |

The keystore location determines how Unity stores the path to the keystore file. If you save the keystore in your Project folder or the dedicated location, Unity saves a relative path to the keystore. Otherwise Unity saves an absolute path to the keystore.

If you store a keystore in a dedicated location, each collaborator on your project can specify a different dedicated location on their machine to store the keystore file. Unity then resolves the keystore location using the dedicated location and the relative path. However, as the dedicated location is outside the Project folder, the keystore file isn’t tracked by **version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
See in [Glossary](Glossary.html#versioncontrol), and hence not accessible for collaboration. To allow collaborators to access the same keystore file, consider storing the keystore file in a shared directory.

## Additional resources

* [Keystore Manager window reference](android-keystore-manager.html)
* [Add keys to a keystore](android-keystore-add-keys.html)

Keystore Manager window reference

Add keys to a keystore

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)