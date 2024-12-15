# AI4Communities on the ATmosphere

**This is a subfile of the primary [[AI4Communities post]], and won't make any sense unless you read its parent first. It explores how the AI4communities idea would look in decentralised social networks powered by ATProto, the Bluesky protocol**.

*(Notes: This is an early draft. As explained in [this newsletter edition](https://mathewlowry.medium.com/exploring-ai4communities-newsletter-6365b2716bb1), I am publishing these early versions as I develop my thoughts in the hope that constructive comments will help me finish the post. More version control in the footer.)*

I knew Bluesky existed but not much else when I published my [manifesto posts of 1/1/23](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4), so early versions of the [[AI4Communities post]] were Fediverse-oriented. I created the first versions of this post in early November 2024 to explore how AI4Communities would look "on Bluesky". By the time I synthesised my first research into [my November 2024 newsletter](https://mathewlowry.medium.com/ai4communities-bluesky-newsletter-331a25909cc5)  I had concluded that in many ways Bluesky *already* supports AI4communities, but not in the Fediverse-friendly "cozyweb village" paradigm I had been using until then. 

I continued my research for my December newsletter, which spawned a blog post in the process:

* [This newsletter is posted on Bluesky](https://whtwnd.com/mathewlowry.bsky.social/3lcb34ugiq22t)
* [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.bsky.social/3lcb22vzc3r2x)

Both were published on Whitewind, a blogging platform on the ATMosphere, which is why in this version of this page has been renamed from "*AI4Communities on Bluesky*" to "*AI4Communities on the ATmosphere*". Because this is about much more than Bluesky, it's about the ATmosphere - the ecosystem underpinned by ATProto, and the innovation we'll see in it.

## Bluesky

**But first, back to Bluesky: how does it support AI4communities?** 

### Open marketplace

Individual Bluesky users can already subscribe to custom feeds (ie **Content discovery services**) and moderation tools (ie **Content moderation services**, known as labellers in Bluesky) *provided by 3rd parties.* These can range from human-powered labelling through to AI-powered, although most currently are custom feeds driven by pretty simple search expressions. 

The first custom feed I installed, for example, was “[Science](https://bsky.app/profile/bossett.social/feed/for-science)”, developed by [Dani cRabaiotti](https://bsky.app/profile/danirabaiotti.bsky.social), a zoologist and data scientist working at the Zoological Society in London. This is possible because Bluesky wants to give users [Algorithmic choice](https://bsky.social/about/blog/3-30-2023-algorithmic-choice). Instead of suffering the problems created by a one-size-fits-all algorithm, as seen on platforms like X and Facebook, Bluesky users can choose from an open and diverse "marketplace of algorithms". In this approach, algorithms "*act as aggregator services, similar to search engines*" - users add algorithms to their clients seamlessly, with Bluesky allowing them "*to swipe between favorite algorithms or view a multi-algorithm feed*".

Bluesky doesn't even control feed creation. Instead, they provide "*APIs for feed generation... allowing for custom feed and moderation systems to be created as independent services ... [and] a feed selection system that enables users to explore third-party feeds and access them as effortlessly as their home timeline... we’re using a similar approach to address reputation, misinformation labeling, and moderation.*" 

To test this I created some Bluesky feeds for the Brussels Bubble, to see whether that will help them off their nasty Xitter habit, and added them to the [Bluesky Brussels Bubble Starter Pack](https://go.bsky.app/LZExyns). I tested two 3rd party services (Bluesky Feed Creator and Skyfeed), neither AI-driven, and published my first results in my [November newsletter](https://mathewlowry.medium.com/ai4communities-bluesky-newsletter-331a25909cc5). Bluesky Feed Creator reached out with some advice following that, which led to significant improvements I still need to document.  

Although I'm pretty happy with Bluesky's direction of travel, concerns remain - for example: 

* although they assure us that they [won’t “enshittify” the Bluesky service](https://www.wired.com/story/bluesky-ceo-jay-graber-wont-enshittify-ads/), Cory Doctorow, who [coined the term](https://doctorow.medium.com/https-pluralistic-net-2024-10-14-pearl-clutching-this-toilet-has-no-central-nervous-system-266e69b4c8f9), is [not convinced](https://doctorow.medium.com/https-pluralistic-net-2024-11-02-ulysses-pact-tie-yourself-to-a-federated-mast-b2f89bb5b4d8);
* unlike the older Fediverse, Bluesky is not currently proven: there's currently still really only one app, one "firehose" run by one company, etc.

But see "Onto the ATmosphere", below.

### Porous communities, light AI4communities

**While it's already easy to imagine how a community could form around their own AI-powered labellers and custom feeds,** these would be very porous communities - there is currently only one ATProto network, not a connected archipelago of servers, and it's very open: "*Anyone who knows how to code can write an app or tool that can read practically any data about anyone, without having to ask anyone for permission*" ([A complete guide to Bluesky](https://mackuba.eu/2024/02/21/bluesky-guide?utm_source=pocket_shared)). 

Is this a feature or a bug? Bluesky's openness, and the fact that the entire network can be searched, makes AI4communities more feasible, but it's a light version - there will be no separate villages, or private groups for collaboration.

My metaphor is therefore upended: we won't see a community collectively choosing some algorithms, sharing their data with them, and monetising the result, as in [[AI4Communities on the Fediverse]]. Instead, each member will go to the store individually, and anyone who subscribes to the same algorithm will automatically join the club.

One possibility of making such a community less open: the store puts the algorithm out of reach of non-members, which would mean that the *store* becomes the community's gatehouse. But at the end of the day, the content is still open to everyone - only the *curation* would "belong to the community".

## Onto the ATmosphere

As mentioned above (and [on Bluesky](https://bsky.app/profile/mathewlowry.bsky.social/post/3lcnf3fkim22t)), my December newsletter and the blog post I extracted from it were both published on Whitewind: 

> "a platform for posting blogs onto the ATmosphere, with content stored on any ATProto Personal Data Server (PDS). So if you have a Bluesky account you just login and your posts will be stored on the PDS BlueSky gave you... but that content remains _yours_... [plus there's] seamless comments integration with BlueSky: a comment posted to the blog is shared on the commenter's Bluesky account, and whenever someone shares the post on Bluesky it also appears under the post." - [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.bsky.social/3lcb22vzc3r2x)

That post mainly focused on what Whitewind offered my personal "thinking transparently" process (of which the newsletter, blog post, this page and wiki are all integral parts), so if you're into personal content strategies and tools4thought, check it out in full.

But the significance of Whitewind goes much deeper - it's a fully-fledged ATMosphere app, with its own longform content affordances, but totally integrated with Bluesky. This echoes the integration between different Fediverse apps (Mastodon, Plieroma, etc.), but the seamlessness and user-friendliness is on another level, to say nothing of the fact that the ATmosphere is one global conversation. 

On the ATmosphere, therefore, AI4communities could take the form of many different apps, each providing their own community and collaboration features, yet part of the wider global conversation mediated by Bluesky. Schematically, it will look something like the right half of the image I ended the "Thinking transparently" blog post with: a bunch of personal ATmosphere apps for curating, writing, collaborating and more, calling on additional apps which use AI to remix and further add value to the content for communities and other users: 

![[atproto-ecosystem.png]]
*Caption: seamless integration between one users' personal writing stack (left), collaboration with friends and publishing tools, and the wider ATmosphere.*

Things get even more interesting, for me at least, when I consider what organisations could do with this: not only could they build online communities which are deeply integrated into the wider Bluesky conversations, they can also offer their staff both identity- and PDS-related services. But that will have to wait for the next version of this page, because I think I'm reaching the edge of my technical knowledge - I need to spend some time with protocol engineers.

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: 
	- 2024-12-08: renamed this to AI4Communities on the *ATmosphere* to reflect the new emphasis on the wider ecosystem, and integrated my two December posts, published to Whitewind ([This newsletter is posted on Bluesky](https://whtwnd.com/mathewlowry.bsky.social/3lcb34ugiq22t), [Thinking transparently in the ATmosphere](https://whtwnd.com/mathewlowry.bsky.social/3lcb22vzc3r2x)).
- version control
    - this is version: current
    - this is the current version: [[AI4Communities on the ATmosphere]]
    - here is the previous version: [[AI4Communities on Bluesky 2]]