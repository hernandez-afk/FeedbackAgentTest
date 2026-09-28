# Page brief: Modified Game Sort on Game Feedback Engine

<!-- Transcribed verbatim from "Atari Usability UX/UI Context Sheet — Game Sort on
     Game Feedback Engine" (PDF, 3 pages). Author's wording is unchanged; the
     agent's changes live in brief-optimization-report.yaml, never here. -->

There is already a kind of a design system in place with a story book of components available. Although, I am already aware there will be new components that need to be added.

## Purpose

We want to make the game sorting of the feedback engine more intuitive. As of now, there is no way to sort though games other than on the home list page. It would be useful to sort by people such as Game developer, platform type, by studio, or by project. By each title there will also be a more specific product (that in console specific) with the granular being a product version (e.g. title: asteroids, product asteroids arezion, product version: msn)

## Users and context

- **Who:** Anyone typing to find the game in the game engine feedback tool should be able to find use this. They should be able to easily find specific games of the platform that is being looked for.
- **Device:** Any, users should be able to navigate through the games but, should probably be collapsing left side window for mobile devices

## Where it fits

This would fit on the "games" and "sessions" pages as a main way to sort. Also for each individual session it would also be useful.

## Goals (ranked)

1. Users should be able to sort through long lists of content
2. Should be easily scaleable
3. Easy to use for anybody

## What users need to do

- Select a filter on the homepage — starts from: [sessions or game page]
- Needs to find a game of a specific platform and type — starts from: [need to find a game from msn -> goes to sort by platform -> can then find MSN]

## Content and data

- All sub groups can be read and sorted through
- The header contains the game title, platform, date uploaded, build type, edit, import documents, view dashboard

## States

- **Loading:** [what's slow, if anything]
- **Empty:** [what a new user with no data sees]
- **Error:** [what can fail, and what the user can do about it]
- **Success:** [how the user knows it worked]

## Constraints

- The framework should be as close as possible to the current design system

## Acceptance criteria

- When sorting the games and sessions become easily to filter and locate what is existing
- Card format and list format of games
- Sessions can be suggested to be sorted based on what recently got the most responses

## Out of scope

- It does not use any AI to locate features

## Related pages and designs

- From Andreas Beijer

## Open questions

- [Anything you don't know yet. Better listed here than guessed.]
