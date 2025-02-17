**How would MyHub.ai evolve to become part of the ATmosphere?**

*(Notes: This is an early draft. As explained in [this newsletter edition](https://mathewlowry.medium.com/exploring-ai4communities-newsletter-6365b2716bb1), I am publishing these early versions as I develop my thoughts in the hope that constructive comments will help me finish the post. More version control in the footer.)*

In 2025, the ATmosphere is the right ecosystem to bet on for developing decentralised collective intelligence. As this is more than just exchanging 300-character status updates, the ATmosphere will need:

* more apps, offering deeper and more valuable content and collaboration 
* a business model to sustain those apps
* productive, trustable interconnections between them, so that growth in one app lifts many boats.

How would moving MyHub.ai onto the ATmosphere help? My basic answer can be found in my January 2023 manifesto posts, but that was before I understood really anything about ATProtocol. I've therefore created this page to collect my evolving ideas for how those ideas would translate onto the ATmosphere.

## Idea in a nutshell

**Transform the myhub.ai platform into a opensource, markdown-based, ATmosphere-enabled publishing toolkit interconnected with thinking and collaboration tools, and use it to explore how productive online communities can be made self-sustaining.** 

## So what's a Hub? 

Today, a Hub is just a personal site combining social bookmarking ("Stuff I Like"), blogging ("Stuff I Think"), and a personal portfolio ("Stuff I Do"). It is published on the myhub.ai platform, which I launched in March 2020. 

As you'll see from my Hub (https://myhub.ai/@mathewlowry/):

* it contains a searchable, filterable set of **cards**: resources ("Stuff") I Like, Think or Do. Each card is either:
	* hosted: the card points to a full longform piece of content hosted on the Hub 
	* curated: it contains my notes on a resource located at an external URL, and was created using the myhub bookmarklet
* each card has a **Type** (Like, Think or Do) and **tags**. 
* tags can be easily combined, creating **Collections** like:
	* [what I Like, Think and Do about Bluesky](https://myhub.ai/@mathewlowry/?tags=bluesky&types=like&types=do&types=think&timeframe=anytime&quality=all )
	* [what I Do and Think tagged both productivity *and* content strategy](https://myhub.ai/@mathewlowry/?quality=all&types=do&types=think&tags=productivity&tags=content+strategy&timeframe=anytime)
	* [what I Think tagged ATprotocol *and* Collective Intelligence](https://myhub.ai/@mathewlowry/?tags=collective+intelligence&types=like&types=do&types=think&timeframe=anytime&quality=all&tags=atprotocol).
*  each Hub's Collection has its own RSS feed ([here's the feed for the above Collection](https://myhub.ai/rss/@mathewlowry/?tags=collective+intelligence&types=like&types=do&types=think&timeframe=anytime&quality=all&tags=atprotocol)).

As a result, a Hub:

* brings together a Hub Editor's content from across the web
* plays an important role in a Editor's "thinking and writing stack"
* "knows" an enormous amount of what interests the Editor, which can be leveraged by AI 

But that's what a Hub is *today*. Having played with mine in one form or another since 2013, I have more than a few ideas about its future. Moreover, the toolkit I want to create will enable users to create a wide variety of ATmosphere-connected sites, not just Hubs.

### Dream outcome
**Cards are made to be shared, and Hubs - as their name implies - are designed to be connected. But why limit this to Hubs?**

As set out in those [January 2023 manifesto posts](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4), I want to connect Hubs in three different ways:

* connect a Hub to its Editor's thinking and writing tool
* connect Hubs (and their Editors, and *their* thinking tools) to each other and other ATmosphere apps to create social communities on the ATmosphere
* connect Hubs with AI services to improve creativity and open up new business models.

These are explored in the next three sections. There are also a couple of other key features required for Hub monetisation, explored in "Business model", after that. Finally, the tools we will develop will allow users to create other sorts of ATmosphere-connected sites, not just Hubs.
#### Connection 1: Thinking tool -> Hub

**Goal: offer seamless interconnection between each Editors' private library of notes and their public Hub, ready for the ATmosphere.** 

In practice, this means creating a "Hub toolkit": an opensource dynamic site publishing toolkit for ATmosphere, including a first Hub theme. This toolkit will allow users to: 

* create and publish their own Hub on their own domain and PDS 
* monetise their content, as set out in "Business models"
* create their own theme, allowing them to create and publish other sorts of ATmosphere-connected site
* share and monetise those themes.

These sites are published on the ATmosphere, enabling their interconnection with other Hubs and other ATProto accounts, as explored in Connection 2, below. 

Moreover, each site is the **public-facing edge of the user's private library** of notes and drafts, stored in markdown format either on the cloud or on their own machine, to which Editors can invite Trusted Friends to collaborate (not shown):

!["This is my ideal workflow, abstracted from my earlier posts"](https://whtwnd.com/api/cache?did=did:plc:2zxlmj2dvub7smpul2lvwqfk&cid=bafkreidgciur5nbnpmjj2nydusx7jznn26hdaw3e2vbz3dn4x53lu27wei)
*(from [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.bsky.social/3lcb22vzc3r2x), December 2024)*

**Results:**

* a more productive and creative "thinking and publishing stack" for individual Editors
* more powerful collaboration possibilities for networked Editors (given ATmosphere connections, next).

***What's this got to do with the ATmosphere?*** In the next section we'll briefly describe how Hubs will be networked together via the ATmosphere, and with Bluesky and other ATmosphere apps. The above developments are therefore required to:

* network, via the ATmosphere, integrated "thinking and publishing stacks", and their associated high-value, longform content, which is vital to the AI4communities business model;
* introduce collaboration-oriented communities into the ATmosphere, tackling the "too many blogs, not enough wikis" problem (see Whitewind post, below).

**How:** 

* create the markdown-based dynamic site builder, and the Hub template
* either create connectors between popular Tools4Thought and the  dynamic site builder (eg plugins for Obsidian, etc.), or create the dynamic site builder CMS as a simple Tool4Thought, or both.
* develop a "repost style flow" that allows for the organization of links in the Hub to lead to amplification by other authors.

**More reading:**

* (2023 manifesto post): [Thinking and writing in a decentralised collective intelligence ecosystem](https://mathewlowry.medium.com/thinking-and-writing-in-a-decentralised-collective-intelligence-ecosystem-16dd2b1893cc )
* (December 2024 on Whitewind): [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.bsky.social/3lcb22vzc3r2x) 

#### Connection 2: Hub->ATmosphere->Hub

**Goal: Each Hub (and, behind it, the Editor's thinking tool) is networked with other Hubs and other apps on the ATmosphere** - essentially, both ends (Inbox and Outbox) of each integrated writing & thinking stack are connected to everyone via ATProto. 

!["This is my ideal workflow, abstracted from my earlier posts"](https://whtwnd.com/api/cache?did=did:plc:2zxlmj2dvub7smpul2lvwqfk&cid=bafkreihmgjhhgvtlnvi3zdhnzh7kv6k7ppgbc6oomxpjmvqd7s3kmfjxci)
*(from [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.bsky.social/3lcb22vzc3r2x), December 2024, updating [Thinking and writing in a decentralised collective intelligence ecosystem](https://mathewlowry.medium.com/thinking-and-writing-in-a-decentralised-collective-intelligence-ecosystem-16dd2b1893cc), January 2023)*

Results:

* an Editor's thinking tool's Inbox (or their Hub's integrated Bluesky client) includes content from ATmosphere accounts they Follow and feeds they subscribe to (and, eventually, content from RSS feeds, ActivityPub accounts and newsletters)
* Hub editors can: 
    * interact directly with a post in their Inbox (eg reply to a Bluesky post, reHub a Hubbed card) 
    * and/or feed it into their thinking tool for further added-value processing, resulting (hopefully) in something unique emerging from their Outbox, and into their *Followers'* Inboxes
* because anyone with an ATmosphere account can Follow: 
	* the entirety of a Hub's output, or to a subscriber-defined Collection
	* multi-Hub custom feeds (free or premium, AI-powered and/or tag-based - see AI Services, below)
	* premium subscriptions (e.g., "get everything I Think, plus everything I read developing it", or even "Platinum subscribers can also access part of my private Library and hang out with me on Wednesdays", etc. - see Business Model, below)
* comments to hosted Hub items can be shared via the commenter's Bluesky account, if a commenter wishes (as in Whitewind or MarkPub), widening conversation reach 
* Hub Editors can invite Trusted friends into one or more notes in their thinking tool, allowing both to edit and publish something collaboratively (as in MarkPub).

More reading:
* (2023 manifesto post): [Social knowledge graphs for collective intelligence](https://mathewlowry.medium.com/social-knowledge-graphs-for-collective-intelligence-75c436889320) 
* (video, April 2023) [Why I'm massively into massive.wiki](https://www.youtube.com/watch?v=qfYl3SiZJWU]) (MarkPub's old name)

#### Connection 3: Hub <-> AI services

**As set out under Business Model (next), one of the two revenue streams to explore is something I have come to call AI4communities.** It means that individuals or - ideally - communities of people in the ATmosphere can collectively lease or own a range of AI services to help them be more productive and/or creative online. 

!["From 2023"](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*mrMrYtsN5b1XwlmkVXThrw.png)
*(from [How Artificial Intelligence will finance Collective Intelligence](https://mathewlowry.medium.com/how-artificial-intelligence-will-finance-collective-intelligence-5d17adcce98b), January 2023, but currently being updated on my wiki - see below)*

There could be a range of business models for providing these services, from pure subscription through to the community leasing or owning "their" model, and affraying the costs though data-sharing, as set out in my experimental wiki:


 > Moreover, as I pointed out in 2020 when I launched myhub.ai, each community could act as a **data union**: rather than just buying or renting an AI to support their community, they could monetise the resulting algorithm to at least help cover the costs of running the community. While I shelved this idea when ChatGPT appeared, the model collapse paper now suggests that the **training data** created by well-managed communities could be the new currency of collective intelligence" - [AI4Communities: a model for a self-sustaining, user-owned public sphere](https://experiments.myhub.ai/ai4communities_post) 


Many AI services will support individuals (cf Bluesky users subscribing to custom feeds and block lists) but other services could support communities, and can be configured and fine-tuned by the members to ensure they reflect their interests and preferences. 

The post explores a range of possible AI services (content discovery, content moderation and governance, "centaur services" to support individual's and communities' creativity, etc.), and links to subfiles exploring how they would look on [the Fediverse](https://experiments.myhub.ai/ai4communities_on_the_fediverse) and [ATmosphere](https://experiments.myhub.ai/ai4communities_on_the_atmosphere) (one on Nostr is next). However, there are certainly many more. 

All of them, moreover, become more valuable to users when they have more content to work with. That's important, because when you have a Hub on the ATmosphere you can choose to give your AI services access to a *lot* of content:

* what you do on your social network(s)
* every article you bookmark or Hub (and so find really, really useful)
* the notes you make about it as you curate it (which tells the AI exactly _what_ you find useful about it)
* everything else (blog posts and professional references, mainly) which you publish alongside them
* and everything else in your private knowledge library you make accessible to it.

Individual users and communities would access these services via what the Three Legged Stool manifesto calls a “**Friendly Neighborhood Algorithm Store**”, so this project needs to demonstrate:

* how such a Store can provide AI services to both individuals and communities, using Hubs and other ATmosphere apps 
* the value of some initial services - eg AI-curated custom ATmosphere feeds - to stimulate other suppliers to add their services to the Store, and/or launch more Stores.

**More reading:**

* (2023 manifesto post): the idea was first developed in [How Artificial Intelligence will finance Collective Intelligence](https://mathewlowry.medium.com/how-artificial-intelligence-will-finance-collective-intelligence-5d17adcce98b) 
* the model collapse paper prompted me to redevelop it, which I'm currently doing in public via my experimental wiki:  [AI4Communities: a model for a self-sustaining, user-owned public sphere](https://experiments.myhub.ai/ai4communities_post)  


## Business model  

**The goal is both to develop a set of opensource tools which anyone can build on and with, *and* in the process explore two revenue streams.** 

When I set out to create myhub.ai, I initially intended to simply develop a personal Hub for myself. My developer, however, suggested making it a platform to see if anyone else would want one. So we did, just as covid struck. It was a bad moment to market anything, so I simply explored the tool and developed my ideas, occasionally including a link to a Collection on my Hub in social conversations. Despite zero marketing, I have over 200 signups.

With the emergence of the ATmosphere, however, I think Hubs are a good tool to break down the barriers between social and publishing, creating and curating. However, a business model is required if it is really going to make an impact. 

To explore these new opportunities we therefore need to build the above tools so that we can explore and demonstrate the following revenue models:
### Premium subscriptions

As mentioned above, with a few features added each Hub will become a "Substack on Steroids", allowing Editors to offer subscribers access to:
* some or all of the Editor's finished posts (as in Substack, Ghost, etc.)
* everything the Editor read, particularly the resources influencing those finished posts, with the Editor's notes
* collaborative spaces and groups for the Editor and his/her subscribers
* selected parts of their private Library.

As a result we will support creators for not just creating, but also *curating*, high-value content, and integrate this content into social and collaborative networks.

### AI Services and AI4communities

Subscriptions are also relevant to the communities we want to see develop in the ATmosphere. Community members may pay a small subscription fee for access to an improved community environment and tools, supplied by, inter alia: 

* apps which go beyond shortform chat (collaboration, co-creation), 
* manual community management
* a wide range of customisable AI services, as explored above.

Moreover, the model collapse phenomenon may mean that a user's or communities' content may become valuable AI training data. This is *particularly* the case where a community is using apps which go beyond simple shortform chat - ie, the more communities curate, discuss and (co-)create longform, original content, the more valuable training data they will create, which they can then monetise as a community.

Note that this is somewhat speculative, not least because the existence of the original model collapse phenomenon has been called into question since the original papers in [May](https://arxiv.org/abs/2305.17493) and [July](https://www.nature.com/articles/s41586-024-07566-y). I nevertheless believe that authentically human, high-value content created by communities may become valuable to future AI development, for example to [provide seeds for synthetic training data](https://simonwillison.net/2024/Dec/15/phi-4-technical-report/). 

## Development programme

Currently I'd tackle the above developments in the following order:

* Hub-ATmosphere integration. This can be broken down into several steps:
	* move the existing myhub.ai platform to ATmosphere to explore the basic features: 
		* Hub editors can use their existing Bluesky account/PDS to host their Hub and connect it to the rest of the ATmosphere; 
		* if they dont have one, myhub.ai gives them one:
			* Hub address: myhub.ai/@username; 
			* bluesky address: @username.myhub.ai
	* add content monetisation possibilities to the Hub product
	* based on what we learn, create the dynamic site builder "Hub toolkit" set out earlier, allowing anyone to build their own Hub on their own domain and PDS, create other sorts of site, integrate the Hub/ATmosphere interface into their existing site, etc.
* Hub-thinking tool integration: there are already plenty of open source tools integrating publishing and Tools4Thought (I'm using one to publish this wiki). Overall, two directions are possible, and both may be a good idea:
	* develop plug-ins for popular Tools4Thought to integrate with their Hubs
	* develop the Hub CMS as a simple Tool4Thought 
* develop the "friendly neighbourhood algorithm store" business model.

## Conclusion & Summary

I thought I'd conclude with the final image from my latest Whitewind post, which takes one of the images from my January 2023 manifesto posts and updates it for the ATmosphere.

![from "Thinking transparently in the ATmosphere"](https://whtwnd.com/api/cache?did=did:plc:2zxlmj2dvub7smpul2lvwqfk&cid=bafkreiex5a5pnc3qcw5s2wy5e33biyyrovams6sbigtpnj4tilvujwmfhy)

*(from [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.bsky.social/3lcb22vzc3r2x), December 2024.)*

It shows:

* three key parts of an individual user's thinking tool
* how it can Follow ATmosphere and other information sources (left) and be Followed by others (top right)
* that the user can invite Trusted Friends into the thinking tool to collaborate (centre top), as I invited Peter and Aram to work on this proposal
* that the user can publish selected notes from the thinking tool directly to a variety of ATmosphere personal publishing apps
* how conversations about that post can appear both on the user's app (eg blog comments) and elsewhere (eg Bluesky posts about a Whitewind blogpost)
* how that content is then "remixed" by other ATmosphere apps, the outputs of which can in turn be followed by the original user

It doesn't show AI services supporting users in their thinking tool, but no one image can capture all the possibilities, and no one project should attempt to build everything. 

Instead, everything that is to be built must be built to work with everything else.


---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- none, as this is the first, originally circulated to some friends in December 2024
- version control
    - this is version: 1
    - this is the current version: [[MyHub on the ATmosphere]]
    - here is the previous version: n/a