* [Platform development](PlatformSpecific.html)
* [Embedded systems](embedded-systems.html)
* Configurations for embedded platforms

Embedded systems

Logging in embedded platforms

# Configurations for embedded platforms

Unity supports a wide range of embedded platform configurations through [embedded support plans](https://unity.com/products/compare-plans/embedded).

When starting an embedded support plan, the chosen configuration will be fixed and supported throughout the length of the support plan. Unity only supports deployment to these embedded platforms with a valid embedded support plan. For more information, contact your Account Manager or the [Unity Sales](https://create.unity.com/unity-for-industries) team.

**Note:** For all configurations, usage of Unity for commercial embedded systems is subject to the [Embedded Software Restriction](https://unity.com/legal/terms-of-service#:~:text=Embedded%20Software%20Restriction) in the Unity terms of service.

## Configurations supported with Full Embedded Support plan

Unity is verified and supported to run on chipsets from AMD, Intel, Mediatek, Qualcomm, Renesas, Rockchip, Samsung, and others, depending on the requirements of each project. Support for these chipsets is currently limited to a [Full Embedded Support plan](https://unity.com/products/compare-plans/embedded#:~:text=Full).

## Verified configurations with Basic Embedded Support plan

Verified embedded platform configurations are continuously tested and confirmed to run Unity, using a publicly available board support package (BSP) provided by the chipset or OS vendor. These are the only configurations supported through the [Basic Embedded Support plan](https://unity.com/products/compare-plans/embedded#:~:text=Basic).

| **Vendor** | **Model** | **Verified OS/BSP** |
| --- | --- | --- |
| **NVIDIA** | [Jetson AGX Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/) | Ubuntu for Tegra |
| **NXP** | [I.MX8 QM](https://www.nxp.com/design/design-center/development-boards-and-designs/i-mx-evaluation-and-development-boards/i-mx-8quadmax-multisensory-enablement-kit-mek:MCIMX8QM-CPU) | * Yocto Linux * QNX 7.1 * QNX 8 * Android Automotive 13 * Android Automotive 14 |
| **Raspberry Pi** | * [Raspberry Pi 4b](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) * [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) | **For Raspberry Pi 4b:**  * QNX 7.1 (Vulkan only) * Yocto Linux  **For Raspberry Pi 5:**  * Yocto Linux * Raspberry Pi OS |

**Notes:**

* The configurations listed above are verified to run Unity with the following graphics APIs:
  + Vulkan 1.0
  + OpenGL ES 3.0
* The performance of these configurations is hardware-dependent and might vary based on the specific use case. On some embedded configurations, the available **feature set**A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](FeatureSets.html)  
  See in [Glossary](Glossary.html#featureset) is limited.
* Multisample anti-aliasing (MSAA) might cause rendering issues on i.MX8 devices for both QNX and embedded Linux. If you’re experiencing rendering issues, disable MSAA in your **project settings**A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](comp-ManagerGroup.html)  
  See in [Glossary](Glossary.html#ProjectSettings).

## Additional resources

* [Unity for embedded systems](https://unity.com/solutions/embedded)
* [System requirements](system-requirements.html)

Embedded systems

Logging in embedded platforms

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)