* [Animation](AnimationSection.html)
* [Mecanim Animation system](animation-mecanim.html)
* [Animator Controller](animation-animator-controller.html)
* [Animation state machine](AnimationStateMachines.html)
* Animation Parameters

Animation States

State Machine Transitions

# Animation Parameters

Animation Parameters are variables that are defined within an **Animator Controller**Controls animation through Animation Layers with Animation State Machines and Animation Blend Trees, controlled by Animation Parameters. The same Animator Controller can be referenced by multiple models with Animator components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) that can be accessed and assigned values from **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). This is how a script can control or affect the flow of the **state machine**The set of states in an Animator Controller that a character or animated GameObject can be in, along with a set of transitions between those states and a variable to remember the current state. The states available will depend on the type of gameplay, but typical states include things like idling, walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine).

![Animation Parameters in the Animator window.](../uploads/Main/AnimationEditorParametersSection.png)


Animation Parameters in the Animator window.

For example, the value of a parameter can be updated by an [animation curve](animeditor-AnimationCurves.html) and then accessed from a script so that, say, the pitch of a sound effect can be varied as if it were a piece of animation. Likewise, a script can set parameter values to be picked up by Mecanim. For example, a script can set a parameter to control a [Blend Tree](class-BlendTree.html).

Default parameter values can be set up using the Parameters section of the **Animator window**The window where the Animator Controller is visualized and edited. [More info](AnimatorWindow.html)  
See in [Glossary](Glossary.html#AnimatorWindow), selectable in the top right corner of the Animator window. They can be of four basic types:

* *Integer* - a whole number
* *Float* - a number with a fractional part
* *Bool* - true or false value (represented by a checkbox)
* *Trigger* - a boolean parameter that is reset by the controller when consumed by a transition (represented by a circle button)

Parameters can be assigned values from a script using functions in the Animator class: [SetFloat](../ScriptReference/Animator.SetFloat.html), [SetInteger](../ScriptReference/Animator.SetInteger.html), [SetBool](../ScriptReference/Animator.SetBool.html), [SetTrigger](../ScriptReference/Animator.SetTrigger.html), and [ResetTrigger](../ScriptReference/Animator.ResetTrigger.html).

Here’s an example of a script that modifies parameters based on user input and **collision**A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#collision) detection:

```
using UnityEngine;
using System.Collections;

public class SimplePlayer : MonoBehaviour {

    Animator animator;
    
    // Use this for initialization
    void Start () {
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update () {
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");
        bool fire = Input.GetButtonDown("Fire1");

        animator.SetFloat("Forward",v);
        animator.SetFloat("Strafe",h);
        animator.SetBool("Fire", fire);
    }

    void OnCollisionEnter(Collision col) {
        if (col.gameObject.CompareTag("Enemy"))
        {
            animator.SetTrigger("Die");
        }
    }
}
```

Animation States

State Machine Transitions

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)