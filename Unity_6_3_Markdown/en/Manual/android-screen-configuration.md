* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Graphics for Android](android-graphics.html)
* Screen configuration

Graphics for Android

Single-pass stereo rendering for Android

# Screen configuration

Unity provides features that you can use to configure the screen when in the Editor and at runtime.

## Screen orientation

You can control the screen orientation of your application on Android devices. Detecting a change in orientation or forcing a specific orientation is useful for creating behaviors that depend on how the user holds the device.

To retrieve the current application orientation, access [Screen.orientation](../ScriptReference/Screen-orientation.html) property. The available orientations are:

| **Orientation** | **Behavior** |
| --- | --- |
| **Portrait** | The application is in portrait mode and expects the device to be upright and the home button at the bottom. |
| **PortraitUpsideDown** | The application is in portrait mode but upside down and expects the device to be upright and the home button at the top. |
| **LandscapeLeft** | The application is in landscape mode and expects the device to be upright and the home button on the right side. |
| **LandscapeRight** | The application is in landscape mode and expects the device to be upright and the home button on the left side. |

To manually control the screen orientation, set [Screen.orientation](../ScriptReference/Screen-orientation.html) to one of the above orientations, or use [ScreenOrientation.AutoRotation](../ScriptReference/ScreenOrientation.AutoRotation.html). When you enable autorotation, you can still disable some orientation on a case-by-case basis.

The following properties control autorotation:

* [Screen.autorotateToPortrait](../ScriptReference/Screen-autorotateToPortrait.html)
* [Screen.autorotateToPortraitUpsideDown](../ScriptReference/Screen-autorotateToPortraitUpsideDown.html)
* [Screen.autorotateToLandscapeLeft](../ScriptReference/Screen-autorotateToLandscapeLeft.html)
* [Screen.autorotateToLandscapeRight](../ScriptReference/Screen-autorotateToLandscapeRight.html)

The screen orientation of your application may vary depending on the device orientation set by the user, regardless of your application’s default orientation setting.

The following table shows the default screen orientation set for your application and the actual orientation the application loads in based on the device orientation.

|  | **Default screen orientation: Autorotate** | **Default screen orientation: Portrait** | **Default screen orientation: Landscape** |
| --- | --- | --- | --- |
| **Device orientation: Autorotate** | The application screen loads in portrait, and can rotate between portrait, portrait upside down, landscape right, and landscape left orientations. **Note**: On a tablet, the application screen loads in portrait or landscape orientation based on the device orientation. | The application screen loads in portrait and can rotate between portrait and portrait upside down orientations. | The application screen loads in the same orientation as the device orientation. If the device orientation is portrait, the application screen loads in portrait, and can rotate to landscape orientation. In landscape orientation, the screen can only rotate between landscape right or landscape left orientations. **Note**: On a tablet, if the user turns off the device autorotation setting, and then reopens the application, the application screen orientation remains unchanged. |
| **Device orientation: Portrait lock** | The application screen loads and remains locked in portrait orientation.  **Note**: Whilst in portrait orientation, if you set the [ScreenOrientation.AutoRotation](../ScriptReference/ScreenOrientation.AutoRotation.html) property for portrait to false, the application screen remains in portrait until you rotate the device to landscape orientation. Once in landscape, the screen can’t rotate back to portrait orientation. If you now set the [ScreenOrientation.AutoRotation](../ScriptReference/ScreenOrientation.AutoRotation.html) property for landscape to false, the screen orientation remains unchanged. | The application screen loads and remains locked in portrait orientation. | The application screen loads and remains locked in portrait orientation even if you set the portrait option to false. To allow screen rotation, assign the required orientation to [Screen.orientation](../ScriptReference/ScreenOrientation.html) property. You can enable autorotation with [ScreenOrientation.AutoRotation](../ScriptReference/ScreenOrientation.AutoRotation.html). |
| **Device orientation: Landscape lock** | The application loads and remains locked in landscape orientation. | The application loads in landscape and remains locked in landscape left or landscape right orientation depending on the device orientation even if you set either option to false.  To change the orientation, assign the required orientation to [Screen.orientation](../ScriptReference/ScreenOrientation.html) property. You can enable autorotation with [ScreenOrientation.AutoRotation](../ScriptReference/ScreenOrientation.AutoRotation.html). | The application loads in landscape and remains locked in landscape left or landscape right orientation depending on the device orientation. |

## Multi-window mode

Android’s [multi-window mode](https://developer.android.com/guide/topics/large-screens/multi-window-support) supports Unity applications. Users can resize the windows that will contain your Unity applications so it’s best practice to make your user interface scale to non-standard **aspect ratios**The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](Glossary.html#aspectratio) and resolutions.

Graphics for Android

Single-pass stereo rendering for Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)