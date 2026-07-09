* [Platform development](PlatformSpecific.html)
* [Android](android.html)
* [Developing for Android](android-developing.html)
* [Android application entry points](android-application-entries.html)
* [The Activity application entry point](android-application-entries-activity.html)
* [Extend the default Unity activity](AndroidUnityPlayerActivity.html)
* Create a custom activity

Extend the default Unity activity

Specify Android Player command-line arguments

# Create a custom activity

To extend the default Unity activity, you create your own custom activity and set it as the application’s entry point. The process to do this is as follows:

1. Create a new activity that extends the `UnityPlayerActivity` class.

   **Note**: If you’re creating a new activity with GameActivity application entry point, you need to extend the `UnityPlayerGameActivity` class. Make sure you extend the correct class as per the application entry point you set in the [Player settings](class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
   See in [Glossary](Glossary.html#PlayerSettings).
2. Create a **plug-in**A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](./plug-ins.html)  
   See in [Glossary](Glossary.html#plug-in) to deliver the new activity to the final Unity Android application.
3. Override the [Android App Manifest](android-manifest.html) to set your new `activity` as the application’s entry point.

After you do this, you can implement custom behavior in your activity to control interactions between Unity and Android.

## Create a new activity

To create a new activity:

1. In the **Assets** folder, create a new Java (`.java`) or Kotlin (`.kt`) file.
2. In the new file, create a class that extends `UnityPlayerActivity`.

   **Note**: If you’re using GameActivity application entry point, you need to create a class that extends `UnityPlayerGameActivity` class.
3. In the new class, override the various base Activity methods to implement the custom behavior you want your activity to have. For more information, refer to Android’s [Activity](https://developer.android.com/reference/android/app/Activity.html#summary) documentation.

### Example activity

The following code sample shows an example activity that overrides multiple functions.

```
package com.company.product;
import com.unity3d.player.UnityPlayerActivity;
import android.os.Bundle;
import android.util.Log;

public class OverrideExample extends UnityPlayerActivity {
  protected void onCreate(Bundle savedInstanceState) {
    // Calls UnityPlayerActivity.onCreate()
    super.onCreate(savedInstanceState);
    // Prints debug message to Logcat
    Log.d("OverrideActivity", "onCreate called!");
  }
  public void onBackPressed()
  {
    // Instead of calling UnityPlayerActivity.onBackPressed(), this example ignores the back button event
    // super.onBackPressed();
  }
}
```

### Example activity with GameActivity application entry point

The following code sample shows an example activity with GameActivity application entry point that overrides multiple functions.

```
package com.company.product;
import com.unity3d.player.UnityPlayerGameActivity;
import android.os.Bundle;
import android.util.Log;

public class OverrideExample extends UnityPlayerGameActivity {
  protected void onCreate(Bundle savedInstanceState) {
    // Calls UnityPlayerGameActivity.onCreate()
    super.onCreate(savedInstanceState);
    // Prints debug message to Logcat
    Log.d("OverrideActivity", "onCreate called!");
  }
  public void onBackPressed()
  {
    // Instead of calling UnityPlayerGameActivity.onBackPressed(), this example ignores the back button event
    // super.onBackPressed();
  }
}
```

## Create a plug-in for the activity

To use a custom activity for a Unity Android application, you must create a plug-in to contain the activity. Activities are written in either Java or Kotlin, which means you must use one of the following types of plug-ins:

* [Android Library and Android Archive plug-ins](AndroidAARPlugins.html)
* [JAR plug-in](AndroidJARPlugins.html)
* [Java and Kotlin source plug-ins](AndroidJavaSourcePlugins.html)

If you want to create a custom activity for a single project, use Java and Kotlin source plug-ins. To create the source plug-ins, place the source files directly in the **Assets** folder of your project.

If you want to reuse the activity in multiple projects or distribute it to other people, use Android Archive (AAR) or JAR plug-ins. Managing one AAR or JAR plug-in file is easier to deliver functionalities in multiple projects.

Use an Android Library plug-in while you develop the plug-in and then compile it into an Android Archive plug-in when you complete the implementation, want to use it in multiple projects, or distribute it to other people.

After you create the plug-in, add the activity file to it.

## Set the new activity as the application entry point

After you create an activity and add it to a plug-in, you can set it as the application entry point. To do this, [modify the Android Manifest](android-modify-gradle-project-files.html) and set the `name` attribute of the [activity element](https://developer.android.com/guide/topics/manifest/activity-element) to the class name of your custom activity.

The following Android Manifest example shows how to do this:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.company.product">
  <application android:icon="@drawable/app_icon" android:label="@string/app_name">
    <activity android:name="com.YourPackage.name.OverrideExample"
             android:theme="@style/UnityThemeSelector"
             android:label="@string/app_name"
             android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>
  </application>
</manifest>
```

The following Android Manifest example shows how to do this for custom activity with GameActivity application entry point:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.company.product">
  <application android:icon="@drawable/app_icon" android:label="@string/app_name">
    <activity android:name="com.YourPackage.name.OverrideExample"
             android:theme="@style/BaseUnityGameActivityTheme"
             android:label="@string/app_name"
             android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
        <meta-data android:name="android.app.lib_name" android:value="game" />
    </activity>
  </application>
</manifest>
```

Extend the default Unity activity

Specify Android Player command-line arguments

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)