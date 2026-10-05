---
title: Building a Karpathy LLMwiki inside my content pipeline
type: do
source: hosted
visibility: public
publish: false
hub_tags:
  - productivity
description: Early days (v1)
slug: building-a-karpathy-llmwiki-inside-my-content-pipeline
coverImage: hub/site/karpathywiki-v1-graphview.png
version: 1
---

# Building a Karpathy LLMwiki inside my content pipeline

**Loki has found a home, somewhere between my Reading Queue and the rest of my content pipeline.**

As set out in [[MyHub on the ATmosphere]], I started developing the "local-first" version of my content pipeline with version 1 of [[ReadingQ Manager]], an Obsidian plugin which gets a link to content I find useful into my library, and adds a task to read it onto all a central reading queues and all relevant task lists. Back then, the plan was to then build [[Hub Manager]] to support the middle of the content pipeline: from reading and annotating reading queue content through to writing content ready for publication on my Personal Data Server. 

But somewhere in that process I came across the Karpathy LLM wiki model, so I upgraded ReadingQ Manager so that my library becomes a folder of content which Loki, my persistent personal agent, can help me work with directly.

*(Note: This is version 1 of this post. Version control in the footer.)*
## Clipping for Karpathy

Hub Manager was already well underway when I read  [LLM Wiki by Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). I'll be brief, as there's no shortage of articles summarising Karpathy's idea:

* most people using LLMs upload documents into a session, get an answer, and then do it all again next time. One session can't learn from previous ones, so **knowledge doesn't accumulate**. 
* Karpathy suggested grabbing and storing *everything* and getting your LLM to create and maintain **a wiki** from it, along with files telling it how the wiki's organised, and how to keep it that way. Your LLM agent then uses that wiki as a knowledgebase to answer your questions without you having to feed it everything each time. 
* As a result, your LLM compounds, building in value as you use it, exactly like Loki, my persistent agent.

I thought I'd kick those tyres, and upgraded ReadingQ Manager. RQM-v2 now turns my reading queue into the raw material required for this model: rather than just creating tasks pointing to URLs I'd identified as worth reading, it clips the actual *content* into a file new ReadingQueue folder. 

The tasks link remain, but link to both the file and the original URL, as when I actually want to *read* that content I'll go to the source online: the local copy is for Loki, and never enters the publication workflow.

## The LLM Wiki forming in my library

![[Pasted image 20261004202140.png]]

*Ask Loki to "ingest" and the content clipped by [[ReadingQ Manager]] is read, analysed and integrated into a set of "Level 2" syntheses which support Loki's answers to any questions I have relevant to my reading, notemaking and writing (image adapted from [[MyHub on the ATmosphere]])*.

In Karpathy's model, the content in my ReadingQueue folder is "Level 1" content. When I asked Loki to "ingest" a first batch of ReadingQueue content using Karpathy's guidance as a template, it created a first set of "Level 2 content":

* **Entities**: each covers a person, organisation, product or some other "thing" (eg the "standard site" lexicon)
* **Concepts**: ideas that keep coming up (eg "credible exit")
* **Questions**: stuff I'm investigating, particularly issues I'm writing about (eg "how does the Atmosphere pay for itself?")
* **Analyses**: as Loki processes new content into the wiki we have a conversation, which usually results in me asking for one of these documents for future reference
* Management files: Loki keeps three files up to date:
	* an **index** lists and briefly introduces all the questions, analyses, etc by type 
	* a **log** of everything that's happened, as it happens - this is never edited, only appended to
	* **overview**: what the wiki as a whole currently says.

In Karpathy's model, these level 2 pages synthesise content from and link back to all relevant Level 1 source material. Together, Loki can answer questions using this content as a knowledgebase, citing links to content I've already identified as both relevant and interesting.

 > whenever I turn to a draft I can easily see which Level 2 files have something to contribute to it
 
**However, my vault is *also* where I *write***, so each Level 2 file's "Sources" section also highlights relevant content I've written and am writing. And because Obsidian displays backlinks, whenever I turn to a draft I'm working on I can easily see which Level 2 files have something to contribute to it. 

I asked Loki to map this in Obsidian, and then in Mermaid so you can [at least zoom in](https://mermaid.ai/d/e078e5fa-8e50-4fdf-842f-d8fd554277d9):

![[content-map-canvas.png]]

I'm fully aware this is hard to process in detail - I'll probably create something easier to read later this year, once I've processed the rest of the Reading Queue backlog I've been adding to my library since developing ReadingQ Manager over the summer. 

## Dialog bonus

One thing the above diagram does not capture at all, however, is the dialog I have with Loki when it processes a batch of Reading Queue items. After it takes a first look at the content, it suggests how it's relevant and asks for guidance. I then respond, and the resulting to-and-fro does two things:

* ensures the most interesting insights are committed to Loki's Level 2 content 
* establishes some hooks in my own memory, so when I come to read those reading queue items I already have some idea of how they're relevant to what I've read and written before, and what I'm writing now. 

I'm still learning how to get the most out of this, but I tell Loki to commit what I learn to memory, so it becomes second nature to it, and hence to me.

## What's next

Inevitably, of course, I've also started [[Visualising my Karpathy wiki]]:

![[4 Karpathy graphs.png]]
*The first 4 Obsidian Graph Views of my Karpathy LLM wiki*

Once I've imported my backlog of reading queue items and refine this Graph View further I'll add the content I have written and am writing, in another vault folder, to the LLM wiki. There won't be a lot to start with, as I have only been using this vault to draft content for a few weeks. 

> *when I import the 350+ pieces [I Do or Think](https://myhub.ai/@mathewlowry/?quality=all&types=do&types=think&timeframe=anytime) from my Hub, and then have Loki process them ... the fun will really begin*

But when I import the 350+ pieces [I Do or Think](https://myhub.ai/@mathewlowry/?quality=all&types=do&types=think&timeframe=anytime) from my Hub, and then have Loki process them all into my wiki, my Graph View will show me links between:

* the content on my reading queue I haven't yet read, 
* notes on reading queue content I've already made, 
* and everything I have already published or am still drafting. 

And that's when the fun will really begin.

---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version (2026-10-04): n/a
- version control
    - this is version: 1
    - this is the current version: [[Building a Karpathy LLMwiki inside my content pipeline]]
    - here is the previous version: n/a