* [Get started](get-started.html)
* [Install and upgrade](install-and-upgrade.html)
* [Deploy Unity across your enterprise](ent-deployment.html)
* Enable Unity Editor installation by standard users (Windows)

Deploy Unity across your enterprise

Set up Unity for web proxies

# Enable Unity Editor installation by standard users (Windows)

By default, installing Unity Editors is a process that requires administrator privileges.

Starting with 2023.1, you can enable standard users on Windows to install Unity Editors without elevated privileges.

## Important considerations for third-party requirements

Once enabled, this feature can reduce the administrators’ involvement to installing only the following items:

* Any optional components, such as Visual Studio Code or platform-specific build support.
* Any [missing dependencies](#next-steps) the Unity installer detects, such as Visual C++ runtime libraries. These dependencies change infrequently, so an administrator doesn’t need to intervene every time a standard user installs other instances of the Unity Editor.

## Before you begin

Make sure you have write access to the `C:\ProgramData\Unity\config` folder.

Be sure to follow these practices when editing JSON files:

* Use straight double quotes ("") and not curly quotes (“”).
* Separate key:value pairs with a comma.
* Check the syntax of the JSON with a validator. You can use the `Get-Content` and `ConvertFrom-Json` cmdlets in the PowerShell, as shown in [this example](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json?view=powershell-5.1#example-3-convert-a-json-string-to-a-custom-object).

## Procedure

To enable standard users to install the Unity Editor:

1. Make sure the following path exists. Create any of its folders, if necessary:

   ```
   C:\ProgramData\Unity\config
   ```
2. Make sure the following file exists. Create it, if necessary:

   ```
   C:\ProgramData\Unity\config\services-config.json
   ```

   If you need to create the file, make sure it has at least the following content:

   ```
   {  
   }
   ```
3. Add the following entry between the curly braces in `services-config.json`:

   ```
   "hubDisableElevate": true
   ```
4. Optional: To allow multiple users of the same computer to share Unity Editor binary files without installing the same version multiple times, create a folder that will be a common destination for all Unity Editors, such as `C:\UnityEditors`. **Important**: Make sure you grant **Read** and **Write** access to this folder for **All Users**.
5. Optional: If you created a common folder in the previous step, add the `machineWideSecondaryInstallLocation` key to `services-config.json`, to make the Unity Hub use this folder. Using the folder from the previous step, the entry looks like this:

   ```
   "machineWideSecondaryInstallLocation": "C:\\UnityEditors"
   ```
6. Quit the Unity Hub and make sure it’s stopped and not just minimized to the taskbar.

## Sample configuration file

Using the values from the previous procedure, a sample `services-config.json` file looks like this:

```
{
  "hubDisableElevate": true,
  "machineWideSecondaryInstallLocation": "C:\\UnityEditors"
}
```

## Next steps

The standard user’s computer is now able to install Unity Editors without intervention from an administrator, unless the installation requires optional components or if there are dependencies. An administrator must install these items.

### Missing dependencies warning

Here’s an example of a dependencies warning that a standard user might encounter:

![Warning for missing dependencies that an administrator must install](../uploads/Main/ent-unpriv-install-00.png)


Warning for missing dependencies that an administrator must install

### List of missing dependencies

If a standard user receives a warning about missing dependencies, the installer writes a list of dependencies to a text file. The warning identifies the location of this text file. An administrator must install these dependencies before the standard user can have a stable experience using Unity.

Here’s an example of a list of missing dependencies that the Unity Installer might generate:

```
Dependency: Visual C++ 2010 runtime (x64)
Download location: https://www.microsoft.com/en-ca/download/details.aspx?id=26999
Local Installer: C:\Users\nonadmin\AppData\Local\Unity 2023.1.0a5\MissingDependencies\vcredist_x64_2010.exe
 
Dependency: Visual C++ 2013 runtime (x64)
Download location: https://www.microsoft.com/en-ca/download/details.aspx?id=40784
Local Installer: C:\Users\nonadmin\AppData\Local\Unity 2023.1.0a5\MissingDependencies\vcredist_x64_2013.exe
 
Dependency: Visual C++ 2015 runtime (x64)
Download location: https://www.microsoft.com/en-ca/download/details.aspx?id=48145
Local Installer: C:\Users\nonadmin\AppData\Local\Unity 2023.1.0a5\MissingDependencies\vcredist_x64_2015.exe
 
Make sure that the following rules are set:
netsh advfirewall firewall delete rule name=all program='C:\Users\nonadmin\AppData\Local\Unity 2023.1.0a5\Editor\Unity.exe'
netsh advfirewall firewall delete rule name=all program='C:\Users\nonadmin\AppData\Local\Unity 2023.1.0a5\Editor\Data\Tools\nodejs\node.exe'
netsh advfirewall firewall add rule name='Unity 2023.1.0a5 Editor' dir=in action=allow program='C:\Users\nonadmin\AppData\Local\Unity 2023.1.0a5\Editor\Unity.exe' profile=domain protocol=any
netsh advfirewall firewall add rule name='Unity 2023.1.0a5 Editor' dir=in action=block program='C:\Users\nonadmin\AppData\Local\Unity 2023.1.0a5\Editor\Unity.exe' profile=public protocol=any
```

## Additional resources

* [Deploy Unity across your enterprise](ent-deployment.html)
* [Install Unity](GettingStartedInstallingUnity.html)

Deploy Unity across your enterprise

Set up Unity for web proxies

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)