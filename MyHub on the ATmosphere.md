# MyHub.ai on the ATmosphere

**An onramp to cross-platform decentralised collective intelligence, with credible exit throughout.**

*(This is version 4 of this post, published on my experimental wiki using the [permanent versions pattern](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e). Version control in the footer.)*

The ATmosphere is the right ecosystem to bet on for developing decentralised collective intelligence, but it requires more than just exchanging 300-character status updates. We need:

* more apps, offering deeper and more valuable content and collaboration 
* a business model to sustain those apps
* productive, trustable interconnections between them, so that growth in each app lifts many other boats.

*(more: [[Bluesky Adoption Challenge]])*

How would moving MyHub.ai onto the ATmosphere help? My basic answer can be found in my[ January 2023 manifesto posts](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4), but that was before I understood really anything about ATProtocol. I've therefore created this page to collect my evolving ideas for how those ideas would translate onto the ATmosphere.
## Idea in a nutshell

The basic idea is to: 

* **develop the myhub.ai platform** to provide the key parts of a content pipeline: reading queue, a private thinking tool with "Friends only" collaboration spaces, and a public-facing site (Hubs to begin with, but also blogs, newsletters, wikis, etc.)
* provide **credible exit** at each stage of the content pipeline, so users can later swap in alternative tools, self-host, innovate, etc

The platform therefore acts as an **on-ramp**—a simple starting point for newcomers - which doesn't lock them in, as users: 

* store their own content on their own Personal Data Servers and manage their own identity
* can export their myhub content to local-first solutions whenever they like.
## What's a Content Pipeline?

I developed my content pipeline to help tackle the firehose of content coming at me. 

![[pipeline.png]]
*(from [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.eurosky.social/3lcb22vzc3r2x), December 2024)*

In its simplest form, it's:

* your *curated Inboxes*, which contain stuff which might be interesting
* your reading, thinking and writing stack: a reading queue and private library where the Editor makes notes, thinks, drafts and ...
* optionally, hits Publish, pushing the content to a public site.

Editors should also be able to invite Trusted Friends to collaborate within their Library, but I'll leave that for later.
## What's a Hub?  

Today, a Hub is one of these personal public sites - it's the  public facing edge of my thinking and writing stack, combining:

* social bookmarking ("Stuff I Like"), 
* blogging ("Stuff I Think"), 
* and a personal portfolio ("Stuff I Do"). 

It is published on the myhub.ai platform, which I launched in March 2020. As you'll see from my Hub ([https://myhub.ai/@mathewlowry/](https://myhub.ai/@mathewlowry/)):

* it contains a searchable, filterable set of **cards**: resources ("Stuff") I Like, Think or Do. Each card is either:
	* **hosted**: the card points to a full longform piece of content hosted on the Hub 
	* **curated**: it contains my notes on a resource located at an external URL, and was created using the myhub bookmarklet
