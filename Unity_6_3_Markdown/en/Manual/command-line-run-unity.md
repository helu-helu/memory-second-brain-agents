* [Unity Editor interface](unity-editor.html)
* [Command-line interface](CommandLineArguments.html)
* Run Unity from a command-line interface

Command-line interface

Unity Editor command line arguments reference

# Run Unity from a command-line interface

You can launch the Unity Editor from your operating system’s command-line interface and pass in arguments to change how the Editor launches. You can also use the command line to execute specific methods from your project’s C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) at launch.

When launching the Unity Editor, the delimiter for a command-line argument value is a single space. For example, to set the window mode to borderless, use `-window-mode borderless`.

For a full list of command-line arguments, refer to [Unity Editor command-line arguments reference](EditorCommandLineArguments.html) and [Unity Player command-line arguments reference](PlayerCommandLineArguments.html).

## Launching Unity from a command-line interface

To launch a Unity project through a command-line interface, enter the directory path for the Unity application, followed by `-projectPath` and the directory path for the target project.

**Important:** If the project’s pathname contains spaces, enclose it in quotes. For example `"Unity Projects/My Game"`.

When launched in this way, the Editor receives commands and information on startup, which can be useful for test suites, automated builds, and other production tasks.

If you encounter any errors, consult the [Unity log files](log-files.html) for additional information that can help diagnose problems.

### Prerequisites

[Install the Unity Editor](GettingStartedInstallingUnity.html) in the default location through the Unity Hub. If your Editor is installed in a different location, adjust the path to reflect this. For more information about how to find your Editor’s location path, refer to [Install and uninstall Editor versions](https://docs.unity.com/hub/add-editor.html).

### Launch Unity on Linux

Type the following into the Terminal to launch Unity:

`/home/<user>/Unity/Hub/Editor/<version>/Editor/Unity -projectPath <project path>`

### Launch Unity on macOS

Type the following into the Terminal to launch Unity:

`/Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/MacOS/Unity -projectPath <project path>`

### Launch Unity on Windows

Type the following into the Command Prompt to launch Unity:

`"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -projectPath "<project path>"`

To prevent syntax errors on Windows, make sure the directory path doesn’t end with a single backslash. Use either double backslashes (`\\`) or no backslash as follows:

```
  * `"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -projectPath "C:\MyUnityProjects\MyProject"`
  * `"C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -createProject "C:\MyUnityProjects\MyProject\\"`
```

## Example script for executing methods at launch

You can use the command line to execute specific methods from your project’s C# scripts at Editor launch. The following examples demonstrate a C# script, and the command-line arguments used to execute methods from that script at launch:

An example C# script in the project:

```
using UnityEditor;
class MyEditorScript
{
     static void PerformBuild ()
     {
        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
        buildPlayerOptions.scenes = new[] { "Assets/Scene1.unity", "Assets/Scene2.unity" };
        BuildPipeline.BuildPlayer(buildPlayerOptions);
     }
}
```

The following command runs the Editor in batch mode, calls the `MyEditorScript.PerformBuild` method from the previous script, and then quits upon completion. In the Editor path, replace `<version>` with the version of Unity you want to launch, or replace the path entirely if your Unity Editor path isn’t the default.

* **Windows:**

  ```
  "C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe" -quit -batchmode -projectPath "C:\Users\UserName\Documents\MyProject" -executeMethod
  MyEditorScript.PerformBuild
  ```
* **macOS:**

  ```
  /Applications/Unity/Hub/Editor/<version>/Unity.app/Contents/MacOS/Unity -quit -batchmode -projectPath ~/UnityProjects/MyProject -executeMethod
  MyEditorScript.PerformBuild
  ```

## Additional resources

* [Unity Editor command-line arguments reference](EditorCommandLineArguments.html)
* [Unity Player command-line arguments reference](PlayerCommandLineArguments.html)

Command-line interface

Unity Editor command line arguments reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)