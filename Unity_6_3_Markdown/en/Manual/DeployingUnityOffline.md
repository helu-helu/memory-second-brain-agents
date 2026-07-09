* [Get started](get-started.html)
* [Install and upgrade](install-and-upgrade.html)
* [Install Unity](GettingStartedInstallingUnity.html)
* Install Unity on offline computers

Install Unity from the command line

Deploy Unity across your enterprise

# Install Unity on offline computers

The Unity Download Assistant supports offline deployment.

## Before you begin

Make sure you’ve run the Download Assistant on an online computer. For more information, refer to [Install Unity using Download Assistant](install-unity-with-download-assistant.html). This process generates the installer files and the script that the offline computers require for the installation process.

## Unity installation on offline computers

Follow these steps to run the script that the Download Assistant generates to install Unity Editor and components on offline computers.

1. Transfer the folder that includes all the downloaded installation files and the `install.sh` or `install.bat` file to the offline computer.
2. On the offline computer, run the `install.sh` or `install.bat` file:

   * On macOS:
     1. Open Terminal.
     2. Go to the folder that contains the `install.sh` file.
     3. Run `sudo ./install.sh`. This command prompts you for your password, which doesn’t appear on the screen as you type it.
   * On Windows:
     1. In the **Start** menu, search for `cmd.exe`.
     2. Right-click **Command Prompt**.
     3. Select **Run as administrator**.
     4. Go to the folder that contains the `install.bat` file.
     5. Run `install.bat`.
3. Confirm that the script installed the Unity Editor on this computer.

   * On macOS, the default location is `Applications/Unity`.
   * On Windows, the default location is `C:\Program Files\Unity <version>`.
4. Repeat these steps on other offline computers if needed.

## Activate a license on the offline computer

After you install the Unity Editor on the offline computer, its user needs to activate their license on that computer by using the [manual activation method](ManualActivationGuide.html).

## Additional resources

* [Install Unity using Download Assistant](install-unity-with-download-assistant.html)
* [Install Unity from the command line](InstallingUnity.html)

Install Unity from the command line

Deploy Unity across your enterprise

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)