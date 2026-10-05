---
title: "Visualising my Karpathy wiki"
type: do
source: hosted
visibility: public
publish: false
hub_tags: ["myhub", "karpathy", "llmwiki", "data visualisation", "knowledge visualisation", "productivity"]
description: ""
slug: visualising-my-karpathy-wiki
coverImage: 
version: 1
---
# Visualising my Karpathy wiki

**I'm [[Building a Karpathy LLMwiki inside my content pipeline]], so it was inevitable I'd see how Obsidian graph view could help me navigate the knowledge being knitted together by Loki in my personal library.**

*(Note: This is version 1 of this post, published after only a small fraction of content has been processed into my LLM wiki. Version control in the footer.)*

## First pass

My first try at an Obsidian graph looked great, until I realised it was only graphing Loki's Level 2 analyses and related management files, and not the actual Reading Queue content:

![[karpathywiki-graphview-1.png]]

So I enlarged the view to everything in the reading queue (orange), and put the management files in a subfolder, which made it easy to ignore them. The graph view filter, in case you need it: 

> (path:wiki OR path:"reading queue") -path:"wiki/management") )

![[karpathywiki-graphview-2a.png]]

This ... isn't great. Immediate problems:

* this picks up everything in the reading queue Loki hasn't processed yet, swamping the signal
* too many tags! (green)
* it also picks up project files, in another part of the vault, with "wiki" in their path

Let's remove the tags and focus the filter: 

> (path:/^wiki\// OR path:"reading queue") -path:"wiki/management"

![[karpathywiki-graphview-3.png.png]]

Still not great, as it shows: 

* **the core LLM wiki**: Loki's "level 2 files" summarizing and linking to the reading queue items it has processed
* **a halo of unlinked nodes**, which Obsidian calls Orphans.
### Exploring the core

Fortunately, Obsidian provides an "Ignore Orphans" toggle, so with a click I can focus on the reading queue items Loki *has* processed, and Loki's level 2 files:

![[karpathywiki-graphview-4.png.png]]

That's starting to look like something I can use, but this is based on a first batch of reading queue content, so I'll return to this when I have 50 resources processed by Loki, and then 100...
### Processing the halo

But that  halo of unlinked nodes bothers me, as it is actually composed of two sorts of very different content:

* Queued resources Loki hasn't processed yet
* some (but not all) of the "thin notes" - files with little content in them, generally tagged "social" and/or "stub" 

Not knowing which is which is a bit of a problem.
#### Unprocessed queued notes 

The halo is probably full of unprocessed reading queue items, as we've currently only processed the first batch of my backlog. When I've processed the rest of the backlog, these much fewer unlinked nodes will hopefully give me a visual sense of the ongoing content to be processed by Loki into my Karpathy wiki.

Note that these files *are* linked to from files across my vault (Reading Queue, Project Maps of Content and Daily Notes). Those notes, however, are all outside this graph's particular domain, so as far as this graph is concerned they're Orphans, which makes hiding them easy.
#### Thin notes

The problem is that the halo also contains "thin" reading queue items. These notes are all tagged "stub" because there's little content in them, generally because the queued resource is hiding most of its content behind a paywall, or is on a social platform (in which case it is also tagged "social").

With little content to work worth, Loki often can't see their relevance to any existing Level 2 file, so most of these thin note remain an Orphan. Occasionally, Loki adds one of these notes to a Level 2 file's Sources section, giving the item an inbound link and removing its Orphan status. But that link is *itself* by definition thin, based on little content.

Actually reading all of this content, of course, is still managed using the to-dos that Reading Queue Manager creates for me. But until I do, some of those files appear in the halo, some appear in the core, and I can't tell one from the other in the present graph view. 

So next I'll process a few more batches of my backlog, taking screenshots of the resulting graph views as I go, and try and figure out what to do with the thin notes. New versions of this page will allow for comparisons. 


---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version (2026-10-04): n/a
- version control
    - this is version: 1
    - this is the current version: [[Visualising my Karpathy wiki]]
    - here is the previous version: n/a