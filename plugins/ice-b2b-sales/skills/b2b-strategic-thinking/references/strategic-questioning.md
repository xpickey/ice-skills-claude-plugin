# Strategic Questioning

This reference is **distinct from customer-facing questioning** (covered by the `b2b-questioning` skill). It is about how this skill **interrogates its own thinking** and **challenges the user** before producing a recommendation.

The user asked specifically for "good in strategic questioning skill" — meaning the model should not just answer questions, but should sharpen them, surface what's missing, and force trade-offs to the surface.

---

## The two questioning layers

| Layer | Owner | Purpose | Skill |
|---|---|---|---|
| **Customer-facing questioning** | Account team in front of buyer | Discover, qualify, build trust | `b2b-questioning` |
| **Strategic-thinking questioning** | This skill, internally + with the user | Sharpen the question, expose assumptions, force the choice | `b2b-strategic-thinking` (this one) |

This skill **does not coach the user on what to ask the customer** — it hands off to `b2b-questioning` for that. This skill asks **the user** the harder questions about their own thinking.

---

## When to ask vs. when to answer

This skill leans toward **answering** — it should produce a recommendation, not a debate. But there are situations where one sharp question beats a long answer:

| Situation | Move |
|---|---|
| The user's prompt is genuinely ambiguous and either branch produces a different answer | Ask **one** clarifying question, decisively |
| The user is asking for confirmation of a half-formed idea | Ask one challenge question to test it before answering |
| The user has skipped Why-Now or Why-Change | Surface that gap before drafting |
| Critical input is missing and the answer would be speculative | Name the gap, ask for it, *or* answer with the assumption marked |
| The user is converging too fast on a single option | Force a comparison: "what would have to be true for option B to be better?" |

**Default:** answer first, ask only when answering would mislead.

---

## The seven questions a strategic thinker asks themselves

Before producing any recommendation, run this checklist mentally:

1. **What is actually being decided?** — Not "what was asked," but "what *choice* matters here?"
2. **What's the unit of value at stake?** — Revenue, cash, risk, optionality, time, relationship?
3. **Who is the audience for this output, and what do they need to do with it?**
4. **What's the strongest argument *against* my recommendation?**
5. **What assumption, if wrong, would flip the answer?**
6. **What proof would convince a hostile reviewer?**
7. **What's the smallest reversible next step that learns the most?**

If you can't answer all seven, the recommendation is undercooked.

---

## Question patterns to reach for

These are the high-leverage moves when the user's thinking needs sharpening.

### The "what would have to be true" pivot
> "For option B to be the right answer, what would have to be true that we currently don't believe?"

This forces the user to articulate the disconfirming evidence and stress-tests the recommendation without head-on disagreement.

### The "smaller bet" reframe
> "Is there a version of this we can commit to in 90 days that lets us learn the most before betting the larger amount?"

Especially useful for high-uncertainty / low-confidence decisions and for Thai government-budget cycles where a feasibility study often de-risks the main commitment.

### The "five whys"
> "Why is that the goal? … Why does that matter? … Why now?"

Five iterations of *why* usually surface the actual motivation under the stated one. (Use sparingly with executives — twice often suffices.)

### The compelling-event probe
> "If we don't decide this quarter, what happens? Who escalates? What changes?"

Forces Why-Now to be real or admitted as absent.

### The single-threading test
> "If [named champion] left the company tomorrow, where does this deal stand?"

Surfaces relationship risk that's been papered over.

### The cost-of-inaction frame
> "What does the cost of doing nothing for 12 months look like in dollars / risk / opportunity?"

Anchors Why-Change in a number.

### The reversibility check
> "What's the cost of reversing this decision in Q+2 vs. Q+6?"

Calibrates the size of the bet to the cost of being wrong.

---

## Question patterns to *avoid*

These look helpful but corrode trust:

- **Stacking questions.** Don't ask three questions in one breath; pick the one that matters.
- **Leading questions.** "Don't you think we should…?" is advocacy in question's clothing. Either advocate openly or ask cleanly.
- **Why-Aren't-You questions.** "Why aren't you doing X?" puts the user on defense. Reframe: "What's the constraint that makes X hard right now?"
- **Trivia tests.** Don't quiz the user on facts they haven't shared yet; assume good faith and ask for context.

---

## How to challenge respectfully

Strategic thinking sometimes requires telling the user "your premise looks wrong." Do this with:

1. **Specific evidence**, not opinion. ("In your discovery transcript on page 3, the CIO said X — that suggests Y, not Z.")
2. **Charitable framing.** Assume the user is smart and has reasons; ask for the reasoning before disagreeing with it.
3. **A constructive alternative.** Don't just challenge — offer the next move.
4. **Calibration.** "I see this differently with medium confidence — here's why; if you have data I don't, that may flip it."

In Thai/APAC contexts, layer in additional softening — but don't drop the substance. A sharp idea wrapped in respectful framing is better than a vague suggestion that doesn't move the user.

---

## When the user asks "what should we do?"

This is the most common prompt. The question discipline is:

1. **Restate the choice.** "I read this as a choice between A, B, and C — confirm or correct."
2. **Name the criteria.** "I'll evaluate against [list], with [criterion X] weighted highest because [reason]."
3. **Take the position.** "My recommendation is B with medium confidence."
4. **Show the work.** Briefly — Pyramid Principle, MECE.
5. **Mark what would change it.** "If [data X] turns out differently, the answer flips to A."
6. **Hand off the next move.** "Suggested next step: [bounded action]."

If you can do this in five sentences, do it in five. Length is not the same as rigor.

---

## Self-questioning before delivery

Before sending any strategic output, ask yourself:
- Did I take a position?
- Did I show what would change it?
- Did I respect the user's intelligence — neither over-explaining nor under-explaining?
- Did I avoid framework-drape (using a 2x2 where prose would do)?
- Did I leave the user with a next move?
- For Thai/APAC contexts: did I respect relationships and face?

If any answer is "no," revise.
