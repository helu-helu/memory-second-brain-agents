* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* [Package manifest](cus-pkg-manifest.html)
* Edit the package manifest

Package manifest

Package manifest reference

# Edit the package manifest

The package manifest (`package.json`) defines the metadata for a Unity Package Manager (UPM) package, including its registered name, version, dependencies, Unity Editor compatibility, and other configuration details. The Unity Editor uses this file to identify, load, and manage the package within the project.

You can view or edit the package manifest depending on the context:

* View the contents of the package manifest for **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
  See in [Glossary](Glossary.html#UPMpackage) you added to your project from a registry, as a tarball, or from a Git URL.
* Edit the contents of the package manifest for packages you’re developing or customizing.

## View the package manifest

For all packages, including **immutable**You cannot change the contents of an immutable (read-only) package. This is the opposite of **mutable**. Most packages are immutable, including packages downloaded from the package registry or by Git URL.  
See in [Glossary](Glossary.html#immutable) packages, you can view most of the package manifest’s properties directly in the Unity Editor:

1. Open the **Package Manager** window.
2. Select a package from the [list panel](upm-ui-list.html).
3. Use one of the following methods to access the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window:

   * From the [details panel](upm-ui-details.html), select **Manage** > **Open Manifest**.
   * Manually open or go to the [Inspector window](InspectorOptions.html).

The **Inspector** window displays information about the package, which it reads from the package manifest file (`package.json`).

To view all fields, including ones not shown in the **Inspector** window, open the `package.json` file with one of the following methods:

* From the [details panel](upm-ui-details.html), select **Manage** > **Open Manifest Externally**, to open `package.json` in the script editor defined in [Preferences](Preferences.html) > **External Tools**.
* [Locate the manifest file](#locate-manifest) manually and open it in a script editor.

## Locate the manifest file

You can locate the `package.json` file to view the complete contents of the package manifest. If the package is **mutable**You can change the contents of a mutable package. This is the opposite of **immutable**. Only **Local package****s** and **Embedded package****s** are mutable.  
See in [Glossary](Glossary.html#mutable), you can also edit the file.

You can use several methods to locate the manifest file.

### Locate the manifest file using the Package Manager window

1. Open the **Package Manager** window.
2. Select a package from the [list panel](upm-ui-list.html).
3. From the [details panel](upm-ui-details.html), select **Locate**. Focus shifts to the **Project** window, with the package manifest file (`package.json`) highlighted.
4. To open the package manifest file, right-click `package.json` and select **Open**. You can also select **Show in Explorer** (Windows) or **Reveal in Finder** (macOS), then open the file manually.

### Locate the manifest file manually

1. Open your operating system’s file management application.
2. Go to the folder for your Unity project or the folder where you’re developing a **local package**A *local* package already exists on the file system, usually outside the project folder. To install the package, notify the Package Manager of its location through the **Packages** window. [More info](upm-ui-local.html)  
   See in [Glossary](Glossary.html#localpackage).
3. If you’re in the Unity project folder, open the `Packages` subfolder, then go to your package’s subfolder
4. Open the `package.json` file with your preferred script editor.

With the `package.json` file open, refer to the [package manifest reference](upm-manifestPkg.html) to identify the different fields and their usage.

## Edit the manifest file for mutable packages

If you’re developing a UPM package or customizing a registry package you copied into your project, follow these steps when you need to make changes to the manifest file.

You can use several methods to edit the manifest file.

### Edit the manifest file within the Unity Editor

1. Open the **Package Manager** window.
2. Select your package from the [list panel](upm-ui-list.html).
3. From the [details panel](upm-ui-details.html), select the **Manage** dropdown button and select **Edit Manifest**.

   **Note**: You can also manually open or change to the [Inspector window](InspectorOptions.html) and select **Edit**.
4. Make your changes while referring to the [package manifest reference](upm-manifestPkg.html).

   **Note**: If you change the **Name** field in the **Inspector** window, changes replace only the final identifier in the `name` property of the [package manifest](upm-manifestPkg.html)Each package has a *manifest*, which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)  
   See in [Glossary](Glossary.html#packagemanifest) file.
5. Select **Apply** to save your changes.

If fields you need to edit aren’t available in the **Inspector** window, use the manual method for [editing the manifest file in a script editor](#edit-man-editor).

### Edit the manifest file in a script editor

1. Open the **Package Manager** window.
2. Select your package from the [list panel](upm-ui-list.html).
3. From the [details panel](upm-ui-details.html), select the **Manage** dropdown button and select **Edit Manifest Externally**. The `package.json` file opens in the script editor defined in [Preferences](Preferences.html) > **External Tools**.
4. Make your changes while referring to the [package manifest reference](upm-manifestPkg.html).
5. Save the file.

## Additional resources

* [Package types](upm-package-types.html)
* [Package creation](cus-pkg-lp.html)
* [Package manifest reference](upm-manifestPkg.html)

Package manifest

Package manifest reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)