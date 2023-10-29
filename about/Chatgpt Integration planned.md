---
creation date: 2023-07-25 10:30
modification date: 206 July 2023 10:30:02
---
# ChatGPT integration
**What will the LLM integration into MyHub.ai look like in the future?**

## At a glance

This video sets out some wireframes: 

<< video>> 

However, behind the scenes there are some calculations being made, as explained in [[chatgpt experiment - method]]:

## Upon item creation
When User Hubs a Resource, including creating a note about the resource, the following test is made:

* if note>threshold.length then create an **AI Summary** of the note of length **threshold.length**

Notes on threshold length:

* higher threshold length: each item sent to chatgpt is on average larger, and is more likely to be an original note, not a summary. As a result:
	* more original notes and fewer summaries are used
	* sending larger Collections to ChatGPT risks breaching the token length limit.
* lower threshold length: more summaries are generated, so 
	* it's possible to send larger Collections to ChatGPT
	* but with fewer original notes: ChatGPT will be sent more summaries, and they'll be shorter.

Figuring out the right threshold length is therefore an important goal of this experimental programme.

## Accessing MyHub LLM Agents

Logged-in Hub Editors will have: 

* dropdown access to a set of MyHub Agents ("AIgents"?)
* a system for customising them, creating their own and sharing them as part of the MyHub user community.

Each of these Agents will be capable of taking the current Collection of Hubbed items (ie, the resources on the page at the time the Agent was called) and carrying out a specific task - for example:

- summarise them for a newsletter,
- synthesise them for decisionmakers,
- mind-map their key concepts,
- serve as my inspirational muse, etc.

## Using the LLM interface
### Submitting a Collection: basic process

When User applies an Agent to Collection C, containing C.i items:
* if sum(summaries)>8000 tokens then reject
* elseif sum(notes)<=8000 tokens then use notes as prompt context 
* elseif 7000<sum(summaries)<8000 then use summaries as prompt context 
* else create and send mix of notes and summaries (next)

### Create mix of notes and summaries

This process only happens when sum(notes)>8000 and sum(summaries)<7000.

The goal: create a **mix** for the prompt context by replacing some summaries with notes, keeping sum(mix) < 8000.

To begin with: sum(mix) = sum(summaries) - the prompt context is composed of summaries, totalling <7000 tokens. So:

* where note > threshold.length
	* where Highlight = YES
		* choose item with longest note
		* replace summary with note in mix
		* if sum(mix) > 8000 then exit and use mix as prompt context
		* else repeat with next longest note
	* if sum(mix) < 8000 then repeat for Highlight = NO
