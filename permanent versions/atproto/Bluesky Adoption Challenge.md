# Unpacking Bluesky's Adoption Challenges

**The more you look at the challenge of getting people off X and onto Bluesky, the more multilayered it becomes.**

*(This is version 3, published on my experimental wiki because I'm looking for comments, feedback and ideas ([ping me](https://bsky.app/profile/mathewlowry.bsky.social)). Version control in the footer)* 

![[adoptionchallenge.png]]
As I mentioned in  [Feel the ATmosphere: it's 1995 all over again](https://myhub.ai/items/feel-the-atmosphere-its-1995-all-over-again), my Ahoy! workshop in April 2025 explored one aspect of what I've come to call "the Bluesky Adoption challenge": getting people to move away from X and the rest and onto Bluesky and the rest of the ATmosphere. 

Back then I had a reasonably simplistic view of the problem:

* the first wave of early adopters, largely disaffected or disgusted with Elon Musk's X, would peter out soon if it hasn't already, falling well short of 50m; 
* many of those could easily kick Bluesky's tyres and lose interest if they can't quickly build a rewarding social graph, particularly as many won't make good use of its unique features, somewhat hidden behind Bluesky's superficial similarity to X (hence [3 things you may not know about Bluesky](https://myhub.ai/items/three-things-you-probably-didnt-know-about-bluesky)).
* even if they want to move to Bluesky, many people and organisations on X will stay there because they're both trapped by their followers and trap those they follow in a classic vicious circle (hence [Do you need an eXit Strategy?](https://mailchi.mp/dc14cf1c690b/your-hub-is-ready-to-go-16531829)). 

There's therefore a direct line between the above two posts and my Ahoy! conference session, which focused on developing software, services and content to help large organisations adopt Bluesky, the one way I thought a non-developer like me could help (see the [Ahoy! proposal](https://whtwnd.com/mathewlowry.bsky.social/3lmym62gvdg2w) and the current version: [[how could a large organisation best use bluesky]]).. 

But at Ahoy! and since, amid wave after wave of *mostly* nonsensical "Bluesky is dying" hot-takes, I've discovered that the Adoption challenge is a little more multilayered. I'm following up with those who attended, so this post is me getting my thoughts in order before continuing those conversations.

## Decentralisation: theory vs. practice

**It's not enough to have decentralised technology: people have to _use_ it for true decentralisation.**

### "Wait, a decentralised network *crashed*?"

Top of mind for everyone throughout the conference was that on day one [Bluesky apparently "went down](https://techcrunch.com/2025/04/24/wait-how-did-a-decentralized-service-like-bluesky-go-down/)", leading to a predictable flurry of snark from Mastodon users across the Fediverse (and also, strangely, on Bluesky).

Of course, the truth was far more nuanced:

- there was a highly targeted denial of service attack on Bluesky Social PBC's servers
- that's where most people host their Personal Data Services (PDSs) because Bluesky Social PBC provides them free of charge — those users were affected
- users who host their PDS elsewhere were _not_ affected.

As one of Bluesky's engineers mentioned in [a testy exchange](https://bsky.app/profile/dustyweb.bsky.social/post/3lnmvff5c322s) with ActivityPub co-author Christine Lemmer Webber, the same sort of attack would have taken down a Mastodon server just as quickly. The attack had high impact because although Bluesky's *architecture* is decentralised, currently "[things are still pretty operationally centralized on bluesky infrastructure](https://social.coop/@bnewbold/114441655585484859)". Or, as another person put it, the headline could equally have been ["Bluesky Hit with Massive, Targeted DDoS Attack, Some Users Didn't Even Notice"](https://bsky.app/profile/goose.art/post/3lnnn6gmnws2t).

### "Wait, a decentralised network *censored* people?"

The above attack came days after another, equally misunderstood episode, when [Bluesky restricted access to 72 accounts in Turkey at the request of the Turkish government](https://techcrunch.com/2025/04/23/government-censorship-comes-to-bluesky-but-not-its-third-party-apps-yet). This inevitably leading to [claims](https://bsky.app/profile/aliskorkut.com/post/3lmuztdhwk22g) that Bluesky is "just like Twitter", from which many Turkish users had fled to Bluesky [earlier that month](https://bsky.app/profile/mackuba.eu/post/3lm34ddbhjc2y), fearing government censorship.

Except it's _not_ "just like Twitter"… but again this is hard to follow for those who simply see Bluesky as "Twitter minus Nazis". As Ahoy! co-organiser [Laurens Hof](https://bsky.app/profile/laurenshof.online) explains in [Bluesky, censorship and country-based moderation](https://fediversereport.com/bluesky-censorship-and-country-based-moderation), the blocked content was visible to not only everyone outside Turkey and anyone in Turkey using a VPN, but _also_ to anyone in Turkey using a 3rd party Bluesky client, which are **free to ignore Bluesky PBC's geographic moderation** labeller.

This is therefore a second example of a **technically decentralised network looking centralised** in practice because most people still use Bluesky Social PBC's apps and/or infrastructure, creating "_a single chokepoint where governments can apply pressure_".

Moreover, as Laurens points out "_The output of the geographic moderation labelers is easily and publicly accessible"_, so custom feeds can easily highlight the content various governments don't want their citizens to see.

> governments trying to censor Bluesky would just embarrass themselves and highlight the content they're trying to suppress

If people made real use of the ATmosphere's decentralised nature, therefore, these chokepoints would disappear: governments trying to censor Bluesky would simply embarrass themselves *and* highlight the content they're trying to suppress.

### Undermining Bluesky's key argument

These examples show that while almost everyone on Bluesky uses one company's infrastructure, the network will *look* centralised, even when built with decentralis*able* technology. 

> getting users onto alternative infrastructure may be almost as important

This undermines one of Bluesky's differentiators against its better-funded, walled garden incumbent competitors.  Getting people to migrate to Bluesky is therefore only part of the challenge - getting users onto alternative infrastructure may be almost as important.

I'm embarrassed to admit that I didn't until [Eurosky Social made it easy](https://eurosky.tech/accounts/migrate/), as like 99% of the population I don't have the skills to self-host (see [Building resilient social media](https://medium.com/@mathewlowry/building-resilient-social-media-9f7568a501a6)).

## Create value worth paying for

**At the risk of stating the blindingly obvious: we won't meet the adoption challenge without something it makes sense for people and organisations to adopt.** 

The past few months have demonstrated that only a small percentage of X users will move to Bluesky in disgust at the prospect of continuing to reinforce the influence of the world's richest Nazi. If this didn't get them to make the move, what on earth will?

![[Elon_Musk_gesture.gif]]

In a better world, perhaps, people and organisations (companies, governments, civil society, etc.) would adopt Bluesky simply because it's an ethically superior microblogging alternative. But in our timeline, the facts are: 

* perhaps 10% of X's userbase has tested Bluesky's waters 
* fewer have made Bluesky their main social media
* even fewer have ditched their X account entirely.

We all know why. X has massive **social lock-in:** it's where its users' friends and audiences are, and in many cases that network of followers is mission-critical to their livelihood. They're trapped by their followers who are trapped by them, and the "idealist" reason to migrate to Bluesky is simply not strong enough to get most of them to escape the trap, despite what they think of Elon Musk.

I have to say that while this disappoints me, maybe it's crazy to think another outcome was possible.

Update (*January 2026*): apparently even releasing [an AI which generates child porn on demand](https://www.bbc.com/news/articles/cvg1mzlryxeo) was not enough. Words fail me.

### Make the most of Bluesky

Talking of crazy... how about launching a product which is almost identical to an incumbent competitor which: 

* is massively entrenched, benefiting from insuperable social lock-in  
* is superfinanced, owned by the world's richest man
* has big (albeit orange and fickle) friends at the very summit of political power
* is advertising-financed, a proven business model which you deny yourself?

I'm not criticising Bluesky Social's decision-making: it's precisely *because* they launched a product similar to X that we have 43+m people with ATmosphere accounts, all able to kick the tyres of every other ATmosphere app under development (if they knew what an ATmosphere account actually is).

Moreover, there are plenty of novel things one can do on Bluesky that you cannot do on X. The problem is that most people don't even *see* them, or really understand what they are and how they can use them. 

Partly this is because of its deliberate similarity to X: we're so used to microblogging as defined by X, it's difficult for many people to see Bluesky as it's own thing, rather than a left-leaning X. It will take time for people to understand what you can and cannot do with features like custom feeds, labellers and verifiers ...if they stick around long enough to scratch below the surface. 

That speaks to the tension at the heart of Bluesky's onboarding challenge:

> feeds, lists and labellers are too much for most users. It's confusing, there are so many of them. Overwhelming with choice situation. When someone joins new we should have good straightforward curated experiences from the get go rather than throw the kitchen sink at them - *[Sherif](https://bsky.app/profile/sherif.eurosky.social/post/3mpsoj4ri7224) , 4 July 2026*

If new users arrive expecting X, in other words, the features that make Bluesky genuinely different are exactly those ones that can overwhelm them. 

That leaves Bluesky's only pitch as "we're like Twitter but without Nazis (or your friends)", which means there's no *positive* reason to migrate. We've already attracted most of those motivated by negative reasons, but I'm not sure Elon Musk can get any worse (although, as shown above, I've been wrong about that before).
### Power users and power communities

**So do we hide the power features to smooth the onboarding experience? That seems like a mistake, because custom feeds and labellers are precisely what allows communities to form, creating value impossible to replicate on X.**

The resolution, I think, is to separate the two audiences: **feeds are for power users, but power communities are for everyone.** Power users build the feeds, starter packs and labellers that create communities worth joining — and those communities become the on-ramps for everyone else. 

> Power users build the feeds, starter packs and labellers that create communities worth joining ... the on-ramps for everyone else.

So power users create power communities which then attract normal users, because the hard work of curation, integration and community-building has already been done. 

Because you can do a lot in terms of open community building, notably by combining Bluesky with other ATmosphere-capable tools into entire ecosystems (see [Three things you probably didn't know about Bluesky](https://myhub.ai/items/three-things-you-probably-didnt-know-about-bluesky)). But to make those benefits accessible will take high-quality information, inspirational demonstrations and (perhaps most importantly) new management tools, as I explored in Ahoy!

> "*One way to encourage the transition from X to Bluesky is to help large organisations efficiently organise and manage their Bluesky presence. The better they use Bluesky, the quicker they can accelerate [their eXit Strategy](https://mathewlowry.medium.com/x-strategy-or-exit-strategy-a-cost-benefit-analysis-framework-024af4abd1a0)*" - [[how could a large organisation best use bluesky]]).

### Value through innovation, not mimicry

Most presentations at Ahoy!, however, introduced some of the apps currently under development. At least some appear to be offering "ATmosphere alternatives" of existing incumbents (Tiktok, Instagram, etc.) which are *also* massively entrenched and superfinanced, with friends at the very summit of political power and are advertising-financed, a proven business model which these new apps (I think!) deny themselves. Sound familiar?

These similarities are probably superficial: just as digging into Bluesky surfaces roll-your-own custom feeds and labellers, I'm sure these apps are improvements over the originals. But maybe we need to step back and ask whether every ATmosphere app wants to make a promise along the lines of *"we're just like X/Instagram/X, but with none of your friends, an unclear business plan and a few months of funding"?*

Also, the incumbents they're competing with are designed as they are because they're built around the surveillance capitalism business model - they dropped features that weren't useful to that model, and chose features and designs that were. If we *don't* want to join the surveillance capitalism club, is even superficially mimicking those feature and design choices the best idea? 

> maybe the best battlefield for competing with incumbents is by offering something they cannot?

Instead, maybe the best battlefield for competing with incumbents is by offering something they cannot? I doubt most people will pay for social media which is identical to the free incumbents but lacks their audience. I can imagine some of them paying for something which delivers greater value than incumbent social media ever can. There are so many things you cannot do with X, Facebook and the rest. **Can we have some apps that provide value people cannot get anywhere else, and can we communicate the differences, not the similarities?**

Maybe, at the end of the day, the social media we have today is the social media which can be supported by advertising, and X-style microblogging simply cannot provide enough value for most individuals and organisations to pay for it. But there are plenty of online content applications that some people *do* pay for, and to date they are either productivity software or longform publishing (enewsletter and website publishing). My goal is to combine them, but that's another story.

## Start with ATScience

There's a prior question lurking beneath the whole adoption challenge: *which* users, and in which order?

If you want epistemologically sound information online — on social networks, and indeed anywhere else — you need to create spaces where high quality information is valued. And that means prioritising three sectors to adopt the ATmosphere: **news, science, and the public sector**. All three are supposed to publish information they can back up with evidence - after all, that's why we have the scientific method, the journalistic method, and public sector accountability, even if they are regularly honoured in the breach.

It's therefore no accident that my presentation at the EuroSky launch was entitled *"[How newsrooms, science and public organizations can get the most out of Bluesky](https://mathewlowry.medium.com/how-newsrooms-scientific-institutions-governments-can-best-use-bluesky-ee97d840a058)"*.  And it's also no surprise that science showed the most interest:

* Newsrooms are desperately short of cash. Their shrinking revenues depend on reaching as many people as possible, while the ATmosphere is still a fraction of the size of legacy social media. Even accounting for the huge number of X bots and its diminishing reach for links, it's a lot to ask of cash-strapped news organisations to invest in rebuilding their audiences elsewhere.
* The public sector, of course, is slow to do anything.
* Science is different. Its revenue base includes the public purse, and doesn't require massive audiences to secure funding. It's also full of people who are comfortable with technology, and therefore more open to innovation than average. It's no coincidence scientists were early Bluesky adopters.

That's why my current focus is **[ATscience](https://atproto.science/)**: helping the science sector adopt the ATmosphere, explore innovative solutions, and demonstrate the cost-effectiveness of the ecosystem for both science-to-science and science-to-society communications.

Beyond improving the quality of epistemologically sound information online, success here has a second purpose: it increases the value of the ATmosphere for everyone else, and creates demonstrated models that newsrooms and the public sector can eventually point to and adopt. Science isn't just the easiest starting point — it's the beachhead.

## In summary

The adoption challenge sounds simple - let's get people to move from X to Bluesky! - but it's in fact a multi-layered challenge that needs to be tackled on several interrelated fronts:

* **differentiate Bluesky from X** by:
	* demonstrating how people and organisations can create real-world value from its unique features,
	* providing the management tools they need to exploit them  
	* using **power users to build power communities** that serve as on-ramps for the majority who'll never configure a feed or labeller themselves
* **creating experiences which provide value the incumbents can't** 
	* through creating unique apps
	* and combining apps together in innovative ecosystems
* **start with the sectors most likely to succeed** — focus on science as the beachhead, build demonstrated models, and let news and public sector follow when the path is proven
* encouraging all users to move to **alternative infrastructure**
* **education, education, education**, particularly to win [SaveSocial](https://savesocial.eu/en/)'s argument that the public sector should post on the ATmosphere at least as much as they post on (and thus support) X and the other incumbents actively undermining democracy (is that so much to ask?). 

These activities and goals are interrelated. To envision this I like frameworks. Unfortunately I'm not an artist, but hopefully this shows that my Hamburg workshop tackled a small part of one part of meeting this challenge:

![[adoption2.png]]

Have I missed anything? Let me know*. 

`*` Unless it's "solve the Bluesky Purity Spiral" argument, which I deliberately left out because (a) I want to tackle problems that can be solved, and (b) I'm totally chicken.


---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version (*updated 2026-07-06*): 
	- developed the idea of power users and power communities
	- added "Start with ATScience" 
- version control
    - this is version: 3 
    - this is the current version: [[Bluesky Adoption Challenge]]
    - here is the previous version: [[Bluesky Adoption Challenge 2]]

