---
creation date: 2023-07-25 10:30
modification date: 206 July 2023 10:30:02
---
# ChatGPT integration
**What will the LLM integration into MyHub.ai look like in the future?**

## First AI features at a glance

Right now I'm experimenting with integrating ChatGPT into each Hub as set out in [[Pilot integration]]. Assuming these experiments show promise, the first features to be developed are briefly explained from around ~1m40 of [this video](https://www.youtube.com/watch?v=PykfgbRwZiY):

[![[aidropdown.jpg]]](https://www.youtube.com/watch?v=PykfgbRwZiY)

Logged-in Hub Editors will have: 

* dropdown access to a set of MyHub Agents ("AIgents"?). Each of these Agents will be capable of taking the current Collection of Hubbed items (ie, the resources on the page at the time the Agent was called) and carrying out a specific task (summarising resources for a newsletter, synthesising them for decisionmakers, mind-mapping their key concepts, serving as an  inspirational muse, etc.)
* a system for customising them and creating their own 
* a library for storing and retrieving their conversations 
* (later) many other things, such as:
	* sharing Agents across the MyHub Editor community
	* publishing conversations and/or content based on conversations, labelled with the "AI content" 
	* (more ideas jotted down in [[Ideas log]]).

## Behind the scenes: respecting token limits

Behind the scenes, obviously, there are some calculations being made to ensure the token limit is not exceeded, as explained in [[chatgpt experiment - method]].

### Upon item creation
When User Hubs a Resource, including creating a note about the resource, the following test is made: 

* if note>threshold.length then create an **AI Summary** of the note of length **threshold.length**

Notes on threshold length:

* higher threshold length: each item sent to chatgpt is on average larger, and is more likely to be an original note, not a summary. As a result:
	* more original notes and fewer summaries are used
	* sending larger Collections to ChatGPT risks breaching the token length limit.
* lower threshold length: more summaries are generated, so 
	* it's possible to send larger Collections to ChatGPT
	* but with fewer original notes: ChatGPT will be sent more summaries, and they'll be shorter.

Figuring out the right threshold length is therefore a goal of this experimental programme.

### Applying an Agent to a Collection

When User applies an Agent to Collection C, containing C.i items:

* if sum(summaries)>8000 tokens then reject
* elseif sum(notes)<=8000 tokens then use notes as prompt context 
* elseif 7000<sum(summaries)<8000 then use summaries as prompt context 
* else create and send mix of notes and summaries (next)

### Creating a mix of notes and summaries

This process only happens when sum(notes)>8000 and sum(summaries)<7000.

The goal: create a **mix** for the prompt context by replacing some summaries with notes, keeping sum(mix) < 8000.

To begin with: sum(mix) = sum(summaries) - the prompt context is composed of summaries, totalling <7000 tokens. So **where note > threshold.length:**

* where Highlight = YES
	* choose item with longest note
	* replace summary with note in mix
	* if sum(mix) > 8000 then exit and use mix as prompt context
	* else repeat with next longest note
* if sum(mix) < 8000 then repeat for Highlight = NO
