---
title: Hub Manager Obsidian plugin
type: do
source: hosted
visibility: public
publish: false
hub_tags:
  - myhub
  - obsidian
description: v1
slug: hub-manager-obsidian-plugin
coverImage: content-pipeline-localfirst-all.png
version: 1
---
# Hub Manager: drawing the line AI won't cross

**Another plugin is coming for my content pipeline. But not for all of it.** 

While [[ReadingQ Manager]] gets content into my library and adds a task to read it onto various reading queues, "Hub Manager" then takes over, supporting the rest of the content pipeline until content is ready to publish on my Hub, as set out in [[MyHub.ai on the ATmosphere]].

*(Notes: This is version 1 of this post. Version control in the footer.)*

![[content-pipeline-localfirst-hubmanager-1.png]]

*The Hub Manager plugin takes over where [[ReadingQ Manager]] stops, helping create and move content through my pipeline until it's ready to publish onto my Personal Data Server (PDS) (image adapted from [[MyHub on the ATmosphere]])*.

As the above diagram shows, Hub Manager provides a lot of different features, but with a couple of exceptions ('Edit it', 'Sync all') they are all variants of the same task: create a new file with certain metadata (known in Obsidian as frontmatter). 

![[hub manager - new hosted item.png]]

*The dialog called up by New hosted item as I created [[Building a Karpathy LLMwiki inside my content pipeline]].*

The above screenshot gives a glimpse of the entire content pipeline as managed with Obsidian: 

* By default, Hub Manager assumes 
	* this content will eventually be public (so **visibility = public**)...
	* ... but shouldn't be pushed to the PDS just yet (so **publish = No**). 
	* both defaults can easily be changed as I edit the content. 
* **Type** corresponds to the three types of content on [my Hub](https://myhub.ai/@mathewlowry/). If it's empty the content will become part of my wiki, which will move from its separate subdomain into a layer of content integrated underneath the Hub)
* The **slug** (the address the content will have on my Hub if/when publish = Yes) is auto-generated from the title
* As it's a new file, **version = 1**. This can only changed by another feature (Create New Version, first imagined [in early 2023](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)), which is only available on content which has already been published. 
* I chose the **tags** from a dropdown which currently reads from an export of the tags on my Hub - when I finish integrating this workflow into my Hub's publication process, that taxonomy will be managed in the opposite direction: from my library, pushed to the Hub.

## Drawing a line

Both plugins were vibe-coded by Loki, which also manages the [[Building a Karpathy LLMwiki inside my content pipeline|LLM wiki]] sitting inside my Private Library. But while these tools all *support* the processes of curating other people's content, creating my own, and publishing everything onto my Hub, **the actual writing cannot be performed by AI, because writing = thinking**. 

> writing = thinking

Not that Loki can't write - it can, badly, but like all LLMs it's improving. But the process of writing is indispensable to both learning other people's ideas and coming up with your own. If you rely on an AI to write your notes, posts and articles for you, none of that knowledge will actually get into your head, where it can connect to everything else there to spark new ideas. As the authors of [a recent MIT report](https://aiandeducation.mit.edu/report/) put it, "Getting the right answer from a chatbot can create the illusion of learning".

So while Loki may help me organise, it's still me who identifies what's valuable and why, and writes every word. Otherwise I'll internalise, and publish, nothing of value.

---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version (2026-10-04): n/a
- version control
    - this is version: 1
    - this is the current version: [[Hub Manager]]
    - here is the previous version: n/a