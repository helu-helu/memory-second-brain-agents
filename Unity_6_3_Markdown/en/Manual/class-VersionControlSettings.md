* [Unity Editor interface](unity-editor.html)
* [Unity Editor settings reference](editor-settings-reference.html)
* [Project Settings reference](comp-ManagerGroup.html)
* Version Control

UI Toolkit project settings

Unity Editor analytics

# Version Control

You can use Unity in conjunction with most common version control tools, including Perforce and [Unity Version Control](https://unity.com/solutions/version-control).

To access the Version Control settings, go to **Edit** > **Project Settings** then select the **Version Control** category.

| **Property** |  | **Description** |
| --- | --- | --- |
| **Mode** |  | Select the version control mode. |
|  | **Hidden meta files** | Hide the .meta files in your operating system’s file explorer. Unity does not show .meta files in the Project view, no matter which mode you choose. |
|  | **Visible meta files** | Select this option to work with a version control system that Unity doesn’t support. This is the default setting. You can then manage the source Assets and metadata for those Assets with a version control system of your choice. |
|  | **Perforce** | Select this option if you use [Perforce](https://www.perforce.com/)A version control system for file change management. [More info](perForceIntegration.html) See in [Glossary](Glossary.html#Perforce) as your version control system. |
| **Username** |  | Enter the username associated with your Perforce account. This property is only visible when **Mode** is set to **Perforce**. |
| **Password** |  | Enter the password associated with your Perforce account. This property is only visible when **Mode** is set to **Perforce**. |
| **Workspace** |  | Enter your workspace. For example, `Example**Workspace**1`. This property is only visible when **Mode** is set to **Perforce**. |
| **Server** |  | Enter the server your Unity Project is on. For example, localhost:1666. This property is only visible when **Mode** is set to **Perforce**. |
| **Host** |  | Enter the hostname that you want your computer to impersonate. For example, workstation123.perforce.com. This property is only visible when **Mode** is set to **Perforce**. |
| **Log Level** |  | Select how much version control information to receive in Unity’s console log. |
|  | **Verbose** | Log every operation related to version control. This option provides very detailed logging, and is useful if you want to debug your version control setup. This property is only visible when **Mode** is set to **Perforce**. |
|  | **Info** | Log errors, warnings, and information related to version control. |
|  | **Notice** | Log errors and warnings. |
|  | **Fatal** | Unity prints only fatal errors to the console. |
| **Status** |  | Display information on the status of the connection to the version control system. If you are not connected, select **Connect** to connect to the system you have configured. This property is only visible when **Mode** is set to **Perforce**. |
| **Automatic Add** |  | When this setting is enabled, automatically add your files to the version control system when you add them to the Project, either via the Editor or the folder on disk. When this setting is disabled, you need to add files manually to the version control system. This setting is enabled by default. This property is only visible when **Mode** is set to **Perforce**. |
| **Work Offline** |  | Enable this setting to work offline. When this setting is enabled, you need to reconcile offline work in P4V or use the reconcile command in P4 to bring the Perforce server depot up to date with the work you did while offline. For more information, refer to [Working offline with Perforce](perForceIntegration.html). This property is only visible when **Mode** is set to **Perforce**. |
| **Async Update** |  | Enable this setting to use asynchronous version control status queries. When enabled, Perforce updates the version control status of files without stalling the Unity Editor. Use this setting when the connection to your version control server has high latency.    **Note:** Only status queries are asynchronous. Unity synchronously performs operations that change the state of files, or require up-to-date knowledge of a file status. This property is only visible when **Mode** is set to **Perforce**. |
| **Show Failed Checkouts** |  | Enable this property to display a dialog when Perforce can’t perform the check out operation. This might happen if you lose connection, or if another user has exclusively checked out the Asset you want to edit. This property is only visible when **Mode** is set to **Perforce**. |
| **Overwrite Failed Checkout Assets** |  | When you enable this setting, Unity saves any Assets that can not be checked out. This means Unity forces through a save to a file, even if Perforce cannot check out the file. This is enabled by default. If you disable it, Unity doesn’t force your files to save if Perforce can’t check them out. This property is only visible when **Mode** is set to **Perforce**. |
| **Smart Merge** |  | [Smart Merge](SmartMerge.html) makes it easier for Unity to merge files that have changes on the same line. This is useful if several users are working on the same Project at the same time. This property is only visible when **Mode** is set to **Perforce**. |
|  | **Off** | Disable Smart Merge. |
|  | **Ask** | Enable Smart Merge, but receive a notification before you merge, if a conflict happens. This is the default setting. |
|  | **Premerge** | Automatically use Smart Merge. |
| **Version Packages Outside Project** |  | Tracks changes to packages that reside on disk outside of the Unity project’s root folder while still in the local workspace. This property is only visible when **Mode** is set to **Perforce**. |
| **Overlay Icons** |  | Enable this setting to display version control status icons in the Editor. This property is only visible when **Mode** is set to **Perforce**. |

## Additional resources

* [Version Control](VersionControl.html)A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html)  
  See in [Glossary](Glossary.html#versioncontrol)
* [Version control integration](Versioncontrolintegration.html)
* [PerForce](perForceIntegration.html)
* [SmartMerge](SmartMerge.html)

UI Toolkit project settings

Unity Editor analytics

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)