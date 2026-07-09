* [Programming in Unity](scripting.html)
* [Code optimization](scripting-optimization.html)
* [Write multithreaded code with the job system](job-system.html)
* Jobs overview

Job system overview

Create and run a job

# Jobs overview

A job is a small unit of work that does one specific task. A job receives parameters and operates on data, similar to how a method call behaves. Jobs can be self-contained, or they can depend on other jobs to complete before they can run. In Unity, a job refers to any struct that implements [the `IJob` interface.](../ScriptReference/Unity.Jobs.IJob.html)

Only the main thread can schedule and complete jobs. It can’t access the content of any running jobs, and two jobs can’t access the contents of a job at the same time. To ensure efficient running of jobs, you can make them dependent on each other. Unity’s job system allows you to create complex dependency chains to ensure that your jobs complete in the correct order.

## Job types

* [IJob](../ScriptReference/Unity.Jobs.IJob.html): Runs a single task on a job thread.
* [IJobParallelFor](../ScriptReference/Unity.Jobs.IJobParallelFor.html): Runs a task in parallel. Each worker thread that runs in parallel has an exclusive index to access shared data between worker threads safely.
* [IJobParallelForTransform](../ScriptReference/Jobs.IJobParallelForTransform.html): Runs a task in parallel. Each worker thread running in parallel has an exclusive Transform from the transform hierarchy to operate on.
* [IJobFor](../ScriptReference/Unity.Jobs.IJobFor.html): The same as `IJobParallelFor`, but allows you to schedule the job so that it doesn’t run in parallel.

## Additional resources

* [Create a job](job-system-creating-jobs.html)
* [Job dependencies](job-system-job-dependencies.html)
* [Parallel jobs](job-system-parallel-for-jobs.html)

Job system overview

Create and run a job

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)