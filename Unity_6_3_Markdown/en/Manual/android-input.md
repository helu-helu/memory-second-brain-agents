* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* Input for Android devices

Android mobile scripting

Android application size restrictions

# Input for Android devices

Mobile devices are the primary target for Android applications. Unity provides an [Input System package](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest?subfolder=/manual/index.html) to handle user input on Android devices. This input solution is enabled by default for new projects.

**Note**: Unity also supports the legacy [Input Manager](class-InputManager.html)Settings where you can define all the different input axes, buttons and controls for your project. [More info](class-InputManager.html)  
See in [Glossary](Glossary.html#InputManager) for existing projects. You can choose between the two input solutions through **Android Player settings** > **Other Settings** > **Configuration** > [**Active Input Handling**](class-PlayerSettingsAndroid.html#AndroidApplicationConfiguration).

The Input System package supports a variety of input devices on the Android platform, including mouse, keyboard, pen, touchscreen, sensors, joystick, and gamepads. For more information, refer to [Supported input devices](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest?subfolder=/manual/SupportedDevices.html) in the Input System package documentation.

For additional input features on Android, refer to the following sections:

## On-screen keyboard support

Android devices automatically display an on-screen touchscreen keyboard when users select editable UI elements, such as Input Fields created using [UGUI](https://docs.unity3d.com/Packages/com.unity.ugui@latest?subfolder=/manual/script-InputField.html), or **TextField controls**A TextField control displays a non-interactive piece of text to the user, such as a caption, label for other GUI controls, or instruction. [More info](gui-Controls.html)  
See in [Glossary](Glossary.html#TextFieldcontrol) created using [UI Toolkit](UIE-uxml-element-TextField.html), or [IMGUI](gui-Controls.html). Unity automatically activates the Android keyboard and handles input from it. If you want to manually activate and configure the Android touchscreen keyboard behavior, refer to [Mobile Keyboard](MobileKeyboard.html).

## Gamepad support

Unity provides gamepad support allowing users to use physical controllers when playing your Android games. You can configure the level of gamepad support in the **Android Player settings** > **Other Settings** > **Configuration** > [**Android Gamepad Support Level**](class-PlayerSettingsAndroid.html#AndroidApplicationConfiguration). To handle gamepad input, use the [Input System package APIs](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest?subfolder=/manual/Gamepad.html).

## Additional resources

* [Introduction to Input](input-introduction.html)
* [`gamepadSupportLevel` API](../ScriptReference/PlayerSettings.Android.gamepadSupportLevel.html)

Android mobile scripting

Android application size restrictions

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)