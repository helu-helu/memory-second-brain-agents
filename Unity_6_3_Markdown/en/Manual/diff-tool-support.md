* [Get started](get-started.html)
* [Project configuration](project-configuration.html)
* [Version control](VersionControl.html)
* Diff tool support

Smart merge

Default project directories

# Diff tool support

You can use the [**Revision Control Diff/Merge** setting](preferences-external-tools.html) to set an installed diff tool as the default revision tool. You can also use this setting to define a custom revision tool with specific layouts.

If you want to change the diff tool that Unity uses, open the [Preferences](Preferences.html) window, and navigate to the **External Tools** section. Select your preferred tool from the **Revision Control Diff/Merge** dropdown list.

## Set up a custom revision tool

To set up a custom revision tool, follow these steps:

1. Open the [Preferences](Preferences.html) window, and navigate to the **External Tools** section.
2. In the **Revision Control Diff/Merge** dropdown list, select **Custom Tool**.
3. Enter the path to the custom tool’s installation folder. On macOS, this should point to the *Contents / MacOS* folder in the tool’s installation folder.
4. Enter the arguments for two-way diffs, three-way diffs, and merges.

To specify file layout in the revision tool, use these arguments:

| **Property** | **Function** |
| --- | --- |
| `#LTITLE` | Left title |
| `#RTITLE` | Right title |
| `#ATITLE` | Ancestor title |
| `#LEFT` | Left file |
| `#RIGHT` | Right file |
| `#ANCESTOR` | Ancestor file |
| `#OUTPUT` | Output file |
| `#ABSLEFT` | Absolute path to the left file |
| `#ABSRIGHT` | Absolute path to the right file |
| `#ABSANCESTOR` | Absolute path to the ancestor file |
| `#ABSOUTPUT` | Absolute path to the output file |

Examples:

![SourceGear DiffMerge](../uploads/Main/SourceGearDiffMerge.png)


SourceGear DiffMerge


![P4Merge](../uploads/Main/P4DiffMerge.png)


P4Merge

## Additional resources

* [Preferences reference](Preferences.html)
* [Version control integrations](Versioncontrolintegration.html)

Smart merge

Default project directories

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)