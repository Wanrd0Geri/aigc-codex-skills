# Diagnosis Rubric

Use this reference to decide whether a single AIGC shot frame should move forward, be repaired, or be redesigned.

## Greenlight

The frame can move into image editing or Seedance video generation when:

- The shot has a clear story function and emotional read.
- The subject is immediately readable, with a clear first point of attention.
- The composition, camera angle, and depth support the intended shot.
- Light direction, contrast, and color mood are coherent enough to preserve.
- Character identity, costume, props, and environment feel consistent.
- AIGC artifacts are minor and can be fixed through targeted image editing.
- The frame implies a plausible next action, camera movement, or continuation.

Recommended handoff:

- Use `aigc-image-edit-prompt` when only targeted repair is needed.
- Use `aigc-seedance-prompt` when the frame is stable enough for image-to-video.

## Yellowlight

The frame can continue, but only after fixing 1-3 high-impact problems:

- The idea is readable, but the camera or composition weakens the subject.
- Lighting or color is close, but the frame lacks depth, atmosphere, or hierarchy.
- Production design is mostly usable, but details feel random, cheap, or inconsistent.
- Identity, anatomy, hands, eyes, props, or materials show visible AIGC instability.
- The frame can become video, but the action path, camera behavior, or start/end state is under-defined.

Recommended handoff:

- Use this skill to name the blockers and preserve list.
- Then use `aigc-image-edit-prompt` for a repair prompt before entering Seedance.

## Redlight

Do not move into video generation yet when:

- The shot purpose is unclear or emotionally empty.
- The subject cannot be read quickly.
- Blocking, pose, silhouette, or crop makes the frame unusable as a shot.
- Lighting, color, and production design fight each other rather than form one world.
- The frame has major identity drift, malformed anatomy, broken props, or style averaging.
- There is no clear action, motion direction, camera intent, or continuation path.

Recommended handoff:

- Use `aigc-creative-director` when the concept or emotional purpose is weak.
- Use `aigc-visual-diagnose` when the frame needs deeper artistic diagnosis before repair.

## Check Dimensions

- **Story purpose**: What must the viewer understand from this shot?
- **Subject readability**: Where does the eye go first, and is that correct?
- **Composition**: Does the shot size, angle, crop, and depth serve the subject?
- **Lighting**: Is there a motivated source, clear contrast, and useful atmosphere?
- **Color**: Does color guide attention instead of flattening the frame?
- **Production design**: Do costume, props, setting, and materials belong to the same world?
- **AIGC trace**: Are there artifacts, style averaging, over-smoothing, or prompt-control failures?
- **Action potential**: Does the frame imply what happens next?
- **Seedance controllability**: Can the shot be described with stable subject, motion, camera, start state, and end state?

## Routing Rules

- Route weak concepts to `aigc-creative-director`.
- Route broad visual diagnosis to `aigc-visual-diagnose`.
- Route targeted repair prompts to `aigc-image-edit-prompt`.
- Route video prompt writing to `aigc-seedance-prompt`.
- If the user only asks for a production decision, stay in this skill and provide the next-step checklist.
