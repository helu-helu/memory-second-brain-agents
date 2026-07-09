* [Assets and media](assets-and-media.html)
* [Caching assets](importing-caching-assets.html)
* Monitor Unity Accelerator

Stop and restart Unity Accelerator

Use Unity Accelerator on the command line

# Monitor Unity Accelerator

Unity **Accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator) has a built-in dashboard to monitor and configure changes.

The URL to access your dashboard is `http://hostname[:port]/dashboard` where `hostname:port` is the hostname/IP and port number of the Unity Accelerator you have installed. Note that the default port is `80` for http and `443` for https but you can change this after the installation.

Each Unity Accelerator hosts [Prometheus metric reports](https://prometheus.io/) as `http://hostname[:port]/metrics`, which you can query from the local network. For a full list of metrics monitoring, refer to [Unity Accelerator Prometheus metrics reference](accelerator-metrics-reference.html). The full configuration of Unity Accelerator is available through its unity-accelerator.cfg file.

## Additional resources

* [Unity Accelerator Prometheus metrics reference](accelerator-metrics-reference.html)
* [Configure Unity Accelerator in the Editor](accelerator-configure.html)

Stop and restart Unity Accelerator

Use Unity Accelerator on the command line

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)