---
creation date: 2023-07-25 10:30
modification date: 206 July 2023 10:30:02
---
# ChatGPT integration
**What will the LLM integration into MyHub.ai look like?**

## Upon item creation
When User Hubs a Resource, including creating a note about the resource:
* if note>threshold.length then create an **AI Summary** of the item of length **threshold.length**

Notes on threshold length: 
* higher threshold length - each item sent to chatgpt is on average larger and more likely to be an original note, not a summary, so:
	* more original notes and fewer summaries are used
	* larger collections impossible 
* lower threshold length - more summaries are generated, so larger collections are possible, but with fewer original notes: chatgpt will be sent more summaries

## Accessing MyHub LLM Agents
Logged-in Hub Editors will have: 
* dropdown access to a set of MyHub Agents
* a system for customising them, creating their own and sharing them as part of the MyHub user community.

Each of these Agents will be capable of taking the current Collection of Hubbed items (ie, the resources on the page at the time the Agent was called and carrying out a specific task - for example:
- summarise them for a newsletter,
- synthesise them for decisionmakers,
- mind-map their key concepts,
- serve as my inspirational muse, etc.

## Using the LLM interface
### Submitting a collection
When User applies an Agent to Collection C, containing C.i items:**
* if sum(summaries)>8000 tokens then reject
* elseif sum(notes)<=8000 tokens then use notes as prompt context 
* elseif 7000<sum(summaries)<8000 then use summaries as prompt context 
* else** create and send mix of notes and summaries** (next)

### Create mix of notes and summaries
* givens:
	* sum(notes)>8000
	* sum(summaries)<7000
* goal: create a mix for the prompt context by replacing some summaries with notes, keeping sum(mix) < 8000:
	* to begin with: sum(mix) = sum(summaries) - the prompt context is composed of summaries, totalling <7000 tokens
	* where note > threshold.length
		* where Highlight = YES
			* choose item with longest note
			* replace summary with note in mix
			* if sum(mix) > 8000 then exit and use mix as prompt context
			* else repeat with next longest note
		* if sum(mix) < 8000 then repeat for Highlight = NO
