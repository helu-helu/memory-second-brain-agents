* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Testing and debugging](android-testing-and-debugging.html)
* Debug on Android devices

Testing and debugging

Android symbols

# Debug on Android devices

Unity supports the following ways to debug an application on an Android device:

* [USB debugging](#usb-debugging).
* Both wired and wireless connection through [Android Debug Bridge](#android-debug-bridge).

## USB debugging

Unity supports USB debugging for Android devices. To use USB debugging, enable developer options on your device. To do this, refer to Android’s [Configure developer options](https://developer.android.com/studio/debug/dev-options) documentation.

Use a USB cable to connect the device to your computer. If you are developing on a Windows computer, you might need to install a device-specific USB driver. Refer to the manufacturer’s website for your device for additional information.

The setup process differs for Windows and macOS. For more information on connecting your Android device to the SDK, refer to the [Run Your App](https://developer.android.com/studio/run/device) section of the Android Developer documentation.

## Android Debug Bridge

Unity supports Android Debug Bridge (ADB) over USB and wireless connection for Android devices. Wireless connection is useful when you can’t perform USB debugging, when a controller is plugged into the Android device, or when debugging **VR**Virtual Reality [More info](VROverview.html)  
See in [Glossary](Glossary.html#VR) applications and you insert the Android device into the VR Kit.

### Connect via USB

To connect an Android device to Unity through **ADB**An Android Debug Bridge (ADB). You can use an ADB to deploy an Android package (APK) manually after building. [More info](https://developer.android.com/studio/command-line/adb.html)  
See in [Glossary](Glossary.html#ADB) using a USB:

1. Enable ADB on the device. For information on how to do this, refer to [Set up a device for development](https://developer.android.com/studio/run/device#setting-up).
2. Use a USB cable to connect your Android device to the machine running Unity.
3. Navigate to **File** > **Build Profiles**.
4. Select or add an Android **build profile**A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
   See in [Glossary](Glossary.html#buildprofile).
5. From the **Run Device** build setting, select your device from the available options. If your device doesn’t appear, click **Refresh**.
6. Select **Build And Run** to build the application and run it on the device.

### Connect wirelessly

To wirelessly connect an Android device to Unity through ADB:

1. Enable wireless ADB on the device. For information on how to do this, refer to [Connect to your device using Wi-Fi](https://developer.android.com/studio/run/device#wireless).
2. Find the IP address of your device. The process to do this depends on your device manufacturer.
3. Navigate to **File** > **Build Profiles**.
4. Select or create an Android build profile.
5. From the **Run Device** build setting, select the **<Enter IP>** option.
6. In the window that opens, enter the IP address and port number of the device. If the device’s port number is `5555`, you don’t need to enter it.
7. Select **Add**. Once Unity connects to the device, the device name appears in the **Run Device** list and is selected.
8. Select **Build And Run** to build the application and run it on the device.

## View Android logs

When you run a build of your application on an Android device, Android collects messages such as stack traces and [logs](../ScriptReference/Debug.Log.html) from **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). To see these messages, Android provides the [logcat command-line tool](https://developer.android.com/studio/command-line/logcat). To use this tool with your Unity application, either:

* Launch ADB with the `logcat` parameter:  
  `$ adb logcat`
* Use the [Android Logcat](https://docs.unity3d.com/Packages/com.unity.mobile.android-logcat@latest/index.html) package which implements the logcat command-line tool and displays messages from the application in a dedicated window in Unity.

## Attach IDE to an Android application

You can attach your Integrated Development Environment (IDE) to debug the managed C# code in your Unity Android application running on the device. To do this using Visual Studio, follow these steps:

1. Run your Unity application on the Android device.
2. In Visual Studio, go to **Debug** > **Attach Unity Debugger**.
3. In the **Select Unity Instance** window, locate the Unity instance running on the device. The **Machine** column displays the device where the instance is active.
4. Choose the correct instance and select **OK**.

For information on attaching other IDEs for debugging, such as Visual Studio Code and JetBrains Rider, refer to the relevant documentation: [Unity development with VS Code](https://code.visualstudio.com/docs/other/unity) and [Debug Unity Applications](https://www.jetbrains.com/help/rider/Debugging_Unity_Applications.html).

**Tip**: Use the **Wait for Managed Debugger** [Android build setting](android-build-settings.html) to attach the debugger to the application before you run it on the device. It allows you to debug your application’s initialization code.

## Additional resources

* [Android Logcat](https://docs.unity3d.com/Packages/com.unity.mobile.android-logcat@latest/index.html)
* [Debug C# code in Unity](managed-code-debugging.html)

Testing and debugging

Android symbols

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)