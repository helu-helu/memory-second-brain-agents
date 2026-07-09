* [Assets and media](assets-and-media.html)
* [Caching assets](importing-caching-assets.html)
* Configure Unity Accelerator in the Editor

Verify the Unity Accelerator version

Stop and restart Unity Accelerator

# Configure Unity Accelerator in the Editor

To configure your Unity Editor to use Unity **Accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator), perform the following steps:

1. Open the **Project Settings** window (**Edit** > **Project Settings**) and select **Editor** from the left panel.
2. Under the **Accelerator Cache Server** section, set **Mode** to **Enabled**.
3. Fill in the **IP address** with the cache server address (hostname/IP and port). The setup wizard displays the server address at the end of setup in this format: `[Hostname]:[Port]`. You can also find this information in the `unity-accelerator.log` file. The default port for secure access is `10443`. For insecure access, it is `10080`.
4. Select the **Check Connection** button to test connectivity.

If the Check Connection test fails, check the hostname/IP and port values are correct and that the hostname/IP is accessible from your current machine.

## Customize settings

You can configure further settings such as a different namespace prefix, and upload and download preferences in the **Project Settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings) window. Note that the namespace prefix is used as the prefix to 3 different namespaces, one for metadata, one for import artifacts and one for **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) compilation artifacts.

It’s best practice to set a different namespace prefix from the default, so that you can ensure isolation from other projects and can help prevent cache corruption. You could use a namespace prefix that includes your project name, and the Unity version you’re using, for example `GameProjectX_6000.1`. To set the namespace, edit the **Namespace prefix** field.

You can also individually disable uploading or downloading. For example, for larger teams it is often good practice to only allow developers to pull from the cache, and only allow a single user or a build machine to upload. When used in combination with source control, the single user or build machine would check out the latest source, and perform a full import of any new asset data and upload the resulting artifacts to the Accelerator. Developers would then be able to pull from source control and pull the import artifacts from the Accelerator saving them the time importing them. This might help mitigate any issues with corrupted assets, ensuring that everyone recieves the same import data from a single source of truth.

You can also configure Unity Accelerator to use the global settings (**Unity** > **Settings** > **Asset Pipeline**) which is used by default for all projects unless overridden in the Project Settings.

For more information on the settings refer to [Cache Server Project Settings reference](cache-server-project-settings.html).

## Connectivity status

The status of the Unity Accelerator’s connectivity is displayed in the bottom right corner of the Unity Editor window.

![Unity Accelerator connectivity](../uploads/Main/AcceleratorConnect.png)


Unity Accelerator connectivity

## Additional resources

* [Install Unity Accelerator with the installer](accelerator-install-installer.html)
* [Install Unity Accelerator with Docker Hub](accelerator-install-docker.html)
* [Cache Server Project Settings reference](cache-server-project-settings.html)

Verify the Unity Accelerator version

Stop and restart Unity Accelerator

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)