# Introducing the MyHub/GPT integration experimental programme

**A guide to the experimental programme underway to design MyHub/GPT integration.**

Integrating MyHub.ai with AI has been [the idea from the outset](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4) (the hint's in the ".ai"), with the longterm goal being "creating a decentralised, open-source ecosystem ... developing cooperatively-owned AI engines to benefit society as a whole" ([How Artificial Intelligence will finance Collective Intelligence](https://mathewlowry.medium.com/how-artificial-intelligence-will-finance-collective-intelligence-5d17adcce98b)).

The best way for me to discover the most valuable way(s) of integrating a Hub with an AI today, however, is to use ChatGPT. Earlier this summer, therefore, I added a pilot version of ChatGPT integration to MyHub.ai to support the research.

I am sharing the results of this research in the hope others can contribute their thoughts and ideas. This post provides the context for the experiments and a guide to the experiment nomenclature - see also:
* [[ChatGP experiment home]]
* [[chatgpt experiment - method]]
* [[chatgpt integration system]]
* my [[ToDos]]

## Pilot integration
Firstly a quick note on the pilot integration. 

When I'm logged in I see the following form at https://myhub.ai/@mathewlowry/chat.
![[myhub-chatgpt-pilot-form.png]]

Using this form I can:
- paste into Context URLs the URL of a MyHub Collection - eg [All the Stuff I Like about Everything tagged #creativity & #innovation, Anytime](https://myhub.ai/@mathewlowry/?tags=creativity&types=like&timeframe=anytime&quality=all&tags=innovation). This defines the notes I want to chat with ChatGPT about
- optionally, include a search term in Search within context query to narrow down the content further
- Write a prompt to start the conversation with ChatGPT, including the content wherever I want to discuss by clicking the "insert content placeholder" button.

## Goal: MyHub Agents
The above form, however, is not what I intend releasing to the world: when my experiments are finished, logged-in Hub Editors will have dropdown access to a set of MyHub Agents, as well as a system for customising them, creating their own and sharing them as part of the MyHub user community.

Each of these Agents will be capable of taking any Collection of Hubbed items and carrying out a specific task - for example:

- summarise them for a newsletter,
- synthesise them for decisionmakers,
- mind-map their key concepts,
- serve as my inspirational muse, etc.

## Experimental programme variables
Each experiment involves a number of different variables:

- the **Agent Prompt**, corresponding to the task the Agent is designed to perform for the User
- the **Collection** of Hubbed items created by the User, to which the Agent Prompt is applied 
- the **Summariser** used (explained below)
- the **maximum length** applied using that Summariser (explained below).

![[experiment-method1.png]]
*This diagram is also explained left to right in [[chatgpt experiment - method]].*

My first experiment, for example, is called C-1-S-1-150-P-1: testing Prompt 1 on Collection 1 using Summariser 1 to a max length of 150 words. Let's take each in turn:

### The right Prompt for each Agent
**When I started investigating this I thought that designing each Agent would just be a question of finding the right Prompt.**

For example, **Prompt 1** is written to take a Collection of Hubbed notes and:

> "write a 500 word editorial summarising the main themes ... in particular highlighting themes common to several articles. Follow the editorial with the articles listed in the following format: 
> ## article title 
> An 80 word summary of the article. 
> 
> Provide all content in markdown format, with each article title linked to the URL provided with it." - [[Prompt 1 - newsletter A]]

But if it was that simple, I would have done many experiments by now.

### The right Summariser
**There's a complicating factor: the ChatGPT token limit.**

I'm using the ChatGPT3.5 API, which gives me a 16k context - ie, the content I throw at ChatGPT, and the content it throws back, should not be more than 16000 tokens, or ~12000 words. The moment I break that limit, ChatGPT will start "forgetting" earlier parts of the conversation.

After analysing the most active Hubs, I calculated that if MyHub Agents sent the full notes of each Hubbed item, it would break the token limit for any Collection over 15-20 items.

So we need a Summariser: once an Editor has Hubbed an item, MyHub checks its length. If it is over a certain length ("Summary Threshold"), MyHub will ask ChatGPT to create a Summary of the note, of length Summary Threshold.

Moreover, we also need Collection Composer: when an Editor activates an Agent, this algorithm checks the total length of all the notes in the Collection:

- if it's under (say) 8000 tokens, then ChatGPT is sent the full notes.
- on the other hand, if all the notes' Summaries total 8000 tokens, the Collection is rejected as too large from the outset
- something interesting happens in the middle ground: where the notes total over 8000 tokens, Collection Composer substitutes some notes with their Summaries, starting with notes which are not Highlighted and which are only slightly over the Summary Threshold.

In this way ChatGPT gets the Editor's notes of the Collection where possible, and their Summaries if the Collection's notes are either too numerous, too long, or both.

## Questions to answer
So we now have several questions requiring experiments to answer:

- What is the best Agent Prompt for each task?
- What is the best Summariser Prompt for capturing the essence of each note?
- How long should Summary Threshold be?

Moreover, is the best combination of Summariser Prompt, Summary Threshold and Agent Promot good for *all* Collections, or just the one I used in my first round of tests?

## Experimental nomenclature
Hence the name of my first experiment (C-1-S-1-150-P-1): testing Prompt 1 on Collection 1 using Summariser 1 to a max length of 150 words.

For the experiments to be meaningful, I need to compare several approaches in each experiment, which requires the creation of several files:

- Basic inputs
	- Collection 1: this is a URL, as set out above.
	- [[Prompt 1 - newsletter A]]
- **Summariser 0** is the original Summariser, written off the cuff for the ChatGPT pilot without much thought. It creates very short summaries and so serves as our "baseline Summariser" (see postscript).
	- [[C-1-S-0]] is the content ChatGPT received, created using Summariser 0 (ie short summaries of the Collection 1 notes)
	- hence [[C-1-S-0-response-P-1]]: what ChatGPT returns when sent C-1-S-0.md and asked Prompt 1
- **Summariser 1** (see [[Summarisers#^29496d]])
	- [[C-1-S-1-150]]: the content ChatGPT received, created using Summariser 1 set to 150 words
	- [[C-1-S-1-150-response-P-1]]: what ChatGPT returns when sent C-1-S-1-150 and asked Prompt 1
- **AllNotes**: to test if and how Summarisers affect the quality of ChatGPT's response, we need to apply the Prompt to the entirety of the notes, as well:
	- [[C-1-AllNotes]] contains the entirety of the notes in Collection 1, created by taking the [Collection's RSS feed](https://myhub.ai/rss/@mathewlowry/?tags=creativity&types=like&timeframe=anytime&quality=all&tags=innovation) and applying [[RSS AllNotes Prompt]]
	- [[C-1-AllNotes-response-P-1]]: what ChatGPT returns when sent C-1-AllNotes.md and asked Prompt 1
- finally, the analysis: [[Experiment 1 Analysis]], itself written with the help of ChatGPT ([[Experiment 1 Analysis chatgpt execsumm]]).

  