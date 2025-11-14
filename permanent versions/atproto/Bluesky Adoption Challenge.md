# Unpacking Bluesky's Adoption Challenges

**The more you look at the challenge of getting people off X and onto Bluesky, the more multilayered it becomes.**

*(This is version 2, published on my experimental wiki because I'm looking for comments, feedback and ideas ([ping me](https://bsky.app/profile/mathewlowry.bsky.social)). Version control in the footer)* 

![[adoptionchallenge.png]]
As I mentioned in  [Feel the ATmosphere: it's 1995 all over again](https://myhub.ai/items/feel-the-atmosphere-its-1995-all-over-again), my Ahoy! workshop in April 2025 explored one aspect of what I've come to call "the Bluesky Adoption challenge": getting people to move away from X and the rest and onto Bluesky and the rest of the ATmosphere. 

Back then I had a reasonably simplistic view of the problem:

* the first wave of early adopters, largely disaffected or disgusted with Elon Musk's X, would peter out soon if it hasn't already, falling well short of 50m; 
* many of those could easily kick Bluesky's tyres and lose interest if they can't quickly build a rewarding social graph, particularly as many won't make good use of its unique features, somewhat hidden behind Bluesky's superficial similarity to X (hence [3 things you may not know about Bluesky](https://myhub.ai/items/three-things-you-probably-didnt-know-about-bluesky)).
* even if they want to move to Bluesky, many people and organisations on X will stay there because they're both trapped by their followers and trap those they follow in a classic vicious circle (hence [Do you need an eXit Strategy?](https://mailchi.mp/dc14cf1c690b/your-hub-is-ready-to-go-16531829)). 

There's therefore a direct line between the above two posts and my Ahoy! conference session, which focused on developing software, services and content to help large organisations adopt Bluesky, the one way I thought a non-developer like me could help (see the [Ahoy! proposal](https://whtwnd.com/mathewlowry.bsky.social/3lmym62gvdg2w) and the current version: [[how could a large organisation best use bluesky]]).. 

But at Ahoy! and since, amid wave after wave of *mostly* nonsensical "Bluesky is dying" hot-takes, I've discovered that the Adoption challenge is a little more multilayered. I'm following up with those who attended, so this post is me getting my thoughts in order before continuing those conversations.

## Decentralisation: theory vs. practice

**It’s not enough to have decentralised technology: people have to _use_ it for true decentralisation (and I don't).**

### “Wait, a decentralised network *crashed*?”

Top of mind for everyone throughout the conference was that on day one [Bluesky apparently “went down](https://techcrunch.com/2025/04/24/wait-how-did-a-decentralized-service-like-bluesky-go-down/)”, leading to a predictable flurry of snark from Mastodon users across the Fediverse (and also, strangely, on Bluesky).

Of course, the truth was far more nuanced:

- there was a highly targeted denial of service attack on Bluesky Social PBC’s servers
- that’s where most people host their Personal Data Services (PDSs) because Bluesky Social PBC provides them free of charge — those users were affected
- users who host their PDS elsewhere were _not_ affected.

As one of Bluesky’s engineers mentioned in [a testy exchange](https://bsky.app/profile/dustyweb.bsky.social/post/3lnmvff5c322s) with ActivityPub co-author Christine Lemmer Webber, the same sort of attack would have taken down a Mastodon server just as quickly. The attack had high impact because although Bluesky’s *architecture* is decentralised, currently “[things are still pretty operationally centralized on bluesky infrastructure](https://social.coop/@bnewbold/114441655585484859)”. Or, as another person put it, the headline could equally have been ["Bluesky Hit with Massive, Targeted DDoS Attack, Some Users Didn't Even Notice"](https://bsky.app/profile/goose.art/post/3lnnn6gmnws2t).

### “Wait, a decentralised network *censored* people?”

The above attack came days after another, equally misunderstood episode, when [Bluesky restricted access to 72 accounts in Turkey at the request of the Turkish government](https://techcrunch.com/2025/04/23/government-censorship-comes-to-bluesky-but-not-its-third-party-apps-yet). This inevitably leading to [claims](https://bsky.app/profile/aliskorkut.com/post/3lmuztdhwk22g) that Bluesky is “just like Twitter”, from which many Turkish users had fled to Bluesky [earlier that month](https://bsky.app/profile/mackuba.eu/post/3lm34ddbhjc2y), fearing government censorship.

Except it’s _not_ “just like Twitter”… but again this is hard to follow for those who simply see Bluesky as “Twitter minus Nazis”. As Ahoy! co-organiser [Laurens Hof](https://bsky.app/profile/laurenshof.online) explains in [Bluesky, censorship and country-based moderation](https://fediversereport.com/bluesky-censorship-and-country-based-moderation), the blocked content was visible to not only everyone outside Turkey and anyone in Turkey using a VPN, but _also_ to anyone in Turkey using a 3rd party Bluesky client, which are **free to ignore Bluesky PBC’s geographic moderation** labeller.

This is therefore a second example of a **technically decentralised network looking centralised** in practice because most people still use Bluesky Social PBC’s apps and/or infrastructure, creating “_a single chokepoint where governments can apply pressure_”.

Moreover, as Laurens points out “_The output of the geographic moderation labelers is easily and publicly accessible”_, so custom feeds can easily highlight the content various governments don’t want their citizens to see.

> governments trying to censor Bluesky would just embarrass themselves and highlight the content they’re trying to suppress

If people made real use of the ATmosphere’s decentralised nature, therefore, these chokepoints would disappear: governments trying to censor Bluesky would simply embarrass themselves *and* highlight the content they’re trying to suppress.

### Undermining Bluesky's key argument

These examples show that while almost everyone on Bluesky uses one company's infrastructure, the network will *look* centralised, even when built with decentralis*able* technology. 

This undermines one of Bluesky's differentiators against its better-funded, walled garden incumbent competitors.  Getting people to migrate to Bluesky is therefore only part of the challenge - **getting them onto alternative infrastructure may be almost as important.**

I'm embarrassed to admit that I for one still haven’t: like 99% of the population, I don’t have the skills to self-host. Setting up easy-to-use hosting services, in my view, should therefore be a priority for Europe in general, and in particular [eurosky.social](eurosky.social), which is launching in a few days' time (see [Building resilient social media](https://medium.com/@mathewlowry/building-resilient-social-media-9f7568a501a6))

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

### Make the most of Bluesky

Talking of crazy... how about launching a product which is almost identical to an incumbent competitor which: 

* is massively entrenched, benefiting from insuperable social lock-in  
* is superfinanced, owned by the world's richest man
* has big (albeit orange and fickle) friends at the very summit of political power
* is advertising-financed, a proven business model which you deny yourself?

I'm not criticising Bluesky Social's decision-making: it's precisely *because* they launched a product similar to X that we have 40m people with ATmosphere accounts, all able to kick the tyres of every other ATmosphere app under development. 

Moreover, there are plenty of novel things one can do on Bluesky that you cannot do on X. The problem is that most people don't make good use of them - many people don't even *see* them, or really understand what they are and how they can use them. 

Partly this is because of its deliberate similarity to X: we're so used to microblogging as defined by X, it's difficult for many people to see Bluesky as it's own thing, rather than a left-leaning X. I think it will take time for people to understand what you can and cannot do with features like custom feeds, labellers and verifiers ...if they stick around long enough to scratch below the surface. 

Fwiw, my sense is that you can do a lot in terms of open community building, notably by combining Bluesky with other ATmosphere-capable tools into entire ecosystems (see [Three things you probably didn't know about Bluesky](https://myhub.ai/items/three-things-you-probably-didnt-know-about-bluesky)). But to make those benefits accessible will take high-quality information, inspirational demonstrations and (perhaps most importantly) new management tools, as I explored in Ahoy!

> "*One way to encourage the transition from X to Bluesky is to help large organisations efficiently organise and manage their Bluesky presence. The better they use Bluesky, the quicker they can accelerate [their eXit Strategy](https://mathewlowry.medium.com/x-strategy-or-exit-strategy-a-cost-benefit-analysis-framework-024af4abd1a0)*" - [[how could a large organisation best use bluesky]]).

### Value through innovation, not mimicry

Most presentations at Ahoy!, however, introduced some of the apps currently under development. At least some appear to be offering "ATmosphere alternatives" of existing incumbents (Tiktok, Instagram, etc.) which are *also* massively entrenched and superfinanced, with friends at the very summit of political power and are advertising-financed, a proven business model which these new apps (I think!) deny themselves. Sound familiar?

These similarities are probably superficial: just as digging into Bluesky surfaces roll-your-own custom feeds and labellers, I'm sure these apps are improvements over the originals. But maybe we need to step back and ask whether every ATmosphere app wants to make a promise along the lines of *"we're just like X/Instagram/X, but with none of your friends, an unclear business plan and a few months of funding"?*

Also, the incumbents they're competing with are designed as they are because they're built around the surveillance capitalism business model - they dropped features that weren't useful to that model, and chose features and designs that were. If we *don't* want to join the surveillance capitalism club, is even superficially mimicking those feature and design choices the best idea? 

> maybe the best battlefield for competing with incumbents is by offering something they cannot?

Instead, maybe the best battlefield for competing with incumbents is by offering something they cannot? I doubt most people will pay for social media which is identical to the free incumbents but lacks their audience. I can imagine some of them paying for something which delivers greater value than incumbent social media ever can. There are so many things you cannot do with X, Facebook and the rest. **Can we have some apps that provide value people cannot get anywhere else, and can we communicate the differences, not the similarities?**

Maybe, at the end of the day, the social media we have today is the social media which can be supported by advertising, and X-style microblogging simply cannot provide enough value for most individuals and organisations to pay for it. But there are plenty of online content applications that some people *do* pay for, and to date they are either productivity software or longform publishing (enewsletter and website publishing). My goal is to combine them, but that's another story.

## In summary

The adoption challenge sounds simple - let's get people to move from X to Bluesky! - but it's in fact a multi-layered challenge that needs to be tackled on several interrelated fronts:

* **differentiate Bluesky from X** by:
	* demonstrating how people and organisations can create real-world value from it's unique features,
	* providing the management tools they need to exploit them (see [[how could a large organisation best use bluesky]])
* **creating experiences which provide value the incumbents can't** 
	* through creating unique apps
	* and combining apps together in innovative ecosystems
* encouraging all users to move to **alternative infrastructure**
* **education, education, education**, particularly to win [SaveSocial](https://savesocial.eu/en/)'s argument that the public sector should post on the ATmosphere at least as much as they post on (and thus support) X and the other incumbents actively undermining democracy (is that so much to ask?). 

These activities and goals are interrelated. To envision this I like frameworks. Unfortunately I'm not an artist, but hopefully this shows that my Hamburg workshop tackled a small part of one part of meeting this challenge:

![[adoption2.png]]

Have I missed anything? Let me know*. 

`*` Unless it's "solve the Bluesky Purity Spiral" argument, which I deliberately left out because (a) I want to tackle problems that can be solved, and (b) I'm totally chicken.

## More reading

- I followed up on my Hamburg workshop with [[how could a large organisation best use bluesky]], which led to the creation of [ATConnect](https://www.atconnect.eu/)
- And I'm back in Germany for the launch of eurosky.social - see [Building resilient social media](https://medium.com/@mathewlowry/building-resilient-social-media-9f7568a501a6)
- There's a [Bluesky/ATmosphere overview](https://myhub.ai/@mathewlowry/overview/46/?quality=all&types=like&types=do&types=think&timeframe=anytime) on my Hub, where you'll also find [everything tagged Ahoy](https://myhub.ai/@mathewlowry/?tags=ahoy2025).

---

## Revision Notes

This is one of this wiki's pages managed with the **permanent versions pattern** described in  [Two wiki authors and a blogger walk into a bar…](https://mathewlowry.medium.com/two-wiki-authors-and-a-blogger-walk-into-a-bar-7106c8376c6e)  

- changes in this version (*updated 2025-11-14*): 
	- minor tweaks, pre eurosky.social's Berlin event
- version control
    - this is version: 2 
    - this is the current version: [[Bluesky Adoption Challenge]]
    - here is the previous version: [[Bluesky Adoption Challenge 1]]