* each card has a **Type** (Like, Think or Do) and **tags**. 
* Types and tags can be easily combined, creating **Collections** like:
	* [what I **Like, Think and Do** about Bluesky](https://myhub.ai/@mathewlowry/?tags=bluesky&types=like&types=do&types=think&timeframe=anytime&quality=all )
	* [what I **Think and Do** tagged both productivity *and* content strategy](https://myhub.ai/@mathewlowry/?quality=all&types=do&types=think&tags=productivity&tags=content+strategy&timeframe=anytime)
	* [what I **Think** tagged ATprotocol *and* Collective Intelligence](https://myhub.ai/@mathewlowry/?tags=collective+intelligence&types=like&types=do&types=think&timeframe=anytime&quality=all&tags=atprotocol)
*  each Hub's Collection has its own RSS feed ([here's the feed for the above Collection](https://myhub.ai/rss/@mathewlowry/?tags=collective+intelligence&types=like&types=do&types=think&timeframe=anytime&quality=all&tags=atprotocol)).

Note that a Hub not only brings together a Hub Editor's content from across the web, it "knows" an enormous amount of what interests the Editor, which is handy for any personal AI assistant.

## Why connect this to the Atmosphere?

Both ends (Inbox and Public Site) of each thinking/writing stack can be connected to everyone elses' via ATproto and other protocols (RSS, ActivityPub, SMTP):

!["This is my ideal workflow, abstracted from my earlier posts"](https://whtwnd.com/api/cache?did=did:plc:2zxlmj2dvub7smpul2lvwqfk&cid=bafkreihmgjhhgvtlnvi3zdhnzh7kv6k7ppgbc6oomxpjmvqd7s3kmfjxci)

The above figure shows:

* **an Editor's Inboxes**: presents content from email, ATmosphere accounts they Follow, Bluesky Custom Feeds & RSS feeds, ActivityPub accounts, ...
* Hub editors: 
    * Scan their inboxes, adding useful content to their Reading Queue
    * read it, take notes in their thinking tool, integrate it into their personal knowledge
    * resulting (hopefully!) in something unique emerging onto their public site & newsletter...
    * and from there into their *Followers'* Inboxes (next)
* anyone with an ATmosphere account can Follow: 
	* the entirety of a Hub's output, or to a subscriber-defined Collection, 
	* multi-Hub custom feeds 
	* premium subscriptions (e.g., "*get everything I Think, plus everything I read developing it*", or even "*Platinum subscribers can also access part of my private Library and hang out with me on Wednesdays*")
* Hub Editors inviting **Trusted friends** into selected notes in their thinking tool, allowing both to edit and publish collaboratively

There's plenty which is not shown: comments to hosted Hub items, for example, can be shared via the commenter's Bluesky account, widening conversation reach.
## Two development paths

I want to both develop the myhub.ai platform to support this *and* provide credible exit to local-first alternatives, so two development paths are required.

![[Pasted image 20260824171349.png]]
### Developing MyHub.ai
myhub.ai already provides the basic public-facing end of the pipeline, but needs:

* *(optionally, top left)* integrated inboxes for protocols (email, RSS; etc.), although stand-alone tools already exist 
* *(top centre)* the rest of the private content pipeline (reading queue, thinking tool), built into the MyHub Editor
	* note: we'll use [private atproto spaces](https://atproto.com/blog/atproto-spaces-alpha), as this allows Friends-only collaboration
* *(top right)* a marketplace where users can choose a variety of site types (Hubs, blogs, newsletters, wikis, etc.), and through which developers and designers can sell site types and designs.
* *(bottom right)* to source the content from, and write to, the user's PDS, and so publish content onto the Atmosphere using [standard.site](https://standard.site/) - an Atmosphere lexicon for longform content
	* note: in this way these sites can be interconnected with other sites and other ATProto apps (see Connection 2, below). 
* *(right)* to integrate enewsletter and Fediverse publication services with the public site.
### Local-first path

This path is already well-served, as: 

* there are plenty of stand-alone inboxes out there
* Obsidian and others like it already provide excellent thinking tools based on markdown files, and are easily extensible (eg see my [[ReadingQ]] Obsidian plugin)
* [Groundmist](https://myhub.ai/@mathewlowry/?types=like&types=do&types=think&timeframe=anytime&quality=all&tags=groundmist) allows users to push local files to their PDS, from where they can be published by any CMS using the PDS for storage.

**This provides credible exit:** any user can get started on MyHub in the knowledge that at any point they can export their content from the platform into markdown files on their hard drive, and start playing with Obsidian (or its alternatives) and Groundmist. 

Note that users can **exit *partially*** - there's nothing stopping somebody managing their content using Obsidian, for example, but using the MyHub platform for the public-facing site.

## Business model: where's the revenue?

**The single most important development the Atmosphere needs to grow is for someone to create something some people are prepared to pay for.**
### Fremium plans

Some people enjoy fine-tuning Obsidian and configuring Groundmist, their PDS and CMS, but I'm betting many others will pay a couple of euros a month to have myhub take care of it for them, safe in the knowledge that if the platform does go in a direction they don't like they can always take the local-first path.

### Substack on Steroids

Moreover, the fully-featured Hub you'd get for your subscription will be a Substack on steroids:

**a) Better content offering:** Editors will be able to offer subscribers access to some or all of the Editor's finished posts (as in Substack, Ghost, etc.), *plus:*

* everything the Editor read, particularly the resources influencing those finished posts, with the Editor's notes
* collaborative spaces and groups for the Editor and his/her subscribers
* selected parts of their private Library.

As a result we will support creators for not just creating, but also *curating*, high-value content, and integrate this content into social and collaborative networks.

**b) Better content productivity:** then there's the productivity bonus the Editor gets from the integration between the inbox, the reading queue and thinking tool with their public and subscriber-only publishing engine.
### Open innovation

Finally, the marketplace will be open - designers and developers will be free to develop and market new site types and designs.

---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- credible exit emphasised, 
	- took out AI4Communities (too speculative)
- version control
    - this is version: 4
    - this is the current version: [[MyHub on the ATmosphere]]
    - here is the previous version: [[MyHub on the ATmosphere 3]]