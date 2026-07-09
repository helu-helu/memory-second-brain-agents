* [Assets and media](assets-and-media.html)
* [Caching assets](importing-caching-assets.html)
* Use Unity Accelerator on the command line

Monitor Unity Accelerator

Mirror multiple Unity Accelerator instances

# Use Unity Accelerator on the command line

Unity **Accelerator**The Unity Accelerator is an external tool that provides an asset cache that keeps copies of a team’s imported assets. The goal of the Accelerator is to speed up teamwork and reduce iteration time by coordinating asset sharing so that you don’t need to reimport portions of your project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator) has a large set of command line tools you can use to troubleshoot, configure, and make use of one or more cache servers. For ease of use, it’s best practice to add the location of the `unity-accelerator` executable to your `PATH`. The executable was installed in the path you chose when running the installer, for example `C:\Program Files\Unity\accelerator`.

The CLI tool has an extensive help system. To get started, you can run `unity-accelerator` with no arguments:

```
$ unity-accelerator
Unity Accelerator v1.0.524+g96c5e18

Run on a local network to speed up transactions with Unity Services.

.....
```

You can also run `unity-accelerator --all-help` to output all the help text for all commands in one go.

When working on a specific cache server, to reconfigure it for example, it’s best to change your working directory to the same as where the `unity-accelerator.cfg` file is. You can also set the `UNITY_ACCELERATOR_PERSIST` environment variable to that directory, or you can try to remember to always use the `--persist <dir>` option.

One rather common set of cli tools used are the dashboard tools:

```
$ unity-accelerator dashboard password newaccount
Password: ****
   Again: ****
$ unity-accelerator dashboard list
admin
newaccount
$ unity-accelerator dashboard url
http://172.18.37.249:8080/dashboard/
```

That final tool, `dashboard url`, is useful to find out what URL to put in your browser to visit the built-in dashboard.

## Additional resources

* [Command line arguments reference](EditorCommandLineArguments.html#accelerator)

Monitor Unity Accelerator

Mirror multiple Unity Accelerator instances

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)