* [Assets and media](assets-and-media.html)
* [Caching assets](importing-caching-assets.html)
* Cache Server Project Settings reference

Mirror multiple Unity Accelerator instances

Unity Accelerator Prometheus metrics reference

# Cache Server Project Settings reference

You can adjust how Unity Accelerator works with the Cache Server Project Settings. To open the Cache Server settings go to **Edit > Project Settings > Editor > Accelerator Cache Server**

| **Setting** | **Description** |
| --- | --- |
| **Mode** | Choose whether to use the cache server. Choose from the following options:  * **Use global settings:** Uses the settings in the **Preferences** window (**Settings > Asset Pipeline > Unity Accelerator**). * **Enabled**: Enable the cache server. * **Disabled:** Disable the cache server. |
| **IP Address** | Input the **accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html) See in [Glossary](Glossary.html#Accelerator)’s IP address and port. |
| **Check Connection** | Select **Check Connection** to test the connectivity of the accelerator. |
| **Namespace prefix** | Set a custom namespace for the server. |
| **Download** | Enable downloads from the cache server. |
| **Upload** | Enable uploads from the cache server. |
| **TLS/SSL** | Enable encryption on the cache server. |
| **Authentication (Using Unity ID)** (Obsolete) | **Warning:** This setting is obsolete. Do not use it in your project.  Enable authentication for the cache server using Unity ID. |
| **Content Validation** | Select the level of content validation: Disabled, Upload Only, Enabled, Required. |
| **Download Batch Size** | Set the size of download. |

## Additional resources

* [Configure Unity Accelerator in the Editor](accelerator-configure.html)

Mirror multiple Unity Accelerator instances

Unity Accelerator Prometheus metrics reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)