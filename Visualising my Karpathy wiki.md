---
title: Visualising my Karpathy wiki
type: do
source: hosted
visibility: public
publish: false
hub_tags:
  - myhub
  - karpathy
  - llmwiki
  - data visualisation
  - knowledge visualisation
  - productivity
description: ""
slug: visualising-my-karpathy-wiki
coverImage:
version: 2
---
# Visualising my Karpathy wiki

**I'm [[Building a Karpathy LLMwiki inside my content pipeline]], so it was inevitable I'd see how Obsidian graph view could help me navigate the knowledge being knitted together by Loki in my personal library.**

*(Note: This is version 2 of this post, and uses Obsidian graph view to explore the evolution of my LLMwiki. To understand graph view,  [[Visualising my Karpathy wiki 1|version 1]] is a good place to start. Version control in the footer.)*

[[Visualising my Karpathy wiki - 1 - 2026-10-04|Version 1]] showed the first reading queue items I asked Loki to process, as well as Loki's level 2 files:

![[karpathywiki-graphview-4.png]]

## Batch 2: Exploring verification, trust & WSocial

In the weeks that followed I had Loki ingest a fair bit of content about verification on the Atmosphere in general and WSocial in particular as I wrote [Proof of human](https://mathewlowry.leaflet.pub/3mxgh342lsc2a) and then [How not to build trust](https://mathewlowry.leaflet.pub/3mxwiozz7ns27). The above view evolved as a result, with most of the additions centring around WSocial:
![[karpathywiki-graphview-5wsocial.png]]

The highlighted node is an **entity page** that synthesises everything I've bookmarked, read and written on them, highlighting the arguments and where the various sources agree and disagree. Loki wrote:

> "*How to read this page (Mathew's steer, 2026-10-13):* **verifiable facts** are listed as bullets: statements that a document, record, recording or date could confirm or refute. They are not verified here; each says only who reported it. **Arguments and opinions** are in prose, attributed. **Where the sources agree and disagree** has its own section near the end" - Wsocial entity page

These are early days for my LLMwiki, so I find Loki's writing style not to my liking. But the way it can bring everything together into a structured overview was incredibly useful for writing [How not to build trust](https://mathewlowry.leaflet.pub/3mxwiozz7ns27), which included over 20 links. But as I point out in [[Hub Manager]], I'm the one holding the pen. 

---

In late October I decided to backfill the rest of my reading queue, asking Loki to cluster my reading queue backlog using my project tags, and then do each cluster in a batch so it could consult me on the process (see [[Building a Karpathy LLMwiki inside my content pipeline#Dialog bonus| Building a Karpathy LLMwiki ...> Dialog bonus]]).

## Batch 3: atprotocol
This is what resulted after another 33 reading queue items clustered around atprotocol were ingested and I had given Loki some steering, identifying permissioned data as "super important" and asking for more focus on emerging ATprotocol products. Loki created new entity pages for Semble and Nostr and 11 new tags (not shown):

![[karpathywiki-graphview-6.png]]


## Batch 4: 31 productivity resources
Ingesting another 31 pages tagged productivity led to six new level 2 pages: Andrej Karpathy and his LLM-wiki pattern, Andy Matuschak, AI's effect on human cognition, agentic personal workflows, malleable software and Peter Kaminski's AI Starter Kit, which underpins the whole thing:

![[karpathywiki-graphview-7.png]]

## Batch 5: The last 80 resources

That left over 80 resources tagged #tagme - resources Loki had auto-assigned any project tags to. This is unsurprising - I have a small number of projects I want to focus on, but my reading areas of interest are much wider, which is why my post-backlog LLMwiki now has:

* AI as another centre of gravity
* a level 2 page summarising everything relevant to the myhub relaunch that this is a part of
* the intersection of social media, politics and ethics and democracy, particularly the Nazi Bar problem.


![[karpathywiki-graphview-8.png]]



## Final thoughts, looking ahead

How useful, at the end of the day, is graph view?  I've never used it until now, and chances are I'll simply ask Loki to guide me to the content I need rather than clicking and poking these graphs.

But that might change when I've figured out how to include the content I'm working on and imported the content I've already published. That should show me links between the content I've queued to read, Loki's level 2 syntheses of key concepts and questions, the content I've published (which is versioned, like this page), and what I'm currently working on. 

Check back for version 3, I guess... 

---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version  (2026-11-03): 
	- Batches 2-5
	- final thoughts, looking ahead
- version control
    - this is version: 2
    - this is the current version: [[Visualising my Karpathy wiki]]
    - here is the previous version: [[Visualising my Karpathy wiki 1]]