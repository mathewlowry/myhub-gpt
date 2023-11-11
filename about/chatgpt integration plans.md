---
creation date: 2023-07-25 10:30
modification date: 206 July 2023 10:30:02
---
# ChatGPT integrations planned

**What will the LLM integration into MyHub.ai look like in the future?**

## Introduction

For the first 5 experiments I used the two ways of accessing ChatGPT open to me at the time: directly via the ChatGPT website, and using the pilot version of the MyHub.ai "GPT wrapper" set out in [[pilot integration]]. As I was working on the analysis of [[experiment 5]], however, OpenAI released the "*Create your own GPT*" feature, so I created my first GPT and quickly ran [[experiment 6]].

Which means I now have at least two ways forward to investigate and compare:

* the [[chatgpt integration plans#API-based AIgent approach|API-based AIgent approach]] I always had planned, as set out in detail below
*  [[chatgpt integration plans#Integrating MyHub.ai with GPTs|integrating MyHub.ai with GPT]] instead: this is only outlined below, because while people can do this today there's not currently nearly enough information to judge whether this is the right way forward.

Life being what it is, I'm reasonably certain that I'll have to combine both to allow Editors to explore and innovate, because if MyHub.ai *only* offered GPT integration, Hub Editors (and their subscribers?) would be restricted to the tasks those GPTs are capable of doing.

Either way, the picture  emerging looks something like this (image adapted from [Social knowledge graphs for collective intelligence](https://mathewlowry.medium.com/social-knowledge-graphs-for-collective-intelligence-75c436889320)):

![[myhub-gpt-aigents.png]]
---
## API-based AIgent approach

Before *Create your own GPT* came along, my original idea was to build on the basic approach set out in [[pilot integration]]: allow Hub Editors to create "AIgents" that talk to ChatGPT via its API, as briefly explained from around ~1m40 of [this video](https://www.youtube.com/watch?v=PykfgbRwZiY):

[![[aidropdown.jpg]]](https://www.youtube.com/watch?v=PykfgbRwZiY)

Logged-in Hub Editors will have: 

* dropdown access to a set of MyHub Agents ("AIgents"?). Each of these Agents will be capable of taking the current Collection of Hubbed items (ie, the resources on the page at the time the Agent was called) and carrying out a specific task (summarising resources for a newsletter, synthesising them for decisionmakers, mind-mapping their key concepts, serving as an  inspirational muse, etc.)
* a system for customising them and creating their own 
* a library for storing and retrieving their conversations 
* (later) many other things, such as:
	* sharing Agents across the MyHub Editor community
	* publishing conversations and/or content based on conversations, labelled with the "AI content" 
	* (more ideas jotted down in [[Ideas log]]).

Behind the scenes, obviously, there are some calculations being made to ensure the token limit is not exceeded - see [[AIgents behind the scenes]].

--- 
## Integrating MyHub.ai with GPTs

As I write this (2023-11-11), details of OpenAI's GPT Store are still fuzzy, particularly wrt their claim that creators of popular GPTs will get [a share of the revenue](https://www.theverge.com/2023/11/6/23949371/more-on-how-openai-is-going-to-pay-gpt-creators). So this is just conjecture for now.

But clearly it opens interesting possibilities, all based on the mechanic set out in  [[chatgpt integration plans#API-based AIgent approach|API-based AIgent approach]]. Instead of creating AIgents on MyHub which talk to ChatGPT, Hub Editors create **"GPT Agents"** which send the user's selection of Hubbed resources to the GPT, hosted on OpenAI.

### "Pay as you Chat" with my Hub

Caveat: critical to this idea is that it is the *user* who pays for the use of the GPT, via their OpenAI subscription. This is still unclear (as is whether GPTs have APIs at all), but if this is the case GPT usage will be zero cost to the Editor.

And that means:

* there is absolutely no reason to limit this to Editors: **any visitor to any Hub should be able to use GPTs to chat about any collection of the Hub's content** 
* it's also zero profit for the Editor: if anyone else makes any money out of it, it's the GPT's creator.

An Editor *could* monetise their Hub by prioritising *their* GPTs on their Hub's interface to all users, but I for one will prioritise making my Hub as useful to my visitors as possible by putting the best GPTs front and centre, not just the ones I have a small profit share in.

Best case scenario: the GPT Store supports **a marketplace of MyHub-compatible GPTs** which any Hub Editor could add to their Hub, for themselves and their visitors. 

### "Subscribe to chat with my Hub"

A second alternative is that the Editor bears the cost of GPT usage, but limits usage to Hub Subscribers, who pay to access the GPTs and other "premium services". 

After all, a Hub would then provide much more than any blog or Substack, offering Hub subscribers: 

* the Editor's blog *and* newsletter *and* the resources the author has read and recommends *and* his/her notes about them, 
* all easily searchable and filterable
* PLUS an array of chatbots, each writing like the Hub Editor and focused on helping each subscriber get the most out of the Hub's resources.

The Editor, moreover, has all of the above *plus* a set of reading, thinking and writing tools arrayed in a content creation pipeline, with each stage supported by dedicated GPTs, as I explained

The downside of the subscriber model is that the subscribers' fees (which are generally flat) will need to cover the subscribers' GPT usage, which may vary from zero to infinite from one month to the next. And the costs of sending content to a GPT is several times higher than simply sending it to ChatGPT. A system to manage that risk will therefore need to be developed, but this is the same for every GPT wrapper out there.

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- 2023-11-11: updated to account for [[experiment 6]], the release of GPTs, etc, ad shortened with the extraction of [[AIgents behind the scenes]] into a separate file.
- version control
    - this is version: current
    - here is the previous version: [[chatgpt integration plans 1]]
