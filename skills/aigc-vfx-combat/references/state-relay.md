# State Relay — 逐镜状态接力

Use this file after Fight Direction is drafted and before feasibility is declared complete. Its invariant is:

`shot N+1 opening = shot N terminal state` for every material fact, unless the accepted story explicitly authorizes a time or location discontinuity.

State Relay is a design ledger, not a claim that a generated video passed continuity review. Track only facts that affect the next action, ownership, topology, location, support, or visible residue; do not repeat an entire character bible in every row.

## 1. Relay unit

For each shot or generation unit, record:

1. **opening** — inherited state before any new action;
2. **change** — the visible action or authorized transition that changes it;
3. **terminal** — exact state at the cut, including unresolved motion;
4. **next cut-in** — the subset the next shot must show immediately;
5. **evidence** — the body relation, object, surface, world anchor, form boundary or residue that makes the inheritance visible.

Do not write “保持一致” as a substitute for the actual state. A cut may change screen side because the camera crosses visibly; it does not change world position, owner, grip, support, contact or action phase.

## 2. Six state families

### A. BodyState — pose, facing and physical contact

Track each visible fighter's posture, facing, guard, loaded/support limb, occupied limb, center-of-mass condition and any body-to-body contact. A block, grapple, bind, pin or blade catch remains active until a visible release changes it.

Minimum fields when material:

```text
character; pose; facing; support limb; occupied limb; contact partner/point/state; balance or recovery state
```

### B. MotionState — direction, speed and action phase

Track world vector and screen vector separately, plus whether the action is preparing, accelerating, in contact, rebounding, recovering or at rest. A cut inside movement inherits the current phase; it does not restart the action.

For aerial action use the complete chain:

`support/load → push-off and last contact → ascent → apex → descent/attack deployment → contact → landing or continuing fall → recovery`

Name the last real support, takeoff vector, current height relation and intended landing/contact surface. Airborne bodies do not gain a new impulse, stop, hover or begin a second jump unless an authorized ability supplies force. If the sequence promises contact and landing, both must reach visible terminal states rather than being replaced by a suspended pose.

When the request explicitly says to avoid an unsupported or hovering attack, the design must close the strike/contact phase and a landing or recovered-support phase. If the exact target or landing surface was not supplied, retain `既定目标触点` and `既定落面` as typed unresolved slots, complete every other mechanic, and mark a design-only card `warn`; request the missing facts only before final-video `design_ready`. Do not invent an opponent, weapon, injury, damage or new surface, and do not omit either phase. This source-gap exception does not make slots the default for ordinary open-design contacts; use `combat-tension.md` to distinguish them.

### C. WorldState — location, height, support and anchors

Track the physical location rather than only screen left/right:

```text
named zone; depth relation; height; support surface; distance to anchor; persistent visible anchors; allowed route
```

Use architecture, terrain seams, roof ridge, tile slope, railing, pillar, doorway, floor marks or an established horizon as evidence. An orbit, close-up or foreground wipe may hide an anchor briefly, but its end must re-establish enough world evidence to prove no teleport occurred.

### D. WeaponPropState — owner, grip, orientation and condition

For every action-relevant weapon or prop, track:

```text
object; owner/controller; hand or contact method; grip; world orientation; screen direction;
contact partner/point/state; intact/damaged/dropped state; terminal world position
```

Touching, blocking, trapping or pushing a weapon is not ownership. A transfer requires a visible release by the old owner, a visible acquisition by the new owner, and a new stable grip. Without all three, ownership remains unchanged. When the user locks one owner, every shot must show that owner retaining the declared grip or provide a non-ambiguous occluded continuation; the opponent's hands remain open or use the declared non-gripping contact.

### E. FormVFXState — owner, source, stage, topology and residue

Track effects and transformations as an inheritable system:

```text
owner; source/attachment point; stage; coverage boundary; propagation frontier;
topology and connections; route/envelope; contact/result; visibility/occlusion; residue and exit state
```

A staged transformation begins from the exact previous coverage. New material grows from a named source or frontier; it cannot reset to an ordinary body, jump to full coverage, move to another owner or complete an unrequested creature form. Preserve negative topology locks such as “no head,” “no closed sleeve,” or “no complete dragon” through every later stage.

An effect remains connected to its declared source until it detaches visibly. Its trail or residue follows the established route. When it ends, show dissipation, separation, absorption, impact residue or another authorized exit; do not simply delete it between shots if its absence affects the next image.

### F. OpponentEnvironmentState — actionability and world residue

