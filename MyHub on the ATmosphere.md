# MyHub.ai on the ATmosphere


**How would MyHub.ai evolve to become part of the ATmosphere?**

*(This is version 3 of this post, published on my experimental wiki using the [permanent versions pattern](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e). Version control in the footer.)*

The ATmosphere is the right ecosystem to bet on for developing decentralised collective intelligence, but it requires more than just exchanging 300-character status updates. We need:

* more apps, offering deeper and more valuable content and collaboration 
* a business model to sustain those apps
* productive, trustable interconnections between them, so that growth in one app lifts many boats.

*(more: [[Bluesky Adoption Challenge]])*

How would moving MyHub.ai onto the ATmosphere help? My basic answer can be found in my[ January 2023 manifesto posts](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4), but that was before I understood really anything about ATProtocol. I've therefore created this page to collect my evolving ideas for how those ideas would translate onto the ATmosphere.
## Idea in a nutshell

As I summarised in [this video](https://www.youtube.com/watch?v=OfX1-T96QXA), the basic idea is to: 

* transform the myhub.ai platform into a opensource, markdown-based, ATmosphere-enabled publishing toolkit 
* interconnected with a multi-protocol inbox, thinking and collaboration tools, 
* and use it to explore how productive online communities and decentralised collective intelligence can be made self-sustaining.

## So what's a Hub? 

Today, a Hub is just a personal site combining social bookmarking ("Stuff I Like"), blogging ("Stuff I Think"), and a personal portfolio ("Stuff I Do"). It is published on the myhub.ai platform, which I launched in March 2020. 

As you'll see from *my* Hub (https://myhub.ai/@mathewlowry/):

* it contains a searchable, filterable set of **cards**: resources ("Stuff") I Like, Think or Do. Each card is either:
	* **hosted**: the card points to a full longform piece of content hosted on the Hub 
	* **curated**: it contains my notes on a resource located at an external URL, and was created using the myhub bookmarklet
* each card has a **Type** (Like, Think or Do) and **tags**. 
* Types and tags can be easily combined, creating **Collections** like:
	* [what I **Like, Think and Do** about Bluesky](https://myhub.ai/@mathewlowry/?tags=bluesky&types=like&types=do&types=think&timeframe=anytime&quality=all )
	* [what I **Think and Do** tagged both productivity *and* content strategy](https://myhub.ai/@mathewlowry/?quality=all&types=do&types=think&tags=productivity&tags=content+strategy&timeframe=anytime)
	* [what I **Think** tagged ATprotocol *and* Collective Intelligence](https://myhub.ai/@mathewlowry/?tags=collective+intelligence&types=like&types=do&types=think&timeframe=anytime&quality=all&tags=atprotocol)
*  each Hub's Collection has its own RSS feed ([here's the feed for the above Collection](https://myhub.ai/rss/@mathewlowry/?tags=collective+intelligence&types=like&types=do&types=think&timeframe=anytime&quality=all&tags=atprotocol)).

**As a result, a Hub:**

* brings together a Hub Editor's content from across the web
* plays an important role in each Editor's "thinking/writing stack"
* "knows" an enormous amount of what interests the Editor, which could be leveraged by a (user-owned) AI 

But that's what a Hub is *today*. Having played with mine in one form or another since 2013, I have more than a few ideas about its future. 

## 3 connections

**Cards are made to be shared, and Hubs - as their name implies - are designed to be connected. But why limit this to Hubs?**

The toolkit I want to create will enable users to create a wide variety of ATmosphere-connected sites, not just Hubs. As set out in those [January 2023 manifesto posts](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4), that means connecting these sites in three different ways:

* connect each site to its Editor's **thinking and writing tool**
* connect all sites (and their Editors, and *their* thinking tools) **to each other and other ATmosphere apps** 
* (possibly - speculative) connect these sites *and* thinking tools to AI services to improve creativity and improve discovery.

These are explored in the next three sections. There are also a couple of other key features required for Hub monetisation, explored in "Business model", after that.  
## Connection 1: Thinking tool -> Site

**Goal: offer seamless interconnection between each Editors' private library of notes and their public site.** 

In practice, this means creating:
### Site publishing toolkit

An opensource dynamic site publishing toolkit for sites on the Atmosphere, using a range of themes (Hubs, newsletters, etc.).

This toolkit will allow users to: 

* create and publish their own site on their own domain, with content stored on their own PDS 
* monetise their content, as set out in "Business models"
* create their own theme, and share and monetise it.

Because these sites are published on the ATmosphere, they can be interconnected with other sites and other ATProto apps, as explored in Connection 2, below. 

*(late 2025 update)*: the fundamental work has been done, and it's called [standard.site](https://standard.site/) . 
### Thinking tool -> site integration

Each site is also connected to thinking tools, making it the **public-facing edge of the user's private library** of notes and drafts, stored in markdown format either on the cloud or on their own machine.

The thinking tool basically spans the "Reading Queue -> My Library" stages in the middle of the user's *"reading, thinking, writing & publishing stack"*:

![[pipeline.png]]
*(from [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.eurosky.social/3lcb22vzc3r2x), December 2024)*

The Library is where the Editor makes notes, thinks, drafts and then hits a Publish button, pushing the content out the door to the Public site. Editors can also invite Trusted Friends to collaborate within their Library (not shown, explored later).
## Connection 2: Hub->Atmosphere->Hub

**Goal: Each Hub (and, behind it, the Editor's thinking tool) is networked with other Hubs and other apps on the ATmosphere.**

Essentially, both ends (Inbox and Public Site) of each thinking/writing stack are connected to everyone else via ATproto and other protocols (RSS, ActivityPub, SMTP):

!["This is my ideal workflow, abstracted from my earlier posts"](https://whtwnd.com/api/cache?did=did:plc:2zxlmj2dvub7smpul2lvwqfk&cid=bafkreihmgjhhgvtlnvi3zdhnzh7kv6k7ppgbc6oomxpjmvqd7s3kmfjxci)

The above figure introduces

* **an Editor's Inbox**: presents content from ATmosphere accounts they Follow, Custom Feeds they subscribe to, RSS feeds, ActivityPub accounts, newsletters...
* Hub editors: 
    * interacting directly with a post in their Inbox (eg reply to a Bluesky post, reHub a Hubbed card) 
    * and/or feeding it into their thinking tool for further added-value processing... 
    * resulting (hopefully!) in something unique emerging onto their public site & newsletter... 
    * and from there into their *Followers'* Inboxes.
* anyone with an ATmosphere account Following: 
	* the entirety of a Hub's output, or to a subscriber-defined Collection, 
	* multi-Hub custom feeds 
	* premium subscriptions (e.g., "*get everything I Think, plus everything I read developing it*", or even "*Platinum subscribers can also access part of my private Library and hang out with me on Wednesdays*", etc. - see Business Model, below)
* Hub Editors inviting **Trusted friends** into one or more notes in their thinking tool, allowing both to edit and publish something collaboratively (as in tools like [MarkPub](https://markpub.org/), used in this wiki).
* comments to hosted Hub items can be shared via the commenter's Bluesky account, if a commenter wishes (as in Whitewind, Leaflet.pub, etc), widening conversation reach 

## Connection 3: Hub <-> AI services

**As set out under Business Model (next), one of the two revenue streams to explore is something I have come to call AI4communities.** 

*Warning: you've entered this project's speculative edge, originally explored in 2022 and not validated since.*

AI4communities means that individuals or - ideally - communities of people can collectively lease or own a range of AI services to help them be more productive and/or creative online. 

!["From 2023"](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*mrMrYtsN5b1XwlmkVXThrw.png)
*(from [How Artificial Intelligence will finance Collective Intelligence](https://mathewlowry.medium.com/how-artificial-intelligence-will-finance-collective-intelligence-5d17adcce98b), January 2023)*

There could be a range of business models for providing these services, from pure subscription through to the community leasing or owning "their" model, and affraying the costs though data-sharing.

Many AI services will support individuals (cf Bluesky users subscribing to custom feeds and block lists) but other services could support entire communities, and can be configured and fine-tuned by the members to ensure they reflect their interests and preferences. After all, when you have a Hub on the ATmosphere you can choose to give your AI services access to a *lot* of content:

* what you do on your social network(s)
* every article you bookmark or Hub (and so find really, really useful)
* the notes you make about it as you curate it (which tells the AI exactly _what_ you find useful about it)
* everything else (blog posts and professional references, mainly) which you publish alongside them
* and everything else in your private knowledge library you make accessible to it.

Individual users and communities would access these services via what the [Three Legged Stool manifesto](https://publicinfrastructure.org/2023/03/29/the-three-legged-stool/) calls a “Friendly Neighborhood Algorithm Store”.

## Business model: two revenue streams

**The second overarching goal of the project is to explore two revenue streams.** 
### Premium subscriptions

As mentioned above, with a few features added each Hub will become a "Substack on Steroids". There are two reasons why it would be better than anything else on the market:

**a) Better content offering:** On the one hand, it will allow Editors to offer subscribers access to some or all of the Editor's finished posts (as in Substack, Ghost, etc.), *plus:*

* everything the Editor read, particularly the resources influencing those finished posts, with the Editor's notes
* collaborative spaces and groups for the Editor and his/her subscribers
* selected parts of their private Library.

As a result we will support creators for not just creating, but also *curating*, high-value content, and integrate this content into social and collaborative networks.

**b) Better content productivity:** in addition, there is the productivity bonus the Editor gets from the integration between the inbox, the reading queue and thinking tool with their public and subscriber-only publishing engine.

### AI Services and AI4communities

Subscriptions are also relevant to the communities we want to see develop in the ATmosphere. Community members may pay a small subscription fee for access to an improved community environment and tools, supplied by, inter alia: 

* apps which go beyond shortform chat (collaboration, co-creation), 
* manual community management
* a wide range of customisable AI services, as explored above.

Moreover, the model collapse phenomenon may mean that a user's or communities' content may become valuable AI training data. This is *particularly* the case where a community is using apps which go beyond simple shortform chat - ie, the more communities curate, discuss and (co-)create longform, original content, the more valuable training data they will create, which they can then monetise as a community.

Note that this is somewhat speculative, not least because the existence of the original model collapse phenomenon has been called into question since the original papers in [May](https://arxiv.org/abs/2305.17493) and [July](https://www.nature.com/articles/s41586-024-07566-y). I nevertheless believe that authentically human, high-value content created by communities may become valuable. 

---
## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- significantly shortened, rewritten to reflect more recent ideas 
- version control
    - this is version: 3
    - this is the current version: [[MyHub on the ATmosphere]]
    - here is the previous version: [[MyHub on the ATmosphere 2]]