# AI4Communities on the Fediverse

**This is a subfile of the primary [[AI4Communities post]], and won't make any sense unless you read its parent first. It explores how the AI4communities idea would look within the  ActivityPub-powered Fediverse**.

*(Notes: This is an early draft. As explained in [this newsletter edition](https://mathewlowry.medium.com/exploring-ai4communities-newsletter-6365b2716bb1), I am publishing these early versions as I develop my thoughts in the hope that constructive comments will help me finish the post. More version control in the footer.)*

My [manifesto posts of 1/1/23](https://mathewlowry.medium.com/a-minimum-viable-ecosystem-for-collective-intelligence-7738848ce9c4) reflected *some* knowledge of the Fediverse, which I'd been tracking for a few years. My early versions of the [[AI4Communities post]], from which the following was extracted, reflected that bias. 

In fact, I'm not sure I would have come up with these ideas if ActivityPub hadn't shown that decentralised social media was at least possible. Moreover, the whole cozyweb idea reflects the Fediverse architecture - it's very easy to map "cozyweb community" <-> "Fediverse instance".

However, as I researched the more modern decentralised protocols for the [[AI4Communities post]] (see [[AI4Communities on Bluesky]], [[AI4Communities on Nostr]]), I came across an introduction to Nostr from one of my favourite thinkers in this space, Gordon Brander. While I'm not yet convinced that Nostr is the solution, [Nature's many attempts to evolve a Nostr](https://substack.com/home/post/p-143032514) provides an excellent explanation of why the ActivityHub-powered Fediverse is flawed: "*Federated networks become oligopolies at scale*", due to general forces seen everywhere: "*airline routes, power grids, trains, banks, Bitcoin mining, protein interactions, ecological food webs, neural networks*". It happened to email, and now it's happening with the Fediverse, where calls to defederate Threads (which was 10x the rest of the Fediverse when it arrived) were ineffective.

Nevertheless, the Fediverse has something the more modern ecosystems (probably - tbc) lack: a diversity of apps working and communicating across a decentralised architecture. So despite my own bad experience (see [All my toots gone](https://mathewlowry.medium.com/all-my-toots-gone-e844f7c5f255)), as well as the [mild toxicity Fedizens have towards other protocols](https://bsky.app/profile/mathewlowry.bsky.social/post/3lb4vximypc2d), it would be a mistake to not consider its suitability for supporting AI4Communities seriously.

## Business models

In AI4Communities on the Fediverse:

* it's the community of users on a Fediverse instance that visits their “Friendly Neighborhood Algorithm Store” to choose some AI algorithms to support their community.  
* those algorithms must access the instance's content, of course, but as the community *owns* the AI as well as their data, there should be no data issues. 
* the AIs are trained both explicitly by its users and by their content implicitly. 

The store will provide an array of products and pricing schemes, including lower-cost subscription plans where the village's data, suitably anonymised, is used to affray the costs. Other villages may select higher-cost plans where the village does not share its data. Some may charge some or all members, and/or display ads.

The diversity of both funding schemes and AI plans means that one village may form a data union, while another sets up a for-profit instance and a third lets users choose between paying a subscription fee or seeing ads.

![](https://cdn-images-1.medium.com/max/1600/1*3WBzTFfnFM1bgbiQsV3T3A.png)

(caption) *Different Fediverse communities offering users different experiences, including AI services sourced from multiple AI marketplaces and individual suppliers.*

## AI Services in the Fediverse

**The main [[AI4Communities post]] summarises various categories of AI service within these ecosystems, so this section examines how the various categories would look in the Fediverse.**

### Content discovery, moderation and governance services

The current draft of these services in the [[AI4Communities post]] is very Fediverse-oriented, referring constantly to "the village's inhabitants", where *village* maps more or less perfectly to *Fediverse instance*. However, while these services could augment the Fediverse offering enormously, they might not be possible to implement.

#### Content discovery

When it comes to content discovery, on the Fediverse you only get three reverse chronological feeds: 

* from everyone you follow; 
* from everyone in your village (*local feed*); 
* from everyone followed by at least one person in your village. 

None of these feeds include content from villages which your village does not federate with, which is widely considered a feature, not a bug (but could limit the effectiveness of AI-supported content discovery, as explored below). 

With AI4communities, an instance could employ content discovery AIs to proactively pull in and surface content of collective interest to the village's inhabitants from across the Fediverse. As that AI would be trained on the inhabitants' interests and explicitly guardrailed by the community's values, it should be an interesting, high-value feed. 

And if your tastes don’t match the village’s, you can move to another village. Balancing an individual’s feed parameters with the village’s content moderation rulebook should be a fun problem to tackle, but far from insuperable, as each village can find its own balance. Which brings me to...

#### Content moderation

Fediverse content discovery and moderation services are in a sense two sides of the same coin: while content discovery AI services pull in *useful* content from across the Fediverse, they would need also to keep unwanted content out.

In addition, however, content moderation AI services would also operate *within* the instance, as described in [[AI4Communities post]]: improving the discussions and collaborations within the instance's local feed. As the local feeds is composed of the community's authored content, this is also where these AI services would find a lot of their training data, and where the community would discuss edge cases.

#### Feasibility & implications

The main problem is that an instance's content discovery algorithm cannot pull in content from an instance it is not federated with. The main opportunity is that AI4communities could make it safer for instances to federate with more servers, and reduce their need to push the nuclear "defederate" button, opting instead to harden their algorithms against specific posts and users.

### Centaur services
to be developed


## Known Unknowns

What I don't know yet:

* what would AI4communities do to the economics of running a Fediverse server? 
	* effective content discovery and moderation would make it more valuable for servers to federate with each other
	* what would the resulting traffic do to their hosting costs?
	* would most users consider those enhanced services worth a subscription fee?
* how much protocol development would be required, if any?
* is AI4communities a good cultural fit for the Fediverse?

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version: mid-November: 
	- introduction
	- AI services begun
- version control
    - this is version: 2
    - this is the current version: [[AI4Communities on the Fediverse]]
    - here is the previous version: [[AI4Communities on the Fediverse 1]]