Track every opponent's world position, facing, posture, distance, current ability to act, recovery state and active threat route. For one-to-many action, fighters who are not in the current contact remain placed and do not silently vanish or join the same center attack.

Track only authorized environment changes: intact/damaged condition, contact receiver, debris direction, smoke/dust, displaced props, water/fire/energy residue and weather continuity. A later shot inherits broken surfaces, fallen objects and moving debris; it does not restore or add damage without a cause.

## 3. Transitions that require a visible bridge

The following changes are invalid when expressed only as a new shot's opening fact:

- takeoff, loss of support, landing or recovery of support;
- weapon release, transfer, drop, break, retrieval or changed grip;
- crossing to a new roof, doorway, room, height band or side of an obstacle;
- grapple lock/release or changed body contact;
- transformation onset, coverage growth, topology change or reversion;
- VFX detachment, impact, dissipation or owner change;
- environment break, prop displacement or weather-state change.

Show the bridge in the outgoing shot, incoming shot, or a dedicated connector whose sole purpose is the transition. A hard cut may omit elapsed travel only when the accepted structure authorizes a time/location jump and the new location is explicitly re-established.

## 4. Camera and state are separate

- **Screen change only:** an orbit or visible axis crossing changes viewpoint; world position, facing relation, contact and support stay fixed.
- **World change:** a dash, fall, leap, recoil or knockback changes physical position; background parallax, anchors, support or landing must prove it.
- **Occlusion:** a foreground object may temporarily hide a state but cannot silently rewrite it. Reappearance inherits the last known state plus only changes that had a visible cause.
- **Close-up:** cropping a weapon owner, support foot or opponent does not waive those states. If they control the next action, re-establish them before the action resolves.

## 5. Compact relay ledger

Use one row per shot boundary; expand only the families that change or control the next shot.

```text
【StateRelay｜shot N → shot N+1】
BodyState: <terminal -> next opening; evidence>
MotionState: <vector/speed/phase -> inherited phase; evidence>
WorldState: <location/height/support/anchors -> inherited world state>
WeaponPropState: <owner/grip/orientation/contact/condition/end position -> next opening>
FormVFXState: <owner/source/stage/coverage/connections/residue -> next opening>
OpponentEnvironmentState: <positions/actionability/damage/weather residue -> next opening>
Visible bridge or authorized discontinuity: <what changes and where it is shown>
```

For a design-only request that explicitly asks for continuity or ownership self-check, render the relevant rows with localized evidence. For a final video handoff, keep the full ledger internal and pass only the material next-shot subset to `aigc-video`.

## 6. Load and failure recovery

| Trigger | First response | If still unresolved |
|---|---|---|
| Too many changing state families in one shot | freeze nonessential changes and keep one attack-response relation | split at contact, release, landing, separation or initiative transfer |
| Weapon owner or grip drifts | restate owner, both hands/contact method, orientation and terminal position at each boundary | add checked pose/start-end references and reduce camera movement |
| Aerial action restarts or hovers | carry the exact support/flight phase and retain takeoff vector plus landing evidence | split at last support, apex/contact or landing and use the prior terminal frame |
| Location changes during orbit or close-up | restore named world anchors and distinguish screen from world position | reduce orbit/crop or insert a neutral spatial re-establishing shot |
| Transformation resets or completes the wrong creature | lock source, frontier, coverage and negative topology at each stage | use stage-state images and separate growth from aggressive camera motion |
| VFX vanishes or changes owner | show source connection, route and explicit exit/residue | split physical contact and effect resolution; add checked effect state references |
| Environment repairs or breaks without cause | inherit condition and residue from the last visible contact | remove unsupported damage or add the missing authorized contact bridge |

After three failures of the same protected state, stop adding synonyms. Change method through a simpler beat, lower camera load, checked motion/clay/stage-state/start-end references, or a causal split.

## Version binding and receiving contract

Bind each relay boundary to both endpoint shot ids and their current structure versions; record only material state families and their existing source/dependency owners. Reuse the CombatHandoff mapping in `../../aigc-video/references/video-contracts.md` and the existing closure in `../../aigc-video/references/change-impact-and-delivery.md`.

When an endpoint, support, grip, phase, effect residue or another tracked state changes, recheck its outgoing and incoming rows until the next stable unaffected boundary. Invalidate only affected cached states and audit findings, rebuild their dependent mechanics/direction, and rebind after the gate resolves. A later shot can retain its confirmed structure when the recheck proves its fields unchanged; record the newly checked boundary without rewriting that shot. Never carry an old two-hand grip into a newly one-hand opening merely because the weapon owner or camera is unchanged.
